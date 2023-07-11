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
from ArticutAPI import Articut
import re

accountDICT = json.load(open("account.info",encoding="utf-8"))
articut = Articut(username=accountDICT["username"],apikey=accountDICT["api_key"])

DEBUG_sinica_Jihu = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open('USER_DEFINED.json', 'r', encoding='utf-8'))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

#print(userDefinedDICT)

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

def formMSG(tmpInputSTR, pat):
    '''
    input: 我差一點跌倒ㄟ
    output : <MODIFIER>差一點</MODIFIER><ACTION_verb>跌倒</ACTION_verb><ENTITY_nouny>ㄟ</ENTITY_nouny>
    把 inputSTR 轉成 Articut 結果
    '''
    tmpResultDICT = articut.parse(tmpInputSTR, userDefinedDictFILE="./USER_DEFINED.json")
    if tmpResultDICT["status"] == True:
        posSTR = ''.join(tmpResultDICT["result_pos"])
        return posSTR
    else:
        raise Exception("Invalid Articut result:{}".format(tmpResultDICT["message"]))

def getResult(inputSTR, utterance, pat, args, resultDICT):
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
            #print(pat)
            #print(articut.parse(inputSTR, userDefinedDictFILE="./USER_DEFINED.json")['result_pos'])
            #print(re.search(pat, ''.join(articut.parse(inputSTR, userDefinedDictFILE="./USER_DEFINED.json")['result_pos'])).group(2))
            pass
        #print(re.findall(pat, ''.join(articut.parse(inputSTR, userDefinedDictFILE="./USER_DEFINED.json")['result_pos'])))
        if re.search(pat, ''.join(articut.parse(inputSTR, userDefinedDictFILE="./USER_DEFINED.json")['result_pos'])).group(2) != "":
            #print("2")
            #print(re.findall(pat, ''.join(articut.parse(inputSTR, userDefinedDictFILE="./USER_DEFINED.json")['result_pos'])))
            resultDICT[utterance].append(inputSTR)
        else:
            pass
        if re.search(pat, ''.join(articut.parse(inputSTR, userDefinedDictFILE="./USER_DEFINED.json")['result_pos'])).group(3) in userDefinedDICT['_asIdiom']:
            #print("3")
            #print(re.findall(pat, ''.join(articut.parse(inputSTR, userDefinedDictFILE="./USER_DEFINED.json")['result_pos'])))
            resultDICT[utterance].append(inputSTR)
        else:
            pass
            
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
            
    if utterance == "幾乎呈左右對照配置":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎處於無免疫力狀態":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎清一色丹麥裔":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
    
    if utterance == "幾乎全身被割傷":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎包羅了所有可能的片語結構":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎撞個正著":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
    
    if utterance == "幾乎被認定為民主進步必經之路":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎全武行的紀錄":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎在一夜之間統統升級":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎全村七十九戶有適齡的孩子都會共襄盛舉":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
    
    if utterance == "幾乎純理性的思維習慣":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎被破壞殆盡":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎平均二名打者就有一名被三振":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎全面漲停的榮景之際":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎涵蓋所有的中文字":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎像窗邊族這樣":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎多為他們員工撰寫":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
    
    if utterance == "幾乎使她致命的車禍和因車禍而起的官司":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎逐字拷貝之行為":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎全是視力健全的少年":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎再次暈過去":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎想也沒想":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "佈佔幾乎全部的畫面":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎難以辨認":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎「太親切」啦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎人手一台":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            #resultDICT['Sinica'].append('sinica')
            resultDICT[utterance].append(inputSTR)
            
    if utterance == "幾乎每一頁出現":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        if re.search(pat, ''.join(articut.parse(inputSTR, userDefinedDictFILE="./USER_DEFINED.json")['result_pos'])).group(5) != None:
            maybeVERB = re.search(pat, ''.join(articut.parse(inputSTR, userDefinedDictFILE="./USER_DEFINED.json")['result_pos'])).group(5)
            #print(re.findall(pat, ''.join(articut.parse(inputSTR, userDefinedDictFILE="./USER_DEFINED.json")['result_pos'])))
            #print(maybeVERB)
            if re.search('<(ACTION_verb|VerbP)>[^<]*?</(ACTION_verb|VerbP)>', ''.join(articut.parse(maybeVERB, userDefinedDictFILE="./USER_DEFINED.json")['result_pos'])) != None:
                resultDICT[utterance].append(inputSTR)
            else:
                pass            
        else:
            resultDICT[utterance].append(inputSTR)
        
           
    return resultDICT