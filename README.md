# Wordlecheats
Use this code to narrow down your choices for your next wordle guess. 

Read below to find suggestions about how to best utilize the code -- consistant wins on third guess (no guaratees!!) 

Word bank retrieved from: https://github.com/seanpatlan/wordle-words/blob/main/word-bank.csv 

.........................................

One method to get relatively good results: 

First guess: CRANE 

(Second guess: MOIST)  --- if "CRANE" does not yield good feedback after you process the results with the code 

.........................................

How to use this code: 

------GENERAL RULE OF WORDLE------
1) Enter any five letter word into the wordle interface
2) you should be getting the letters with three possible colors 
3) if you get a green colored on a letter, that means that letter exist in the answer and is at the correct position. However, it might not be the only appearance of that letter. For example, if the answer is 'deeds' but you guessed 'lemon', then the e in 'lemon' will be colored green, but it doesn't imply that there is only one 'e' in the answer, as seen with 'deeds'. 
4) if you get a yellow colored on a letter, that means that letter exists in the answer but not at the position that you put it at. it also doesn't imply that that letter will not be repeated in the answer. For example, if the answer is 'apple' and you guessed 'lemon' then the 'l' and 'e' will appear yellow. 
5) if you get a grey colored on a letter, that means that letter does not exist in the answer anywhere at all! 

------USING THIS CODE KNOWING HOW WORDLE WORKS------
1) after your first attempt, you should get a piece of information for every letter in your first guess. 
2) run the code 
3) it will prompt you "what letter is tested? (A-Z)" 
4) enter the first letter of your guess, case not sensitive
5) it will then prompt you "is this letter in the word?(Y/N)" 
6) if the letter is colored green or yellow, enter 'y'. if the letter is colored grey, enter 'n' 

if you entered 'y' 
1) it will then ask "what place is tested? (1-5)"
2) enter the place of the letter -- for the first letter, enter 1, for the second, 2 ... for the fifth, 5. 
3) it will also ask "is position correct? (Y/N)" 
4) if the letter is colored green, enter 'y'. if the letter is colored yellow, enter 'n' 
5) either way, you will receive a list with all of the possible words that either contains the letter (in case of yellow) or contains the letter at the correct spot (in case of green). 
6) before your next try with a guess, repeat these steps for the next four letters in your first guess. 
7) you should see that the number of possible answer words should drastically decrease as you enter in all five letters from your first guess. 

if you entered 'n'
1) you will receive a list that contains all of the words that does not contain that letter anywhere 
2) before your next try with a guess, repeat these steps for the next four letters in your first guess. 
7) you should see that the number of possible answer words should drastically decrease as you enter in all five letters from your first guess. 


ENJOY!
