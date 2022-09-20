#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

def utterance_divider():
    utterance = {"jihu_punc":[],"jihu":[], "chiabuduo":[], "chiabuduo_punc":[], "chiayidian":[], "chiayidian_punc":[]}
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
    
    with open("sinicaCorpus_Chiabuduo_purged.txt", encoding="utf-8") as g:
        lines = ''.join(g.readlines()).split("\n")
        
    for i in range(len(lines)):
        if "「" in lines[i] or "」" in lines[i] or "％" in lines[i] or "…" in lines[i]:
            utterance["chiabuduo_punc"].append(lines[i])
        elif lines[i] == '':
            pass
        else:
            utterance["chiabuduo"].append(lines[i])
    g.close()    
    
    with open("sinicaCorpus_Chiayidian_purged.txt", encoding="utf-8") as k:
        lines = ''.join(k.readlines()).split("\n")
        
    for i in range(len(lines)):
        if "「" in lines[i] or "」" in lines[i] or "％" in lines[i] or "…" in lines[i]:
            utterance["chiayidian_punc"].append(lines[i])
        elif lines[i] == '':
            pass
        else:
            utterance["chiayidian"].append(lines[i])
    k.close()    
    
    with open("utterance.json", "w",encoding="utf-8") as fp:
        json.dump(utterance,fp,ensure_ascii=False)


if __name__ == "__main__" :
    utterance_divider()