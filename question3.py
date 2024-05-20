#write a program to find the factorial of a nummber
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
a=int(input("Enter a number:"))
n = factorial(a)
print(n)