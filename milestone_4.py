class Hangman:
    def __init__(self, word_list,num_lives=5):
        import random
        self.word_list       = word_list
        self.word            = random.choice(word_list)
        self.word_guessed    = ['_']*len(self.word)
        self.num_lives       = num_lives
        self.num_letters     = int
        self.list_of_guesses = []

    