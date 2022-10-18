# Pattern

* [差一點] 其後子句沒有 overt 主詞，optionally 可連用「就/便」，而「第一個」動詞需為 telic verb。

  * telic verb 分三類： **1.詞尾 (e.g. 昏「倒」) ** 、**2. 詞首 (e.g. 「落」馬)** **3. 無法從字面判斷者 (e.g. 當選)** 

  * **Regex：**
  
  * 1. **詞尾 (e.g. 昏「倒」)：**需要再細分有無需要排除其餘結構取得**「第一個」動詞** (此法將會包含被動及  negation沒 的用法)：
  
    * ```<MODIFIER>差一點</MODIFIER>(<FUNC_inner>就</FUNC_inner>|<MODAL>便</MODAL>)?<(ACTION_verb|VerbP)>[^<]*?[上下出入了昏倒出來去爆死亡完光掉好成]+</(ACTION_verb|VerbP)>```
  
      1. 差一點昏倒
  
      2. 差一點忘了
  
      3. 我真的感動得眼淚都差一點掉下來了
      4. 原來他差一點摔倒了
      5. 又曾經在泳渡深潭時不慎捲入旋渦差一點溺死
      6. 在這場危險風暴中差一點丟了性命
      7. 當年差一點回不來 (?)
      8. 差一點笑出來
  
    * ```<MODIFIER>差一點</MODIFIER>.+?(?!(?:<ACTION_verb>).)*?<(ACTION_verb|VerbP)>([^<]*?[上下出入了昏倒斃出來去爆死亡完光掉好成]+)</(ACTION_verb|VerbP)>```
      1. 只差一點沒和那漂亮女人做成一回好事
      2. 可是我差一點被卡子抓走
      3. 把經理差一點嚇昏了過去 (?應該要到 1)
      4. 卻真實地讓他以為差一點就跌入了萬丈深淵 (?)
      5. 差一點沒到九十分 (*)
      6. 我的隨從差一點就傷了妳 (?)
      7. 我差一點就笑了起來 (?)
      8. 居然只差一點被執行了 (?)
      9. 我差一點認不出她來 (?)
      10. 差一點就放棄再騎下去的意念 (?)
      11. 差一點就撞上他 (?)
    * ```<MODIFIER>差一點</MODIFIER>(<FUNC_inner>就</FUNC_inner>|<MODAL>便</MODAL>)?<(ACTION_verb|VerbP)>([^<]*?不[^<]*?)</(ACTION_verb|VerbP)>```
      1. 否則差一點看不到新中國
    * ```<MODIFIER>差一點</MODIFIER>(<FUNC_inner>就</FUNC_inner>|<MODAL>便</MODAL>)?<(MODIFIER|ModifierP)>[^<]*?</(MODIFIER|ModifierP)><ASPECT>([^<]*?)</ASPECT>```
      1. 差一點就沒命了
  
     
  
    2. **詞首 (e.g. 「落」馬)：**
  
    * ```<MODIFIER>差一點</MODIFIER>(<FUNC_inner>就</FUNC_inner>|<MODAL>便</MODAL>)?<(ACTION_verb|VerbP)>[溺落]+[^<]*?</(ACTION_verb|VerbP)>```
  
      1. 爭三連霸的瑞典名將艾柏格則差一點落馬
  
      2. 畢業生的一位曾經在美濃溪差一點溺水
  
         
  
    				3. **無法從字面判斷者 (e.g. 當選)**：
  
    * ```<MODIFIER>差一點</MODIFIER>(<FUNC_inner>就</FUNC_inner>|<MODAL>便</MODAL>)?<(ACTION_verb|VerbP)>([^落溺]+[^上下出入了昏倒出來去爆死亡完光掉好成]+)</(ACTION_verb|VerbP)>```
      1. 最後還差一點就當選高雄區的立法委員
    * ```<MODIFIER>差一點</MODIFIER>(<FUNC_inner>就</FUNC_inner>|<MODAL>便</MODAL>)?.+?(?!(?:<(ACTION_verb|VerbP)>).)*?<(ACTION_verb|VerbP)>([^落溺]+[^上下出入了昏倒出來去爆死亡完光掉好成]+)</(ACTION_verb|VerbP)>```
      1. 雖然差一點而沒挑戰成功
      2. 三個年輕人差一點就要去大鬧天宮
      3. 差一點提前引爆華隆跳票的引信 (*)
      4. 七歲的妹妹差一點被二個壞人強暴
    * ```<MODIFIER>差一點</MODIFIER>(<FUNC_inner>就</FUNC_inner>|<MODAL>便</MODAL>)?(<(ACTION_verb|VerbP)>遭到</(ACTION_verb|VerbP)>|<ACTION_lightVerb>[遭被]</ACTION_lightVerb>)```
      1. 差一點遭到截肢

----

* [差一點] 其後子句沒有 overt 主詞，optionally 可連用「就/便」，若第一個動詞為 atelic verb，則該動詞需要被否定 或 為被動式

  * **Regex：**

  * 1. ```<MODIFIER>差一點</MODIFIER>(<FUNC_inner>就</FUNC_inner>|<MODAL>便</MODAL>)?<ACTION_lightVerb>被</ACTION_lightVerb><(ACTION_verb|VerbP)>([^<]*?)</(ACTION_verb|VerbP)>```
       1. 差一點被抓*

    

    

---

* [差一點] 其後子句有 overt 主詞，strictly 不可連用「就/便」，而要加在該主詞後，若第一個動詞為 atelic verb，則該動詞需要被否定
  * **Regex：**
  * 1. ```<MODIFIER>差一點</MODIFIER>(<ENTITY_pronoun>([^<]*?)</ENTITY_pronoun>|<(UserDefined|ENTITY_(nounHead|nouny|noun|oov))>([^<]*?)</(UserDefined|ENTITY_(nounHead|nouny|noun|oov))>)(<FUNC_inner>就</FUNC_inner>|<MODAL>便</MODAL>)?.+?(?!(?:<(ACTION_verb|VerbP)>).)*?<(ACTION_verb|VerbP)>[^<]*?</(ACTION_verb|VerbP)>```
       1. 差一點他那神父爸爸便不能認這個孩子

---

*  [差一點] 其後為「讓…」字句，optionally 可連用「就/便」，其後第一個動詞需為 telic verb，若用被動式，optionally 能用「被/給…」passive
  * **Regex：**
    1. ```<MODIFIER>差一點</MODIFIER>(<FUNC_inner>就</FUNC_inner>|<MODAL>便</MODAL>)?<(ACTION_verb|VerbP)>讓</(ACTION_verb|VerbP)>.+?(?!(?:<ACTION_verb>).)*?(<ACTION_lightVerb>[給被]/ACTION_lightVerb>)?<ACTION_verb>([^<]*?)</ACTION_verb>```
       1. 差一點就讓這種傳統工藝走不回來

---

* ```<MODIFIER>差一點</MODIFIER><AUX>[^<]*?</AUX>```
  * 謝長亨差一點就是中華職棒第一個「選秀狀元」







## 以上為 web 測試結果：(*表示我認為可以針對該劇見新 Pattern) (?表示該句不應該在這)

---

* ** Loki 測試結果：**

  ```
  1:
  [adv_sinica_chiayidian] 爭三連霸的瑞典名將艾柏格則差一點落馬 ===> 爭三連霸的瑞典名將艾柏格則差一點落馬
  2:
  [adv_sinica_chiayidian] 只差一點沒和那漂亮女人做成一回好事 ===> 只差一點沒和那漂亮女人做成一回好事
  3: #差一點見上面*
  4:
  [adv_sinica_chiayidian] 差一點忘了 ===> 差一點昏倒
  5:
  [adv_sinica_chiayidian] 可是我差一點被卡子抓走 ===> 只差一點沒和那漂亮女人做成一回好事
  6:
  [adv_extend_chiayidian] 我差一點被抓去坐牢 ===> 差一點被執行
  [adv_sinica_chiayidian] 我差一點被抓去坐牢 ===> 雖然差一點而沒挑戰成功
  7:
  [adv_sinica_chiayidian] 把經理差一點嚇昏了過去 ===> 只差一點沒和那漂亮女人做成一回好事
  8:
  [adv_sinica_chiayidian] 我真的感動得眼淚都差一點掉下來了 ===> 差一點昏倒
  9:
  [adv_sinica_chiayidian] 差一點沒把手指頭當菜切了 ===> 只差一點沒和那漂亮女人做成一回好事
  10:
  [adv_sinica_chiayidian] 差一點把爸爸心愛的上等酒給打翻了 ===> 差一點把爸爸心愛的上等酒給打翻了
  11:
  [adv_sinica_chiayidian] 差一點昏倒 ===> 差一點昏倒
  12:
  [adv_sinica_chiayidian] 原來他差一點摔倒了 ===> 差一點昏倒
  13:
  [adv_sinica_chiayidian] 又曾經在泳渡深潭時不慎捲入旋渦差一點溺死 ===> 差一點昏倒
  14:
  [adv_sinica_chiayidian] 卻真實地讓他以為差一點就跌入了萬丈深淵 ===> 只差一點沒和那漂亮女人做成一回好事
  15:
  [adv_sinica_chiayidian] 在這場危險風暴中差一點丟了性命 ===> 差一點昏倒
  16:
  [adv_extend_chiayidian] 否則差一點看不到新中國 ===> 差一點站不起來
  [adv_sinica_chiayidian] 否則差一點看不到新中國 ===> 差一點昏倒
  17:
  [adv_sinica_chiayidian] 差一點沒到九十分 ===> 只差一點沒和那漂亮女人做成一回好事
  18: #沙琰翎差一點陰溝裡翻船*
  19:
  [adv_sinica_chiayidian] 最後還差一點就當選高雄區的立法委員 ===> 雖然差一點而沒挑戰成功
  20:
  [adv_sinica_chiayidian] 雖然差一點而沒挑戰成功 ===> 雖然差一點而沒挑戰成功
  21:
  [adv_sinica_chiayidian] 三個年輕人差一點就要去大鬧天宮 ===> 雖然差一點而沒挑戰成功
  22:
  [adv_extend_chiayidian] 當年差一點回不來 ===> 差一點站不起來
  [adv_sinica_chiayidian] 當年差一點回不來 ===> 差一點昏倒
  23: #她差一點栽在印度芭娜姬的手中*
  24: #即使差一點*
  25:
  [adv_sinica_chiayidian] 差一點提前引爆華隆跳票的引信 ===> 雖然差一點而沒挑戰成功
  26:
  [adv_sinica_chiayidian] 我的隨從差一點就傷了妳 ===> 只差一點沒和那漂亮女人做成一回好事
  27:
  [adv_sinica_chiayidian] 我差一點就笑了起來 ===> 只差一點沒和那漂亮女人做成一回好事
  28:
  [adv_sinica_chiayidian] 差一點笑出來 ===> 差一點昏倒
  29: #這些胎生的小苗萬一在第一次落下運氣差一點*
  30:
  [adv_extend_chiayidian] 居然只差一點被執行了 ===> 差一點被抓
  [adv_sinica_chiayidian] 居然只差一點被執行了 ===> 只差一點沒和那漂亮女人做成一回好事
  31:
  [adv_sinica_chiayidian] 還差一點旅行社才開門辦公 ===> 雖然差一點而沒挑戰成功
  32:
  [adv_sinica_chiayidian] 畢業生的一位曾經在美濃溪差一點溺水 ===> 爭三連霸的瑞典名將艾柏格則差一點落馬
  33: #若是評估質素差一點的*
  34:
  [adv_sinica_chiayidian] 差一點他那神父爸爸便不能認這個孩子 ===> 差一點他那神父爸爸便不能認這個孩子
  35:
  [adv_sinica_chiayidian] 差一點就讓這種傳統工藝走不回來 ===> 只差一點沒和那漂亮女人做成一回好事
  36:
  [adv_sinica_chiayidian] 七歲的妹妹差一點被二個壞人強暴 ===> 雖然差一點而沒挑戰成功
  37:
  [adv_extend_chiayidian] 我差一點認不出她來 ===> 差一點跑不動
  [adv_sinica_chiayidian] 我差一點認不出她來 ===> 只差一點沒和那漂亮女人做成一回好事
  38:
  [adv_sinica_chiayidian] 差一點就放棄再騎下去的意念 ===> 只差一點沒和那漂亮女人做成一回好事
  39:
  [adv_sinica_chiayidian] 差一點遭到截肢 ===> 差一點遭到截肢
  40: #差一點就車畚斗*
  41: #差一點就抽腳筋*
  42:
  [adv_sinica_chiayidian] 差一點就沒命了 ===> 差一點就沒命了
  43:
  [adv_sinica_chiayidian] 差一點就撞上他 ===> 只差一點沒和那漂亮女人做成一回好事
  44:
  [adv_sinica_chiayidian] 謝長亨差一點就是中華職棒第一個「選秀狀元」 ===> 謝長亨差一點就是中華職棒第一個「選秀狀元」



















