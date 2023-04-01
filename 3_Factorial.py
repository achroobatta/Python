def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial(n-1)

num = 5
print("Factorial of {0} is {1}".format(num, factorial(num)))