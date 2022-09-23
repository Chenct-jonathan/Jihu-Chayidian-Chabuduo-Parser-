#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for chiayidian

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json
import os
import re

from ArticutAPI import Articut
with open("../account.info", "r", encoding="utf-8") as f:
    accountDICT = json.load(f)
articut = Articut(username=accountDICT["username"], apikey=accountDICT["apikey"])

DEBUG_chiayidian = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_asNoun":["卡子","婦女支援組織","意念","艾柏格","身心","隨從"],"_asVerb":["打轉","抽腳筋","車畚斗","陰溝裡翻船"],"_tmpToken":["畢業生","盛況","質素"],"_extractFromPunc":["仇人席","保守","大智若愚","平分秋色","拉一把","晚晴協會","活古蹟","眼淚歌后","選秀狀元","鄉土"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_chiayidian:
        print("[chiayidian] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[七][歲]的[妹妹][差一點]被[二個][壞][人]強暴":
        # write your code here
        pass

    if utterance == "[三個][年輕][人][差一點]就要去大鬧[天宮]":
        # write your code here
        pass

    if utterance == "[只][差一點]沒和那[漂亮][女人]做成[一]回[好事]":
        # write your code here
        pass

    if utterance == "[她][差一點]栽在[印度][芭娜姬]的[手][中]":
        # write your code here
        pass

    if utterance == "[差一點][他]那[神父][爸爸][便]不[能]認[這個][孩子]":
        # write your code here
        pass

    if utterance == "[差一點][沒把][手指頭]當[菜]切了":
        # write your code here
        pass

    if utterance == "[差一點]就[抽腳筋]":
        # write your code here
        pass

    if utterance == "[差一點]就[沒命]了":
        # write your code here
        pass

    if utterance == "[差一點]就撞上[他]":
        # write your code here
        pass

    if utterance == "[差一點]就放棄再騎下去的[意念]":
        # write your code here
        pass

    if utterance == "[差一點]就讓[這種][傳統工藝]走不回來":
        # write your code here
        pass

    if utterance == "[差一點]忘了":
        # write your code here
        pass

    if utterance == "[差一點]把[爸爸][心愛]的[上等酒]給打翻了":
        # write your code here
        pass

    if utterance == "[差一點]提[前]引爆[華隆]跳票的[引信]":
        # write your code here
        pass

    if utterance == "[差一點]昏倒":
        # write your code here
        pass

    if utterance == "[差一點]沒到[九十分]":
        # write your code here
        pass

    if utterance == "[差一點]笑出來":
        # write your code here
        pass

    if utterance == "[差一點]見[上面]":
        # write your code here
        pass

    if utterance == "[差一點]遭到[截肢]":
        # write your code here
        pass

    if utterance == "[我][差一點]就笑了起來":
        # write your code here
        pass

    if utterance == "[我][差一點]被抓去坐牢":
        # write your code here
        pass

    if utterance == "[我][差一點]認不[出][她]來":
        # write your code here
        pass

    if utterance == "[我][真]的感動得[眼淚][都][差一點]掉下來了":
        # write your code here
        pass

    if utterance == "[我]的[隨從][差一點]就傷了[妳]":
        # write your code here
        pass

    if utterance == "[最後]還[差一點]就當選[高雄區]的[立法委員]":
        # write your code here
        pass

    if utterance == "[沙琰翎][差一點][陰溝裡翻船]":
        # write your code here
        pass

    if utterance == "[畢業生]的[一位]曾經在[美濃溪][差一點]溺水":
        # write your code here
        pass

    if utterance == "[當年][差一點]回不來":
        # write your code here
        pass

    if utterance == "[這些][胎生]的[小苗][萬一]在[第一次]落下[運氣][差一點]":
        # write your code here
        pass

    if utterance == "即使[差一點]":
        # write your code here
        pass

    if utterance == "卻[真實地]讓[他]以為[差一點]就跌入了萬丈深淵":
        # write your code here
        pass

    if utterance == "原來[他][差一點]摔倒了":
        # write your code here
        pass

    if utterance == "又曾經在[泳]渡[深潭]時[不慎]捲入[旋渦][差一點]溺死":
        # write your code here
        pass

    if utterance == "可是[我][差一點]被[卡子]抓走":
        # write your code here
        pass

    if utterance == "否則[差一點]看不到[新][中國]":
        # write your code here
        pass

    if utterance == "在[這場][危險風暴][中][差一點]丟了[性命]":
        # write your code here
        pass

    if utterance == "居然[只][差一點]被執行了":
        # write your code here
        pass

    if utterance == "把[經理][差一點]嚇昏了過去":
        # write your code here
        pass

    if utterance == "爭[三]連[霸]的[瑞典][名將][艾柏格]則[差一點]落馬":
        # write your code here
        pass

    if utterance == "若是評估[質素][差一點]的":
        # write your code here
        pass

    if utterance == "還[差一點][旅行社][才]開門辦公":
        # write your code here
        pass

    if utterance == "雖然[差一點]而沒挑戰[成功]":
        # write your code here
        pass

    return resultDICT