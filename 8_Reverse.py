num = 153
Reverse = 0
while(num!=0):
    Remainder = num%10
    Reverse = Reverse*10 + Remainder
    num = num //10

print(Reverse)