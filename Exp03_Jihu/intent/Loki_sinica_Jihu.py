#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for sinica_Jihu

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

from random import sample
import json
import os

DEBUG_sinica_Jihu = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_sinica_Jihu.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_sinica_Jihu:
        print("[sinica_Jihu] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "幾乎一樣":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['Sinica'].append('sinica')

    if utterance == "幾乎可以看":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['Sinica'].append('sinica')

    if utterance == "幾乎垂直參宿三星":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['Sinica'].append('sinica')

    if utterance == "幾乎完全消失":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['Sinica'].append('sinica')

    if utterance == "幾乎很少人知道":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['Sinica'].append('sinica')

    if utterance == "幾乎是五年前的兩倍":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['Sinica'].append('sinica')

    if utterance == "幾乎未訂捐贈公共設施的回饋辦法":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['Sinica'].append('sinica')

    if utterance == "幾乎每個家庭的物質生活都相當富裕":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['Sinica'].append('sinica')

    if utterance == "幾乎每兩三個月就跳增一倍":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['Sinica'].append('sinica')

    if utterance == "幾乎注定是會賠錢的":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['Sinica'].append('sinica')

    if utterance == "幾乎瓦解於旦夕":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['Sinica'].append('sinica')

    if utterance == "幾乎都是屬於這種古老的岩層":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['Sinica'].append('sinica')

    return resultDICT