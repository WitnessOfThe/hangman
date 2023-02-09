import random

class Hangman:
    def __init__(self, word_list,num_lives=5):
        
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
            for _ in range(len(self.word)):
                if self.word[_] == guess:
                    self.word_guessed[_] = guess
            self.num_letters -= 1

    def ask_for_input(self):
        while True:
            guess = input("Enter a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
    '''
    def ask_for_input(self):

        while True:
#            if not(len(set(self.list_of_guesses)) == self.num_letters):

            # without breaks this create infinite loop. Breaks are not specified in the task workflow
            guess = input("Gimmi a letter: ")
            if not(len(guess) == 1 and guess.isalpha() == 1): 

                print("Invalid letter. Please, enter a single alphabetical character.")

            elif guess in self.list_of_guesses:

                print("You already tried that letter!")
            else:
                self.check_guess(guess)
#               print(f'{self.list_of_guesses}')
  #          else:
   #             break          
    '''                
if __name__ == '__main__':

    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    Hangman(word_list).ask_for_input()