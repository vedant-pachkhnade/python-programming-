print("Enter a number.")
num = int(input())

digit = 0

while (num > 0):
    r = num % 10
    num = num // 10
    digit = digit + r

print(digit)
