print("Enter the number")
num = int(input())

store = num
absnum = abs(num)

rev = absnum % 10
absnum = absnum // 10

while absnum > 0:
    r = absnum % 10
    absnum = absnum // 10
    rev = rev * 10 + r

if store < 0:
    rev = -rev

print(rev)
