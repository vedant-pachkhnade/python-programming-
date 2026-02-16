text = input("Enter a string: ")
vowels = "aeiouAEIOU"
if any(char in vowels for char in text):
    print("yes")
else:
    print("no")
