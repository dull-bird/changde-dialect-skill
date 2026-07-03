#!/usr/bin/env python3
"""UserPromptSubmit hook: keyword-toggled dialect persona, with two
mutually-exclusive dialect modes so Hanshou (龙阳话) and Taoyuan vocabulary
never mix in the same response.

- "说常德话" and friends -> Hanshou mode (the default persona; verified
  against hanshou-ipa-vocab.md / hanshou-accent.md).
- "说桃源话" and friends -> Taoyuan mode (水兵's glossary.md).
- Switching between the two replaces the mode outright, it does not layer.

State is stored per session_id so different sessions don't interfere with
each other.
"""
import json
import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
STATE_DIR = SKILL_DIR / "state"

ON_KEYWORDS_HANSHOU = [
    "说常德话", "讲常德话", "切换常德话", "开启常德话", "常德话模式",
    "切换方言", "开启方言模式", "用方言跟我聊", "用常德话跟我聊", "讲方言",
    "说汉寿话", "讲汉寿话", "切换汉寿话", "汉寿话模式",
    "说龙阳话", "讲龙阳话", "切换龙阳话", "龙阳话模式",
]
ON_KEYWORDS_TAOYUAN = [
    "说桃源话", "讲桃源话", "切换桃源话", "开启桃源话", "桃源话模式",
    "用桃源话跟我聊",
]
OFF_KEYWORDS = [
    "退出常德话", "退出方言", "说普通话", "切回普通话", "关闭方言模式",
    "不用讲方言了", "不用说方言了", "恢复普通话", "别说方言了",
    "退出汉寿话", "退出龙阳话", "退出桃源话",
]

ADDITIONAL_CONTEXT_HANSHOU = (
    "汉寿话（龙阳话）对话模式已开启。回应用户时改写成汉寿话，例：了→哒，"
    "什么→么嘚/么得，现在→而今，自己→自家，一起→一路，很→蛮，讲/说→讲，"
    "吃→吃，喜欢→爱，漂亮→乖，我们/你们/他们→顽=/你安=/他安=（共享同一个"
    "鼻音后缀），我、你保持原样。"
    "具体某个词该怎么说，查 changde-dialect 技能的 "
    "references/hanshou-ipa-vocab.md（可用 scripts/dialect_lookup.py 核对），"
    "查不到再看 references/hanshou-accent.md。保持句子结构清楚、用户能听懂"
    "大意，不要为了凑方言词而牺牲可理解性。代码、命令、报错等技术性输出不要"
    "方言化。用户说'退出方言/说普通话'等话时立刻恢复普通话。"
)

ADDITIONAL_CONTEXT_TAOYUAN = (
    "桃源腔对话模式已开启（水兵《常德方言词语汇1000》记录的口音）。回应用户"
    "时改写成桃源腔，例：了→哒，讲→港，去→克，看到→看斗，我→俺，很/非常→"
    "几得，什么→么得，自己→各人，一起→同斗，吃→恰/呷。"
    "详细词表、语法和歇后语参考 changde-dialect 技能的 references/glossary.md，"
    "按需引用即可，不必整篇背诵。骂人/粗语类词条只在轻度打趣或用户主动问"
    "该词含义时使用，不用来真正冒犯用户。保持句子结构清楚、用户能听懂大意，"
    "不要为了凑方言词而牺牲可理解性。代码、命令、报错等技术性输出不要方言化。"
    "用户说'退出方言/说普通话'等话时立刻恢复普通话。"
)


def state_path(session_id: str) -> Path:
    safe_id = re.sub(r"[^a-zA-Z0-9_-]", "_", session_id or "default")
    return STATE_DIR / f"{safe_id}.json"


def read_mode(path: Path) -> str | None:
    """Returns 'hanshou', 'taoyuan', or None (off)."""
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
    mode = data.get("mode")
    if mode in ("hanshou", "taoyuan"):
        return mode
    # backward-compat with the old {"enabled": true/false} format
    if data.get("enabled"):
        return "hanshou"
    return None


def write_mode(path: Path, mode: str | None) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"mode": mode}), encoding="utf-8")


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        payload = {}

    prompt = payload.get("prompt", "") or ""
    session_id = payload.get("session_id", "default")
    path = state_path(session_id)
    mode = read_mode(path)

    toggled_hanshou = any(kw in prompt for kw in ON_KEYWORDS_HANSHOU)
    toggled_taoyuan = any(kw in prompt for kw in ON_KEYWORDS_TAOYUAN)
    toggled_off = any(kw in prompt for kw in OFF_KEYWORDS)

    system_message = None
    if toggled_off:
        mode = None
        system_message = "已切回普通话。"
    elif toggled_taoyuan:
        mode = "taoyuan"
        system_message = "桃源腔模式已开启，接下来俺跟你用桃源话港。"
    elif toggled_hanshou:
        mode = "hanshou"
        system_message = "汉寿话模式已开启，接下来我跟你用汉寿话讲。"

    write_mode(path, mode)

    output = {}
    if mode == "hanshou":
        output["hookSpecificOutput"] = {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": ADDITIONAL_CONTEXT_HANSHOU,
        }
    elif mode == "taoyuan":
        output["hookSpecificOutput"] = {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": ADDITIONAL_CONTEXT_TAOYUAN,
        }
    if system_message:
        output["systemMessage"] = system_message

    if output:
        print(json.dumps(output, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
