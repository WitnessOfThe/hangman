# Hangman

Hangman is a classic game in which a player thinks of a word, and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word, and the user tries to guess it.

# Milestone 1

Milestone one is about the connection of VsCode to GitHub.

# Milestone 2

Code in milestone_2.py creates a list of 5 character vectors. In the first part of the program, we randomly select the list element and show it in the command prompt. The random selection is performed by using the random package.

The second part of the code demonstrates a method of interaction with the user by using the "while true" statement. It allows the rejection of incorrect inputs and asks a user to try again. Here, we check the user's input to be a single character.

# Milestone 3

The code in milestone_3.py separate functions of asking and checking the user input on one side and checking if the letter that the user guessed belongs to the randomly selected word from the list.

# Milestone 4

The code in milestone_4.py consists of different functions created in Milestone 3 into the single class object. Here we store all game parameters in the __init__  function and develop two other methods for the game. The first method gets the user's input and checks it for correctness, while the second method is responsible for the game function, i.e. checking if the user's guess is correct and counting the number of lives the user got. 

# Milestone 5 

The code in milestone_5.py is the full implementation of the Hangman game. The core of the game is the Hangman class. The __init__ method stores the class parameters, such as the "word" the user needs to guess by providing a guessed letter. The "word" is chosen randomly from the list provided by a user. The function "ask_for_input" checks the user input for validity, where all non-single, not alphabet symbols are rejected. If the user input is valid, the "letter" is passed to the method "check_guess", where it is determined if the provided letter is present in the "word". If not user loses a life; if yes, the number of unguessed letters decreases. The external function "play_game" runs the game using the Hangman class, determining whether the user won.
