def checkPrime(num):
    flag = True
    for i in range(2,num//2+1):
        if num%i == 0:
            flag = False
            break
    return flag

num = 9
if checkPrime(num) == True: print("{0} is Prime".format(num))
else: print("{0} is not Prime".format(num))

# check prime in range
def checkPrime(start_range, last_range):
    prime_list = []
    for num in range(start_range, last_range+1):
        # print(num)
        flag = True
        for i in range(2,num//2+1):
            if num%i == 0:
                flag = False
                break
        if flag == True: prime_list.append(num)
    return prime_list

start_num = 2
last_num = 21
lst=checkPrime(start_num, last_num)
print("Prime Numbers in range {0} and {1} is {2}".format(start_num,last_num,lst))