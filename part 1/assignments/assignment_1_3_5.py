from random import shuffle

correct_list = [str(x) for x in range(0,10)]
shuffle(correct_list)
correct_list = correct_list[0:4]
correct = ''.join(correct_list)

guess = ''

while correct != guess:
    print('\nGuess the right number: ')
    guess = input()
    
    if guess == 'nyerah':
        print('numbers: ', correct)
        break
    
    guess_list = list(guess)

    intersection = set(correct_list).intersection(set(guess_list))
    print(len(intersection), 'in the set.')
    
    right = 0
    for a,b in zip(correct_list, guess_list):
        if a == b:
            right += 1
    print(right, 'correct guess.')
    
    if right == 4:
        print('Congrats!')
        break
    