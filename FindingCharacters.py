def findchar(word_list, char): #funct name and variable names
    new_list = []

    for i in range (0, len(word_list)):
        if word_list[i].find(char) != -1: #-1 indicates there is no "char", otherwise .find outputs at position "char" is located
            new_list.append(word_list[i])

    print new_list

this_list = ["hello","world","my","name","is","Sarah"] #test set

findchar(this_list, "o") #call funct and define variables
