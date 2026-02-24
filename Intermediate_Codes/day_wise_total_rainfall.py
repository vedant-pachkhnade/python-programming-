print("Enter days.")
day = int(input())

for i in range(1,day+1):
    total=0
    print("Enter the rainfall of day",i)
    rain = int(input())
    while(rain != -1):
        total = total + rain
        print("Enter the rainfall of day", i)
        rain = int(input())
    print(total)    
