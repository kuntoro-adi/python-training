import random

while True:
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    print('\n',x,' ',y,' -> ')
    z = input()
    if z == 'exit':
        break
    z = int(z)
    c = (x + y) % 10
    if c == z:
        print('correct!')
    