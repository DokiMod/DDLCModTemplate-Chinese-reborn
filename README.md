> This mod template fork is designed for creators in Chinese to make their DDLC mods. You might be interested in the [original English mod template project](https://github.com/Bronya-Rand/DDLCModTemplate2.0) if you mainly use English to create DDLC mods.

> 在该版本模板完善之前，请勿将该版本模板用于创作模组。

# DDLC 中文 Mod 模板（重生版）

<p align="center">
  <img src=".github/IMAGES/Logos/SmallBronyaLogo.png" width=250px/>
</p>

---

**使用此模板之前请注意！本项目包含对 DDLC 的剧透。我们希望您能在通关 DDLC 原作后使用该模板进行模组开发，以避免影响游戏体验。**

**您仍需为自己的心理健康做周全的考虑。DDLC 本质上为心理恐怖游戏，并不适合所有玩家，且游戏内已经做了充足的提醒。心理健康比一切都重要。**

---

重新出发的文学社创作，就此开始！这里是全新的 DDLC 中文 Mod 模板（重生版），基于 Azariel Del Carmen (bronya_rand) 制作的 [DDLC Mod Template](https://github.com/GanstaKingofSA/DDLCModTemplate2.0) 进行翻译，并整合了过往汉化模板的功能。整个模板遵循 [Team Salvato 的知识产权（IP）准则](https://teamsalvato.com/ip-guidelines/) 针对饭制模组的规定，并支持 Ren'Py 6.99.12.4 与 7.3.5+ 版本。

> 针对原项目的贡献者名录，请参阅 [此处](./CREDITS.md)。

> Ren'Py 8 支持目前暂时不是本模板的重心，请稍作等待。

### 免责声明
   - <u>Team Salvato</u>
      > 本模板内含的代码 / 文件仅针对需要使用 DDLC 原版素材与 Ren'Py 的 DDLC 饭制游戏或模组。请勿将此模板用于制作与 DDLC 无关的项目。原版 DDLC Mod Template 与 DDLC 中文 Mod 模板均与 Team Salvato 没有任何关联。
   - <u>bronya_rand</u>
      > 请勿将此模板用于制作非官方 DDLC 修补工具等。
   - <u>DokiMod (imgradeone)</u>
      > 使用 DDLC 中文 Mod 模板并不意味着您可以在中国大陆的平台正常发布与 DDLC 有关的内容。

### **署名要求**

依照原模版规定，如需使用 DDLC 中文 Mod 模板（重生版），您必须在模组的制作人员名单或 `credits.txt` 文件中对模板的原作及翻译团队署名。下方为您提供了参考用例：
   > 本模组借助由 bronya_rand 开发、DokiMod 社区翻译的 DDLC 中文 Mod 模板制作: https://github.com/DokiMod/DDLCModTemplate-Chinese-reborn

默认情况下，署名功能已在游戏中启用。它可能在“额外功能”屏幕的“关于”按钮，也可能是游戏内的其他按钮（如果额外功能屏幕被禁用了）。

这里还有一些备选（但也十分欢迎）的署名方案（在改）：
   1. 将 Team Salvato 的 Logo（或 / 和您模组的标志）与 `Bronya Rand` 标志（素材可在 [此处](.github/IMAGES/Logos) 获取）放置在游戏的启动屏幕。
   2. 在游戏的免责声明文案中提及模组借助 bronya_rand 开发、DokiMod 翻译的模组模板进行开发。
   3. 添加包含 `Bronya Rand` 标志（素材可在 [此处](.github/IMAGES/Logos) 获取）的启动前屏幕。
   4. Present a custom idea to me for approval either through Discord or Reddit.

### 模板功能
1. 使用 Ren'Py 6* / 7 构建，且兼容 Team Salvato 内容的模组 + 启动屏幕（免责声明）！
   > \* - 为跟随 Ren'Py 的开发生命周期，上游模板针对 Ren'Py 6 的支持将在未来终止，中文 Mod 模板也将同时不再支持 Ren'Py 6。我们 **高度** 建议您升级到 Ren'Py 7 以进行模组开发。[了解更多（英文）](https://www.reddit.com/r/DDLCMods/wiki/notices/#wiki_why_is_the_megathread_and_other_users_recommending_me_to_create_my_mod_in_ren.27py_7.3F)
2. DDLC 的原版 RPY 文件，辅以（中文？）注释。
3. 支持 macOS、Linux* 与 Android**！
   > \* - Linux 用户需要使用 `LinuxLauncher.sh` 来运行模组。

   > \*\* - 若您的模组使用简易代码与 Mod 模板内置功能。更复杂的代码、手机端不友好的功能可能需要修改。See *Android Mod Guide.pdf* or visit the DDMC Discord for additional help.
4. Xcode 支持！直接在 Xcode 打开工程，无需启动 Ren'Py 启动器即可编辑、构建、测试模组！
    > 备注：您需要在 Xcode 里修改 `RENPY_TOOL`，使其指向您安装的 Ren'Py SDK 应用位置。[Learn more &rsaquo;](XCODE.md)
5. “遮羞布解除”和“实况共玩”模式！增强内容容许度，同时保护实况主的信息，更支持自动识别部分直播 / 录屏软件并自动启用实况模式。
6. 全自动界面配色 + 菜单按钮颜色定制！随心为游戏内界面与菜单按钮修改配色，无需修改原文件！
7. Terra's in-depth Poem Game guide!
8. 由 Yagamirai01 贡献的 NVL 支持！
9. 针对部分 Ren'Py 版本及 Windows 功能的补丁。
10. 动态超分辨率 (DSR/DSP) + 自定义分辨率！动态超分辨率 (DSR/DSP) + 自定义分辨率！Scale positions and/or your assets higher than they usually can go and display DDLC in different resolution modes. 尽情调节分辨率吧！
11. 玩家名称更改！听说你手抖打错字了？现在您可以轻松更改玩家名称了！
12. 新版莫妮卡终端和赏诗反应脚本！总之就是用起来更轻松了。
13. 特效改进！

此外，模板还提供了部分可选的额外功能：
- **[BETA]** 人称支持！让玩家随心选择符合自己的人称代词！
- 绝赞·完美“蓝屏死机”画面！轻松显示“蓝屏死机”画面，支持各类操作系统！（汉化版本仍在重制）
- 图库菜单、成就菜单！让玩家欣赏游戏画作，并且在游玩过程中获得更多成就！

### 中文模板（重生版）更新内容与特色功能

1. 更规范、更完善的中文翻译，包括代码注释。
2. 支持原生 Ren'Py 文件结构方式。
3. 拓展了直播 / 录屏软件的识别列表（包括 Twitch Studio、Gamecaster、哔哩哔哩直播姬[^1]、Bandicam 等）。
4. 合入了来自 DDLC Plus 的（新）汉化文本（感谢 Riotloc 团队以及社区汉化参与者）。
5. 整合社区版、Plus 版诗歌内容翻译。

### 恢复功能
1. Ghost Menu. (Dan's spooky easter egg)
2. Sayori Kill Script (plays if Sayori is deleted before the game starts).
3. Monika Kill Script (plays if Monika is deleted before a new game starts).
4. Special Poems! (The random poems in DDLC that appear in Act 2) <u>[now improved!]</u>.

[^1]: 实况共玩模式无法改变 DDLC 在中国大陆的屏蔽现状，因此请不要在中国大陆的平台直播与 DDLC 有关的内容。同时，无论如何，请注意安全。