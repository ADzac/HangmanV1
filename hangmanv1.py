import requests
import random

lives = 6
used_char = []
word_site = "https://www.mit.edu/~ecprice/wordlist.10000" #library containing words 
response = requests.get(word_site)
words = response.content.splitlines()
rndm_nb = random.randint(0,len(words)) # choose a random number
hangword = words[rndm_nb].decode() #choose a random word from the list using random number
hangword = [char for char in hangword] #seperate a string into a list of characters
answer = hangword[:] # create another list with the same size
for i in range(len(answer)): #replace the characters with ""
    answer[i] = ""
print('Welcome to Hangman Game')
while lives != 0 : 
    print('You have ' + str(lives)+ ' tries')
    print('Characters used')
    print(*used_char, sep = ", ") #put out already used characters 
    print(answer) # users can see the amount of characters needed
    char = input("Choose a character : ")
    if char not in used_char: # if a char hasn't been used, add it to used list
        used_char.append(char)
        indices = [i for i, x in enumerate(hangword) if x == char] # find the positions of inputted character if it exists
        if len(indices) != 0:
            for i in indices:
                answer[i] = char # insert the char at the positions found before
            indices = []
            str_answer = "".join(answer) # create a string of the current answer
            str_hangword = "".join(hangword) # create a string of the word
            if str_answer == str_hangword:
                print(str_hangword)
                print("You win")
                break
        else:
            lives -=1
    else:
        print("Character already use")
if lives == 0:        
    print('Game Over')
    hangword = "".join(hangword)
    print('The word is ' + hangword)
