print("Please think of a number between 0 and 100!")
low = 0
high = 100
guess = (low + high) // 2

while True:
    print("Is your secret number " + str(guess) + "?")
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if response == 'c':
        print("Game over. Your secret number was: " + str(guess))
        break
    elif response == 'h':
        high = guess
    elif response == 'l':
        low = guess
    else:
        print("Sorry, I did not understand your input.")
    guess = (low + high) // 2
