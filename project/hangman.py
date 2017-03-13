import random
words = ["continental", "hangman", "chairs", "backpack", "bodywash", "clothing", "computer", "python", "program", "glasses", "sweatshirt", "sweatpants", "mattress", "friends", "clocks", "biology", "algebra", "suitcase", "knives", "ninjas", "shampoo", "ray", "daisy", "assassination", "hopscotch", "beads", "chargeable", "amongst", "chameleon", "calling", "aerial", "accommodation", "smuggler", "compact", "swollen", "elsewhere", "art", "absurd", "trial", "royalty", "loser", "opposition", "bitter", "downward", "computation", "empire", "hideout", "expression", "inverse", "indecent", "address", "creative", "heavyhearted", "conflict", "toy", "high", "flicker"]
def choose_a_word():
	word_position = random.randint(0, len(words) - 1)
	return words[word_position]
