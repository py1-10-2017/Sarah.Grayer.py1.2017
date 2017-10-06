#input
mixedlist = ['magical unicorns ',19,'hello ',98.98,'world ']
integerlist = [1,2,3,4,5]
stringlist = ["spiff ", "moon ", "robot "]

def typelist(list): #function name
    newstring = ""
    total = 0

    for value in list:
        if isinstance(value, int) or isinstance(value, float): #each occurence, if any number, add up
            total = total + value
        elif isinstance (value, str): #each occurence, if str, concatenate
            newstring += value
    if newstring and total:
        print newstring #new conatenated string variable
        print total #running sum of numbers
        print "This array has mixed value types." #analysis of what elements are in string

    elif newstring:
        print newstring #new conatenated string variable
        print "This array is all strings." #analysis of what elements are in string

    else:
        print total #running sum of numbers
        print "This array is all numbers." #analysis of what elements are in string

print typelist(mixedlist)

print typelist(integerlist)

print typelist(stringlist)
