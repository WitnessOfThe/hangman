import random

if __name__ == '__main__':

    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    word      = random.choice(word_list)
    while True:
        guess = input("Gimmi a letter: ")
        if len(guess) == 1 and guess.isalpha() == 1: 
            if guess in word:
                print(f"Good guess! {guess}")
                break
            else:
                print(f"Sorry, {guess} is not in the word. Try again.")
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
