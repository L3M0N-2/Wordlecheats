


import pandas as pd 
words = pd.read_csv('wordbank.csv') 
i=1
while i==1:
    letter=input("what letter is tested? (A-Z)").lower()
    contain=input("is this letter in the word?(Y/N)").lower()
    if contain =='y':        
        words=words[(words ==letter).any(axis=1)]      
        place = int(input("what place is tested? (1-5)"))
        correct=input("is position correct? (Y/N)").lower()        
        if correct == 'y': 
            words=words[words.iloc[:,place] == letter] 
            print(words)
            print('you have a total of ',len(words.index),'remaining options')
        elif correct == 'n':
            words=words[words.iloc[:,place] != letter]
            print(words)
            print('you have a total of ',len(words.index),'remaining options')
    elif contain == 'n':
        for ind in range (1,6):  
            words=words[words.iloc[:,ind] != letter] 
            ind+=1
        print(words)
        print('you have a total of ',len(words.index),'remaining options')
    stop=input("are you done with this round?(Y for yes)").lower()
    if stop=='y':
        print('Thank you for using!')
        break
    else:
        continue