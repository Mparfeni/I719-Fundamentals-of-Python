import random
import dictionary


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
