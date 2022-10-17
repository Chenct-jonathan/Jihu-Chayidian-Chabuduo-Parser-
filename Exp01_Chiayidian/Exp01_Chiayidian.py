#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 3.0 Template For Python3

    [URL] https://api.droidtown.co/Loki/BulkAPI/

    Request:
        {
            "username": "your_username",
            "input_list": ["your_input_1", "your_input_2"],
            "loki_key": "your_loki_key",
            "filter_list": ["intent_filter_list"] # optional
        }

    Response:
        {
            "status": True,
            "msg": "Success!",
            "version": "v223",
            "word_count_balance": 2000,
            "result_list": [
                {
                    "status": True,
                    "msg": "Success!",
                    "results": [
                        {
                            "intent": "intentName",
                            "pattern": "matchPattern",
                            "utterance": "matchUtterance",
                            "argument": ["arg1", "arg2", ... "argN"]
                        },
                        ...
                    ]
                },
                {
                    "status": False,
                    "msg": "No Match Intent!"
                }
            ]
        }
"""

from requests import post
from requests import codes
import math
import re
import json
try:
    from intent import Loki_sinica_chiyidian_adv
    #from intent import Loki_sinica_chiayidian
    #from intent import Loki_sinica_chiayidian_punc
    from intent import Loki_extend_chiayidian_adv
except:
    from .intent import Loki_sinica_chiyidian_adv
    #from .intent import Loki_sinica_chiayidian
    #from .intent import Loki_sinica_chiayidian_punc
    from .intent import Loki_extend_chiayidian_adv


with open("account.info", "r", encoding="utf-8") as f:
    accountDICT = json.load(f)
    
LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = accountDICT["username"]
LOKI_KEY = accountDICT["lokikey"]
# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []
INPUT_LIMIT = 20

class LokiResult():
    status = False
    message = ""
    version = ""
    balance = -1
    lokiResultLIST = []

    def __init__(self, inputLIST, filterLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []
        # filterLIST 空的就採用預設的 INTENT_FILTER
        if filterLIST == []:
            filterLIST = INTENT_FILTER

        try:
            result = post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": filterLIST
            })

            if result.status_code == codes.ok:
                result = result.json()
                self.status = result["status"]
                self.message = result["msg"]
                if result["status"]:
                    self.version = result["version"]
                    self.balance = result["word_count_balance"]
                    self.lokiResultLIST = result["result_list"]
            else:
                self.message = "{} Connection failed.".format(result.status_code)
        except Exception as e:
            self.message = str(e)

    def getStatus(self):
        return self.status

    def getMessage(self):
        return self.message

    def getVersion(self):
        return self.version

    def getBalance(self):
        return self.balance

    def getLokiStatus(self, index):
        rst = False
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["status"]
        return rst

    def getLokiMessage(self, index):
        rst = ""
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["msg"]
        return rst

    def getLokiLen(self, index):
        rst = 0
        if index < len(self.lokiResultLIST):
            if self.lokiResultLIST[index]["status"]:
                rst = len(self.lokiResultLIST[index]["results"])
        return rst

    def getLokiResult(self, index, resultIndex):
        lokiResultDICT = None
        if resultIndex < self.getLokiLen(index):
            lokiResultDICT = self.lokiResultLIST[index]["results"][resultIndex]
        return lokiResultDICT

    def getIntent(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["intent"]
        return rst

    def getPattern(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["pattern"]
        return rst

    def getUtterance(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["utterance"]
        return rst

    def getArgs(self, index, resultIndex):
        rst = []
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["argument"]
        return rst

def runLoki(inputLIST, filterLIST=[]):
    # 將 intent 會使用到的 key 預先設爲空列表
    resultDICT = {
       #"key": []
    }
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # sinica_chiyidian_adv
                if lokiRst.getIntent(index, resultIndex) == "sinica_chiyidian_adv":
                    resultDICT = Loki_sinica_chiyidian_adv.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getPattern(index, resultIndex), resultDICT)

                # sinica_chiayidian
                #if lokiRst.getIntent(index, resultIndex) == "sinica_chiayidian":
                    #resultDICT = Loki_sinica_chiayidian.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # sinica_chiayidian_punc
                #if lokiRst.getIntent(index, resultIndex) == "sinica_chiayidian_punc":
                    #resultDICT = Loki_sinica_chiayidian_punc.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # extend_chiayidian_adv
                if lokiRst.getIntent(index, resultIndex) == "extend_chiayidian_adv":
                    resultDICT = Loki_extend_chiayidian_adv.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def execLoki(content, filterLIST=[], splitLIST=[]):
    """
    input
        content       STR / STR[]    要執行 loki 分析的內容 (可以是字串或字串列表)
        filterLIST    STR[]          指定要比對的意圖 (空列表代表不指定)
        splitLIST     STR[]          指定要斷句的符號 (空列表代表不指定)
                                     * 如果一句 content 內包含同一意圖的多個 utterance，請使用 splitLIST 切割 content

    output
        resultDICT    DICT           合併 runLoki() 的結果，請先設定 runLoki() 的 resultDICT 初始值

    e.g.
        splitLIST = ["！", "，", "。", "？", "!", ",", "
", "；", "　", ";"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？")                      # output => ["今天天氣"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？", splitLIST=splitLIST) # output => ["今天天氣", "後天氣象"]
        resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"])                # output => ["今天天氣", "後天氣象"]
    """
    contentLIST = []
    if type(content) == str:
        contentLIST = [content]
    if type(content) == list:
        contentLIST = content

    resultDICT = {}
    if contentLIST:
        if splitLIST:
            # 依 splitLIST 做分句切割
            splitPAT = re.compile("[{}]".format("".join(splitLIST)))
            inputLIST = []
            for c in contentLIST:
                tmpLIST = splitPAT.split(c)
                inputLIST.extend(tmpLIST)
            # 去除空字串
            while "" in inputLIST:
                inputLIST.remove("")
        else:
            # 不做分句切割處理
            inputLIST = contentLIST

        # 依 INPUT_LIMIT 限制批次處理
        for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
            lokiResultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)
            if "msg" in lokiResultDICT:
                return lokiResultDICT

            # 將 lokiResultDICT 結果儲存至 resultDICT
            for k in lokiResultDICT:
                if k not in resultDICT:
                    resultDICT[k] = []
                resultDICT[k].extend(lokiResultDICT[k])

    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)

    if "msg" in resultDICT:
        print(resultDICT["msg"])

def testIntent():
    # sinica_chiyidian_adv
    print("[TEST] sinica_chiyidian_adv")
    inputLIST = ['差一點昏倒','差一點見上面','差一點就沒命了','差一點沒到九十分','居然只差一點被執行了','否則差一點看不到新中國','她差一點栽在印度芭娜姬的手中','差一點把爸爸心愛的上等酒給打翻了','差一點他那神父爸爸便不能認這個孩子','畢業生的一位曾經在美濃溪差一點溺水']
    testLoki(inputLIST, ['sinica_chiyidian_adv'])
    print("")

    # sinica_chiayidian
    print("[TEST] sinica_chiayidian")
    inputLIST = ['差一點忘了','差一點昏倒','差一點笑出來','差一點見上面','差一點就抽腳筋','差一點就撞上他','差一點就沒命了','差一點就車畚斗','差一點遭到截肢','差一點沒到九十分','當年差一點回不來','原來他差一點摔倒了','我差一點就笑了起來','我差一點被抓去坐牢','我差一點認不出她來','居然只差一點被執行了','可是我差一點被卡子抓走','否則差一點看不到新中國','我的隨從差一點就傷了妳','把經理差一點嚇昏了過去','沙琰翎差一點陰溝裡翻船','雖然差一點而沒挑戰成功','差一點沒把手指頭當菜切了','還差一點旅行社才開門辦公','差一點就放棄再騎下去的意念','她差一點栽在印度芭娜姬的手中','差一點提前引爆華隆跳票的引信','七歲的妹妹差一點被二個壞人強暴','三個年輕人差一點就要去大鬧天宮','在這場危險風暴中差一點丟了性命','差一點就讓這種傳統工藝走不回來','差一點把爸爸心愛的上等酒給打翻了','我真的感動得眼淚都差一點掉下來了','只差一點沒和那漂亮女人做成一回好事','差一點他那神父爸爸便不能認這個孩子','最後還差一點就當選高雄區的立法委員','畢業生的一位曾經在美濃溪差一點溺水','爭三連霸的瑞典名將艾柏格則差一點落馬','卻真實地讓他以為差一點就跌入了萬丈深淵','又曾經在泳渡深潭時不慎捲入旋渦差一點溺死','這些胎生的小苗萬一在第一次落下運氣差一點']
    testLoki(inputLIST, ['sinica_chiayidian'])
    print("")

    # sinica_chiayidian_punc
    print("[TEST] sinica_chiayidian_punc")
    inputLIST = ['謝長亨差一點就是中華職棒第一個「選秀狀元」']
    testLoki(inputLIST, ['sinica_chiayidian_punc'])
    print("")

    # extend_chiayidian_adv
    print("[TEST] extend_chiayidian_adv")
    inputLIST = ['差一點一個人去']
    testLoki(inputLIST, ['extend_chiayidian_adv'])
    print("")


if __name__ == "__main__":
    # 測試所有意圖
    #testIntent()

    #with open("../corpus/sinicaCorpus_Chiayidian_purged.txt", encoding="utf-8") as k:
        #lines = ''.join(k.readlines()).split("\n")
    #for i in range(len(lines)):
        #inputSTR = (lines[i])
        #print("{}:".format(i+1))
        #runLoki([inputSTR])
        
    inputSTR ="我差一點被跑步"
    runLoki([inputSTR])