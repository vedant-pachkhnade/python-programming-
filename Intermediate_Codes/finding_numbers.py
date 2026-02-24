# finding all positive numbers divisible by 3 , 5 which are smaller than given number.
num = int(input("Enter a number: "))

if (num > 2):
    print(2, end=' ')

for i in range(3, num):
    flag = True
    for j in range(2, i):
        if (i % j == 0):
            flag = False
            break;
        else:
            flag = True
    if flag:
        print(i, end=" ")
