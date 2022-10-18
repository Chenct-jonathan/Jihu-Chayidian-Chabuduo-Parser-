#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for adv_sinica_chiayidian

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

DEBUG_adv_sinica_chiayidian = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_asNoun":["卡子","婦女支援組織","意念","艾柏格","身心","隨從"],"_asVerb":["打轉","抽腳筋","見上面","車畚斗","陰溝裡翻船"],"_tmpToken":["畢業生","盛況","質素"],"_extractFromPunc":["仇人席","保守","大智若愚","平分秋色","拉一把","晚晴協會","活古蹟","眼淚歌后","選秀狀元","鄉土"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_adv_sinica_chiayidian:
        print("[adv_sinica_chiayidian] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "只差一點沒和那漂亮女人做成一回好事":
        # write your code here
        pass

    if utterance == "否則差一點看不到新中國":
        # write your code here
        pass

    if utterance == "差一點他那神父爸爸便不能認這個孩子":
        # write your code here
        pass

    if utterance == "差一點就沒命了":
        # write your code here
        pass

    if utterance == "差一點就讓這種傳統工藝走不回來":
        # write your code here
        pass

    if utterance == "差一點把爸爸心愛的上等酒給打翻了":
        # write your code here
        pass

    if utterance == "差一點昏倒":
        # write your code here
        pass

    if utterance == "差一點遭到截肢":
        # write your code here
        pass

    if utterance == "最後還差一點就當選高雄區的立法委員":
        # write your code here
        pass

    if utterance == "爭三連霸的瑞典名將艾柏格則差一點落馬":
        # write your code here
        pass

    if utterance == "謝長亨差一點就是中華職棒第一個「選秀狀元」":
        # write your code here
        pass

    if utterance == "雖然差一點而沒挑戰成功":
        # write your code here
        pass

    return resultDICT