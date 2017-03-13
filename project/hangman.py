import random
import dictionary
def choose_a_word():
	word_position = random.randint(0, len(dictionary.words) - 1)
	return dictionary.words[word_position]
