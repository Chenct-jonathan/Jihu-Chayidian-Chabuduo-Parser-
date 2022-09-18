#!/user/bin/env python
# -*- coding: utf-8 -*-

import re

reDICT = {
    "Chiayidian":"[０-９ａ-ｚＡ-Ｚ\u4E00-\u9FFF％]*差一點\s*[０-９ａ-ｚＡ-Ｚ\u4E00-\u9FFF％]*",
    "Chiabuduo":"[０-９ａ-ｚＡ-Ｚ\u4E00-\u9FFF％]*差不多\s*[０-９ａ-ｚＡ-Ｚ\u4E00-\u9FFF％]*",
    "Jihu":'[０-９ａ-ｚＡ-Ｚ\u4E00-\u9FFF％]*幾乎\s*[０-９ａ-ｚＡ-Ｚ\u4E00-\u9FFF％]*'
}
with open('sinicaCorpus_{}_raw.txt'.format("Jihu"),encoding="utf-8") as f:
    lines = ''.join(f.readlines())
    purge = re.findall(r'{}'.format(reDICT["Jihu"]), lines)

with open('sinicaCorpus_{}_purge.txt'.format("Jihu"),'w',encoding="utf-8") as g:
    for i in range(len(purge)):
        g.write(str(i+1)+" "+purge[i].replace("\t","")+"\n")





