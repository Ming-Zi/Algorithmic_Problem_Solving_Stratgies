#PICNIC

areFriends=[[False for col in range(10)] for row in range(10)]
isSelect=[False for num in range(10)]

def makePairs(st1,st2):
    if (st1 > st2):
        st1, st2 = st2, st1
    areFriends[st1][st2]=True
    end = st2
    return end

def countPairs(isSelect, areFriends, count):
    firstFree = -1
    for i in range (0, count):
       if(isSelect[i]==False): 
           firstFree = i 
           break
    if (firstFree == -1): return 1
    ret = 0
    for pair in range(firstFree + 1, count):
        if (isSelect[pair]==False and areFriends[firstFree][pair] == True):
            isSelect[pair]=True
            isSelect[firstFree]=True
            ret = ret + countPairs(isSelect, areFriends, count)
            isSelect[pair]=False
            isSelect[firstFree]=False
    return ret
        
count=2
makePairs(0,1)
print(countPairs(isSelect, areFriends, count))

count=6
makePairs(0,1)
makePairs(0,2)
makePairs(1,2)
makePairs(1,3)
makePairs(1,4)
makePairs(2,3)
makePairs(2,4)
makePairs(3,4)
makePairs(3,5)
makePairs(4,5)
print(countPairs(isSelect, areFriends, count))