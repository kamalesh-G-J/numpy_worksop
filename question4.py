#write a program to find the sum of digits of a given number'
a = int(input("Enter the number:"))
sum = 0
while a > 0:
    rem = a % 10
    sum+=rem
    a//=10
print(f"the sum is {sum}")