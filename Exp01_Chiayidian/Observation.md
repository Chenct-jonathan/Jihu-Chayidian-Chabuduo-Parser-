# Pattern

* [差一點] 其後子句沒有 overt 主詞，optionally 可連用「就/便」，而「第一個」動詞需為 telic verb。

  * telic verb 分三類： **1. 詞首 (e.g. 「落」馬)** 、**2. 詞尾 (e.g. 昏「倒」)** **3. 無法從字面判斷者 (e.g. 結婚)** 

  * **Regex：**
  * 1. 需要再細分有無需要排除其餘結構取得**「第一個」動詞** (此法將會包含被動及 negation 用法)：
       1. ```<MODIFIER>差一點</MODIFIER>(<FUNC_inner>就</FUNC_inner>|<MODAL>便</MODAL>)?<(ACTION_verb|VerbP)>[^<]*?[上下出入了昏倒出來去爆死亡完光掉好成]+</(ACTION_verb|VerbP)>```
          1. 差一點昏倒
          2. 我真的感動得眼淚都差一點掉下來了
       2. ```<MODIFIER>差一點</MODIFIER>.+?(?!(?:<ACTION_verb>).)*?<(ACTION_verb|VerbP)>([^<]*?[上下出入了昏倒斃出來去爆死亡完光掉好成]+)</(ACTION_verb|VerbP)>```
          1. 只差一點沒和那漂亮女人做成一回好事
          2. 差一點沒到九十分
          3. 可是我差一點被卡子抓走
          4. 我差一點被抓去坐牢
          5. 把經理差一點嚇昏了過去
    2. 
       1. ```<MODIFIER>差一點</MODIFIER>(<FUNC_inner>就</FUNC_inner>|<MODAL>便</MODAL>)?<(ACTION_verb|VerbP)>[溺落]+[^<]*?</(ACTION_verb|VerbP)>```
          1. 爭三連霸的瑞典名將艾柏格則差一點落馬

----

* [差一點] 其後子句沒有 overt 主詞，optionally 可連用「就/便」，若第一個動詞為 atelic verb，則該動詞需要被否定 或 為被動式

  * **Regex：**

  * 1. ```<MODIFIER>差一點</MODIFIER>(<FUNC_inner>就</FUNC_inner>|<MODAL>便</MODAL>)?<ACTION_lightVerb>被</ACTION_lightVerb><(ACTION_verb|VerbP)>([^<]*?)</(ACTION_verb|VerbP)>```
       1. 差一點被抓*

    

    

    

    

    

    

    

    

    

    

    

    