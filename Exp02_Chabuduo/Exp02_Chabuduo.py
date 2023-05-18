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
                    "msg": "No matching Intent."
                }
            ]
        }
"""

from requests import post
from requests import codes
import math
import json
import re
try:
    from intent import Loki_sinica_Chabuduo
except:
    from intent import Loki_sinica_Chabuduo
    
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
       "Response": [],
       "Predicative": [],
       "Adverbial": [],
       "Modifier": []
       #'唸個差不多': [],
       #'大體差不多': [],
       #'其實差不多啦': [],
       #'和諾可差不多': [],
       #'差不多有十年': [],
       #'差不多的年紀': [],
       #'情況也差不多': [],
       #'情況都差不多': [],
       #'我想三位差不多': [],
       #'聽起來差不多嗎': [],
       #'各縣市情況差不多': [],
       #'基本設計則差不多': [],
       #'好像意思上差不多': [],
       #'差不多也是經典了': [],
       #'摩托車差不多一輛': [],
       #'海青病得差不多了': [],
       #'生命已經差不多了': [],
       #'說像海盜還差不多': [],
       #'差不多……好了……': [],
       #'差不多到一半路程時': [],
       #'差不多是二十八歲吧': [],
       #'差不多都已查證清楚': [],
       #'所使用的工具差不多': [],
       #'由於大家年齡差不多': [],
       #'雖然看起來差不多亮': [],
       #'可是吃飯的時候差不多': [],
       #'夜晚差不多都在村子中': [],
       #'大小差不多和地球一般': [],
       #'身上器官也壞得差不多': [],
       #'兒童奴隸差不多就可消除': [],
       #'就是滿正常的差不多國一': [],
       #'差不多兩個半鐘頭就到了': [],
       #'差不多有廿十來個人要去': [],
       #'差不多ｔｗｏｈｏｕｒｓ': [],
       #'所以兩地人民性情差不多': [],
       #'所以勞逸之勢實在差不多': [],
       #'鄭華娟的回答是差不多的': [],
       #'人生閱歷方面的成熟度差不多': [],
       #'伊的手掌差不多有我的兩倍大': [],
       #'然而大體上說差不多沒有進步': [],
       #'因為一般人吃一個半饅頭差不多': [],
       #'因為差不多的人都回中南部去了': [],
       #'看伊的手骨差不多有我的小腿粗': [],
       #'差不多的古蹟都變成了「活古蹟」': [],
       #'隆乳費用差不多是三萬五千元泰幣': [],
       #'香港差不多全部入口貨品都是免稅的': [],
       #'差不多個個都在批判會上登台自我檢查': [],
       #'這差不多就是其第一個系統所用的詞典': [],
       #'說來說去差不多把這個Ｔａｐｅ給說完了': [],
       #'我接過的國宅案中差不多有９０％都發生這類情況': [],
       #'認為科技的發展自從工業革命以來已差不多到了極致': [],
       #'差不多每七個將軍中就有一個紅安縣人和兩任國家主席': []
    }
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # sinica_Chabuduo
                if lokiRst.getIntent(index, resultIndex) == "sinica_Chabuduo":
                    resultDICT = Loki_sinica_Chabuduo.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

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
    # sinica_Chabuduo
    print("[TEST] sinica_Chabuduo")
    inputLIST = ['和諾可差不多','差不多有十年','情況也差不多','情況都差不多','聽起來差不多嗎','各縣市情況差不多','基本設計則差不多','好像意思上差不多','海青病得差不多了','生命已經差不多了','說像海盜還差不多','差不多到一半路程時','差不多是二十八歲吧','差不多都已查證清楚','所使用的工具差不多','那我不就差不多了嗎','雖然看起來差不多亮','夜晚差不多都在村子中','身上器官也壞得差不多','兒童奴隸差不多就可消除','就是滿正常的差不多國一','所以兩地人民性情差不多','人生閱歷方面的成熟度差不多','差不多的古蹟都變成了「活古蹟」','隆乳費用差不多是三萬五千元泰幣','香港差不多全部入口貨品都是免稅的','我接過的國宅案中差不多有９０％都發生這類情況','認為科技的發展自從工業革命以來已差不多到了極致']
    testLoki(inputLIST, ['sinica_Chabuduo'])
    print("")


if __name__ == "__main__":
    #with open ("./sinicaCorpus_Chiabuduo_purged.txt", encoding='utf-8') as f:
        #lines = ''.join(f.readlines()).split("\n")
        #for i in range(0,51):
            #inputSTR = lines[i]
            #print("{}. ".format(i+1)+inputSTR)
            #resultDICT = runLoki([inputSTR])
    inputSTR = "白癡你做個差不多就好不用太認真"
    resultDICT = runLoki([inputSTR])
    print(resultDICT)
    print(resultDICT["Response"])