import random

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess}")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input(word):
    while True:
        guess = input("Gimmi a letter: ")
        if len(guess) == 1 and guess.isalpha() == 1: 
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
        check_guess(guess)
        
if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    word      = random.choice(word_list)
    ask_for_input(word)