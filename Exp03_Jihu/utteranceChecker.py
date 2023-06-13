#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from Exp03_Jihu import execLoki
import json

missingLIST = []
with open('../corpus/sinicaCorpus_Jihu_purged.txt', 'r', encoding='utf-8') as f:
    utteranceLIST = f.readlines(100)
    for i in utteranceLIST:
        print(i)
        resultDICT = execLoki(i)
        if 'sinica' in resultDICT['Sinica']:
            pass
        else:
            missingLIST.append(i)

with open('missing_Jihu_0614.txt', 'w', encoding='utf-8') as j:
    for i in missingLIST:
        j.write(i)
    