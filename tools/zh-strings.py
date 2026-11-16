#!/usr/bin/env python3
"""Builds docs/zh-strings.md: the English, Ukrainian and Chinese texts of every key, in the order
the screens show them, so a translation can be checked without a console and without reading C.

Usage: python3 tools/zh-strings.py            (writes docs/zh-strings.md)
       python3 tools/zh-strings.py --check    (fails when the file is out of date)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "app" / "source"
OUT = ROOT / "docs" / "zh-strings.md"

ENTRY = re.compile(r'X\((S_\w+),\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\)')

# Where a screen starts, in the order i18n.h keeps them. Every key is listed under the last
# heading above it, so nothing has to be maintained here when a key is added inside a group.
SECTIONS = [
    ("面板 · 状态与统计", "S_STATE_READY"),
    ("面板 · 按钮与说明", "S_TILE_RECORDER"),
    ("面板 · 提示行与提示消息", "S_TILE_HELP_SUB"),
    ("首次运行 · 语言选择", "S_LANG_CONTINUE"),
    ("首次运行 · 新手引导", "S_GUIDE_OF"),
    ("首次运行 · 录制前检查", "S_FR_EYEBROW"),
    ("帮助页", "S_HELP_TITLE"),
    ("帮助 · 正文", "S_H1"),
    ("设置页 · 开机自启", "S_AUTOSTART"),
    ("面板 · 回放 30 秒", "S_REPLAY"),
    ("设置页", "S_SETTINGS"),
    ("设置页 · 文件内容卡片", "S_FILE_TITLE"),
    ("设置页 · 快捷键", "S_HK_SCREEN"),
    ("卸载", "S_UN_EYEBROW"),
    ("手机下载页（主机上的二维码页面）", "S_PH_EYEBROW"),
    ("录像库 · 转换状态", "S_GAL_PREP_READY"),
    ("播放器", "S_PLAY_FAILED"),
    ("录像库", "S_GAL_NTH"),
    ("卸载 · 执行与结果", "S_UNINSTALL"),
    ("通用按钮", "S_EXIT"),
]

# Deliberate choices worth a second look while reading the table.
NOTES = {
    "S_LANGUAGE": "设置页那一行的标题；原英文是 `Language · Мова`，中文按「当前语言 · 另一种语言」写",
    "S_SKIPPED": "统计卡片里的副标题，位置窄，缩成「丢 N」",
    "S_TARGET": "帧率卡片的副标题，原英文是 target",
    "S_FR_RUNNING_NO": "面板检查项的值：录制器未运行",
    "S_HK_SAVED2": "保存回放快捷键后的提示",
    "S_UN_ALSO": "卸载对话框的勾选项，%lu 个录像 + 大小",
    "S_PH_LEFT": "手机页剩余时间，原文只有「≈ %u min」",
    "S_GAL_NTH": "录像库第几个，原文「Recording %d of %d」",
    "S_CLIP_MORE": "回放片段排队时的「%s · %d more」",
    "S_UN_APP_CIA": "卸载列表里的「本程序」副标题，CIA 版显示这一条",
}

# Texts the screens hardcode instead of taking from i18n: they are brand names, numbers, key
# names or paths, and stay as they are in every language. Listed so a reader knows the table is
# the whole story except for these.
HARDCODED = [
    ("app.c `draw_lang_top` / `LANG_NAME` / `LANG_PROMPT`",
     "Choose your language · Оберіть мову · 选择语言、English / Українська / 中文（语言页三张卡片）"),
    ("app.c 面板与标题", "3DS Recorder <版本> cn · New 3DS / Old 3DS、REC 圆标、XR32、%d fps"),
    ("app.c 单位与数字", "MB / GB、≈ %lu.%lu MB/s、≈ %lu MB、%llu MB · <N 个录像>"),
    ("app.c 快捷键标签", "L / R / A / B / X / Y / SELECT / ↑ ↓ ← →（键位名，不译）"),
    ("app.c 设置「文件内容」", "XR32 · 无损里的 XR32、XR32 + C420、400×240、320×240（编码与分辨率）"),
    ("app.c 卸载列表", "config.ini, recorder.log、3ds-recorder.3dsx（文件名）"),
    ("app.c 帮助页脚注", "Telegram · t.me/side_quest_ua（作者频道）"),
    ("app.c 引导页图示", "REC、×2（LED 示意）"),
]

HEAD = """# 中文文案对照

`docs/zh-strings.md` 由 `tools/zh-strings.py` 从 `app/source/i18n.h`（英/乌）和
`app/source/i18n_zh.c`（中文）生成，改了文案重新跑一次即可：

```sh
python3 tools/zh-strings.py
```

- **改哪个文件**：中文都在 `app/source/i18n_zh.c`，一条一个键；英文和乌克兰语在 `i18n.h`，不用动。
- **`\\n`**：字符串里的 `\\n` 是换行，帮助正文和引导里用。
- **占位符**：`%s` `%u` `%lu` `%d` `%%` 必须和英文那一列一致，CI 的 `tools/check-i18n.py` 会把不一致的报出来。
- **术语**：recording = 录像，record = 录制，recorder = 录制器，Replay = 回放（最近 30 秒），
  clip = 片段，Gallery = 录像库，hotkey = 快捷键，Launch On Startup = 开机自启，
  Luma3DS / Rosalina / SELECT / START / Wi-Fi / MP4 / CIA / SD 保留原文。

"""


def unescape(text: str) -> str:
    return text.replace('\\n', '\n').replace('\\"', '"').replace("\\\\", "\\")


def cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", "<br>")


def main() -> int:
    strings = ENTRY.findall((SRC / "i18n.h").read_text(encoding="utf-8"))
    zh_text = (SRC / "i18n_zh.c").read_text(encoding="utf-8")
    zh = dict(re.findall(r'\[(S_\w+)\]\s*=\s*"((?:[^"\\]|\\.)*)"', zh_text))

    groups: list[tuple[str, list[tuple[str, str, str, str]]]] = [(SECTIONS[0][0], [])]
    starts = {key: title for title, key in SECTIONS}
    for key, en, uk in strings:
        if key in starts and key != SECTIONS[0][1]:
            groups.append((starts[key], []))
        groups[-1][1].append((key, unescape(en), unescape(uk), unescape(zh.get(key, ""))))

    lines = [HEAD]
    lines.append(f"共 {len(strings)} 条。\n")

    for title, items in groups:
        if not items:
            continue
        short = [i for i in items if len(i[3]) < 40 and "\n" not in i[3]]
        long = [i for i in items if i not in short]
        lines.append(f"## {title}\n")
        if short:
            lines.append("| 键 | English | Українська | 中文 |")
            lines.append("|---|---|---|---|")
            for key, en, uk, cn in short:
                lines.append(f"| `{key}` | {cell(en)} | {cell(uk)} | **{cell(cn)}** |")
            lines.append("")
        for key, en, uk, cn in long:
            lines.append(f"**`{key}`**")
            lines.append("")
            lines.append("```text")
            lines.append(f"EN  {en}".replace("\n", "\n    "))
            lines.append(f"UK  {uk}".replace("\n", "\n    "))
            lines.append(f"ZH  {cn}".replace("\n", "\n    "))
            lines.append("```")
            lines.append("")
        notes = [(k, NOTES[k]) for k, *_ in items if k in NOTES]
        if notes:
            lines.append("说明：\n")
            for key, note in notes:
                lines.append(f"- `{key}`：{note}")
            lines.append("")

    lines.append("## 表外文本（各语言一律原样）\n")
    lines.append("| 位置 | 文本 |")
    lines.append("|---|---|")
    for where, text_ in HARDCODED:
        lines.append(f"| {where} | {cell(text_)} |")
    lines.append("")

    text = "\n".join(lines).rstrip() + "\n"
    if "--check" in sys.argv:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != text:
            print(f"{OUT.relative_to(ROOT)} is out of date: run tools/zh-strings.py", file=sys.stderr)
            return 1
        print(f"{OUT.relative_to(ROOT)} is up to date")
        return 0

    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(strings)} keys, {len(text.splitlines())} lines")
    return 0


if __name__ == "__main__":
    sys.exit(main())
