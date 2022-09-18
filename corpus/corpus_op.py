#!/user/bin/env python
# -*- coding: utf-8 -*-

import re

reDICT = {
    "Chiayidian":"[０-９ａ-ｚＡ-Ｚ\u4E00-\u9FFF％]*差一點\s*[０-９ａ-ｚＡ-Ｚ\u4E00-\u9FFF％]*",
    "Chiabuduo":"[０-９ａ-ｚＡ-Ｚ\u4E00-\u9FFF％]*差不多\s*[０-９ａ-ｚＡ-Ｚ\u4E00-\u9FFF％]*",
    "Jihu":'[０-９ａ-ｚＡ-Ｚ\u4E00-\u9FFF％]*幾乎\s*[０-９ａ-ｚＡ-Ｚ\u4E00-\u9FFF％]*'
}

with open('sinicaCorpus_{}_raw.txt'.format("Chiabuduo"),encoding="utf-8") as f:
    lines = ''.join(f.readlines())
    purge = re.findall(r'{}'.format(reDICT["Chiabuduo"]), lines)

with open('sinicaCorpus_{}_purge.txt'.format("Chiabuduo"),'w',encoding="utf-8") as g:
    for i in range(len(purge)):
        g.write(str(i+1)+" "+purge[i].replace("\t","")+"\n")


def jihu_purger():
    '''
    Extract sentences with Jihu(幾乎) from raw Sinica Corpus file, and save it into _purge file.
    '''
    with open('sinicaCorpus_Jihu.txt',encoding="utf-8") as f:
        lines = ''.join(f.readlines())
        purge = re.findall(r'([０-９ａ-ｚＡ-Ｚ\u4E00-\u9FFF％]*幾乎\t*[０-９ａ-ｚＡ-Ｚ\u4E00-\u9FFF％]*)', lines)

    with open('sinicaCorpus_Jihu_purge.txt','w',encoding="utf-8") as g:
        for i in range(len(purge)):
            g.write(str(i+1)+" "+purge[i].replace("\t","")+"\n")


def main():
    resultDICT = {"JiHu_status":True,
                  "ChaBuDuo_status":True,
                  "ChaYiDian_status":True
                  }
    try:
        jihu_purger()
    except:
        resultDICT["JiHu_status"] = False


    return resultDICT

if __name__ == "__main__":
    main()










