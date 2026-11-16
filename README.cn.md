# 3DS Recorder 简体中文版

这是 [BolgarMaxym97/3ds-recorder](https://github.com/BolgarMaxym97/3ds-recorder) 的汉化分支：
把界面译成简体中文，语言切换与上游原有的 English / Українська 并列，仍是同一个开关。

**当前版本使用主机自带字库（system font），包里不带字库文件。**

## 用起来

- 面板右下角的图标就是语言开关，点一下按 `English → Українська → 中文 → English` 循环；
  手柄上按 `X` 也是同一个操作。
- 「设置 → 语言」里可以直接选三种语言之一。
- 首次运行的语言选择页有三张卡片，选「中文」后写入 `config.ini` 的 `lang=zh`。
- CJK 换行按字断行，`，。、；：！？）》」』】` 之类不会跑到行首。

## 字库说明

中文由主机自己的共享字库绘制（就是 HOME 菜单用的那份），所以安装包很小，也不需要
额外把字库写进 RomFS。代价是**能显示哪些汉字由主机的字库决定**：

- 神游/中国版主机（以及把共享字库换成 `cbf_zh-Hans-CN` 的机器）汉字齐全；
- 其他区域的主机用的是 `cbf_std`，日文汉字大多有，部分简体专用字可能缺字。

字库齐全的自带字库版本（`romfs/hanfont.bcfnt`，取自神游国行共享字库）留作下一步，
思路与 [frilxy/3dsDL_CN](https://github.com/frilxy/3dsDL_CN) 相同。

## 汉化是怎么放进代码的

上游的 `i18n.h` 用一个 `STRINGS(X)` X-macro 保存英文和乌克兰语两列。汉化没有改动这两列：

- `app/source/i18n_zh.c`：新增的一份中文表，`[S_KEY] = "…"` 一条对一个键；
- `app/source/i18n.c`：`Lang` 语言状态与查表，中文缺条时回退英文；
- `tools/check-i18n.py`：CI 里检查「每个键都有中文」且 `%s`/`%u` 这类占位符与英文一致；
- `app/source/ui.c`：中文时字形改走系统字库，并按字断行（拉丁词不拆）；
- `web/app.js`：手机下载页也加了 `zh` 文案。

所以上游升级时，改动集中在 `i18n_zh.c` 和几处语言状态代码，冲突面很小，也方便整理成
PR 提交上游。

## 自己编译

仓库的 GitHub Actions（`.github/workflows/build.yml`）会在 `tools/Dockerfile` 的开发镜像里
构建 sysmodule、Luma 插件、主程序和 CIA，产物在 Actions 运行的 Artifacts 里：
`3ds-recorder-<版本>-cn.3dsx` / `.cia`。

本地等价：

```sh
docker build -t 3dsrec-dev tools/
docker run --rm -v "$PWD:/work" -w /work --user "$(id -u):$(id -g)" 3dsrec-dev make -C sysmod
docker run --rm -v "$PWD:/work" -w /work --user "$(id -u):$(id -g)" 3dsrec-dev make -C plugin
docker run --rm -v "$PWD:/work" -w /work --user "$(id -u):$(id -g)" 3dsrec-dev make -C app
docker run --rm -v "$PWD:/work" -w /work --user "$(id -u):$(id -g)" 3dsrec-dev make -C app cia
```

不想默认中文时，去掉 `app/Makefile` 里的 `CFLAGS += -DCN_BUILD` 即可，其余行为与上游一致。
