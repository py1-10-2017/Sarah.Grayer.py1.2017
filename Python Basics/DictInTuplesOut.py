def tupleout(): #prints 3 lists with the key/val pairs as the data (for loop)
    mydict = {
    "Speros": "(555)555-5555",
    "Michael": "(999)999-9999",
    "Jay": "(777)777-7777"
    }

    for key, value in mydict.iteritems():
        dictlist = ([key, value])
        print dictlist
tupleout()


def tupleout2(): #prints one list with the key/val pairs as tuples
    mydict = {
    "Speros": "(555)555-5555",
    "Michael": "(999)999-9999",
    "Jay": "(777)777-7777"
    }

    mydict.items()
    tuplelist = [(key, value) for key, value in mydict.iteritems()]
    print tuplelist
tupleout2()
