#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for chiayidian

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

DEBUG_chiayidian = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_asNoun":["卡子","婦女支援組織","意念","艾柏格","身心","隨從"],"_asVerb":["打轉","抽腳筋","車畚斗","陰溝裡翻船"],"_tmpToken":["畢業生","盛況","質素"],"_extractFromPunc":["仇人席","保守","大智若愚","平分秋色","拉一把","晚晴協會","活古蹟","眼淚歌后","選秀狀元","鄉土"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_chiayidian:
        print("[chiayidian] {} ===> {}".format(inputSTR, utterance))


def telicyCheck(priorSTR, postSTR):
    """
    priorSTR: 同一語句中，任何在「差一點」之前的字串
    postSTR: 同一語句中，任何在「差一點」之後的字串
    """
    resultBOOL = [None, None]

    priorPatLIST = ["<ACTION_verb>[完光掉好壞成上棄始爆破倒見死溺]+?</ACTION_verb>"]
    priorPat = re.compile("".join(priorPatLIST))
    priorRESULT = articut.parse(priorSTR)
    try:
        if priorRESULT["status"] == True:
            priorPosSTR = priorRESULT["result_pos"][0]
            if re.search(priorPat, priorPosSTR):
                resultBOOL[0] = True
            else:
                resultBOOL[0] = False
        else:
            print("Error as ", priorRESULT["message"])
    except Exception as err:
        print("Error as ", err)
        raise

    postPatLIST = ["<ACTION_verb>[完光掉好壞成上棄始爆破倒見死溺]+?</ACTION_verb>",
                   "<FUNC_negation>不</FUNC_negation>(?!$)",
                   "^(<FUNC_inter>而</FUNC_inter>)?<FUNC_negation>沒</FUNC_negation>",
                   "<VerbP>[^<]+了</VerbP>$",
                   "^<FUNC_inner>就</FUNC_inner>.+?<ASPECT>了</ASPECT>$",
                   "<ACTION_verb>[^<]*(起來|[^<]*[來去走到]|[當落][^<])</ACTION_verb>",
                   "<ACTION_verb>[^<]</ACTION_verb><FUNC_inner>在</FUNC_inner>",
                   "^((<FUNC_inner>就</FUNC_inner>)|(<ACTION_verb>要</ACTION_verb>)){0,2}<ACTION_lightVerb>[^<]+</ACTION_lightVerb>.*?(<ACTION_verb>[^<]+[^<著]</ACTION_verb>$|<ACTION_verb>[^<]*(起來|[^<]*[來去走到]|[當落][^<])</ACTION_verb>)"
                   ]
    postPat = re.compile("|".join(postPatLIST))
    postRESULT = articut.parse(postSTR)
    try:
        if priorRESULT["status"] == True:
            postPosSTR = postRESULT["result_pos"][0]
            if re.search(postPat, postPosSTR):
                resultBOOL[1] = True
            else:
                resultBOOL[1] = False
        else:
            print("Error as ", priorRESULT["message"])
    except Exception as err:
        print("Error as ", err)
        raise

    if postPosSTR in userDefinedDICT["_asVerb"]:
        resultBOOL[1] = True
    return resultBOOL



def inputSTRSpliter(inputSTR, spliterSTR="差一點"):
    resultLIST = [None, None]
    resultLIST = inputSTR.split(spliterSTR)[:2]
    return resultLIST

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[七][歲]的[妹妹][差一點]被[二個][壞][人]強暴":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[三個][年輕][人][差一點]就要去大鬧[天宮]":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[只][差一點]沒和那[漂亮][女人]做成[一]回[好事]":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[她][差一點]栽在[印度][芭娜姬]的[手][中]":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[差一點][他]那[神父][爸爸][便]不[能]認[這個][孩子]":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[差一點][沒把][手指頭]當[菜]切了":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[差一點]就[抽腳筋]":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[差一點]就[沒命]了":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[差一點]就撞上[他]":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[差一點]就放棄再騎下去的[意念]":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[差一點]就讓[這種][傳統工藝]走不回來":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[差一點]忘了":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[差一點]把[爸爸][心愛]的[上等酒]給打翻了":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[差一點]提[前]引爆[華隆]跳票的[引信]":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[差一點]昏倒":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[差一點]沒到[九十分]":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[差一點]笑出來":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[差一點]見[上面]":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[差一點]遭到[截肢]":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[我][差一點]就笑了起來":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[我][差一點]被抓去坐牢":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[我][差一點]認不[出][她]來":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[我][真]的感動得[眼淚][都][差一點]掉下來了":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[我]的[隨從][差一點]就傷了[妳]":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[最後]還[差一點]就當選[高雄區]的[立法委員]":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[沙琰翎][差一點][陰溝裡翻船]":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[畢業生]的[一位]曾經在[美濃溪][差一點]溺水":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[當年][差一點]回不來":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "[這些][胎生]的[小苗][萬一]在[第一次]落下[運氣][差一點]":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "卻[真實地]讓[他]以為[差一點]就跌入了萬丈深淵":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "原來[他][差一點]摔倒了":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "又曾經在[泳]渡[深潭]時[不慎]捲入[旋渦][差一點]溺死":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "可是[我][差一點]被[卡子]抓走":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "否則[差一點]看不到[新][中國]":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "在[這場][危險風暴][中][差一點]丟了[性命]":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "居然[只][差一點]被執行了":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "把[經理][差一點]嚇昏了過去":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "爭[三]連[霸]的[瑞典][名將][艾柏格]則[差一點]落馬":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "還[差一點][旅行社][才]開門辦公":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    if utterance == "雖然[差一點]而沒挑戰[成功]":
        priorSTR, postSTR = inputSTRSpliter(inputSTR)
        telicityLIST = telicyCheck(priorSTR, postSTR)
        if telicityLIST[1] == True:
            resultDICT["差一點"] = True
        else:
            resultDICT["差一點"] = False

    return resultDICT