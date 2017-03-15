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

