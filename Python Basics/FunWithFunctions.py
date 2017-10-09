def odd_even ():
    for i in range (1, 2000):
        if i % 2 != 0:
            print "Number is " + str(i) + ". This is an odd number."
        else:
            print "Number is " + str(i) + ". This is an even number."

print odd_even()

def multiply(list, mult):
    b = []
    for i in list:
        b.append(i * mult)
    return b
print multiply([2,4,10,16], 5)

def layered_multiples(arr):
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0, x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array
print layered_multiples(multiply([2,4,5],3))
