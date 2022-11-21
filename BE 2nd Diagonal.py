import json
def key(js):
    for key, value in js.items():
        names.append(str(key))
def emptys():
    add  = 0
    for i in range(0,len(lsSheet['matric'])):
        add += len(lsSheet['matric'][i])
    
    if add > 0:
        return False
    return True
def getParse(k,c):
    if len(lsSheet['matric'][c]) != 0:
        for i in range(0,k):
            lsSheet['lsN'].append(lsSheet['matric'][c][i])
        lsSheet['matric'][c] = lsSheet['matric'][c][k:]
def getLsNum():
    return lsSheet['lsNum'][0]
def middle():
    getParse(1,1)
def left():
    if len(lsSheet['matric'][0])>1:
        getParse(1,0)
    else:
        getParse(1,0)
def right():
    if len(lsSheet['matric'][-1])>1:
        getParse(1,-1)
    else:
        getParse(1,-1)
def initParse():
    getParse(2,0)
    getParse(1,1)
    getParse(1,-1)
    getParse(1,1)
def matric():
    initParse()
    while emptys() != True:
        left()
        left()
        middle()
        right()
        right()
        middle()
    delim = " "
    temp = list(map(str, lsSheet['lsN']))
    res = delim.join(temp)
    return res
global lsSheet
inps = {"inputs":["[\"[1, 2]\", \"[3, 4]\"]","[\"[1, 2, 3, 4, 5]\", \"[6, 7, 8, 9, 10]\", \"[11, 12, 13, 14, 15]\"]","[\"[0, 1, 4, 3]\", \"[3, 2, 0, 2]\"]","[\"[4, 2, 3, 4]\", \"[1, 1, 4, 4]\", \"[2, 0, 4, 4]\"]","[\"[4, 2, 3, 4]\", \"[1, 1, 4, 4]\", \"[2, 0, 4, 4]\"]","[\"[4, 2, 3, 4]\", \"[1, 1, 4, 4]\", \"[2, 0, 4, 4]\"]","[\"[4, 2, 3, 4]\", \"[1, 1, 4, 4]\", \"[2, 0, 4, 4]\"]","[\"[4, 2, 3, 4]\", \"[1, 1, 4, 4]\", \"[2, 0, 4, 4]\"]","[\"[4, 2, 3, 4]\", \"[1, 1, 4, 4]\", \"[2, 0, 4, 4]\"]","[\"[4, 2, 3, 4]\", \"[1, 1, 4, 4]\", \"[2, 0, 4, 4]\"]"]}
lsSheet = {'lsN':[],'lsNum':[],'matric':[]}

for i in range(0,len(inps["inputs"])):
    lsSheet = {'lsN':[],'lsNum':[],'matric':json.loads(inps["inputs"][i])}
    lsN = []
    lsNum = []
    for k in range(0,len(lsSheet['matric'])):
        lsSheet['matric'][k] = json.loads(lsSheet['matric'][k])
        lsSheet['lsNum'].append(k)
    print(matric())

