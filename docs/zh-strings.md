# 中文文案对照

`docs/zh-strings.md` 由 `tools/zh-strings.py` 从 `app/source/i18n.h`（英/乌）和
`app/source/i18n_zh.c`（中文）生成，改了文案重新跑一次即可：

```sh
python3 tools/zh-strings.py
```

- **改哪个文件**：中文都在 `app/source/i18n_zh.c`，一条一个键；英文和乌克兰语在 `i18n.h`，不用动。
- **`\n`**：字符串里的 `\n` 是换行，帮助正文和引导里用。
- **占位符**：`%s` `%u` `%lu` `%d` `%%` 必须和英文那一列一致，CI 的 `tools/check-i18n.py` 会把不一致的报出来。
- **术语**：recording = 录像，record = 录制，recorder = 录制器，Replay = 回放（最近 30 秒），
  clip = 片段，Gallery = 录像库，hotkey = 快捷键，Launch On Startup = 开机自启，
  Luma3DS / Rosalina / SELECT / START / Wi-Fi / MP4 / CIA / SD 保留原文。


共 251 条。

## 面板 · 状态与统计

| 键 | English | Українська | 中文 |
|---|---|---|---|
| `S_STATE_READY` | Ready to record | Готово до запису | **准备录制** |
| `S_STATE_RECORDING` | Recording · %s | Йде запис · %s | **录制中 · %s** |
| `S_STATE_SAVING` | Saving… | Зберігаю… | **保存中…** |
| `S_STATE_OFF` | Recorder is off | Рекордер вимкнено | **录制器已关闭** |
| `S_STATE_STARTING` | Starting… | Запускаю… | **正在启动…** |
| `S_STATE_STOPPING` | Stopping… | Зупиняю… | **正在停止…** |
| `S_STATE_ERROR` | Recorder error | Помилка рекордера | **录制器错误** |
| `S_PILL_ON` | Recorder on | Рекордер працює | **已开启** |
| `S_PILL_OFF` | Off | Вимкнено | **已关闭** |
| `S_PROFILE` | Profile | Профіль | **配置** |
| `S_PROFILE_STD` | Standard | Стандарт | **标准** |
| `S_FPS` | Frame rate | Частота | **帧率** |
| `S_TARGET` | target | ціль | **目标** |
| `S_SCREENS` | Screens | Екрани | **画面** |
| `S_BOTH` | Both | Обидва | **双屏** |
| `S_TOP` | Top | Верхній | **上屏** |
| `S_BOTTOM` | Bottom | Нижній | **下屏** |
| `S_SOUND_ON` | sound on | звук увімк. | **有声音** |
| `S_SOUND_OFF` | sound off | звук вимк. | **无声音** |
| `S_SD_FREE` | SD free | SD вільно | **SD 剩余** |
| `S_MINUTES` | ≈ %u min | ≈ %u хв | **约 %u 分钟** |
| `S_FRAMES` | Frames | Кадри | **帧数** |
| `S_SKIPPED` | skipped %u | пропущено %u | **丢 %u** |
| `S_FILE` | File | Файл | **文件** |
| `S_LAST` | Last recording | Останній запис | **最近录像** |
| `S_NO_RECORDINGS` | No recordings yet | Записів ще немає | **还没有录像** |
| `S_NO_RECORDINGS_HINT` | In a game or HOME press %s | У грі чи HOME натисніть %s | **在游戏或 HOME 中按 %s** |
| `S_WHOLE_CONSOLE` | The whole console is recorded | Записується вся консоль | **录制整个主机画面** |

**`S_WHOLE_CONSOLE_BODY`**

```text
EN  Games, HOME, applets and switching between them go into one file. Stop with the hotkey or the button below. The LED breathes red while recording.
UK  Гра, HOME, аплети й перемикання між програмами — в одному файлі. Зупинити: хоткей або кнопка нижче. LED «дихає» червоним, поки йде запис.
ZH  游戏、HOME 菜单、小程序以及它们之间的切换都会录进同一个文件。按快捷键或下方按钮停止。录制时 LED 呈红色呼吸效果。
```

说明：

- `S_TARGET`：帧率卡片的副标题，原英文是 target
- `S_SKIPPED`：统计卡片里的副标题，位置窄，缩成「丢 N」

## 面板 · 按钮与说明

| 键 | English | Українська | 中文 |
|---|---|---|---|
| `S_TILE_RECORDER` | Recorder | Рекордер | **录制器** |
| `S_TILE_RECORDER_ON` | Hotkey works in games and HOME | Хоткей у грі й HOME працює | **游戏和 HOME 中快捷键可用** |
| `S_TILE_RECORDER_OFF` | Hotkey does nothing | Хоткей не працює | **快捷键无效** |
| `S_TILE_STOP` | Stop recording | Зупинити запис | **停止录制** |
| `S_TILE_STOP_SUB` | Saved; the LED blinks green twice | Файл збережеться, LED мигне зеленим | **将会保存，LED 闪绿两次** |
| `S_TILE_GALLERY` | Gallery | Галерея | **录像库** |
| `S_TILE_PHONE` | Download | Завантажити | **下载** |
| `S_TILE_PHONE_SUB` | over Wi-Fi | по Wi-Fi | **通过 Wi-Fi** |
| `S_SOON` | coming soon | незабаром | **即将推出** |
| `S_TILE_SETTINGS` | Settings | Налаштування | **设置** |
| `S_TILE_HELP` | Help | Допомога | **帮助** |

## 首次运行 · 语言选择

| 键 | English | Українська | 中文 |
|---|---|---|---|
| `S_LANG_CONTINUE` | Continue | Далі | **继续** |

## 首次运行 · 新手引导

| 键 | English | Українська | 中文 |
|---|---|---|---|
| `S_GUIDE_OF` | How to use · %d of %d | Як користуватися · %d з %d | **使用说明 · %d / %d** |
| `S_GUIDE_NEXT` | Next | Далі | **下一步** |
| `S_GUIDE_DONE` | Got it | Зрозуміло | **知道了** |
| `S_GUIDE_SKIP` | Skip | Пропустити | **跳过** |
| `S_GUIDE_OPEN` | How to use | Як користуватися | **使用说明** |
| `S_G1_TITLE` | Record anything | Записуйте будь-що | **录制任何画面** |
| `S_G2_TITLE` | Stop | Зупинка | **停止** |
| `S_G2_BODY` | Press %s again. The recording is saved to the SD card and the LED blinks green twice. | Натисніть %s ще раз. Запис збережеться на SD-карту, а LED двічі мигне зеленим. | **再按一次 %s。录像会保存到 SD 卡，LED 闪绿两次。** |
| `S_G3_TITLE` | Watch and download | Перегляд і завантаження | **观看与下载** |
| `S_G4_TITLE` | After turning the console on | Після ввімкнення консолі | **开机之后** |

**`S_G1_BODY`**

```text
EN  In a game, in HOME, anywhere: press %s. The whole console is recorded, both screens and sound. The LED breathes red while it records.
UK  У грі, в HOME, будь-де: натисніть %s. Записується вся консоль — обидва екрани і звук. Поки йде запис, LED «дихає» червоним.
ZH  在游戏里、在 HOME 里、在任何地方：按 %s。整个主机都会被录下来——双屏画面和声音。录制时 LED 呈红色呼吸效果。
```

**`S_G3_BODY`**

```text
EN  Open the Gallery: A plays a recording, Y downloads it to a phone over Wi-Fi through a QR code. Or take it straight from the SD card in a computer: /3ds/recorder/recordings (an MP4 lies next to each recording). While this app is open, the console converts recordings into small MP4 videos in the background.
UK  Відкрийте Галерею: A — переглянути запис, Y — завантажити на телефон по Wi-Fi через QR-код. Або заберіть напряму з SD-карти на комп'ютері: /3ds/recorder/recordings (поруч із кожним записом лежить MP4). Поки цей додаток відкритий, консоль у фоні конвертує записи в невеликі відео MP4.
ZH  打开录像库：A 播放录像，Y 通过二维码经 Wi-Fi 下载到手机。也可以在电脑上直接读取 SD 卡：/3ds/recorder/recordings（每个录像旁边都有一个 MP4）。本程序打开期间，主机会在后台把录像转换成小的 MP4 视频。
```

**`S_G4_BODY`**

```text
EN  Open this app once: the recorder starts by itself and keeps running after you leave the app. When it is ready, the LED glows blue for a moment. Turning the console off, leaving System Settings or starting a DS or GBA game restarts the console: a recording is saved and stops, open this app again then. Or switch on Settings → Launch On Startup: the recorder then starts with the console.
UK  Відкрийте цей додаток один раз — рекордер запуститься сам і працюватиме далі, коли ви вийдете з додатка. Коли він готовий, LED на мить засвітиться синім. Вимкнення, вихід з Налаштувань консолі чи запуск DS- або GBA-гри перезапускають консоль: запис збережеться і зупиниться — тоді знову відкрийте додаток. Або ввімкніть «Налаштування → Запуск з консоллю»: тоді рекордер стартує разом з консоллю.
ZH  打开本程序一次：录制器会自动启动，并在你退出程序后继续运行。准备就绪时 LED 会亮蓝色一下。关机、退出系统设置或启动 DS 或 GBA 游戏都会重启主机：录像会保存并停止，之后需要再次打开本程序。也可以在「设置 → 开机自启」中打开该选项，让录制器随主机一起启动。
```

## 面板 · 提示行与提示消息

| 键 | English | Українська | 中文 |
|---|---|---|---|
| `S_TILE_HELP_SUB` | Recording, LED, download | Запис, LED, завантаження | **录制、LED、下载** |
| `S_TILE_SETTINGS_SUB` | fps, screens, hotkey | частота, екрани, хоткей | **帧率、画面、快捷键** |
| `S_START_STOP` | Start / stop: | Старт / стоп: | **开始 / 停止：** |
| `S_HELP` | Help | Допомога | **帮助** |
| `S_MSG_STARTED` | Recorder started: the LED glows blue. | Рекордер запущено: LED світиться синім. | **录制器已启动：LED 亮蓝色。** |
| `S_MSG_STOPPED` | Recorder stopped. | Рекордер зупинено. | **录制器已停止。** |
| `S_MSG_STOP_FAILED` | The recorder did not stop. | Рекордер не зупинився. | **录制器没有停止。** |
| `S_MSG_START_FAILED` | Could not start the recorder (%s, %08lX). | Не вдалося запустити рекордер (%s, %08lX). | **无法启动录制器（%s，%08lX）。** |
| `S_DELETING` | Deleting… | Видаляю… | **正在删除…** |
| `S_MSG_SYSTEM_STOP` | Recording of %s stopped because the console restarted or turned off (System Settings restart it on exit). It is saved. | Запис %s зупинився, бо консоль перезапустилась чи вимкнулась (Налаштування консолі перезапускають її при виході). Його збережено. | **%s 的录像因主机重启或关机而停止（退出系统设置会重启主机）。录像已保存。** |
| `S_MSG_RECOVERED` | Recording of %s was cut off (power or a crash): saved what was on the card. | Запис %s обірвався (вимкнення чи збій): збережено все, що встигло записатися. | **%s 的录像中断了（断电或崩溃）：已保存写入卡中的部分。** |
| `S_MSG_SOON` | This comes in a later update. | Це буде в одному з наступних оновлень. | **此功能将在后续更新中提供。** |

**`S_MSG_GAME_STOP`**

```text
EN  Recording of %s is saved. On Old 3DS a game that needs extra memory restarts the console when it closes, and the recording stops there.
UK  Запис %s збережено. На Old 3DS гра, якій треба більше пам'яті, перезапускає консоль при виході, і запис на цьому зупиняється.
ZH  %s 的录像已保存。在 Old 3DS 上，需要额外内存的游戏关闭时会重启主机，录像也就此停止。
```

## 首次运行 · 录制前检查

| 键 | English | Українська | 中文 |
|---|---|---|---|
| `S_FR_EYEBROW` | Checks before recording | Перевірка перед записом | **录制前检查** |
| `S_FR_ALMOST` | Almost ready | Майже готово | **即将就绪** |
| `S_FR_LUMA` | Luma3DS | Luma3DS | **Luma3DS** |
| `S_FR_LUMA_OK` | v%lu.%lu · supported | v%lu.%lu · підтримується | **v%lu.%lu · 支持** |
| `S_FR_LUMA_UNKNOWN` | not detected | не знайдено | **未检测到** |
| `S_FR_OPTION` | Luma: external modules | Luma: зовнішні модулі | **Luma：外部模块** |
| `S_FR_ON` | on | увімкнено | **开** |
| `S_FR_OFF` | off | вимкнено | **关** |
| `S_FR_MODULE` | Recorder module | Модуль рекордера | **录制器模块** |
| `S_FR_MODULE_OK` | installed | встановлено | **已安装** |
| `S_FR_MODULE_UPDATE` | will be updated | буде оновлено | **将更新** |
| `S_FR_MODULE_MISSING` | will be installed | буде встановлено | **将安装** |
| `S_FR_RUNNING` | Recorder running | Рекордер запущено | **录制器运行中** |
| `S_FR_RUNNING_NO` | no — after power-on | ні — після ввімкнення | **否 — 开机后启动** |
| `S_FR_SD` | Recordings on SD | Запис на SD | **SD 卡上的录像** |
| `S_FR_SD_FREE` | %s free | вільно %s | **剩余 %s** |
| `S_FR_START_TITLE` | Start the recorder | Запустіть рекордер | **启动录制器** |
| `S_FR_LED` | The LED glows blue for 1.5 s: ready | LED засвітиться синім на 1.5 с — готово | **LED 亮蓝色 1.5 秒：就绪** |
| `S_FR_LUMA_TITLE` | Turn on a Luma option | Увімкніть опцію Luma | **打开 Luma 选项** |
| `S_LATER` | Later | Пізніше | **稍后** |
| `S_START` | Start | Запустити | **启动** |

**`S_FR_START_BODY`**

```text
EN  The recorder is not running. Press Start. Then you can leave this app: the recorder keeps running until the console is turned off or restarts.
UK  Рекордер не запущено. Натисніть «Запустити». Потім з додатка можна виходити: рекордер працює, доки консоль не вимкнеться чи не перезапуститься.
ZH  录制器尚未运行。按「启动」。之后就可以离开本程序：录制器会一直运行，直到主机关机或重启。
```

**`S_FR_LUMA_BODY`**

```text
EN  Hold SELECT while turning the console on. In the Luma menu enable "Enable loading external FIRMs and modules", save with START, then open this app again.
UK  Тримайте SELECT під час увімкнення консолі. У меню Luma увімкніть «Enable loading external FIRMs and modules», збережіть START і знову відкрийте цей додаток.
ZH  开机时按住 SELECT。在 Luma 菜单中启用「Enable loading external FIRMs and modules」，按 START 保存，然后重新打开本程序。
```

说明：

- `S_FR_RUNNING_NO`：面板检查项的值：录制器未运行

## 帮助页

| 键 | English | Українська | 中文 |
|---|---|---|---|
| `S_HELP_TITLE` | Help | Допомога | **帮助** |
| `S_HELP_OF` | Help · %d of %d | Допомога · %d з %d | **帮助 · %d / %d** |

## 帮助 · 正文

| 键 | English | Українська | 中文 |
|---|---|---|---|
| `S_H1` | How to record | Як записувати | **如何录制** |
| `S_H2` | What the LED means | Що означає LED | **LED 的含义** |
| `S_H3` | After turning the console on | Після ввімкнення консолі | **开机之后** |
| `S_H4` | Getting a recording off | Як забрати запис | **取出录像** |
| `S_H5` | Hotkeys and limits | Хоткеї і обмеження | **快捷键与限制** |
| `S_H6` | If something is wrong | Якщо щось не так | **出问题时** |
| `S_H7` | Games that need extra memory | Ігри, яким треба більше пам'яті | **需要额外内存的游戏** |
| `S_H8` | Replay: the last 30 seconds | Повтор: останні 30 секунд | **回放：最近 30 秒** |
| `S_H9` | Launch on startup | Запуск з консоллю | **开机自启** |

**`S_H1_BODY`**

```text
EN  1. Open this app: the recorder starts by itself, the LED glows blue for a moment.
    2. Go to HOME and start a game. You can close the app: the recorder keeps running.
    3. Press %s: recording starts, the LED breathes red.
    4. The whole console is recorded: game, HOME, other apps, with sound, into one file.
    5. Press %s again: the recording is saved, the LED blinks green twice.
UK  1. Відкрийте цей додаток — рекордер запуститься сам, LED на мить засвітиться синім.
    2. Вийдіть у HOME і запустіть гру. Додаток можна закрити — рекордер працює далі.
    3. Натисніть %s — почнеться запис, LED «дихає» червоним.
    4. Пишеться вся консоль: гра, HOME, інші програми — в один файл, зі звуком.
    5. Ще раз %s — запис збережено, LED мигне зеленим двічі.
ZH  1. 打开本程序：录制器会自动启动，LED 亮蓝色一下。
    2. 回到 HOME 并启动游戏。程序可以关掉：录制器仍在运行。
    3. 按 %s：开始录制，LED 呈红色呼吸效果。
    4. 整个主机都会被录下来：游戏、HOME、其他程序，带声音，录进同一个文件。
    5. 再按一次 %s：录像已保存，LED 闪绿两次。
```

**`S_H2_BODY`**

```text
EN  Blue for 1.5 s: the recorder started and is ready.
    Red, breathing: recording.
    Faint blue, steady: Replay keeps the last 30 s.
    Green twice: a recording or a clip is saved.
    Red three times: an error, open this app.
    No light and the hotkey does nothing: the recorder is off, or the console was just turned on (see 3).
UK  Синій 1.5 с — рекордер запущено, готовий.
    Червоний «дихає» — іде запис.
    Слабкий синій, постійно — Повтор тримає останні 30 с.
    Зелений двічі — запис або кліп збережено.
    Червоний тричі — помилка, відкрийте додаток.
    LED не горить і хоткей не реагує — рекордер вимкнено або консоль щойно ввімкнули (розділ 3).
ZH  蓝色 1.5 秒：录制器已启动并就绪。
    红色呼吸：正在录制。
    暗蓝色常亮：回放功能正在保留最近 30 秒。
    绿色闪两次：录像或片段已保存。
    红色闪三次：出错了，请打开本程序。
    灯不亮且快捷键无反应：录制器已关闭，或主机刚开机（见第 3 节）。
```

**`S_H3_BODY`**

```text
EN  With Settings → Launch On Startup the recorder starts with the console by itself (see 9). Without it, the recorder starts when you open this app: after each power-on open the app once, that is all. Leaving the app does not stop it; to stop it until the app is opened again, switch Recorder off on the panel. Leaving System Settings and starting a DS or GBA game restart the console like turning it off: a recording is saved and stops there, and the recorder starts again when you open this app (or by itself with Launch On Startup). Closing the lid saves a recording; it goes on in a new file when the lid opens.
UK  Із «Налаштування → Запуск з консоллю» рекордер стартує разом з консоллю сам (див. 9). Без цього він запускається, коли ви відкриваєте цей додаток: після кожного ввімкнення консолі відкрийте додаток один раз — і все. Вихід з додатка його не зупиняє; щоб вимкнути його до наступного відкриття додатка, вимкніть «Рекордер» на пульті. Вихід з Налаштувань консолі й запуск DS- чи GBA-гри перезапускають консоль, як вимкнення: запис там зберігається і зупиняється, а рекордер знову запуститься, коли ви відкриєте додаток (або сам — із запуском з консоллю). Якщо закрити кришку під час запису, він збережеться, а після відкриття продовжиться новим файлом.
ZH  在「设置 → 开机自启」中开启后，录制器会随主机自动启动（见第 9 节）。未开启时，录制器在你打开本程序时启动：每次开机后打开一次本程序即可。退出程序不会停止它；要让它停止直到下次打开程序，请在面板上关闭「录制器」。退出系统设置、启动 DS 或 GBA 游戏都会像关机一样重启主机：录像会保存并停止，再次打开本程序时录制器会重新启动（开启开机自启则会自动启动）。合上盖子会保存当前录像；打开盖子后录到新文件里。
```

**`S_H4_BODY`**

```text
EN  Watch recordings in the Gallery (A) and download them to a phone over Wi-Fi (Y). While this app is open, the console converts each recording into a small MP4 in the background; it lies next to the recording in /3ds/recorder/recordings, so the SD card in a computer has it too.
UK  Записи можна дивитися в Галереї (A) і завантажувати на телефон по Wi-Fi (Y). Поки цей додаток відкритий, консоль у фоні конвертує кожен запис у невелике MP4; воно лежить поруч із записом у /3ds/recorder/recordings, тож є й на SD-карті в комп'ютері.
ZH  在录像库中观看录像（A），并通过 Wi-Fi 下载到手机（Y）。本程序打开期间，主机会在后台把每个录像转换成小的 MP4，它就放在录像旁边的 /3ds/recorder/recordings 里，所以插到电脑上的 SD 卡里也有。
```

**`S_H5_BODY`**

```text
EN  The recording hotkey is %s; Replay has its own for saving a clip (see 8). Change both in Settings → Hotkeys: first the recording one, then the Replay one; START keeps the current one. Not allowed: L + R together (opens the Camera in HOME), L + ↓ + SELECT (the Rosalina menu) or a part of it, START and HOME, and one hotkey holding all the buttons of the other. A long recording goes on in a new file every 4 GB or every hour (a 1-2 s gap); Settings shows how many minutes one file holds.
UK  Хоткей запису — %s; у Повтору свій, для збереження кліпу (розділ 8). Змінити обидва: Налаштування → Хоткеї — спершу хоткей запису, потім Повтору; START лишає поточний. Не можна: L + R разом (у HOME відкриває Камеру), L + ↓ + SELECT (меню Rosalina) чи її частину, START і HOME, а також хоткей, що містить усі кнопки іншого. Довгий запис продовжується в новому файлі кожні 4 GB або щогодини (пауза 1–2 с); скільки хвилин уміщає файл, видно в налаштуваннях.
ZH  录制快捷键是 %s；回放有自己保存片段的快捷键（见第 8 节）。两者都在「设置 → 快捷键」中修改：先改录制快捷键，再改回放快捷键；按 START 保留当前值。不允许：L + R 同时按（在 HOME 中会打开相机）、L + ↓ + SELECT（Rosalina 菜单）或其中一部分、START 和 HOME，以及一个快捷键包含另一个的全部按键。长时间录制每隔 4 GB 或每隔一小时会续写到新文件（有 1-2 秒间隔）；一个文件能录多少分钟会在设置中显示。
```

**`S_H6_BODY`**

```text
EN  Red three times: the recording did not start or stopped, usually because the SD card is full. Skipped frames: the SD card could not keep up, the video is still fine. A 3D game looks jerky in the video: set Settings → Quality → Auto.
    A game does not start or freezes while the recorder runs: switch Recorder off on the panel and play without it. Please tell us in Issues at github.com/BolgarMaxym97/3ds-recorder: name the game and the console, and attach the logs /3ds/recorder/recorder.log and app.log (or Download → Log for the developer).
UK  Червоний тричі — запис не почався або зупинився, найчастіше через заповнену SD-карту. Пропущені кадри — SD не встигала, відео при цьому ціле. 3D-гра у відео смикається — поставте Налаштування → Якість → Авто.
    Гра не запускається або зависає, поки працює рекордер — вимкніть «Рекордер» на пульті й грайте без нього. Будь ласка, напишіть про це в Issues на github.com/BolgarMaxym97/3ds-recorder: назвіть гру й консоль і додайте журнали /3ds/recorder/recorder.log та app.log (або Завантажити → Журнал для розробника).
ZH  红色闪三次：录制没有开始或中途停止，通常是因为 SD 卡满了。出现丢帧：SD 卡速度跟不上，但视频本身没有问题。3D 游戏在视频里卡顿：把「设置 → 质量」设为「自动」。
    录制器运行时游戏无法启动或卡死：在面板上关闭「录制器」后直接玩。请在 github.com/BolgarMaxym97/3ds-recorder 的 Issues 中告诉我们：说明游戏和主机型号，并附上日志 /3ds/recorder/recorder.log 和 app.log（或「下载 → 开发者日志」）。
```

**`S_H7_BODY`**

```text
EN  On Old 3DS some games need more memory: Smash Bros, Pokemon Sun / Moon and Ultra Sun / Ultra Moon, Super Mario Maker, Monster Hunter. The console restarts when they start and when they close. If the recorder runs, it comes back by itself inside the game through a tiny plugin of Luma, a recording goes on in a new file, and Replay works there too. Luma's Plugin Loader must be on for this (Rosalina menu, L + ↓ + SELECT); with Launch On Startup the recorder turns it on just for that game. The game has 2 MB less memory, and the video is less smooth: the console has less power and memory to spare there. For smoother video there, record only the top screen: Settings → Screens → Top. When such a game closes, the recording is saved; open this app to record again, or switch Launch On Startup on (see 9): the recorder then comes back by itself. New 3DS does not restart for these games.
UK  На Old 3DS деяким іграм треба більше пам'яті: Smash Bros, Pokemon Sun / Moon і Ultra Sun / Ultra Moon, Super Mario Maker, Monster Hunter. Консоль перезапускається, коли вони стартують і коли закриваються. Якщо рекордер працює, він сам повертається в гру через маленький плагін Luma, запис продовжується новим файлом, і Повтор там теж працює. Для цього в Luma має бути ввімкнений Plugin Loader (меню Rosalina, L + ↓ + SELECT); із запуском з консоллю рекордер сам вмикає його лише на цю гру. Грі лишається на 2 МБ менше пам'яті, а відео менш плавне: консолі там бракує потужності й пам'яті. Щоб відео було плавнішим, пишіть лише верхній екран: Налаштування → Екрани → Верхній. Коли така гра закривається, запис зберігається; щоб писати далі, відкрийте цей додаток або ввімкніть запуск з консоллю (див. 9) — тоді рекордер повернеться сам. New 3DS для цих ігор не перезапускається.
ZH  在 Old 3DS 上，有些游戏需要更多内存：大乱斗、宝可梦 太阳／月亮 和 究极之日／究极之月、超级马力欧创作家、怪物猎人。它们启动和关闭时主机会重启。如果录制器正在运行，它会通过 Luma 的一个小插件自动回到游戏内，录像续写到新文件，回放在那里也能用。为此需要打开 Luma 的 Plugin Loader（Rosalina 菜单，L + ↓ + SELECT）；开启开机自启时，录制器只会为这类游戏临时打开它。游戏可用内存会少 2 MB，视频也不那么流畅：主机在这里的运算能力和内存都更紧张。想让视频更流畅，可以只录上屏：「设置 → 画面 → 上屏」。这类游戏关闭时录像会保存；想继续录制就再打开本程序，或打开开机自启（见第 9 节），录制器会自己回来。New 3DS 运行这些游戏时不会重启。
```

**`S_H8_BODY`**

```text
EN  Switch Replay 30 s on (the panel). While a game or another program runs (not in the HOME Menu alone), the recorder keeps the last 30 seconds all the time, and the LED glows faint blue (from about 15 seconds after a game starts). Press %s (Settings → Hotkeys changes it) in a game or HOME: the LED blinks green twice and those seconds (a few more at times) become a clip. Open this app: after a short wait the clip is in the Gallery, like any recording.
    The hotkey for recordings works as before: the replay pauses while a recording runs and while this app is open.
    The replay writes to the SD card all the time (several GB an hour in a 3D game): the card wears. It keeps 512 MB of the card while it is on. After the console has been turned off, Replay is off again; with Launch On Startup it stays as you left it. On Old 3DS, games that need extra memory get fewer frames a second in it.
UK  Увімкніть «Повтор 30 с» (на панелі). Поки запущено гру чи іншу програму (не в самому меню HOME), рекордер постійно тримає останні 30 секунд, LED слабко світиться синім (через ~15 с після запуску гри). Натисніть %s (змінити: Налаштування → Хоткеї) у грі чи HOME: LED двічі мигне зеленим, і ці секунди (часом трохи більше) стануть кліпом. Відкрийте цей додаток: за якийсь час кліп з'явиться в Галереї, як звичайний запис.
    Хоткей запису працює як раніше: повтор стає на паузу, поки йде запис і поки відкрито цей додаток.
    Повтор постійно пише на SD-карту (кілька ГБ за годину в 3D-грі): карта зношується. Він займає 512 МБ на карті, поки ввімкнений. Після вимкнення консолі Повтор знову вимкнено; із запуском з консоллю він лишається таким, як ви його залишили. На Old 3DS в іграх, яким треба більше пам'яті, кадрів у ньому менше.
ZH  打开「回放 30 秒」（在面板上）。当游戏或其他程序运行时（单独停留在 HOME 菜单里不算），录制器会一直保留最近 30 秒，LED 呈暗蓝色（游戏开始约 15 秒后）。在游戏或 HOME 中按 %s（可在「设置 → 快捷键」中修改）：LED 闪绿两次，这几秒（有时会多一点）就成为一个片段。打开本程序：稍等片刻，片段就会像普通录像一样出现在录像库里。
    录制快捷键照旧：录制进行中以及本程序打开时，回放会暂停。
    回放会一直往 SD 卡写入（3D 游戏中每小时几 GB）：会磨损存储卡。开启时它占用卡上 512 MB 空间。主机关机后回放会再次关闭；开启开机自启时它会保持你留下的状态。在 Old 3DS 上，需要额外内存的游戏中回放的帧数会更少。
```

**`S_H9_BODY`**

```text
EN  Settings → Launch On Startup (off at first). The recorder then starts by itself each time the console is turned on or restarts: no need to open this app, and Replay stays as you left it. On Old 3DS it also comes back after a game that needs extra memory closes.
    It needs two options in Luma's menu (hold SELECT while turning the console on): "Enable loading external FIRMs and modules" and "Enable game patching".
    It adds one small file for Luma to the SD card; the console's own memory is not changed. If the console ever fails to start with it, turn the console on again: the recorder switches Launch On Startup off by itself. If that does not help, hold SELECT at power-on and turn "Enable game patching" off.
    Before deleting the recorder's files by hand, switch this off or use Settings → Uninstall recorder.
UK  Налаштування → Запуск з консоллю (спершу вимкнено). Тоді рекордер стартує сам щоразу, коли консоль вмикається чи перезапускається: відкривати цей додаток не треба, а Повтор лишається таким, як ви його залишили. На Old 3DS він повертається і після закриття гри, якій треба більше пам'яті.
    Потрібні дві опції в меню Luma (тримайте SELECT під час увімкнення консолі): «Enable loading external FIRMs and modules» і «Enable game patching».
    На SD-карту додається один маленький файл для Luma; пам'ять самої консолі не змінюється. Якщо консоль колись не запуститься, увімкніть її ще раз — рекордер сам вимкне запуск з консоллю. Якщо не допомогло, тримайте SELECT під час увімкнення і вимкніть «Enable game patching».
    Перш ніж видаляти файли рекордера вручну, вимкніть цю опцію або скористайтесь «Налаштування → Видалити рекордер».
ZH  「设置 → 开机自启」（初始为关闭）。开启后，每次主机开机或重启时录制器都会自动启动：不必再打开本程序，回放也保持你留下的状态。在 Old 3DS 上，需要额外内存的游戏关闭后它也会自动恢复。
    它需要 Luma 菜单中的两个选项（开机时按住 SELECT）：「Enable loading external FIRMs and modules」和「Enable game patching」。
    它会在 SD 卡上为 Luma 添加一个小文件，不会改动主机自身的存储。如果主机因此无法启动，请再开一次机：录制器会自动关闭开机自启。如果仍不行，开机时按住 SELECT，关闭「Enable game patching」。
    手动删除录制器文件之前，请先关闭此选项，或使用「设置 → 卸载录制器」。
```

## 设置页 · 开机自启

| 键 | English | Українська | 中文 |
|---|---|---|---|
| `S_AUTOSTART` | Launch On Startup | Запуск з консоллю | **开机自启** |
| `S_MSG_AUTO_ON` | Launch On Startup is on: the recorder now starts with the console. | Запуск з консоллю ввімкнено: тепер рекордер стартує разом з консоллю. | **开机自启已开启：录制器现在随主机启动。** |
| `S_MSG_AUTO_OFF` | Launch On Startup is off. | Запуск з консоллю вимкнено. | **开机自启已关闭。** |
| `S_MSG_AUTO_LATER` | Launch On Startup is saved: it is set up once the recorder runs and no recording is under way. | Запуск з консоллю збережено: він налаштується, коли рекордер працює і не йде запис. | **开机自启已保存：会在录制器运行且没有正在进行的录像时完成设置。** |

**`S_AUTOSTART_NOTE`**

```text
EN  Launch On Startup: the recorder starts with the console, also after it restarts, and Replay stays as you left it. Needs "Enable game patching" in Luma's menu. More in Help, 9.
UK  Запуск з консоллю: рекордер стартує разом з консоллю, і після її перезапуску теж, а Повтор лишається таким, як ви його залишили. Потрібна опція «Enable game patching» у меню Luma. Докладніше: Допомога, 9.
ZH  开机自启：录制器随主机启动，重启后也会启动，回放保持你留下的状态。需要 Luma 菜单中的「Enable game patching」。详见帮助第 9 节。
```

**`S_MSG_AUTO_PATCHING`**

```text
EN  Launch On Startup needs a Luma option: hold SELECT while turning the console on, enable "Enable game patching" and save with START.
UK  Для запуску з консоллю потрібна опція Luma: тримайте SELECT під час увімкнення консолі, увімкніть «Enable game patching» і збережіть START.
ZH  开机自启需要 Luma 的一个选项：开机时按住 SELECT，启用「Enable game patching」并按 START 保存。
```

**`S_MSG_AUTO_UNSUPPORTED`**

```text
EN  Launch On Startup could not be set up on this console (see /3ds/recorder/recorder.log). Nothing was changed.
UK  На цій консолі запуск з консоллю налаштувати не вдалося (див. /3ds/recorder/recorder.log). Нічого не змінено.
ZH  无法在这台主机上设置开机自启（见 /3ds/recorder/recorder.log）。没有做任何改动。
```

**`S_MSG_AUTO_FAILED`**

```text
EN  The console did not start properly with Launch On Startup, so the recorder switched it off. Details are in /3ds/recorder/recorder.log.
UK  Консоль не запустилась як слід із запуском з консоллю, тож рекордер його вимкнув. Подробиці — у /3ds/recorder/recorder.log.
ZH  主机在有开机自启的情况下没能正常启动，录制器已自动关闭该功能。详情见 /3ds/recorder/recorder.log。
```

## 面板 · 回放 30 秒

| 键 | English | Українська | 中文 |
|---|---|---|---|
| `S_REPLAY` | Replay 30 s | Повтор 30 с | **回放 30 秒** |
| `S_TILE_RECORDER_ON_SHORT` | Hotkey works | Хоткей працює | **快捷键可用** |
| `S_TILE_RECORDER_OFF_SHORT` | Hotkey does nothing | Хоткей не працює | **快捷键无效** |
| `S_TILE_REPLAY_ON` | Clip: %s | Кліп: %s | **片段：%s** |
| `S_TILE_REPLAY_OFF` | Keeps the last 30 s | Тримає останні 30 с | **保留最近 30 秒** |
| `S_MSG_REPLAY_ON` | Replay is on. In a game or HOME press %s to save the last 30 seconds. | Повтор увімкнено. У грі чи HOME натисніть %s, щоб зберегти останні 30 секунд. | **回放已开启。在游戏或 HOME 中按 %s 保存最近 30 秒。** |
| `S_MSG_REPLAY_OFF` | Replay is off. | Повтор вимкнено. | **回放已关闭。** |
| `S_MSG_REPLAY_SPACE` | Replay needs 700 MB free on the SD card. | Для повтору треба 700 МБ вільного місця на SD-карті. | **回放需要 SD 卡上有 700 MB 可用空间。** |
| `S_CLIP_PCT` | Saving clip %d%% | Зберігаю кліп %d%% | **正在保存片段 %d%%** |
| `S_GAL_CLIP` | Replay | Повтор | **回放** |
| `S_CLIP_WAIT` | Saving clip… | Зберігаю кліп… | **正在保存片段…** |
| `S_CLIP_MORE` | %s · %d more | %s · ще %d | **%s · 还有 %d 个** |
| `S_MSG_CLIPS` | Clips are being saved: %d. Each appears in the Gallery when it is ready; keep this app open. | Зберігаю кліпи: %d. Кожен з'явиться в Галереї, щойно буде готовий; не закривайте додаток. | **正在保存片段：%d 个。每个准备好后都会出现在录像库里；请保持本程序打开。** |

说明：

- `S_CLIP_MORE`：回放片段排队时的「%s · %d more」

## 设置页

| 键 | English | Українська | 中文 |
|---|---|---|---|
| `S_SETTINGS` | Settings | Налаштування | **设置** |
| `S_LANGUAGE` | Language · Мова | Мова · Language | **语言 · Language** |
| `S_UNINSTALL_ROW` | Uninstall recorder… | Видалити рекордер… | **卸载录制器…** |
| `S_QUALITY` | Quality | Якість | **质量** |
| `S_Q_AUTO` | Auto | Авто | **自动** |
| `S_Q_LOSSLESS` | Lossless | Без втрат | **无损** |
| `S_SOUND` | Sound | Звук | **声音** |
| `S_LED` | LED | LED | **LED** |
| `S_LED_PULSE` | Pulse | Пульс | **呼吸** |
| `S_LED_SOLID` | Solid | Постійно | **常亮** |
| `S_LED_OFF` | Off | Вимк. | **关闭** |
| `S_HOTKEY` | Hotkeys | Хоткеї | **快捷键** |

说明：

- `S_LANGUAGE`：设置页那一行的标题；原英文是 `Language · Мова`，中文按「当前语言 · 另一种语言」写

## 设置页 · 文件内容卡片

| 键 | English | Українська | 中文 |
|---|---|---|---|
| `S_FILE_TITLE` | What goes into the file | Що вийде у файлі | **文件内容** |
| `S_FRAME_IN_FILE` | Frame in the file | Кадр у файлі | **文件中的画面** |
| `S_TOP_BOX` | top 400×240 | верхній 400×240 | **上屏 400×240** |
| `S_BOTTOM_BOX` | bottom 320×240 | нижній 320×240 | **下屏 320×240** |
| `S_CODEC` | Codec | Кодек | **编码** |
| `S_CODEC_VAL` | XR32 · lossless | XR32 · без втрат | **XR32 · 无损** |
| `S_CODEC_AUTO` | XR32 + C420 | XR32 + C420 | **XR32 + C420** |
| `S_STREAM` | To the SD card | Потік на SD | **写入 SD 卡** |
| `S_PER_MIN` | One minute | Хвилина запису | **每分钟** |
| `S_FITS` | Fits on the SD card | Влізе на SD | **SD 卡可容纳** |

**`S_SETTINGS_NOTE`**

```text
EN  Frame rate, screens, sound and LED apply from the next recording, the hotkeys right away. One file holds up to 4 GB, about %u min.
UK  Частота, екрани, звук і LED діють з наступного запису, хоткеї — одразу. Один файл — до 4 GB, це ≈ %u хв.
ZH  帧率、画面、声音和 LED 从下一次录制起生效，快捷键立即生效。单个文件最大 4 GB，约 %u 分钟。
```

## 设置页 · 快捷键

| 键 | English | Українська | 中文 |
|---|---|---|---|
| `S_HK_SCREEN` | 1 of 2 · Start and stop a recording | 1 з 2 · Почати і зупинити запис | **1 / 2 · 开始和停止录制** |
| `S_HK_SCREEN2` | 2 of 2 · Save the last 30 s (Replay) | 2 з 2 · Зберегти останні 30 с (Повтор) | **2 / 2 · 保存最近 30 秒（回放）** |
| `S_HK_ERR_OTHER` | It shares all its buttons with the recording hotkey: both would fire. | Усі її кнопки є в хоткеї запису: спрацювали б обидва. | **它的按键全都包含在录制快捷键里：两个会同时触发。** |
| `S_HK_KEEP` | Keep | Залишити | **保留** |
| `S_HK_SAVED2` | Replay hotkey saved: %s. It works right away. | Хоткей повтору збережено: %s. Він уже діє. | **回放快捷键已保存：%s。立即生效。** |
| `S_HK_HOLD_TITLE` | Hold the new combination | Затисніть нову комбінацію | **按住新的组合键** |
| `S_HK_HOLD_HINT` | Hold for 1 s to set it · 2–3 buttons | Тримайте 1 с, щоб зафіксувати · 2–3 кнопки | **按住 1 秒设定 · 2–3 个按键** |
| `S_HK_TOO_MANY` | At most 3 buttons | Не більше 3 кнопок | **最多 3 个按键** |
| `S_HK_NOW` | Now | Зараз | **当前** |
| `S_HK_REVIEW_TITLE` | New combination | Нова комбінація | **新组合键** |
| `S_HK_ERR_LR` | L + R together is not allowed: in HOME it opens the Camera. | L + R разом не можна: у HOME ця пара відкриває Камеру. | **不能同时用 L + R：在 HOME 中会打开相机。** |
| `S_HK_ERR_ROSALINA` | This is part of L + ↓ + SELECT, the Rosalina menu. | Це частина L + ↓ + SELECT — меню Rosalina. | **这是 L + ↓ + SELECT（Rosalina 菜单）的一部分。** |
| `S_HK_OK` | This combination can be used. | Цю комбінацію можна використати. | **可以使用这个组合。** |
| `S_HK_KEYS_CAPTURE` | START: keep the current one | START: залишити поточний | **START：保留当前** |
| `S_HK_KEYS_RETRY` | B: again · START: keep the current one | B: ще раз · START: залишити поточний | **B：重试 · START：保留当前** |
| `S_HK_KEYS_REVIEW` | A: save · B: again · START: keep | A: зберегти · B: ще раз · START: залишити | **A：保存 · B：重试 · START：保留** |
| `S_RESET` | Reset | Скинути | **重置** |
| `S_SAVE` | Save | Зберегти | **保存** |
| `S_HK_SAVED` | Hotkey saved: %s. It works right away. | Хоткей збережено: %s. Він уже діє. | **快捷键已保存：%s。立即生效。** |

**`S_HK_ERR_FACE`**

```text
EN  Only A / B / X / Y is too easy to press in a game. Add SELECT, L or R.
UK  Лише A / B / X / Y легко натиснути в грі. Додайте SELECT, L або R.
ZH  只用 A / B / X / Y 在游戏中太容易误按。请加上 SELECT、L 或 R。
```

**`S_HK_RULES`**

```text
EN  Not allowed: L + R together (Camera in HOME), L + ↓ + SELECT (Rosalina), START.
UK  Не можна: L + R разом (Камера в HOME), L + ↓ + SELECT (Rosalina), START.
ZH  不允许：L + R 同时按（HOME 中打开相机）、L + ↓ + SELECT（Rosalina）、START。
```

说明：

- `S_HK_SAVED2`：保存回放快捷键后的提示

## 卸载

| 键 | English | Українська | 中文 |
|---|---|---|---|
| `S_UN_EYEBROW` | Settings · Uninstall recorder | Налаштування · Видалити рекордер | **设置 · 卸载录制器** |
| `S_UN_TITLE` | Full removal | Повне видалення | **完全移除** |
| `S_UN_MODULE` | Recorder module | Модуль рекордера | **录制器模块** |
| `S_UN_MODULE_SUB` | stops and leaves Luma | зупиниться й зникне з Luma | **停止并从 Luma 中移除** |
| `S_UN_SETTINGS` | Settings and log | Налаштування і лог | **设置和日志** |
| `S_UN_APP` | This app | Цей додаток | **本程序** |
| `S_UN_APP_CIA` | icon in HOME | іконка в HOME | **HOME 中的图标** |
| `S_UN_RECORDINGS` | Recordings | Записи | **录像** |
| `S_UN_RECORDINGS_KEEP` | kept unless ticked | лишаються, якщо не обрано | **不勾选则保留** |
| `S_UN_ASK` | Uninstall the recorder? | Видалити рекордер? | **卸载录制器？** |
| `S_UN_ASK_BODY` | The console goes back to how it was without the recorder. | Консоль повернеться до стану без рекордера. | **主机会恢复到没有录制器时的状态。** |
| `S_UN_ALSO` | Also delete %lu recordings (%s) | Також видалити записи: %lu (%s) | **同时删除 %lu 个录像（%s）** |
| `S_CANCEL` | Cancel | Скасувати | **取消** |

说明：

- `S_UN_APP_CIA`：卸载列表里的「本程序」副标题，CIA 版显示这一条
- `S_UN_ALSO`：卸载对话框的勾选项，%lu 个录像 + 大小

## 手机下载页（主机上的二维码页面）

| 键 | English | Українська | 中文 |
|---|---|---|---|
| `S_PH_EYEBROW` | Phone and console on one Wi-Fi | Телефон і консоль в одній Wi-Fi | **手机与主机连接同一个 Wi-Fi** |
| `S_PH_TITLE` | Point the phone's camera at the code | Наведіть камеру телефону на код | **用手机摄像头对准二维码** |
| `S_PH_BODY` | The console converts the recording into a small MP4 video, the phone downloads and saves it: nothing to install. | Консоль конвертує запис у невелике відео MP4, а телефон його завантажує й зберігає — програми ставити не треба. | **主机会把录像转换成小的 MP4 视频，手机下载并保存：无需安装任何程序。** |
| `S_PH_CONNECTED` | Phone connected | Телефон підключено | **手机已连接** |
| `S_PH_WAITING` | Waiting for the phone | Чекаю на телефон | **等待手机连接** |
| `S_PH_IDLE` | Scan the code: the phone starts the download by itself. | Відскануйте код — телефон сам почне завантаження. | **扫描二维码：手机会自动开始下载。** |
| `S_PH_SLOW` | Keep the lid open until the phone has the video. | Не закривайте кришку, поки телефон не отримає відео. | **在手机收到视频前请不要合上盖子。** |
| `S_PH_STOP` | Stop | Зупинити | **停止** |
| `S_PH_NO_WIFI` | Wi-Fi is off | Wi-Fi вимкнено | **Wi-Fi 已关闭** |
| `S_PH_FAILED` | Could not start sending | Не вдалося почати передачу | **无法开始发送** |
| `S_PH_FAILED_BODY` | The network did not start. Check Wi-Fi and press A to try again. | Мережа не запустилась. Перевірте Wi-Fi і натисніть A, щоб спробувати ще раз. | **网络没有启动。请检查 Wi-Fi 后按 A 重试。** |
| `S_PH_RETRY` | Try again | Ще раз | **重试** |
| `S_PH_LEFT` | ≈ %u min | ≈ %u хв | **约 %u 分钟** |
| `S_PH_SENDING` | Sending | Передача | **发送中** |
| `S_PH_PICK` | Pick a recording and press Y to download it to the phone. | Виберіть запис і натисніть Y, щоб завантажити його на телефон. | **选择一个录像并按 Y 下载到手机。** |
| `S_PH_HINT` | Download | Завантажити | **下载** |
| `S_PH_READY` | Ready | Готово | **就绪** |
| `S_PH_PREPARING` | Converting | Конвертую | **转换中** |
| `S_PH_PREP_BODY` | The console converts the recording into a small video; the phone waits and then downloads it by itself. | Консоль конвертує запис у невелике відео; телефон зачекає й сам його завантажить. | **主机会把录像转换成小视频；手机会等待并自动下载。** |
| `S_PH_PREP_FAILED` | Could not convert the recording: the phone gets the original. | Не вдалося сконвертувати запис: телефон отримає оригінал. | **无法转换录像：手机将收到原始文件。** |

**`S_PH_SD`**

```text
EN  Without Wi-Fi: turn the console off, take out the SD card and put it in a computer. Recordings are in /3ds/recorder/recordings.
UK  Можна й без Wi-Fi: вимкніть консоль, вийміть SD-карту й підключіть до комп'ютера — записи в /3ds/recorder/recordings.
ZH  没有 Wi-Fi 时：关机，取出 SD 卡并插入电脑。录像在 /3ds/recorder/recordings。
```

**`S_PH_NO_WIFI_BODY`**

```text
EN  Turn Wi-Fi on (the switch on the console, or HOME → settings) and connect to the network the phone is on. Then press A.
UK  Увімкніть Wi-Fi (перемикач на консолі або HOME → налаштування) і підключіться до тієї ж мережі, що й телефон. Потім натисніть A.
ZH  打开 Wi-Fi（主机上的开关，或 HOME → 设置）并连接到手机所在的网络，然后按 A。
```

说明：

- `S_PH_LEFT`：手机页剩余时间，原文只有「≈ %u min」

## 录像库 · 转换状态

| 键 | English | Українська | 中文 |
|---|---|---|---|
| `S_GAL_PREP_READY` | Ready for download | Готово до завантаження | **可下载** |
| `S_GAL_PREP_PCT` | Converting %d%% | Конвертую %d%% | **转换中 %d%%** |
| `S_GAL_PREP_FAILED` | Not converted | Не сконвертовано | **未转换** |

## 播放器

| 键 | English | Українська | 中文 |
|---|---|---|---|
| `S_PLAY_FAILED` | Could not open the recording. | Не вдалося відкрити запис. | **无法打开录像。** |
| `S_PL_SEEK` | ±10 s | ±10 с | **±10 秒** |
| `S_PL_PAUSE` | Pause | Пауза | **暂停** |
| `S_PL_BACK` | Gallery | У галерею | **录像库** |
| `S_PL_SOUND` | sound | звук | **声音** |
| `S_PL_NO_DSP` | No sound: the DSP firmware is missing (run DSP1 once). | Без звуку: немає прошивки DSP (запустіть DSP1 один раз). | **没有声音：缺少 DSP 固件（运行一次 DSP1）。** |
| `S_PL_TOP_ONLY` | Only the top screen was recorded | Записано лише верхній екран | **只录了上屏** |
| `S_PL_BOTTOM_ONLY` | Only the bottom screen was recorded | Записано лише нижній екран | **只录了下屏** |

## 录像库

| 键 | English | Українська | 中文 |
|---|---|---|---|
| `S_GAL_NTH` | Recording %d of %d | Запис %d з %d | **第 %d 个，共 %d 个** |
| `S_DURATION` | Length | Тривалість | **时长** |
| `S_SIZE` | Size | Розмір | **大小** |
| `S_DROPPED` | Frames skipped | Пропущено кадрів | **丢弃帧数** |
| `S_WITH_SOUND` | with sound | зі звуком | **有声音** |
| `S_NO_SOUND` | no sound | без звуку | **无声音** |
| `S_BOTH_SCREENS` | both screens | обидва екрани | **双屏** |
| `S_TOP_SCREEN` | top screen | верхній екран | **上屏** |
| `S_BOTTOM_SCREEN` | bottom screen | нижній екран | **下屏** |
| `S_NOT_CLOSED` | Cut off (power or a crash): what reached the card is saved. | Обірвався (вимкнення чи збій): збережено, що встигло записатися. | **中断（断电或崩溃）：已保存写入卡中的部分。** |
| `S_GAL_CUT` | Cut off | Обірвався | **已中断** |
| `S_UNREADABLE` | This file can't be read. | Цей файл не читається. | **无法读取此文件。** |
| `S_PLAY` | Play | Відтворити | **播放** |
| `S_DELETE` | Delete | Видалити | **删除** |
| `S_OPEN` | Open | Відкрити | **打开** |
| `S_GAL_LOADING` | Reading the SD card… | Читаю SD-картку… | **正在读取 SD 卡…** |
| `S_DEL_TITLE` | Delete this recording? | Видалити цей запис? | **删除这个录像？** |
| `S_DEL_BODY` | %s · %s. The file is removed from the SD card. | %s · %s. Файл буде видалено з SD-картки. | **%s · %s。文件将从 SD 卡中删除。** |
| `S_DEL_BTN` | Delete | Видалити | **删除** |
| `S_DELETED` | Recording deleted. | Запис видалено. | **录像已删除。** |
| `S_DEL_FAILED` | Could not delete the recording. | Не вдалося видалити запис. | **无法删除录像。** |

说明：

- `S_GAL_NTH`：录像库第几个，原文「Recording %d of %d」

## 卸载 · 执行与结果

| 键 | English | Українська | 中文 |
|---|---|---|---|
| `S_UNINSTALL` | Uninstall | Видалити | **卸载** |
| `S_UN_WORKING` | Uninstalling… | Видаляю… | **正在卸载…** |
| `S_UN_DONE` | Uninstalled | Видалено | **已卸载** |
| `S_UN_PARTIAL` | Some files could not be removed | Деякі файли не вдалося видалити | **部分文件无法删除** |

**`S_UN_DONE_BODY`**

```text
EN  3DS Recorder is removed. Luma settings were not changed: if you turned on external modules only for it, you can turn the option off.
UK  3DS Recorder видалено. Налаштування Luma не змінювались: якщо ви вмикали зовнішні модулі лише для нього, опцію можна вимкнути.
ZH  3DS Recorder 已移除。Luma 设置没有改动：如果你只是为了它才开启外部模块，可以关闭该选项。
```

**`S_UN_PARTIAL_BODY`**

```text
EN  Delete what is left by hand: /luma/sysmodules/0004013000F1D302.cxi and this app (Data Management for the HOME icon).
UK  Видаліть залишки вручну: /luma/sysmodules/0004013000F1D302.cxi і цей додаток (іконку — в «Керуванні даними»).
ZH  请手动删除剩余文件：/luma/sysmodules/0004013000F1D302.cxi 和本程序（HOME 图标请到「数据管理」中删除）。
```

## 通用按钮

| 键 | English | Українська | 中文 |
|---|---|---|---|
| `S_EXIT` | Exit | Вийти | **退出** |
| `S_BACK` | Back | Назад | **返回** |
| `S_OK` | OK | OK | **确定** |

## 表外文本（各语言一律原样）

| 位置 | 文本 |
|---|---|
| app.c `draw_lang_top` / `LANG_NAME` / `LANG_PROMPT` | Choose your language · Оберіть мову · 选择语言、English / Українська / 中文（语言页三张卡片） |
| app.c 面板与标题 | 3DS Recorder <版本> cn · New 3DS / Old 3DS、REC 圆标、XR32、%d fps |
| app.c 单位与数字 | MB / GB、≈ %lu.%lu MB/s、≈ %lu MB、%llu MB · <N 个录像> |
| app.c 快捷键标签 | L / R / A / B / X / Y / SELECT / ↑ ↓ ← →（键位名，不译） |
| app.c 设置「文件内容」 | XR32 · 无损里的 XR32、XR32 + C420、400×240、320×240（编码与分辨率） |
| app.c 卸载列表 | config.ini, recorder.log、3ds-recorder.3dsx（文件名） |
| app.c 帮助页脚注 | Telegram · t.me/side_quest_ua（作者频道） |
| app.c 引导页图示 | REC、×2（LED 示意） |
