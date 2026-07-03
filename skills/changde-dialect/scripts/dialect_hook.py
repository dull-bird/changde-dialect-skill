#!/usr/bin/env python3
"""UserPromptSubmit hook: keyword-toggled Changde-dialect persona.

Turns Changde-dialect mode on/off per session based on keywords in the
user's prompt, and injects a reminder into the model's context while the
mode is on. State is stored per session_id so different sessions don't
interfere with each other.
"""
import json
import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
STATE_DIR = SKILL_DIR / "state"

ON_KEYWORDS = [
    "说常德话", "讲常德话", "切换常德话", "开启常德话", "常德话模式",
    "切换方言", "开启方言模式", "用方言跟我聊", "用常德话跟我聊", "讲方言",
]
OFF_KEYWORDS = [
    "退出常德话", "退出方言", "说普通话", "切回普通话", "关闭方言模式",
    "不用讲方言了", "不用说方言了", "恢复普通话", "别说方言了",
]

ADDITIONAL_CONTEXT = (
    "常德话对话模式已开启。接下来用自然语言回应用户时，请用常德方言词汇、"
    "语气词和句式改写普通话表达（例如：了→哒，讲→港，去→克，看到→看斗，"
    "我→俺，很/非常→几得，什么→么得，自己→各人），保持句子结构清楚、"
    "用户能听懂大意，不要为了凑方言词而牺牲可理解性。"
    "详细词表、语法和歇后语参考 changde-dialect 技能的 references/glossary.md，"
    "按需引用即可，不必整篇背诵。骂人/粗语类词条只在轻度打趣或用户主动问"
    "该词含义时使用，不用来真正冒犯用户。代码、命令、报错等技术性输出不要"
    "方言化。用户说'退出方言/说普通话'等话时立刻恢复普通话。"
)


def state_path(session_id: str) -> Path:
    safe_id = re.sub(r"[^a-zA-Z0-9_-]", "_", session_id or "default")
    return STATE_DIR / f"{safe_id}.json"


def read_state(path: Path) -> bool:
    if not path.exists():
        return False
    try:
        return json.loads(path.read_text(encoding="utf-8")).get("enabled", False)
    except (json.JSONDecodeError, OSError):
        return False


def write_state(path: Path, enabled: bool) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"enabled": enabled}), encoding="utf-8")


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        payload = {}

    prompt = payload.get("prompt", "") or ""
    session_id = payload.get("session_id", "default")
    path = state_path(session_id)
    enabled = read_state(path)

    toggled_on = any(kw in prompt for kw in ON_KEYWORDS)
    toggled_off = any(kw in prompt for kw in OFF_KEYWORDS)

    if toggled_on and not toggled_off:
        enabled = True
    elif toggled_off:
        enabled = False

    write_state(path, enabled)

    output = {}
    if enabled:
        output["hookSpecificOutput"] = {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": ADDITIONAL_CONTEXT,
        }
        if toggled_on:
            output["systemMessage"] = "常德话模式已开启，接下来俺跟你用方言唠。"
    elif toggled_off:
        output["systemMessage"] = "已切回普通话。"

    if output:
        print(json.dumps(output, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
