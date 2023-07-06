#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 4.0 Template For Python3

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
from getUtterance import get_UtteranceFormat
from pprint import pprint
import json
import math
import os
import re
try:
    from intent import Loki_sinica_Jihu
except:
    from intent import Loki_sinica_Jihu


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
try:
    accountInfo = json.load(open(os.path.join(os.path.dirname(__file__), "account.info"), encoding="utf-8"))
    USERNAME = accountInfo["username"]
    LOKI_KEY = accountInfo["loki_key"]
except Exception as e:
    print("[ERROR] AccountInfo => {}".format(str(e)))
    USERNAME = ""
    LOKI_KEY = ""

# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []
INPUT_LIMIT = 20
#utteranceDICT =  get_UtteranceFormat('./ref/sinica_Jihu.ref')
#pprint(utteranceDICT)
#pprint(len(utteranceDICT))
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
                    if "word_count_balance" in result:
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
    resultDICT = get_UtteranceFormat('./ref/sinica_Jihu.ref')
    '''
    {
       #'Sinica': [],
       '幾乎一樣': [],
       '幾乎不做講解': [],
       '幾乎不可或缺的參考資料': [],
       '幾乎令我斷氣': [],
       '幾乎只有團體': [],
       '幾乎可以看': [],
       '幾乎和小朋友美術課的大張圖畫紙一樣大': [],
       '幾乎垂直參宿三星': [],
       '幾乎多為如何投資': [],
       '幾乎完全消失': [],
       '幾乎就有自己的使用文字了': [],
       '幾乎年年都獲得全國的各種名次': [],
       '幾乎很少人知道': [],
       '幾乎打破福特內部產品發展的每項紀錄': [],
       '幾乎把荷商擠出歐洲市場': [],
       '幾乎把那小販的祖宗三代都罵過了': [],
       '幾乎損壞殆盡': [],
       '幾乎是五年前的兩倍': [],
       '幾乎有十二億的中國人在等待這一天的來臨': [],
       '幾乎未訂捐贈公共設施的回饋辦法': [],
       '幾乎每個家庭的物質生活都相當富裕': [],
       '幾乎每兩三個月就跳增一倍': [],
       '幾乎比生母施虐高出一倍': [],
       '幾乎注定是會賠錢的': [],
       '幾乎無限長的百科全書': [],
       '幾乎瓦解於旦夕': [],
       '幾乎看不見灰塵': [],
       '幾乎等同於外界利益獨立的經營體': [],
       '幾乎要令他爆炸了': [],
       '幾乎要休學的時候': [],
       '幾乎適合各種場合': [],
       '幾乎都是屬於這種古老的岩層': [],
       "幾乎呈左右對照配置": [],
       "幾乎處於無免疫力狀態": [],
       "幾乎清一色丹麥裔":[],
       "幾乎全身被割傷":[],
       "幾乎包羅了所有可能的片語結構":[],
       "幾乎撞個正著":[],
       "幾乎被認定為民主進步必經之路": [],
       "幾乎全武行的紀錄": [],
       "幾乎在一夜之間統統升級": [],
       "幾乎全村七十九戶有適齡的孩子都會共襄盛舉": [],
       "幾乎純理性的思維習慣": [],
       "幾乎被破壞殆盡": [],
       "幾乎平均二名打者就有一名被三振": [],
       "幾乎全面漲停的榮景之際": [],
       "幾乎難以見一次面":[],
       "幾乎涵蓋所有的中文字":[],
       "幾乎像窗邊族這樣":[],
       "幾乎多為他們員工撰寫":[],
       "幾乎使她致命的車禍和因車禍而起的官司":[],
       "幾乎逐字拷貝之行為":[],
       "幾乎全是視力健全的少年":[],
       "幾乎再次暈過去":[],
       "幾乎想也沒想":[],
       "佈佔幾乎全部的畫面":[],
       "幾乎難以辨認":[],
       "幾乎「太親切」啦":[]
    }
    '''
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # sinica_Jihu
                if lokiRst.getIntent(index, resultIndex) == "sinica_Jihu":
                    resultDICT = Loki_sinica_Jihu.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getPattern(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

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
                if type(lokiResultDICT[k]) == list:
                    resultDICT[k].extend(lokiResultDICT[k])
                else:
                    resultDICT[k].append(lokiResultDICT[k])

    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)

    if "msg" in resultDICT:
        print(resultDICT["msg"])

def testIntent():
    # sinica_Jihu
    print("[TEST] sinica_Jihu")
    inputLIST = ['幾乎一樣','幾乎可以看','幾乎完全消失','幾乎很少人知道','幾乎瓦解於旦夕','幾乎垂直參宿三星','幾乎是五年前的兩倍','幾乎注定是會賠錢的','幾乎每兩三個月就跳增一倍','幾乎都是屬於這種古老的岩層','幾乎未訂捐贈公共設施的回饋辦法','幾乎每個家庭的物質生活都相當富裕']
    testLoki(inputLIST, ['sinica_Jihu'])
    print("")


if __name__ == "__main__":
    # 測試所有意圖
    #testIntent()
    # 測試其它句子
    #filterLIST = []
    #splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
    resultDICT = execLoki("肝等內臟各部器官也幾乎完好如初")            # output => ["今天天氣"]
    #resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST, splitLIST) # output => ["今天天氣", "後天氣象"]
    #resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"], filterLIST)      # output => ["今天天氣", "後天氣象"]