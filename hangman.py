import os, random
os.system("clear")

title = """ 
               _   _                                         
              | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
              | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
              |  _  | (_| | | | | (_| | | | | | | (_| | | | |
              |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                 |___/ """


word_list = ["accident", "banana", "murder", "aeroplane"]
word  = random.choice(word_list)
hash = []
new_hash = "-" * len(word)

for i in range(len(word)):
    hash.append("-")

def print_title(title):
    print(title)

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

#Checks if the guessed word is correct
def guess_the_word(user_input):
    global word, new_hash
    if user_input == word:
        print("Good job!")
    else:
        print("Wrong!")

while True:

    print_title(title)
    print(new_hash)
    user_input = input("Guess the letter: ")
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
        pass

    os.system("clear")