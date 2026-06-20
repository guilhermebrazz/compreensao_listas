def pares():

    return [x for x in input().split() if int(x) % 2 == 0]

print(pares())