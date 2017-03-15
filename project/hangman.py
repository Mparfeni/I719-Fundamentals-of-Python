import random
import dictionary
import gui
lives_left = 10
guessed_letters = ""


print(gui.gallows[0])
lives_left = len(gui.gallows) - 1


def choose_a_word():
	word_position = random.randint(0, len(dictionary.words) - 1)
	return dictionary.words[word_position]


def game():
    our_word = choose_a_word()
    while True:
        guess = get_guess(our_word)
        if guessing(guess, our_word):
            print("You win!")
            break
        if lives_left == 0:
            print("Wasted!")
            print("The word was: " + our_word)
            break


def get_guess(word):
    print_word_with_blanks(word)
    print("Lives left: " + str(lives_left))
    guess = input("Guess a letter or whole word")
    return guess


def print_word_with_blanks(word):
    show_word = ""
    for letter in word:
        if guessed_letters.find(letter) > -1:
            show_word = show_word + letter
        else:
            show_word = show_word + "-"
    print(show_word)


def guessing(guess, word):
    if len(guess) > 1 and len(guess) == len(word):
        return whole_word_guess(guess, word)
    else:
        return one_letter_guess(guess, word)


def one_letter_guess(guess, word):
    global guessed_letters
    global lives_left
    if word.find(guess) == -1:
        lives_left = lives_left - 1
        print(gui.gallows[(len(gui.gallows) - 1) - lives_left])
    guessed_letters = guessed_letters + guess.lower()
    if all_letters_guessed(word):
        return True
    return False


def whole_word_guess(guess, word):
    global lives_left
    if guess.lower() == word.lower():
        return True
    else:
        lives_left = lives_left - 1
        print(gui.gallows[(len(gui.gallows) - 1) - lives_left])
        return False


def all_letters_guessed(word):
    for letter in word:
        if guessed_letters.find(letter.lower()) == -1:
            return False
    return True
game()


