import { promises as fs } from "node:fs";
import path from "node:path";
import os from "node:os";

/**
 * Keyword-toggled Changde-dialect persona for OpenClaw agents.
 *
 * message:received -> detect on/off keywords in the inbound message, persist
 *   per-session state under state/<sessionKey>.json.
 * agent:bootstrap -> if this session's dialect mode is on, append a dialect
 *   reminder to an existing bootstrap file's content. WorkspaceBootstrapFile
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

const ON_KEYWORDS = [
  "说常德话", "讲常德话", "切换常德话", "开启常德话", "常德话模式",
  "切换方言", "开启方言模式", "用方言跟我聊", "用常德话跟我聊", "讲方言",
];
const OFF_KEYWORDS = [
  "退出常德话", "退出方言", "说普通话", "切回普通话", "关闭方言模式",
  "不用讲方言了", "不用说方言了", "恢复普通话", "别说方言了",
];

const REMINDER = [
  "常德话对话模式已开启。接下来用自然语言回应用户时，请用常德方言词汇、",
  "语气词和句式改写普通话表达（例如：了→哒，讲→港，去→克，看到→看斗，",
  "我→俺，很/非常→几得，什么→么得，自己→各人），保持句子结构清楚、",
  "用户能听懂大意，不要为了凑方言词而牺牲可理解性。",
  "详细词表、语法和歇后语参考 changde-dialect 技能的 references/glossary.md，",
  "按需引用即可，不必整篇背诵。骂人/粗语类词条只在轻度打趣或用户主动问",
  "该词含义时使用，不用来真正冒犯用户。代码、命令、报错等技术性输出不要",
  "方言化。用户说'退出方言/说普通话'等话时立刻恢复普通话。",
].join("");

function statePath(sessionKey: string): string {
  const safe = (sessionKey || "default").replace(/[^a-zA-Z0-9_-]/g, "_");
  return path.join(STATE_DIR, `${safe}.json`);
}

async function readEnabled(sessionKey: string): Promise<boolean> {
  try {
    const raw = await fs.readFile(statePath(sessionKey), "utf8");
    return JSON.parse(raw)?.enabled === true;
  } catch {
    return false;
  }
}

async function writeEnabled(sessionKey: string, enabled: boolean): Promise<void> {
  await fs.mkdir(STATE_DIR, { recursive: true });
  await fs.writeFile(statePath(sessionKey), JSON.stringify({ enabled }), "utf8");
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
    const onMatch = ON_KEYWORDS.some((kw) => content.includes(kw));
    const offMatch = OFF_KEYWORDS.some((kw) => content.includes(kw));
    if (onMatch && !offMatch) {
      await writeEnabled(event.sessionKey, true);
    } else if (offMatch) {
      await writeEnabled(event.sessionKey, false);
    }
    return;
  }

  if (event.type === "agent" && event.action === "bootstrap") {
    const enabled = await readEnabled(event.sessionKey);
    if (!enabled) return;
    const context = event.context as { bootstrapFiles: WorkspaceBootstrapFile[] };
    const files = context.bootstrapFiles ?? [];
    const target =
      files.find((f) => f.name === "AGENTS.md" && !f.missing) ??
      files.find((f) => !f.missing) ??
      files[0];
    if (!target) return;
    target.content = `${target.content ?? ""}\n\n<!-- changde-dialect-toggle -->\n${REMINDER}\n`;
    return;
  }
};

export default handler;
