import random
print("""
        Game Name: HANGMAN

        How to Play:
          A mystery word is hidden and you must guess it
          one letter at a time to save the Hangman.
          Each wrong guess adds a new part to the Hangman.
          Guess the complete word before the Hangman is fully drawn!

        Game Rules:
          1. You have only 6 incorrect chances
          2. Each wrong guess draws the Hangman further
          3. You can guess only ONE letter at a time
          4. Both uppercase and lowercase letters are allowed
          5. Guess all letters correctly to win the game

        CLUE:
          The word is a FLOWER
        """)
words = ["Rose","Daisy","Tulip","Lotus","marigold"]
incorrect = 6
hangman_stages = [
                """
                    +---+
                    |   |
                        |
                        |
                        |
                        |
                       ===""", 
                """
                    +---+
                    |   |
                    O   |
                        |
                        |
                        |
                       ===""", 
                """
                    +---+
                    |   |
                    O   |
                    |   |
                        |
                        |
                       ===""",
                """
                    +---+
                    |   |
                    O   |
                   /|\\  |
                        |
                        |
                       ===""",
                """
                    +---+
                    |   |
                    O   |
                   /|\\  |
                    |   |
                        |
                       ===""", 
                """
                    +---+
                    |   |
                    O   |
                   /|\\  |
                    |   |
                   / \\  |
                       ==="""
            ]
flower = random.choice(words)

word = "_ " *len(flower)
print("The word: ",word)

while len(flower) and incorrect > 0:
    guess = input("Guess a letter: ")
    if len(guess) == 1 and guess.isalpha():
        if guess.lower() in flower.lower():
            print("Correct!")
            for i,char in enumerate(flower):
                if char.lower() == guess.lower():
                    word = word[:i*2] + guess.lower() + " " + word[(i*2)+2:]
            print("The word: ",word)
            if "_" not in word:
                print("CONGRATULATIONS!! YOU WON!!")
                break
        else:
            print("Wrong Guess ❌")
            print("HANG!")
            if incorrect > 0:
                incorrect -= 1
                if incorrect == 5:
                    print(hangman_stages[0])
                elif incorrect == 4:
                    print(hangman_stages[1])
                elif incorrect == 3:
                    print(hangman_stages[2])
                elif incorrect == 2:
                    print(hangman_stages[3])
                elif incorrect == 1:
                    print(hangman_stages[4])
                elif incorrect == 0:
                    print(hangman_stages[5])
                    print("Hangman is DEAD!!")
                    print("GAME OVER!!")
                    print(f"The word is {flower}")
                else:
                    continue
                print("Incorrect chances: ",incorrect)
    else:
        print("Invalid! Enter a letter")
