#!/user/bin/env python
# -*- coding: utf-8 -*-

import re

with open('sinicaCorpus_Jihu.txt',encoding="utf-8") as f:
    lines = ''.join(f.readlines())
    purge = re.findall(r'([０-９ａ-ｚＡ-Ｚ\u4E00-\u9FFF％]*幾乎\t*[０-９ａ-ｚＡ-Ｚ\u4E00-\u9FFF％]*)', lines)

with open('sinicaCorpus_Jihu_purge.txt','w',encoding="utf-8") as g:
    for i in range(len(purge)):
        g.write(str(i+1)+" "+purge[i].replace("\t","")+"\n")





