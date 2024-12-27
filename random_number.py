import random

def random_number():
    print('Welcome to the Guessing Number Game.\n1. Easy - (guessing number is single digit)\n2. Medium - (guessing number is double digit)\n3. Hard - (guessing number is triple digit)')
    choice = int(input('Enter the choice(1/2/3): '))
    if choice not in [1,2,3]:
        print('The choice you have choosen is invalid. ')
    else:
        if (choice == 1):
            start = 1
            end = 10
            ans = random.randint(start, end)
            count = 0
            while True:
                guess = int(input('Enter your guessing number: '))
                if (guess > ans):
                    print("The number you have guessed is 'HIGHER THAN' the answer.")
                    count += 1
                elif (guess < ans):
                    print("The number you have guessed is 'LOWER THAN' the answer.")
                    count += 1
                else:
                    print(f'Your guessing number {guess} is correct!!')
                    print(f'You took {count} guesses, to find the right answer.')
                    break
        elif (choice == 2):
            start = 10
            end = 99
            ans = random.randint(start, end)
            count = 0
            while True:
                guess = int(input('Enter your guessing number: '))
                if (guess > ans):
                    print("The number you have guessed is 'HIGHER THAN' the answer.")
                    count += 1
                elif (guess < ans):
                    print("The number you have guessed is 'LOWER THAN' the answer.")
                    count += 1
                else:
                    print(f'Your guessing number {guess} is correct!!')
                    print(f'You took {count} guesses, to find the right answer.')
                    break
        elif (choice == 3):
            start = 100
            end = 999
            ans = random.randint(start, end)
            count = 0
            while True:
                guess = int(input('Enter your guessing number: '))
                if (guess > ans):
                    print("The number you have guessed is 'HIGHER THAN' the answer.")
                    count += 1
                elif (guess < ans):
                    print("The number you have guessed is 'LOWER THAN' the answer.")
                    count += 1
                else:
                    print(f'Your guessing number {guess} is correct!!')
                    print(f'You took {count} guesses, to find the right answer.')
                    break


random_number()