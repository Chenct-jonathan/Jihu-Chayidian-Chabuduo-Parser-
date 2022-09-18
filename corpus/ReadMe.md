# Corpus

The files are named according to the following format ```<source><query><status>.txt ```, encoding utf-8. 

All utterances in ```raw``` files are collected from [Sinica Corpus](http://asbc.iis.sinica.edu.tw/). 

The phrases containing keywords "Jihu", "Chiayidian" or "Chiabuduo" were extracted and put together as ```_purged01``` files.  

---

### Regular Expressions

```regex
[０-９ａ-ｚＡ-Ｚ\u4E00-\u9FFF％]*差一點\s*[０-９ａ-ｚＡ-Ｚ\u4E00-\u9FFF％]*
[０-９ａ-ｚＡ-Ｚ\u4E00-\u9FFF％]*差不多\s*[０-９ａ-ｚＡ-Ｚ\u4E00-\u9FFF％]*
[０-９ａ-ｚＡ-Ｚ\u4E00-\u9FFF％]*幾乎\s*[０-９ａ-ｚＡ-Ｚ\u4E00-\u9FFF％]*
```