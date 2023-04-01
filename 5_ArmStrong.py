n = 153
num = n

def count_number(n):
    count = 0;

    while(n!=0):
        n=n//10
        count += 1
    return count

def power(x,y):
    if y == 0: return 1
    elif y % 2 == 0: return power(x, y//2) * power(x, y//2)
    else: return x*power(x, y//2)*power(x, y//2)

count = count_number(n)
print(n)
sum_num = 0
while (n!=0):
    value = n%10
    print(value)
    sum_num = sum_num + power(value,count)
    n=n//10
    print(n)

print("Value of {0} is {1}".format(num,sum_num))
if num == sum_num: print("num {0} is Armstrong".format(num))
else: print("num {0} is not Armstrong".format(num))