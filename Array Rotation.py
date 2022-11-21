import json
def ArrayRotation(arr):
    lsN = []
    if len(arr) !=0:
        for i in range(int(arr[0]),len(arr)):
            lsN.append(arr[i])
        for i in range(0,arr[0]):
            lsN.append(arr[i])
    delim = ""
    temp = list(map(str, lsN))
    res = delim.join(temp)
    return res
inps = {"inputs":["[2, 3, 4, 1, 6, 10]","[3,2,1,6]","[4,3,4,3,1,2]","[1,1,2]","[0,1,2,3]","[1,2,3,4,5]","[6,2,4,4,4,4,4]","[3,3,3,3,3]","[4,3,2,1,5,6]","[0,0]","[]"]}
for i in range(0,len(inps["inputs"])):
    print(ArrayRotation(json.loads(inps["inputs"][i])))
