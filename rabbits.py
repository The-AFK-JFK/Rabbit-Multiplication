def rabbits(r):
    if r<0:
        raise RabbitOutOfRangeError
    if r<5:
        return[1,1,2,3,5][r]
    else:
        return rabbits(r-1) + rabbits(r-2) - rabbits(r-5)

class RabbitOutOfRangeError(ValueError):
    pass

#s = ""

#for i in range(1,20):
#    s = s + str(rabbits(i)) + " "
#print(s)
#>>> 1 1 2 3 5 7 11 16 24 35 5