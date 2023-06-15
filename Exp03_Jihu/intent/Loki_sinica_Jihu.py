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
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)

    if utterance == "幾乎可以看":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)

    if utterance == "幾乎垂直參宿三星":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)

    if utterance == "幾乎完全消失":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)

    if utterance == "幾乎很少人知道":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)

    if utterance == "幾乎是五年前的兩倍":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)

    if utterance == "幾乎未訂捐贈公共設施的回饋辦法":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)

    if utterance == "幾乎每個家庭的物質生活都相當富裕":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)

    if utterance == "幾乎每兩三個月就跳增一倍":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)

    if utterance == "幾乎注定是會賠錢的":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)

    if utterance == "幾乎瓦解於旦夕":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)

    if utterance == "幾乎都是屬於這種古老的岩層":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
    
    if utterance == "幾乎和小朋友美術課的大張圖畫紙一樣大":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎等同於外界利益獨立的經營體":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎有十二億的中國人在等待這一天的來臨":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎打破福特內部產品發展的每項紀錄":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎看不見灰塵":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎年年都獲得全國的各種名次":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
    
    if utterance == "幾乎損壞殆盡":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎只有團體":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎多為如何投資":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎不可或缺的參考資料":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎不做講解":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎把荷商擠出歐洲市場":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎適合各種場合":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎比生母施虐高出一倍":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎令我斷氣":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎要令他爆炸了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎把那小販的祖宗三代都罵過了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎無限長的百科全書":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎要休學的時候":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎就有自己的使用文字了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)        

    return resultDICT