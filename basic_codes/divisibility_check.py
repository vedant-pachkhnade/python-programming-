number = int(input("Enter a number: "))
if number % 2 == 0 and number % 3 == 0:
    print("divisible by 2 and 3")
elif number % 2 == 0:
    print("divisible by 2")
elif number % 3 == 0:
    print("divisible by 3")
else:
    print("not divisible by 2 and 3")
