import os, random
os.system("clear")

title = """ 
               _   _                                         
              | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
              | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
              |  _  | (_| | | | | (_| | | | | | | (_| | | | |
              |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                 |___/ """

hangman1 = """   
   █████████████████████
   ██
   ██
   ██
   ██
   ██
   ██
   ██
   ██
   ██
   ██
   ██
   ██
   ██
   ██
   ██
   ██
   ██
   ██
   ██
██████████"""

hangman2 = """  
   █████████████████████
   ██                █
   ██	             █
   ██              █████
   ██             ███████
   ██             ███████
   ██              █████
   ██
   ██
   ██
   ██
   ██
   ██
   ██
   ██
   ██
   ██
   ██
   ██
   ██
██████████"""

hangman3 = """   
   █████████████████████
   ██                █
   ██                █
   ██              █████
   ██             ███████
   ██             ███████
   ██              █████
   ██                █
   ██                █
   ██                █
   ██                █
   ██                █
   ██                █
   ██                █
   ██
   ██
   ██
   ██
   ██
   ██
██████████"""

hangman4 = """   
   █████████████████████
   ██                █
   ██                █
   ██              █████
   ██             ███████
   ██             ███████
   ██              █████
   ██                █
   ██               ███
   ██              █ █ █
   ██              █ █ █
   ██                █
   ██                █
   ██                █
   ██                █
   ██               █ █
   ██               █ █
   ██               █ █
   ██
   ██
██████████"""


word_list = ["accident", "banana", "murder", "aeroplane", "competition", "exibition", "throwback", "manipulation", "huricane", "asteroid"]
word  = random.choice(word_list)
hash = []
new_hash = "-" * len(word)
count = 0

for i in range(len(word)):
    hash.append("-")

def art(title, hangman1, hangman2, hangman3, hangman4):
    print(title)
    if count == 0 or count == 1:
        print(hangman1)
    elif count == 2 or count == 3:
        print(hangman2)
    elif count == 4:
        print(hangman3)
    else:
        print(hangman4)


#changes the dashes for letters
def hidden_word_config(word, user_input):

    global hash, new_hash
    indexes = []

    for i in range(len(word)):
        if word[i] == user_input:
            indexes.append(i)

    for i in range(len(word)):
        if i in indexes:
            hash[i] = user_input
        

    new_hash = "".join(hash)

#Picks the word from the word list
def new_hash_make(word):
    for i in range(len(word)):
        new_hash.append("-")

def counter():

    global count
    if user_input not in word:
        count += 1
    elif len(user_input) > 1 and user_input != word:
        count += 1
    else:
        pass


while True:

    art(title, hangman1, hangman2, hangman3, hangman4)
    if count == 5:
        print("")
        print("The word was " + word)
        print("Game Over")
        count = 0
        break
    
    print("")
    print(new_hash)
    user_input = input("Guess the letter or word: ")
    if len(user_input) == 1:
        hidden_word_config(word, user_input)
    elif len(user_input) > 1:
        if user_input == word:
            print("Good job!")
            break
        else:
            print("Wrong!")
        input()
    else:
        print("Invalid input")
    
    counter()
    
    os.system("clear")