def draw_stars(list):
    for i in list:
        print "*" * i

draw_stars([4,6,1,3,5,7,25])

print "modified function-->"

def modified_draw_stars(list):
    for i in list:
        if isinstance(i, int):
            print "*" * i
        else:
            print i[0] * (len(i))

modified_draw_stars([4, "tom", 1, "michael", 5, 7, "jimmy smith"])
