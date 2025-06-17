def count_letter_occurrences():
    text = input("Enter a string: ")
    letter = input("Enter a letter to count: ")
    count = 0
    for character in text:
        if character == letter:
            count += 1
    print(f"The letter '{letter}' appears {count} times in the string.")
count_letter_occurrences()