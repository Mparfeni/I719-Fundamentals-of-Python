import random
words = ["confused", "gossip", "gland", "bluish", "cavity", "airspace", "clean", "whisper", "amputate", "ditch", "alley", "deletion", "ceremony", "gift", "gutless", "buffer", "frigid"]
def choose_a_word():
	word_position = random.randint(0, len(words) - 1)
	return words[word_position]
