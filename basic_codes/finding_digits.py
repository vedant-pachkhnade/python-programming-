print("Enter the number")
num = abs(int(input()))

digit = 1

while (num > 9):
    num = num // 10
    digit = digit + 1

print(digit)
