import random

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    word = random.choice(word_list)
    print(word)
    while True:
        guess = input("Gimmi a letter: ")
        if len(guess) == 1 and guess.isalpha() == 1: 
                print( "Good guess!")
                break
        else:
            print("Oops! That is not a valid input.")
