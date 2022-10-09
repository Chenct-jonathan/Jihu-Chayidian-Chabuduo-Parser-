#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for chiyidian_adv

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

DEBUG_chiyidian_adv = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_asNoun":["卡子","婦女支援組織","意念","艾柏格","身心","隨從"],"_asVerb":["打轉","抽腳筋","車畚斗","陰溝裡翻船"],"_tmpToken":["畢業生","盛況","質素"],"_extractFromPunc":["仇人席","保守","大智若愚","平分秋色","拉一把","晚晴協會","活古蹟","眼淚歌后","選秀狀元","鄉土"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_chiyidian_adv:
        print("[chiyidian_adv] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "否則差一點看不到新中國":
        # write your code here
        pass

    if utterance == "居然只差一點被執行了":
        # write your code here
        pass

    if utterance == "差一點就沒命了":
        # write your code here
        pass

    if utterance == "差一點把爸爸心愛的上等酒給打翻了":
        # write your code here
        pass

    if utterance == "差一點昏倒":
        # write your code here
        pass

    if utterance == "差一點沒到九十分":
        # write your code here
        pass

    return resultDICT