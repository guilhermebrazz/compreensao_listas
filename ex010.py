def positivos():

    return [x for x in input().split() if int(x) >= 0]

print(positivos())

#1 2 3 -1 -5 3 -7 2 9