import json
def getHigher():
    for i in range(0,len(js['names'])):
        upAdd(getNaI(i),highestLs(js['adds'][getNaI(i)]))
def sortList(ls):
    ls.sort()
    return ls
def highestLs(ls):
    return sortList(ls)[-1]
def getNaI(i):
    return js['names'][i]
def addAll():
    add = 0
    for i in range(0,len(js['names'])):
        add += int(js['names'][i])
    return add
def addLs(x,st):
    if x not in js[st]:
        js[st].append(x)
def addJs(x,y,st):
    if x not in js[st]:
        js[st][x] = []
    js[st][x].append(y)
def findIt(x,ls):
    for i in range(0,len(ls)):
        if str(x) == str(ls[i]):
            return i
def getSpRd(x,k):
    return str(js[str(x)][k])
def getRd(x):
    return str(js[str(x)])
def upAddSpF(x,k,z):
    js['adds'][getSpRd(x,k)][findRd(x,k)] = int(z)
def upAddSp(x,k,z):
    js['adds'][x][k] = int(z)
def upAdd(x,z):
    js['adds'][x] = [int(z)]
def getAddSp(x,k):
    return js['adds'][getSpRd(x,k)][findRd(x,k)]
def findRd(x,k):
    return findIt(x,js[getSpRd(x,k)])
def subIt(ls):
    sub = int(ls[0])
    for i in range(1,len(ls)):
        sub -= int(ls[i])
    return sub
def countLs(na):
    ls = js['adds'][na]
    lsN = [0,0,[],0,None]
    for i in range(0,len(ls)):
        if type(ls[i]) is list:
            lsN[0] += 1
            lsN[2].append(i)
        else:
            lsN[1] += int(ls[i])
            lsN[3] += 1
    if lsN[0] == 1:
        lsN[4] = subIt([addAll(),lsN[1],na])
    if lsN[0] == 0:
        lsN[4] = subIt([addAll(),na])
    return lsN
def getTraff(obj1):
    names = []
    for i in range(0,len(obj1)):
        js[str(obj1[i].split(':')[0])] = json.loads(obj1[i].split(':')[1])
    for key, value in js.items():
        names.append(str(key))
    js['have'],js['names'],js['adds'] = [],names,{}
    for j in range(0,len(js['names'])):
        na = js['names'][j]
        for k in range(0,len(js[na])):
            addJs(na,[],'adds')
    for j in range(0,len(js['names'])):
        na = js['names'][j]
        for k in range(0,len(js[na])):
            now = js[na][k]
            if len(js[str(na)]) == 1 and int(js[na][k]) == int(js[na][k]):
                upAddSp(na,k,subIt([addAll(),na]))
                upAddSpF(na,k,na)
    while len(js['have']) != len(js['names']):
        for j in range(0,len(names)):
            na = names[j]
            if na not in js['have']:
                n,add,k,cou,new = countLs(na)
                if new != None and len(k) != 0:
                    upAddSp(na,k[0],new)
                    addLs(na,'have')
                elif len(k) == 0:
                    addLs(na,'have')
                else:
                    for i in range(0,len(k)):
                        if str(js[na][k[i]]) in js['have']:
                            upAddSp(na,k[i]-1,subIt([js['adds'][str(js[na][k[i]])][k[i]-1],add,na]))
def CityTraffic(strArr):
    if len(strArr) == 0:
        return None
    getTraff(strArr)
    getHigher()
    lsN = []
    ls = ''
    for i in range(0,len(js['names'])):
        ls = ls + ','+js['names'][i]+':'+str(js['adds'][js['names'][i]])[1:-1].replace(' ','')
    ls = ls[1:]
    return ls


inps = {"inputs":["[\"1:[5]\", \"4:[5]\", \"3:[5]\", \"5:[1,4,3,2]\", \"2:[5,15,7]\", \"7:[2,8]\", \"8:[7,38]\", \"15:[2]\", \"38:[8]\"]","[\"1:[5]\", \"2:[5]\", \"3:[5]\", \"4:[5]\", \"5:[1,2,3,4]\"]","[\"1:[5]\", \"2:[5,18]\", \"3:[5,12]\", \"4:[5]\", \"5:[1,2,3,4]\", \"18:[2]\", \"12:[3]\"]","[\"1:[12]\", \"12:[1]\"]","[\"4:[100]\", \"100:[4,67]\", \"67:[100,12]\", \"12:[67]\"]","[\"4:[100]\", \"100:[4,67]\", \"67:[100,12,89]\", \"12:[67]\", \"89:[67]\"]","[\"12:[4]\", \"82:[4]\", \"4:[12,82,90]\", \"90:[4,105]\", \"105:[90]\"]","[\"1:[2]\", \"3:[2]\", \"4:[2]\", \"2:[1,3,4,8]\", \"8:[2,67,14]\", \"67:[8]\", \"14:[8]\"]","[\"1:[5]\", \"4:[5]\", \"3:[5]\", \"5:[1,4,3,2]\", \"2:[5,15,7]\", \"7:[2,8]\", \"8:[7,38]\", \"15:[2]\", \"38:[8,104]\", \"104:[38]\"]","[\"56:[2]\", \"2:[56,12]\", \"3:[12]\", \"12:[2,3]\"]","[]"]}
for i in range(0,len(inps["inputs"])):
    global js
    js = {}
    print(CityTraffic(json.loads(inps['inputs'][i])))
exit()
