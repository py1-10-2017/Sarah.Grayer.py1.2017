def dictionarybasics():
    myinfo = {"name": "Sarah", "age": "28", "country of birth": "the United States", "favorite language": "Python",}
    #for keys in myinfo.iterkeys():
        #print keys
    #for val in myinfo.itervalues():
        #print val
    for keys, val in myinfo.items():
        print "My", keys, "is", val
dictionarybasics()

def dictionarybasics2():#this way allows you to select what order this is printed in
    myinfo = {"name": "Sarah", "age": "28", "country of birth": "the United States", "favorite language": "Python",}

    print "My name is", myinfo["name"]
    print "My age is", myinfo["age"]
    print "My country of birth is", myinfo["country of birth"]
    print "My favorite language is", myinfo["favorite language"]
dictionarybasics2()
