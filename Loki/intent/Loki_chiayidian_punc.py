#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for chiayidian_punc

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

DEBUG_chiayidian_punc = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_chiayidian_punc:
        print("[chiayidian_punc] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[謝長亨][差一點]就是[中華][職棒][第一個]「選秀[狀元]」":
        # write your code here
        pass

    return resultDICT