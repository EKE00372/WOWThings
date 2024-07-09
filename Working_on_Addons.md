# Working on Addons

工作紀錄，避免忘記有改過什麼插件

## 翻譯

* ~~AltzUI：WOWInterface 反饋~~
* Bigwigs：
* ClassicCodex：模仿pfQuest導入了芒果單機的資料
   * 資料來源本身就有錯誤，後來改了抓取方式
* wMarker：zhTW/zhCN，後來出過作者自己機翻新詞條卻銘謝我，讓我被朋友打了（並沒有）的事
* [Bigwigs](https://github.com/BigWigsMods/BigWigs/commits?author=EKE00372)：主zhTW偶爾zhCN
  * 此外協力資料收集
    * 資料收集並不針對特定對象，可以查看[本項目的ReadMe](https://github.com/EKE00372/WOWThings/blob/master/README.md)。
* [LittleWigs](https://github.com/BigWigsMods/LittleWigs/commits?author=EKE00372)：主zhTW偶爾zhCN
* BFAInvasionTimer
* LegionInvasionTimer
* [Questie](https://github.com/AeroScripts/QuestieDev/commits?author=EKE00372)：zhTW/zhCN
    * 多語系任務資料錄入 (Item/Quest/NPC)，Vanilla 和 TBC 的 zhTW/zhCN，WLK 和 CATA 的全語系
* [Guidelime](https://github.com/max-ri/Guidelime/commits?author=EKE00372)
    * zhTW/zhCN
    * 關於WORD_LIST系列的詞條：這個東西只在「在遊戲內使用插件的導入工具導入一個中文版的指南文本」時才會發揮作用，也就是說只有在下面四種條件都成立的情況下才會發揮作用。向作者Borick詢問後，他的建議是不必去翻譯這些東西：
        * 編寫的語言是中文
        * 照著WORD_LIST翻譯詞條的格式編寫
        * 純文字的文本，不像CURSE上製成附加模組的攻略
        * 分享出來再被其他人導入
* ~~Guidelime_Shiku~~：zhTW/zhCN，已停更
    * 實施上應該去翻sage......但是sage不願意授權，因為他還在頻繁更新攻略。
* nPlates：zhTW/zhCN
* KuiNameplates：zhTW/zhCN
* [YaHT](https://github.com/Aviana/YaHT/commits?author=EKE00372)：zhTW/zhCN
* [LunaUnitFrames](https://github.com/Aviana/LunaUnitFrames/commits?author=EKE00372)：zhTW/zhCN
* AuctionFaster：zhTW/zhCN
    * 修正某些奇怪的翻譯詞條，否則把一個句子切成多段根本沒法翻，不同語言的語序是不一樣的。
* [modui_classic](https://github.com/obble/modui_classic/commits?author=EKE00372)：zhTW/zhCN
    * 聊天的GlobalStrings待補，這部份要等作者更改格式才會去補。
* Monkey Mods：zhTW/zhCN
    * 修正對東亞語系的支援問題，免得全是問號還要改字體
* RealMobHealth：主zhTW/少量zhCN
    * 增加了選項的詳細說明
* RgsCT
* RSPlates(Col)：zhTW/enUS
* Nioro：zhTW
* EnhancedChatFilterMODFix：zhTW
* ~~Gearmenu：主zhTW/少量zhCN~~拒絕PR
* BuffOverlay：zhTW/zhCN
* Talent Tree Tweaks：zhTW/zhCN
* Talent Tree Viewer：zhTW/zhCN
* Enhanced Raid Frames：zhTW/zhCN
* Merchant Plus：zhTW/zhCN
* RaidSkipper：zhTW/zhCN
* Mission Report Button Plus：zhTW/zhCN
* Animosity：zhTW/zhCN
* Copy Anything：zhCN
* Mythic Plus Pull ReEstimated：zhTW/zhCN
* JiberishUI Icons：zhTW/zhCN
* Global Search：zhTW/zhCN
* ProDamageDisplay：zhTW 修正，跟隨官譯
* ddonLocale：zhTW/zhCN
* KeystoneLoot
* CVarsBackup
* Shotta
* ReforgeLite

## 維護

* ~~KeepIronskin~~：BFA 酒僧小工具
* ~~diminfo~~：訊息條，已重寫為 Kiminfo

## 插件

* ~~EKPlates：名條~~已停更
* EKMinimap：小地圖與追蹤框
* MooseLight：自動調整亮度
* oUF_Ruri：oUF 樣式，含單位框架、團隊框架和名條
* ~~oHWell：**經典版**的自動下座騎、自動站立、快速取消變身~~已停更
* ~~ColorfulMicroMenu~~：微型選單美化，已停更

## TODO？

* [wago.io](https://github.com/oratory/wago.io/issues/52)
* ~~TradeSkillMaster~~
* ~~WCL~~
* zhTW本地化的外部備份
     * Unit/Object/QuestName/QuestLog/Item這些東西的本地化清單
     * 芒果單機的清單不完整，而且與經典版不同的詞條相當多
* ~~Ruf~~
* [AHDB](https://www.curseforge.com/wow/addons/auction-house-database)
* 補完：插件會隨更新增加需要翻譯的詞條
     * PitBull4
     * [RacipeRadarClassic](https://www.curseforge.com/wow/addons/recipe-radar-classic)
* [GB/T 15834―2011标点符号用法]https://people.ubuntu.com/~happyaron/l10n/GB(T)15834-2011.html
     * 備忘，畢竟不熟
