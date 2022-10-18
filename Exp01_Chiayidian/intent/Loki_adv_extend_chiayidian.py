#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for adv_extend_chiayidian

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

DEBUG_adv_extend_chiayidian = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_asNoun":["卡子","婦女支援組織","意念","艾柏格","身心","隨從"],"_asVerb":["打轉","抽腳筋","見上面","車畚斗","陰溝裡翻船"],"_tmpToken":["畢業生","盛況","質素"],"_extractFromPunc":["仇人席","保守","大智若愚","平分秋色","拉一把","晚晴協會","活古蹟","眼淚歌后","選秀狀元","鄉土"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_adv_extend_chiayidian:
        print("[adv_extend_chiayidian] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "差一點站不穩":
        # write your code here
        pass

    if utterance == "差一點站不起來":
        # write your code here
        pass

    if utterance == "差一點被執行":
        # write your code here
        pass

    if utterance == "差一點被抓":
        # write your code here
        pass

    if utterance == "差一點跑不動":
        # write your code here
        pass

    return resultDICT