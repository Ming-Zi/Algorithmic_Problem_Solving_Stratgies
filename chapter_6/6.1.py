# sum 1 to n

def return_Sum(n):
    if n==1 : return 1
    else : return n + return_Sum(n-1)

n = int(input('input n = '))
print(return_Sum(n))
