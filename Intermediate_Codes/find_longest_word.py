# The longest word from the set of words entered by the user

print("Enter words.")
words = (input())

word_len = 0
while(words != '-1'):
    count = 0
    for letter in words:
        count = count + 1
    if(count > word_len):
            word_len = count
    words = input("Enter a word: ")
        
print("The length of the longest word is",word_len)