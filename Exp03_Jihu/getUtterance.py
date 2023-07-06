#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

def get_UtteranceFormat(file):
    catDICT = {}
    with open(f'{file}', 'r', encoding='utf-8') as jFILE:
        utteranceDICT = json.load(jFILE)
        for i in utteranceDICT['utterance'].keys():
            catDICT[i] = []
    #catDICT['missing'] = []
    #pprint(catDICT)
    return catDICT