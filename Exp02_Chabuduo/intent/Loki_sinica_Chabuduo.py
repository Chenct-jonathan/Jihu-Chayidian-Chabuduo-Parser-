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
    userDefinedDICT = {"_asNoun":["海青","諾可","機悟形式","周年慶","貨品","烏托邦","上海話","馬新"],"_asPunc":["..."]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_sinica_Chabuduo:
        print("[sinica_Chabuduo] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "人生閱歷方面的成熟度差不多":
        resultDICT["Sinica"].append("sinica")

    if utterance == "兒童奴隸差不多就可消除":
        resultDICT["Sinica"].append("sinica")

    if utterance == "各縣市情況差不多":
        resultDICT["Sinica"].append("sinica")

    if utterance == "和諾可差不多":
        resultDICT["Sinica"].append("sinica")

    if utterance == "基本設計則差不多":
        resultDICT["Sinica"].append("sinica")

    if utterance == "夜晚差不多都在村子中":
        resultDICT["Sinica"].append("sinica")

    if utterance == "好像意思上差不多":
        resultDICT["Sinica"].append("sinica")

    if utterance == "就是滿正常的差不多國一":
        resultDICT["Sinica"].append("sinica")

    if utterance == "差不多到一半路程時":
        resultDICT["Sinica"].append("sinica")

    if utterance == "差不多是二十八歲吧":
        resultDICT["Sinica"].append("sinica")

    if utterance == "差不多有十年":
        resultDICT["Sinica"].append("sinica")

    if utterance == "差不多的古蹟都變成了「活古蹟」":
        resultDICT["Sinica"].append("sinica")

    if utterance == "差不多都已查證清楚":
        resultDICT["Sinica"].append("sinica")

    if utterance == "情況也差不多":
        resultDICT["Sinica"].append("sinica")

    if utterance == "情況都差不多":
        resultDICT["Sinica"].append("sinica")

    if utterance == "我接過的國宅案中差不多有９０％都發生這類情況":
        resultDICT["Sinica"].append("sinica")

    if utterance == "所以兩地人民性情差不多":
        resultDICT["Sinica"].append("sinica")

    if utterance == "所使用的工具差不多":
        resultDICT["Sinica"].append("sinica")

    if utterance == "海青病得差不多了":
        resultDICT["Sinica"].append("sinica")

    if utterance == "生命已經差不多了":
        resultDICT["Sinica"].append("sinica")

    if utterance == "聽起來差不多嗎":
        resultDICT["Sinica"].append("sinica")

    if utterance == "認為科技的發展自從工業革命以來已差不多到了極致":
        resultDICT["Sinica"].append("sinica")

    if utterance == "說像海盜還差不多":
        resultDICT["Sinica"].append("sinica")

    if utterance == "身上器官也壞得差不多":
        resultDICT["Sinica"].append("sinica")

    if utterance == "那我不就差不多了嗎":
        resultDICT["Sinica"].append("sinica")

    if utterance == "隆乳費用差不多是三萬五千元泰幣":
        resultDICT["Sinica"].append("sinica")

    if utterance == "雖然看起來差不多亮":
        resultDICT["Sinica"].append("sinica")

    if utterance == "香港差不多全部入口貨品都是免稅的":
        resultDICT["Sinica"].append("sinica")

    if utterance == "唸個差不多":
        resultDICT["Sinica"].append("sinica")

    if utterance == "這差不多就是其第一個系統所用的詞典":
        resultDICT["Sinica"].append("sinica")

    return resultDICT