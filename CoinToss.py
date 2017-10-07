def CoinToss(numtosses):
    heads = 0#set variables before for loop begins, otherwise, if inside loop, would be re-set to 0 each time.
    tails = 0
    for i in range (1, numtosses+1):
        import random
        random_num = random.randint(0, 1)
        if random_num == 0:
            heads = heads + 1
            print "Attempt " + str(i) + ": Throwing coin... it's a head! ...Got", heads, "head(s) so far and", tails, "tail(s)."#using commas to seperate requires just variable name, no extra spaces needed in surrounding string
        else:
            tails = tails + 1
            print "Attempt " + str(i) + ": Throwing coin... it's a tail! ...Got " + str(heads) + " heads(s) so far and " + str(tails) + " tail(s)."#concatenating requires + str(variable), and extra spaces in strings. Both work.

CoinToss(5000)
