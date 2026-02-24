print("Enter a number, which you want to find prime no.")
num = int(input())

if (num <= 1):
    print("Not a prime number.")
else:
    flag = True
    for i in range(2, (int((num) ** 0.5) + 1)):
        if (num % i == 0):
            flag = False
            break

    if flag:
        print("prime number.")
    else:
        print("Not a prime number.")
