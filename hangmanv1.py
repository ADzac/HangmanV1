import requests
import random

lives = 6
used_char = []
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
words = response.content.splitlines()
rndm_nb = random.randint(0,len(words))
hangword = words[rndm_nb].decode()
hangword = [char for char in hangword]
answer = hangword[:]
for i in range(len(answer)): 
    answer[i] = ""
print('Welcome to Hangman Game')
while lives != 0 :
    print('You have ' + str(lives)+ ' tries')
    print('Characters used')
    print(*used_char, sep = ", ") 
    print(answer)
    char = input("Choose a character : ")
    if char not in used_char:
        used_char.append(char)
        indices = [i for i, x in enumerate(hangword) if x == char]
        if len(indices) != 0:
            for i in indices:
                answer[i] = char
            indices = []
            str_answer = "".join(answer)
            str_hangword = "".join(hangword)
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
