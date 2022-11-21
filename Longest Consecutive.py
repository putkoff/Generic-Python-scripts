import json
def LongestConsecutive(arr):
    if len(arr) == 0:
        return 0
    arr.sort()
    lsN = [1]
    for i in range(0,len(arr)-1):
      if arr[i+1] != arr[i]:
          if arr[i+1] == arr[i]+1:
              lsN[-1] +=1
          else:
              lsN.append(1)
    lsN.sort()
    arr = lsN[-1]
    return arr
# keep this function call here
imps = ["[4, 3, 8, 1, 2, 6, 100, 9]","[6, 7, 3, 1, 100, 102, 6, 12]","[5, 6, 1, 2, 8, 9, 7]","[9, 9, 9]","[2]","[5, 6, 7, 8, 9, 10, 11, 12]","[11, 6, 6, 5, 7, 10, 1, 2, 3, 12, 9, 8]","[1, 2, 1, 2, 1, 2, 1, 2, 6, 8]","[12, 10, 2, 3, 11, 13, 100, 101, 5]","[5, 15, 16, 21, 4, 5, 10, 9, 8, 22, 23, 7, 3, 2, 24, 1, 6]","[]"]
for i in range(0,len(imps)):
    print(LongestConsecutive(json.loads(imps[i])))
