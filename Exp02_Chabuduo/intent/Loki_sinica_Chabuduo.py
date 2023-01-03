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
    userDefinedDICT = {"_asNoun":["海青","諾可"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_sinica_Chabuduo:
        print("[sinica_Chabuduo] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "人生閱歷方面的成熟度差不多":
        resultDICT["Sinica"].append("sinica")


    if utterance == "你其他的事情我差不多都知道了":
        resultDICT["Sinica"].append("sinica")
        

    if utterance == "台灣現在也與大陸差不多":
        resultDICT["Sinica"].append("sinica")
        

    if utterance == "各縣市情況差不多":
        resultDICT["Sinica"].append("sinica")
        

    if utterance == "和諾可差不多":
        resultDICT["Sinica"].append("sinica")
        

    if utterance == "好像意思上差不多":
        resultDICT["Sinica"].append("sinica")
        

    if utterance == "就是滿正常的差不多國一":
        resultDICT["Sinica"].append("sinica")
        

    if utterance == "差不多是二十八歲吧":
        resultDICT["Sinica"].append("sinica")
        

    if utterance == "差不多有十年":
        resultDICT["Sinica"].append("sinica")
        

    if utterance == "情況也差不多":
        resultDICT["Sinica"].append("sinica")
        

    if utterance == "情況都差不多":
        resultDICT["Sinica"].append("sinica")
        

    if utterance == "我接過的國宅案中差不多有９０％都發生這類情況":
        resultDICT["Sinica"].append("sinica")
        

    if utterance == "所使用的工具差不多":
        resultDICT["Sinica"].append("sinica")
        

    if utterance == "每天給差不多五十塊":
        resultDICT["Sinica"].append("sinica")
        

    if utterance == "海青病得差不多了":
        resultDICT["Sinica"].append("sinica")
        

    if utterance == "然後逛了差不多半個鐘頭":
        resultDICT["Sinica"].append("sinica")
        

    if utterance == "說像海盜還差不多":
        resultDICT["Sinica"].append("sinica")
        

    if utterance == "跟鮮奶價格差不多":
        resultDICT["Sinica"].append("sinica")
        

    if utterance == "隆乳費用差不多是三萬五千元泰幣":
        resultDICT["Sinica"].append("sinica")
        
    
    if utterance == "認為科技的發展自從工業革命以來已差不多到了極致":
        resultDICT["Sinica"].append("sinica")
        
    
    if utterance == "差不多每一個中央委員都捐了十萬元":
        resultDICT["Sinica"].append("sinica")
    
    if utterance == "差不多……好了……":
        resultDICT["Sinica"].append("sinica")
    
    if utterance == "香港差不多全部入口貨品都是免稅的":
        resultDICT["Sinica"].append("sinica")

    return resultDICT