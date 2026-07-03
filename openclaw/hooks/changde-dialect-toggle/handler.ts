import { promises as fs } from "node:fs";
import path from "node:path";
import os from "node:os";

/**
 * Keyword-toggled dialect persona for OpenClaw agents, with two
 * mutually-exclusive modes so Hanshou (龙阳话) and Taoyuan vocabulary never
 * mix in the same response -- mirrors scripts/dialect_hook.py.
 *
 * message:received -> detect on/off keywords in the inbound message, persist
 *   per-session mode ("hanshou" | "taoyuan" | null) under state/<sessionKey>.json.
 * agent:bootstrap -> if this session has an active mode, append that mode's
 *   dialect reminder to an existing bootstrap file's content. WorkspaceBootstrapFile
 *   names are restricted to a fixed set (AGENTS.md, SOUL.md, TOOLS.md, ...),
 *   so this mutates an existing entry rather than pushing a new filename.
 */

const STATE_DIR = path.join(
  os.homedir(),
  ".openclaw",
  "hooks",
  "changde-dialect-toggle",
  "state",
);

const ON_KEYWORDS_HANSHOU = [
  "说常德话", "讲常德话", "切换常德话", "开启常德话", "常德话模式",
  "切换方言", "开启方言模式", "用方言跟我聊", "用常德话跟我聊", "讲方言",
  "说汉寿话", "讲汉寿话", "切换汉寿话", "汉寿话模式",
  "说龙阳话", "讲龙阳话", "切换龙阳话", "龙阳话模式",
];
const ON_KEYWORDS_TAOYUAN = [
  "说桃源话", "讲桃源话", "切换桃源话", "开启桃源话", "桃源话模式",
  "用桃源话跟我聊",
];
const OFF_KEYWORDS = [
  "退出常德话", "退出方言", "说普通话", "切回普通话", "关闭方言模式",
  "不用讲方言了", "不用说方言了", "恢复普通话", "别说方言了",
  "退出汉寿话", "退出龙阳话", "退出桃源话",
];

const REMINDER_HANSHOU = [
  "汉寿话（龙阳话）对话模式已开启。回应用户时改写成汉寿话，例：了→哒，",
  "什么→么嘚/么得，现在→而今，自己→自家，一起→一路，很→蛮，讲/说→讲，",
  "吃→吃/七，喜欢→爱，漂亮→乖，我们/你们/他们→顽/你安/他安（共享同一个",
  "鼻音后缀），我、你保持原样。",
  "词表里字后面带的\"=\"是记音惯例（标借音字），只是文档标注，实际说话/",
  "打字不要把\"=\"写出来。",
  "具体某个词该怎么说，查 changde-dialect 技能的 ",
  "references/hanshou-ipa-vocab.md（可用 scripts/dialect_lookup.py 核对），",
  "查不到再看 references/hanshou-accent.md。保持句子结构清楚、用户能听懂",
  "大意，不要为了凑方言词而牺牲可理解性。代码、命令、报错等技术性输出不要",
  "方言化。用户说'退出方言/说普通话'等话时立刻恢复普通话。",
].join("");

const REMINDER_TAOYUAN = [
  "桃源腔对话模式已开启（水兵《常德方言词语汇1000》记录的口音）。回应用户",
  "时改写成桃源腔，例：了→哒，讲→港，去→克，看到→看斗，我→俺，很/非常→",
  "几得，什么→么得，自己→各人，一起→同斗，吃→恰/呷/七。",
  "详细词表、语法和歇后语参考 changde-dialect 技能的 references/glossary.md，",
  "按需引用即可，不必整篇背诵。骂人/粗语类词条只在轻度打趣或用户主动问",
  "该词含义时使用，不用来真正冒犯用户。保持句子结构清楚、用户能听懂大意，",
  "不要为了凑方言词而牺牲可理解性。代码、命令、报错等技术性输出不要方言化。",
  "用户说'退出方言/说普通话'等话时立刻恢复普通话。",
].join("");

type DialectMode = "hanshou" | "taoyuan" | null;

function statePath(sessionKey: string): string {
  const safe = (sessionKey || "default").replace(/[^a-zA-Z0-9_-]/g, "_");
  return path.join(STATE_DIR, `${safe}.json`);
}

async function readMode(sessionKey: string): Promise<DialectMode> {
  try {
    const raw = await fs.readFile(statePath(sessionKey), "utf8");
    const data = JSON.parse(raw);
    if (data?.mode === "hanshou" || data?.mode === "taoyuan") return data.mode;
    // backward-compat with the old {"enabled": true/false} format
    if (data?.enabled === true) return "hanshou";
    return null;
  } catch {
    return null;
  }
}

async function writeMode(sessionKey: string, mode: DialectMode): Promise<void> {
  await fs.mkdir(STATE_DIR, { recursive: true });
  await fs.writeFile(statePath(sessionKey), JSON.stringify({ mode }), "utf8");
}

interface WorkspaceBootstrapFile {
  name: string;
  path: string;
  content?: string;
  missing: boolean;
}

interface HookEvent {
  type: string;
  action: string;
  sessionKey: string;
  context: Record<string, unknown>;
  messages: string[];
}

const handler = async (event: HookEvent): Promise<void> => {
  if (event.type === "message" && event.action === "received") {
    const content = String((event.context as { content?: string }).content ?? "");
    const offMatch = OFF_KEYWORDS.some((kw) => content.includes(kw));
    const taoyuanMatch = ON_KEYWORDS_TAOYUAN.some((kw) => content.includes(kw));
    const hanshouMatch = ON_KEYWORDS_HANSHOU.some((kw) => content.includes(kw));

    if (offMatch) {
      await writeMode(event.sessionKey, null);
    } else if (taoyuanMatch) {
      await writeMode(event.sessionKey, "taoyuan");
    } else if (hanshouMatch) {
      await writeMode(event.sessionKey, "hanshou");
    }
    return;
  }

  if (event.type === "agent" && event.action === "bootstrap") {
    const mode = await readMode(event.sessionKey);
    if (!mode) return;
    const reminder = mode === "hanshou" ? REMINDER_HANSHOU : REMINDER_TAOYUAN;
    const context = event.context as { bootstrapFiles: WorkspaceBootstrapFile[] };
    const files = context.bootstrapFiles ?? [];
    const target =
      files.find((f) => f.name === "AGENTS.md" && !f.missing) ??
      files.find((f) => !f.missing) ??
      files[0];
    if (!target) return;
    target.content = `${target.content ?? ""}\n\n<!-- changde-dialect-toggle -->\n${reminder}\n`;
    return;
  }
};

export default handler;
