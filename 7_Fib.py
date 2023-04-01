def fibonacci(num):
    if num <= 0: return "Incorrect"
    elif num == 1: return 0
    elif num == 2: return 1
    else: return fibonacci(num-1) + fibonacci(num-2)

Fib_list = []
num = 5
for i in range(1, num+1):
    j = fibonacci(i)
    print(j)
    Fib_list.append(j)

print(Fib_list)