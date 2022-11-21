import json
def largestRectangleArea(inp):
    if len(inp) == 0:
        return 0
    lsN = []
    for i in range(0,len(inp)):
        lsN.append(int(0))
        n = inp[i]
        for k in range(0,len(inp)):
          if n <= inp[k]:
              lsN[-1] += int(n)
          else:
             lsN.append(int(0))
    lsN.sort()
    return lsN[-1]
    
inps = ["[2, 3, 4, 1, 6, 10]","[3,2,1,6]","[4,3,4,3,1,2]","[1,1,2]","[0,1,2,3]","[1,2,3,4,5]","[6,2,4,4,4,4,4]","[3,3,3,3,3]","[4,3,2,1,5,6]","[0,0]","[]"]
for i in range(0,len(inps)):
    inpsNow = json.loads(inps[i])
    input([inpsNow,largestRectangleArea(inpsNow)])

