#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for sinica_Chabuduo

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

DEBUG_sinica_Chabuduo = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_asNoun":["諾可","海青"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_sinica_Chabuduo:
        print("[sinica_Chabuduo] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "人生閱歷方面的成熟度差不多":
        # write your code here
        pass

    if utterance == "台灣現在也與大陸差不多":
        # write your code here
        pass

    if utterance == "各縣市情況差不多":
        # write your code here
        pass

    if utterance == "和諾可差不多":
        # write your code here
        pass

    if utterance == "好像意思上差不多":
        # write your code here
        pass

    if utterance == "就是滿正常的差不多國一":
        # write your code here
        pass

    if utterance == "差不多是二十八歲吧":
        # write your code here
        pass

    if utterance == "差不多有十年":
        # write your code here
        pass

    if utterance == "情況也差不多":
        # write your code here
        pass

    if utterance == "情況都差不多":
        # write your code here
        pass

    if utterance == "每天給差不多五十塊":
        # write your code here
        pass

    if utterance == "海青病得差不多了":
        # write your code here
        pass

    if utterance == "然後逛了差不多半個鐘頭":
        # write your code here
        pass

    if utterance == "說像海盜還差不多":
        # write your code here
        pass

    return resultDICT