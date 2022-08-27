word = input("Enter a word:")
word_list = []
while word != "":
    word_list.append(word)
    word = input("Enter a word: ")

word_list.sort()
print("Final list is: " + str(word_list))