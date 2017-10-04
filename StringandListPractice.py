words = "It's thanksgiving day. It's my birthday, too!"
print words
print words.index("day")
print words.replace("day", "month", 1)

x = [2,54,-2,7,12,98]
print max(x)
print min(x)

list = ["hello",2,54,-2,7,12,98,"world"]
print (list[0], list[len(list)-1])

array = [19,2,54,-2,7,12,98,32,10,-3,6]
array.sort()
first_list = array[:len(array)/2]
second_list = array[len(array)/2:]
second_list.insert(0, first_list)
print second_list
