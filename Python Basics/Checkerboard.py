def checkerboard():
    for i in range (0, 8):#will loop through these ranges, don't need to increase i
        if i % 2 == 0:
            print "* " * 4
        elif i % 2 != 0:
            print " *" *4

print checkerboard()#no variables to pass through
