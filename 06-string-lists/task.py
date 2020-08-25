inputWord = input("Input a word: ")
inputWord = inputWord.replace(" ", "")

reverseWord = inputWord[::-1]

if inputWord == reverseWord:
    print("The word is a palindrome")
else:
    print("The word is not palindrome")
