#### guess the random number and program ends
#### it counts the number of guess and prints them once you guess correctly

import random, time
num = random.randint(0, 1000)
counter = 0

while True:
    user = int(input("\nGuess a random number between 0 and 1000: "))
    if user > num:
        print('Too high\n')
        counter += 1
    elif user < num:
        print('Too low\n')
        counter += 1
        print()
    elif user == num:
        print('You win!')
        time.sleep(3)
        print("It took you " + str(counter) + " guesses to determine the random number.")
        break

