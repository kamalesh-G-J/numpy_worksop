# find if the given number is a palindrome or not?
a = int(input("Enter a number:"))
a=str(a)
if a[::-1]==a:
    print(f"It is palindrome")
else:
    print(f"It is not a palindrome")