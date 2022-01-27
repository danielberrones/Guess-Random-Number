#### Silly game I made on 9/20/2015
### Guess the random number and program ends


import random, time
num = random.randint(0, 1000)
counter = 0
guesses=[]

while True:
    user = int(input("\nGuess a random number between 0 and 1000: "))
    if user > num:
        print('Too high\n')
        guesses.append(user)
        counter += 1
    elif user < num:
        print('Too low\n')
        guesses.append(user)
        counter += 1
    elif user == num:
        print('You win!')
        time.sleep(3)
        print("Here was the random number: " +str(num))
        print("It took you " + str(counter) + " guesses to determine the random number.")
        print("Here are your guesses: " + str(guesses))
        with open("yourScore.text","w") as f:
            f.write("It took you " + str(counter) + " guesses to determine the random number.")
            f.write("\nHere are your guesses: " + str(guesses))
            f.write("\nThe random number was " + str(num))
        break

