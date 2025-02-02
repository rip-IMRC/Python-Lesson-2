word=str(input("Enter your word: "))
letter=(input("Enter the letter you want to count: "))
i=0
count=0
while(i<len(word)):
    if (word[i])==letter:
        count=count+1
    i=i+1
print("The number of times", letter, "occurred in the word", word, "is", count)