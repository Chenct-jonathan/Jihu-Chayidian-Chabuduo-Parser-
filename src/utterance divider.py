#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

def utterance_divider():
    utterance = {"jihu_punc":[],"jihu":[], "chabuduo":[], "chabuduo_punc":[], "chayidian":[], "chayidian_punc":[]}
    with open("sinicaCorpus_Jihu_purged.txt", encoding="utf-8") as f:
        lines = ''.join(f.readlines()).split("\n")
        
    for i in range(len(lines)):
        if "「" in lines[i] or "」" in lines[i] or "％" in lines[i] or "…" in lines[i]:
            utterance["jihu_punc"].append(lines[i])
        elif lines[i] == '':
            pass
        else:
            utterance["jihu"].append(lines[i])
    f.close()
    
    with open("sinicaCorpus_Chabuduo_purged.txt", encoding="utf-8") as g:
        lines = ''.join(g.readlines()).split("\n")
        
    for i in range(len(lines)):
        if "「" in lines[i] or "」" in lines[i] or "％" in lines[i] or "…" in lines[i]:
            utterance["chabuduo_punc"].append(lines[i])
        elif lines[i] == '':
            pass
        else:
            utterance["chabuduo"].append(lines[i])
    g.close()    
    
    with open("sinicaCorpus_Chayidian_purged.txt", encoding="utf-8") as k:
        lines = ''.join(k.readlines()).split("\n")
        
    for i in range(len(lines)):
        if "「" in lines[i] or "」" in lines[i] or "％" in lines[i] or "…" in lines[i]:
            utterance["chayidian_punc"].append(lines[i])
        elif lines[i] == '':
            pass
        else:
            utterance["chayidian"].append(lines[i])
    k.close()    
    
    with open("utterance.json", "w",encoding="utf-8") as fp:
        json.dump(utterance,fp,ensure_ascii=False)


if __name__ == "__main__" :
    utterance_divider()