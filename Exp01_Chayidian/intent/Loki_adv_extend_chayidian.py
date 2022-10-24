#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for adv_extend_chayidian

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

accountDICT = json.load(open("account.info",encoding="utf-8"))
articut = Articut(username=accountDICT["username"],apikey=accountDICT["apikey"])
userDefinedDictFILE = "./intent/USER_DEFINED.json"


DEBUG_adv_extend_chayidian = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_asNoun":["卡子","婦女支援組織","意念","艾柏格","身心","隨從"],"_asVerb":["打轉","抽腳筋","見上面","車畚斗","陰溝裡翻船"],"_tmpToken":["畢業生","盛況","質素"],"_extractFromPunc":["仇人席","保守","大智若愚","平分秋色","拉一把","晚晴協會","活古蹟","眼淚歌后","選秀狀元","鄉土"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_adv_extend_chayidian:
        print("[adv_extend_chayidian] {} ===> {}".format(inputSTR, utterance))

def inputSTRSpliter(inputSTR, spliterSTR="差一點"):
    tmpInputSTR = inputSTR.split(spliterSTR)[-1]
    return "差一點"+tmpInputSTR

def formMSG(tmpInputSTR, pat):
    '''
    input: 我差一點跌倒ㄟ
    output : <MODIFIER>差一點</MODIFIER><ACTION_verb>跌倒</ACTION_verb><ENTITY_nouny>ㄟ</ENTITY_nouny>
    把 inputSTR 轉成 Articut 結果
    '''
    tmpresultDICT = articut.parse(tmpInputSTR, userDefinedDictFILE=userDefinedDictFILE)
    if tmpresultDICT["status"] == True:
        posSTR = ''.join(tmpresultDICT["result_pos"])
        return posSTR
    else:
        raise Exception("Invalid Articut result:{}".format(resultDICT["message"]))

def getResult(inputSTR, utterance, pat, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "差一點站不穩":
        tmpInputSTR = inputSTRSpliter(inputSTR)
        tmpPosSTR = formMSG(tmpInputSTR, pat)
        resultDICT["FirstVerb"] = re.search(pat,tmpPosSTR).group(3)+re.search(pat,tmpPosSTR).group(5)
        #print(re.findall(pat,tmpPosSTR ))
        resultDICT["reason"] = "[差一點] 後的第一個動詞 [{}] 符合 [{}] 詞彙結構，為一結束體事件(accomplishment)語意，故可使用 [差一點]。".format(resultDICT["FirstVerb"],"V "+resultDICT["FirstVerb"][1:])
        resultDICT["key"] = "結束體(accomplishment)"

    if utterance == "差一點跑不動":
        tmpInputSTR = inputSTRSpliter(inputSTR)
        tmpPosSTR = formMSG(tmpInputSTR, pat)
        resultDICT["FirstVerb"] = re.search(pat,tmpPosSTR).group(3) + re.search(pat,tmpPosSTR).group(5) + re.search(pat,tmpPosSTR).group(6)
        #print(re.findall(pat,tmpPosSTR ))
        resultDICT["reason"] = "[差一點] 後的第一個動詞 [{}] 符合 [{}] 詞彙結構，為一結束體事件(accomplishment)語意，故可使用 [差一點]。".format(resultDICT["FirstVerb"],"V "+resultDICT["FirstVerb"][1:])
        resultDICT["key"] = "結束體(accomplishment)"

    if utterance == "差一點沒和那漂亮女人看一部電影":
        tmpInputSTR = inputSTRSpliter(inputSTR)
        tmpPosSTR = formMSG(tmpInputSTR, pat)
        resultDICT["FirstVerb"] = re.search(pat,tmpPosSTR).group(1)
        resultDICT["classifier"] = re.search(pat,tmpPosSTR).group(2)
        resultDICT["FirstVerbP"] = re.search(pat,tmpPosSTR).group(1)+ re.search(pat,tmpPosSTR).group(2)
        #print(re.findall(pat,tmpPosSTR ))
        resultDICT["reason"] = "[差一點] 後的第一個動詞 [{}] 為一活動體事件(activity)語意，但其後的 [{}] 可使 [{}] 變成結束貌(achievement)，故可使用 [差一點]。".format(resultDICT["FirstVerb"],resultDICT["classifier"],resultDICT["FirstVerbP"])
        resultDICT["key"] = "結束貌(achievement)"

    if utterance == "差一點他那神父爸爸便看到這個孩子":
        tmpInputSTR = inputSTRSpliter(inputSTR)
        tmpPosSTR = formMSG(tmpInputSTR, pat)
        resultDICT["FirstVerb"] = re.search(pat,tmpPosSTR).group(17) 
        #print(re.findall(pat,tmpPosSTR ))
        resultDICT["reason"] = "[差一點] 後的第一個動詞 [{}] 為一結束體事件(accomplishment)語意，故可使用 [差一點]。".format(resultDICT["FirstVerb"])
        resultDICT["key"] = "結束體(accomplishment)"

    if utterance == "差一點就沒時間了":
        tmpInputSTR = inputSTRSpliter(inputSTR)
        tmpPosSTR = formMSG(tmpInputSTR, pat)
        resultDICT["negation"] = re.search(pat,tmpPosSTR).group(2)#待更改
        resultDICT["nouny"] = re.search(pat,tmpPosSTR).group(5)
        resultDICT["aspect"] = re.search(pat,tmpPosSTR).group(8)
        #print(re.findall(pat,tmpPosSTR ))
        resultDICT["reason"] = "[差一點] 後的 [{}] 為一完成貌事件(perfective)語意，故可使用 [差一點]。".format(resultDICT["negation"]+resultDICT["nouny"]+resultDICT["aspect"])
        resultDICT["key"] = "完成貌 (perfective)"

    if utterance == "差一點就使這種傳統工藝走不回來":
        if "inputSTR" in resultDICT.keys():
            pass
        else:
            resultDICT["inputSTR"] = inputSTR
        tmpInputSTR = inputSTRSpliter(inputSTR)
        tmpPosSTR = formMSG(tmpInputSTR, pat)
        #print(re.findall(pat,tmpPosSTR ))
        resultDICT["reason"] = "[差一點] 後的子句 [{}] 為一完成貌事件(perfective)語意，故可使用 [差一點]。".format("使"+"".join(tmpInputSTR.split("使")[1:]))
        
    if utterance == "差一點被截肢":
        tmpInputSTR = inputSTRSpliter(inputSTR)
        tmpPosSTR = formMSG(tmpInputSTR, pat)
        resultDICT["passive"] = re.search(pat,tmpPosSTR).group(4)
        #print(re.findall(pat,tmpPosSTR ))
        resultDICT["reason"] = "[差一點] 後的被動式子句 [{}] 為一完成貌事件(perfective)語意，故可使用 [差一點]。".format(resultDICT["passive"]+tmpInputSTR.split(resultDICT["passive"])[1])
        resultDICT["key"] = "完成貌(perfective)"
        
    if utterance == "差一點將爸爸心愛的上等酒給打翻了":
        tmpInputSTR = inputSTRSpliter(inputSTR)
        tmpPosSTR = formMSG(tmpInputSTR, pat)
        resultDICT["FirstVerb"] = re.search(pat,tmpPosSTR).group(7)
        #print(re.findall(pat,tmpPosSTR ))
        resultDICT["reason"] = "[差一點] 後的 [將...] 字句 [{}] 為一完成貌事件(perfective)語意，故可使用 [差一點]".format("將"+"".join(tmpInputSTR.split("將")[1:]))
        resultDICT["key"] = "完成貌 (perfective)"
        
    if utterance == "我差一點沒趕上":
        tmpInputSTR = inputSTRSpliter(inputSTR)
        tmpPosSTR = formMSG(tmpInputSTR, pat)
        resultDICT["negation"] = re.search(pat,tmpPosSTR).group(4)
        print(re.findall(pat,tmpPosSTR ))
        resultDICT["reason"] = "[差一點] 後的 [{}] 為一完成貌事件(perfective)語意，故可使用 [差一點]。".format(resultDICT["negation"] + tmpInputSTR.split(resultDICT["negation"])[-1])
        resultDICT["key"] = "完成貌 (perfective)"
        
    if utterance == "差一點沒命":
        tmpInputSTR = inputSTRSpliter(inputSTR)
        tmpPosSTR = formMSG(tmpInputSTR, pat)
        resultDICT["FirstVerb"] = re.search(pat,tmpPosSTR).group(3)
        print(re.findall(pat,tmpPosSTR ))
        resultDICT["reason"] = "[差一點] 後的第一個動詞 [{}] 若為一達成體事件(achievement)語意，故可使用 [差一點]。".format(resultDICT["FirstVerb"])
        resultDICT["key"] = "達成體事件(achievement)"
        
    if utterance == "他差一點天天玩":
        tmpInputSTR = inputSTRSpliter(inputSTR)
        tmpPosSTR = formMSG(tmpInputSTR, pat)
        resultDICT["time"] = re.search(pat,tmpPosSTR).group(4)
        resultDICT["FirstVerb"] = re.search(pat,tmpPosSTR).group(7)
        print(re.findall(pat,tmpPosSTR ))
        resultDICT["reason"] = "[差一點] 後的第一個動詞組 [{}] 若為一達成體事件(achievement)語意，故可使用 [差一點]。".format(resultDICT["time"] + resultDICT["FirstVerb"])
        resultDICT["key"] = "達成體事件(achievement)"        

    return resultDICT