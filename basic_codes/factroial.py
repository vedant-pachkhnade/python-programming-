print("Enter a number")
num = int(input())

fact = 1

if (num < 0):
    print("Not defined")
else:
    while (num > 0):
        fact = num * fact
        num = num - 1

    print(fact)
