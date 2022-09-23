#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for chiabuduo_punc

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
with open(os.path.join(os.path.dirname(__file__), "../account.info"), "r", encoding="utf-8") as f:
    accountDICT = json.load(f)
articut = Articut(username=accountDICT["username"], apikey=accountDICT["apikey"])

DEBUG_chiabuduo_punc = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_asNoun":["卡子","婦女支援組織","意念","艾柏格","身心","隨從"],"_asVerb":["打轉","抽腳筋","車畚斗","陰溝裡翻船"],"_tmpToken":["畢業生","盛況","質素"],"_extractFromPunc":["仇人席","保守","大智若愚","平分秋色","拉一把","晚晴協會","活古蹟","眼淚歌后","選秀狀元","鄉土"]}


def verbTelicityChecker(verbSTR):
    resultBOOL = None

    return resultBOOL

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_chiabuduo_punc:
        print("[chiabuduo_punc] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[也][差不多][僅][能]從回憶[中]找回[這位][當年][風靡][大街][小巷]「[眼淚歌后]」受歡迎[盛]況":
        # write your code here
        pass

    if utterance == "[他們][差不多]是以[這種][邏輯]把[七十年代]曖昧[不清]的「[鄉土]」[觀念][明確]的":
        # write your code here
        pass

    if utterance == "[你]的[心智]和[思想]就「[差不多]」在[原地][打轉]":
        # write your code here
        pass

    if utterance == "[差不多][第一][印象][都]是[他們]是[一個]「[保守]」":
        # write your code here
        pass

    if utterance == "[差不多]……好了……":
        # write your code here
        pass

    if utterance == "[差不多]的[古蹟][都]變成了「[活古蹟]」":
        # write your code here
        pass

    if utterance == "[性別]與[省籍][差不多][都]是「[平分秋色]」":
        # write your code here
        pass

    if utterance == "[玉肉]和[好孔][差不多]的[叫]「好肉若一":
        # write your code here
        pass

    if utterance == "[第一個][民間][自發性]的[婦女支援組織]以輔導離婚[婦女]走過[身心][劇]創的「[晚晴協會]」[前身]組織「[拉一把]」[也][差不多][同時]成立":
        # write your code here
        pass

    if utterance == "[該]有[個]「[仇人席]」還[差不多]":
        # write your code here
        pass

    if utterance == "[這個][意思]和[另][一個][成語]「[大智若愚]」[差不多]":
        # write your code here
        pass

    return resultDICT