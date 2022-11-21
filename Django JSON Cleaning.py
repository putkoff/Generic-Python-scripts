import requests
import json
def getKeys(js):
    names = []
    for key in js:
        names.append(key)
    return names
def delJsVar():
    del js
def checkLs(na,ls):
    for i in range(0,len(ls)):
        for k in range(0,len(js[na])):
            if js[ls[i]][k] in ['N/A','',"",'-']:
                del js[ls[i]][k]
def checkStr(st):
    if js[st] in ['N/A','',"",'-']:
        del js[st]
def checkJs(jso,nam):
    for i in range(0,len(nam)):
        if jso[nam[i]] in ['N/A','',"",'-']:
            del jso[nam[i]]
def isLs(x):
    return (type(x) is list)
def isStr(x):
    return (type(x) is str)
def isInt(x):
    return (type(x) is int)
global js
js = requests.get('https://coderbyte.com/api/challenges/json/json-cleaning').json()
jsN = {'names':{},'str':[],'ls':[],'js':[],'int':[]}
jsN['names']['all'] = getKeys(js)
for i in range(0,len(jsN['names']['all'])):
    na = jsN['names']['all'][i]
    n = js[na]
    if isLs(n) == True:
        jsN['ls'].append(na)
        checkLs(na,jsN['ls'])
    elif isStr(n) == True:
        jsN['str'].append(na)
        checkStr(na)
    elif isInt(n) == True:
        jsN['int'].append(na)
    else:
         jsN['js'].append(na)
         if na not in jsN:
             jsN[na] = getKeys(js[na])
             checkJs(js[na],jsN[na])
print(js)          

