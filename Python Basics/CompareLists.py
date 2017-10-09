def comparelists(list_one, list_two):
    if list_one == list_two:
        print "they match!"
    else:
        print "no match"

#input
list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

comparelists(list_one, list_two)

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]

comparelists(list_one, list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]

comparelists(list_one, list_two)

list_one = ['celery', 'carrots', 'bread', 'milk']
list_two = ['celery', 'carrots', 'bread', 'cream']

comparelists(list_one, list_two)
