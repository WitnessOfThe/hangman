class Hangman:
    def __init__(self, word_list,num_lives=5):
        import random
        self.word_list       = word_list
        self.word            = random.choice(word_list)
        self.word_guessed    = ['_']*len(self.word)
        self.num_lives       = num_lives
        self.num_letters     = len(set(self.word))
        self.list_of_guesses = []
    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
#        else:
 #           print(f"Sorry, {guess} is not in the word. Try again.")
    def ask_for_input(self):
        while True:
            guess = input("Gimmi a letter: ")
            if not(len(guess) == 1 and guess.isalpha() == 1): 
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                
if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    Hangman(word_list).ask_for_input()