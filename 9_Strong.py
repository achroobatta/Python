num = 145
original = num

sum = 0
def fac(n):
    if n==1 or n==0: return 1
    else: return n*fac(n-1)

while(num!=0):
    n = num%10
    sum += fac(n)
    num = num //10

print(sum)

if original == sum: print("{0} is Strong number".format(original))
else: print("{0} is not a Strong number".format(original))