name = ["Anne,", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar", "Sarah", "Justin"]
favoriteanimal = ["horse", "cat", "spider", "giraffe", "dog", "dolphins", "llamas"]

def makedict(arr1, arr2):
    newdict = dict(zip(arr1, arr2))
    print newdict
makedict(name, favoriteanimal)
