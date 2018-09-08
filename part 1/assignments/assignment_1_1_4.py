f0 = 0
f1 = 1

n = int(input('n = '))
c = 0
while c < n:
    fth = f1 + f0
    print(fth)
    f0 = f1
    f1 = fth
    c = c+ 1