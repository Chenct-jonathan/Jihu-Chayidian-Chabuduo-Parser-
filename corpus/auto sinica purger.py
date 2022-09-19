#!/user/bin/env python
# -*- coding: utf-8 -*-

import re
import json 

with open("corpus_op_re.json","r",encoding="utf-8") as f:
    corpus_op_re = json.load(f)
regexLIST = list(corpus_op_re.items())

def sinica_purger(i):
    with open('sinicaCorpus_{}_raw.txt'.format(regexLIST[i][0]),encoding="utf-8") as f:
        lines = ''.join(f.readlines())
        purge = re.findall(r'{}'.format(regexLIST[i][1]), lines)
    with open('sinicaCorpus_{}_purge.txt'.format(regexLIST[i][0]),'w',encoding="utf-8") as g:
        for j in range(len(purge)):
            g.write(purge[j].replace("\t","").replace("\s","").replace(" ","")+"\n")
            

def main(i):
    resultDICT = {"JiHu_status":True,
                  "ChaBuDuo_status":True,
                  "ChaYiDian_status":True
                  }
    try:
        sinica_purger(i)
    except:
        resultDICT["{}_status".format(regexLIST[i][0])] = False


    return resultDICT

if __name__ == "__main__":
    for i in range(len(corpus_op_re)):
        main(i)

