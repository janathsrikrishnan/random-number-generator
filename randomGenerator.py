# efficiently work from 3-digit number
def middleSquareRandom(n = 1):
    
    # declaring the static varible  seed and initializing it
    if not hasattr(middleSquareRandom, "seed"):
        middleSquareRandom.seed = n
    
    # get the no of digits
    length = len(str(middleSquareRandom.seed))

    # square the seed
    doublelength = list(str(middleSquareRandom.seed * middleSquareRandom.seed))
    
    # if the length of square less than 2 * length then append zeros in the front
    if (len(doublelength) < 2 * length):
        NoOfZeros = 2 * length - len(doublelength)
        for i in range(NoOfZeros): doublelength.insert(0, '0')

    # choose middle n number from square has next seed 
    startN = (2 * length)//4
    endN = (2*length)//4 + length
    # if startN contains 0 increment until non 0 also increment endN so that next digit has n number
    while(doublelength[startN] == '0'):
        startN += 1
        if (endN == 2*length): break
        endN += 1

    # updating the seed value for next number and return the current number
    middleSquareRandom.seed = int("".join(doublelength[startN:endN]))
    return middleSquareRandom.seed

# for testing 
#print(middleSquareRandom(15464534))
#for i in range(100): print(middleSquareRandom())
