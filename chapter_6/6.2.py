# choose n numbers at m

def pick(n, picked, toPick):
    if(toPick == 0):
        print(picked)
        return 
    if not picked:
        smallest = 0
    else:
        smallest = picked[-1]+1
    for next in range(smallest, n):
        picked.append(next)
        pick(n, picked, toPick-1)
        picked.pop()

n = int(input("input n = "))
m = int(input("input m = "))
pick(n, [], m)
    
