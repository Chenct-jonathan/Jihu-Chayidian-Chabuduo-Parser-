#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from Exp03_Jihu import execLoki
from getUtterance import get_UtteranceFormat
from pprint import pprint
import json

catDICT = get_UtteranceFormat('./ref/sinica_Jihu.ref')
catDICT['missing'] = []
pprint(catDICT)

count = 1
with open('../corpus/sinicaCorpus_Jihu_purged.txt', 'r', encoding='utf-8') as f:
    utteranceLIST = f.readlines()
    for i in utteranceLIST[1501:]:
        print(f'({count}) : {i}')
        resultDICT = execLoki(i)
        if all(value == [] for value in resultDICT.values()) == True:
            catDICT['missing'].append(i)
        else:
            for key,value in resultDICT.items():
                if value != []:
                    #print(f'對到 {key}')
                    catDICT[key].append(i)
                else:
                    pass
        count += 1
        
with open('./log/Jihu_cat_0707.txt', 'w', encoding='utf-8') as jFILE:
    json.dump(catDICT, jFILE, ensure_ascii=False, indent='\t')

'''
with open('../corpus/sinicaCorpus_Jihu_purged.txt', 'r', encoding='utf-8') as f:
    utteranceLIST = f.readlines()
    for i in utteranceLIST[:501]:
        print(i)
        resultDICT = execLoki(i)
        if 'sinica' in resultDICT['Sinica']:
            pass
        else:
            missingLIST.append(i)

with open('./log/missing_Jihu_0616.txt', 'w', encoding='utf-8') as j:
    for i in missingLIST:
        j.write(i)
'''    