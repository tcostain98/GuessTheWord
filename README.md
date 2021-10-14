Guess The Word

Guess the word is a python terminal game that runs in the Code Institute Terminal.
Users have to guess the letters of the word to win the game.

# How To Play

Guess The Word is based on a the classic pen-and-paper game that many of us played in school when classes would finish early or just before the holidays were going to begin.

You have 10 lives (attempts) to guess the word.

The player simply enters a letter of the alphabet on the keyboard.

If the player guesses correctly the letter will be displayed and all lives will be intact.

If the player guessses incorrectly then a life will be deducted.

After guessing the letter the player will be prompted keep guessing until the word is displayed or until the number of lives reaches 0.

## Features

-Existing Features

    -Each hidden letter is displayed as an underscore '_'.

    -The number of lives are displayed after each guess is attempted.

    -There are 3 levels of difficulty: Easy, Medium, Hard.

    -Accepts user input.

    -Play again option.

    -Input validation and error correcting
        -You must enter characters in the English alphabet.

        -You cannot enter the same character more than once.

        -You can enter upper case or lower case letters.

-Future Features

    -Add more levels of difficulty.

    -Add more words to each difficulty level.

### Data Model

I used a json file to store the data for each difficulty level.

I created a variable and assigned it to the value of the json file.

#### Testing

I have manually tested this project by doing the following:

    -Passed the code through PEP8 linter and confirmed there are no problems
    
    -Given invalid inputs: symbols and numbers when alpahbetic characters are expected, same input more than once.

    -Tested in my local terminal by friends and family.

Bugs


    -No bugs shown.

-Validator Testing

    -PEP8
        
        -No errors were returned from PEP8online.com.


##### Deployment

This project was deployed using Git.

    -Steps for deployment:

        -Fork or clone this repository.

        -Set the building blocks to python and nodejs in that order.

        -Click on deploy.
        

###### Credits

    -Code Institute for deployment terminal.

    -My Mentor Antonio Rodriguez for continuous and helpful feedback.

    -Tutor support at Code Institute for their support.



