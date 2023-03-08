import os, random, time, sys
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

word_list = ["accident", "banana", "murder", "aeroplane", "competition", "exibition", "throwback", "manipulation", "huricane", "asteroid","facilitate", "original", "ability", 
"purity", "chemical","altitude", "gratitude", "pedicure", "quantity", "comical", "hesitate", "helicopter", "pessimist", "clerical", "authority", "president", "identical", 
"sensibility", "historical", "certificate", "magnificent", "electricity", "medicine", "ventilate", "estimate", "difficult", "optimist", "humidity", "nautical"]
count = 0
score = 0

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

def hidden_word_config(word, user_input):

    global hash, new_hash
    indexes = []

    for i in range(len(word)):
        if word[i] == user_input:
            indexes.append(i)

    for i in range(len(word)):
        if i in indexes:
            hash[i] = user_input

    if user_input not in used_letters:
        used_letters.append(user_input)
        

    new_hash = "".join(hash)

def counter():
    global count

    if user_input not in word:
        count += 1
    elif len(user_input) > 1 and user_input != word:
        count += 1
    else:
        pass

def win():
    global score, count
    print("Good job!")
    time.sleep(2)
    score += 1
    del hash[:]
    os.system("clear")
    count = 0

def main():
    global user_input, hash, word, new_hash, count, score, used_letters

    word  = random.choice(word_list)
    hash = []
    new_hash = "-" * len(word)
    used_letters = []

    for i in range(len(word)):
        hash.append("-")

    while True: 
        art(title, hangman1, hangman2, hangman3, hangman4)
        print("")
        print("Your score: " + str(score))
        print("Used letters:")
        print(used_letters)

        #Failstate
        if count == 5:
            print("")
            print("The word was " + word)
            print("Game Over")
            time.sleep(2)
            os.system("clear")
            count = 0
            score = 0
            break
    
        #Main word manipulation and game stage section
        print("")
        print(new_hash)
        user_input = input("Guess the letter or word: ")
        user_input = user_input.lower().strip()

        if len(user_input) == 1:
            hidden_word_config(word, user_input)
            
            #auto win
            if "-" not in new_hash:
                win()
                break

        elif len(user_input) > 1:
            if user_input == word:
                win()
                break
            else:
                print("Wrong!")
                time.sleep(2)
        else:
            print("Invalid input")
            time.sleep(2)
    
        counter()
        os.system("clear")

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=38, cols=73))

while True:   
    main()