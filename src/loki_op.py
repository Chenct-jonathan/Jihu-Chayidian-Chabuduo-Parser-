#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import argparse
from glob import iglob
import re
import os
try:
    import rapidjson as json
except ModuleNotFoundError:
    import json
from pprint import pprint
from requests import post
from time import sleep
from json import JSONDecodeError


def listUtterance(payloadDICT):
    url = "https://api.droidtown.co/Loki/Utterance/"

    for i in range(0, len(payloadDICT["intent"]), 20):
        payload = {
            "username"    : payloadDICT["username"],
            "loki_key"    : payloadDICT["loki_key"],
            "intent_list" : payloadDICT["intent"][i:i+20]
        }
        response = post(url, json=payload).json()
        if response["status"] == True:
            sleep(0.5)
        else:
            return response["msg"]
    return response

def addUtterance(payloadDICT):
    url = "https://api.droidtown.co/Loki/Command/"

    for i in range(0, len(payloadDICT["utterance"]), 20):
        payload = {
            "username" : payloadDICT["username"],
            "loki_key" : payloadDICT["loki_key"],
            "intent"   : payloadDICT["intent"],
            "utterance": payloadDICT["utterance"][i:i+20]
        }
        response = post(url, json=payload).json()
        if response["status"] == True:
            sleep(0.5)
            print("processed:{}\n".format("\n".join(payloadDICT["utterance"][i:i+20])))
        else:
            return response["msg"]
    return response

if __name__== "__main__":
    """
    Basic usage:
        To add postve_num utterances listed in the corpus to the Loki webpage:
        $ python3 loki_op.py au postve_num
        To list utterances in an intent in the Loki webpage:
        $ python3 loki_op.py lu postve_num
        To add postve_num utterances listed in the purged corpus to the Loki webpage:
        $ python3 loki_op.py apu postve_num
    """

    #parser = argparse.ArgumentParser()
    #parser.add_argument("command")
    #parser.add_argument("intent")
    #args = parser.parse_args()
    command = "au" #args.command
    intent = "jihu" #args.intent

    utteranceDICT = json.load(open("../corpus/utterance.json", encoding = "utf-8"))

    if command.lower() in ("au", "lu"): #au stands for "addUtterance"; lu stands for "listUtterance"; apu stands for "addPurgedUtterance"
        payloadDICT = json.load(open("account.info"))
        if command.lower() == "au":
            payloadDICT["intent"] = intent
            payloadDICT["utterance"] = utteranceDICT["jihu"]

            if payloadDICT["utterance"] == []:
                print("Well...I don't see any intent named {}.".format(intent))
            else:
                try:
                    pprint(payloadDICT["utterance"])
                    response = addUtterance(payloadDICT)
                    if response["status"] == True:
                        pass
                    else: #response["status"] == False
                        print(response["msg"])
                        pprint(response)
                except JSONDecodeError:
                    print(payloadDICT["utterance"][i])

        else: #command is "lu"
            payloadDICT["intent"] = [intent]
            response = listUtterance(payloadDICT)
            pprint(response)
    else:
        print("{}? What do you mean by that? I don't get it.".format(command))