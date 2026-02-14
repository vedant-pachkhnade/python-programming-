print("Enter your birth year.")
birth_year = int(input())

current_year = 2026
age = current_year - birth_year

if (age < 18):
    print("You can not watch this movie.\n")
else:
    print("You can watch this movie.\n")
