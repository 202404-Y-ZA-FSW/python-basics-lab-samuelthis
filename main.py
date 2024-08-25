import random

def guessgame():
    # A number guess game where a player will try to guess a randomly generated number between 1 and 100
    numbertoguess = random.randint(1, 100)
    attempts = 0

    print("This is a random generated number guess game")
    print("Just guess a number between 1 and 100.")

    while True:
        attempts += 1
        guess = int(input("Enter your guess number: "))

        if guess == numbertoguess:
            print(f"Awesome you guessed the right number in {attempts} attempts.")
            break
        elif guess < numbertoguess:
            print("Very Low! Don't give up, Try.")
        else:
            print("Very High! Don't give up, Try.")

if __name__ == "__main__":
    guessgame()
