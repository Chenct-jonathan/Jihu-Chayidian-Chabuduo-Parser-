#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

def utterance_divider():
    utterance = {"Jihu_punc":[],"Jihu":[], "Chiabuduo":[], "Chiabuduo_punc":[], "Chiayidian":[], "Chiayidian_punc":[]}
    with open("sinicaCorpus_Jihu_purged.txt", encoding="utf-8") as f:
        lines = ''.join(f.readlines()).split("\n")
        
    for i in range(len(lines)):
        if "「" in lines[i] or "」" in lines[i] or "％" in lines[i] or "…" in lines[i]:
            utterance["Jihu_punc"].append(lines[i])
        elif lines[i] == '':
            pass
        else:
            utterance["Jihu"].append(lines[i])
    f.close()
    
    with open("sinicaCorpus_Chiabuduo_purged.txt", encoding="utf-8") as g:
        lines = ''.join(g.readlines()).split("\n")
        
    for i in range(len(lines)):
        if "「" in lines[i] or "」" in lines[i] or "％" in lines[i] or "…" in lines[i]:
            utterance["Chiabuduo_punc"].append(lines[i])
        elif lines[i] == '':
            pass
        else:
            utterance["Chiabuduo"].append(lines[i])
    g.close()    
    
    with open("sinicaCorpus_Chiayidian_purged.txt", encoding="utf-8") as k:
        lines = ''.join(k.readlines()).split("\n")
        
    for i in range(len(lines)):
        if "「" in lines[i] or "」" in lines[i] or "％" in lines[i] or "…" in lines[i]:
            utterance["Chiayidian_punc"].append(lines[i])
        elif lines[i] == '':
            pass
        else:
            utterance["Chiayidian"].append(lines[i])
    k.close()    
    
    with open("utterance.json", "w",encoding="utf-8") as fp:
        json.dump(utterance,fp,ensure_ascii=False)


if __name__ == "__main__" :
    utterance_divider()