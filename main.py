import random

a = ord('a')
eng_alp_low = ''.join([chr(i) for i in range(a, a + 26)])

b = ord("а")
rus_alp_low = ''.join([chr(i) for i in range(b, b + 32)])

print("Welcome to Viselica.\nViselica is a game to pass the time.")

def rule_check():
    while True:
        rules = input("So, are you already familiar with the rules of the game? Yes or Not:\n")
        answer1 = "Yes"
        answer2 = "Not"

        if rules.capitalize() == answer1:
            return "Great!"

        elif rules.capitalize() == answer2:
            print("That's all right, now let's talk about the rules.")
            return "\nThe player is given a word that they must guess using the \nletters of the alphabet and the ability to make a limited number of mistakes.\nIf there is such a letter in the word, it is substituted for the dash. \nIf there is no such letter in the word, the computer draws a part of \nthe gallows. Each a wrong guess results in a new part of the gallows. \nThe player has 5 lives. The player wins if the word is guessed before \nthe picture is complete. The computer wins if it manages to 'hang' its \nopponent.\n"

        else:
            print("You entered something else")
            continue


print(rule_check())

print("Let's start the game.")
lives_counter = 5

word_list = ("live", "world", "galaxy", "universe", "earth", "dream")
guess_word = random.choice(word_list)
print("\nThe executioner made a word")
print(guess_word)
print(eng_alp_low)
encrypted_list = []

for i in guess_word:
    encrypted_list.append("*")
print(encrypted_list)

while encrypted_list != list(guess_word):
    res = []
    word_as_list = list(guess_word)
    letter = input("choose a letter: ")

    for idx, x in enumerate(word_as_list):
        if x == letter:
            res.append(idx)

    for i in res:
        encrypted_list[i] = letter
    print(encrypted_list)

    if letter not in guess_word:
        print("you didn't guess the letter. -1hp .")
        lives_counter -= 1

    if lives_counter == 0:
        print("Game Over")
        break

print("Session ended")
