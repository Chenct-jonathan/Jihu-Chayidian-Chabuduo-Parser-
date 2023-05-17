#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from Exp02_Chabuduo import execLoki
import json
    
#catLIST = []
#catDICT = {}
#with open('./ref/sinica_Chabuduo.ref', 'r', encoding='utf-8') as f:
    #content = json.load(f)
    #for i in content['utterance'].keys():
        #catLIST.append(i)
#for i in catLIST:
    #catDICT[i] = []

#with open("../corpus/sinicaCorpus_Chabuduo_purged.txt", encoding="utf-8") as f:
    #corpusLIST = f.readlines()

checkDICT = {
    "Missing":[],
    "Predicative": [],
    "Adverbial": [],
    "Modifier": []
}
   
#for c in corpusLIST[:]:
    #resultDICT = execLoki(c)
    #for i in catLIST:
        #if resultDICT[i] != []:
            #catDICT[i].append(c)
        #else:
            #pass
    #if all(value == [] for value in resultDICT.values()) == True:
        #print("Missing: {}".format(c))
        #checkDICT["Missing"].append(c)
    #elif "Predicative" in resultDICT["Predicative"]:
        #print("Predicative: {}".format(c))
        #checkDICT["Predicative"].append(c)
    #elif "Adverbial" in resultDICT["Adverbial"]:
        #print("Adverbial: {}".format(c))
        #checkDICT["Adverbial"].append(c)
    #elif "Modifier" in resultDICT["Modifier"]:
        #print("Modifier: {}".format(c))
        #checkDICT["Modifier"].append(c)
    #else:
        #pass

#with open("missing_Chabuduo_0517.json", "w", encoding="utf-8") as jFILE:
    #json.dump(checkDICT, jFILE, ensure_ascii=False, indent=4)
    
#with open("Chabuduo_result_0517.json", "w", encoding="utf-8") as jFILE:
    #json.dump(catDICT, jFILE, ensure_ascii=False, indent=4)

with open("Chabuduo_result_0517.json", "r", encoding="utf-8") as jFILE:
    content = json.load(jFILE)
    for i in content.keys():
        print(i)
        resultDICT = execLoki(i)
        if all(value == [] for value in resultDICT.values()) == True:
            print("Missing: {}".format(i))
            checkDICT["Missing"].append(i)
        elif "Predicative" in resultDICT["Predicative"]:
            print("Predicative: {}".format(i))
            checkDICT["Predicative"].append(i)
        elif "Adverbial" in resultDICT["Adverbial"]:
            print("Adverbial: {}".format(i))
            checkDICT["Adverbial"].append(i)
        elif "Modifier" in resultDICT["Modifier"]:
            print("Modifier: {}".format(i))
            checkDICT["Modifier"].append(i)
        else:
            pass        
        

with open("utterance_cat.json", "w", encoding="utf-8") as jFILE:
    json.dump(checkDICT, jFILE, ensure_ascii=False, indent=4)