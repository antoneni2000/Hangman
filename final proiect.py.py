import random #pentru a face variabilele random 
import sys #pentru sys.exist
import os
#functie pt logo
def get_logo():
    print(""" 
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                       
""")
player_state=[]
#welcoming message
get_logo()
print("Welcome to Hangman Country!")
print("\nHow to play:")
print("You will see a number of short lines together that represent the number of letters in the word you have to guess")
print("Write the letter that you think is included in the word")
print("If you guess the correct letter, that letter will replace one of the litte lines, in the appropriate position in the words")
print("If the letter you guessed is not in the word, a part of the body will appear on the diagram and you lose 1 life.")
print("If the body becomes completed, you are 'hanged' which means you have lost")
print("If you guess all the letters in the word before you are 'hanged', you win.")
input("Press ENTER to continue\n")
#aici avem nevoie doar de capitale 
lists_of_countries_and_capitals = open("countries-and-capitals.txt").read().splitlines()   # Reads the countries-and-capitals file
list_of_countries = [] # Creats new a list
for country_and_capital in lists_of_countries_and_capitals:   
    list_of_countries.append(country_and_capital.split(" | ")[0]) # Puts the country name into the list, fara separatorul de bara
    #print(list_of_countries)
#difficulty levels:
choose_level = input("\nChoose Level of Difficulty:\n1-Easy (7 lives)\n2-Hard (3 lives)\nQuit\n") # Choosing the level of difficulty
lives = 0
while choose_level != "1" and choose_level != "2" and choose_level.lower() != "quit":
    print("Choose correct Level of Difficulty")
    choose_level = input("\nChoose Level of Difficulty:\n1-Easy (7 lives)\n2-Hard (3 lives)\nQuit")
selected_country = ""
if choose_level == "1":
    lives = 7
    filtered_list = list(filter(lambda country: len(country) <= 6, list_of_countries))    #cuvinte <= 6 litere pt nivelul easy
    selected_country = random.choice(filtered_list)
    
elif choose_level == "2":
    lives = 3
    filtered_list = list(filter(lambda country: len(country) > 6, list_of_countries)) #cuvinte >6 litere nivel hard
    selected_country = random.choice(filtered_list)
    print(selected_country)
elif choose_level.lower() == "quit":
    lives=0
    sys.exit('Good bye') #oricum am scrie quit sa ne scoata din joc 
else:
  print("Choose correct Level of Difficulty")

list_of_letters = list(selected_country) 
player_state = []
for i in list_of_letters:
    if i == " ":
        player_state.append(" ")
    else:
        player_state.append("_")    #cand ne printeaza cuvantul sa nu puna " _ " si pentru spatiu
#functie pentru desene hangman
def print_hangman(lives):
    if choose_level == "1":
        if lives == 7:          #nivel easy
            print(f"Remaining lives: {lives}")
            print("""
   ____
    | /
    |
    |
    |
    |
    |
    | ____
    """)
        elif lives == 6:
            print(f"Remaining lives: {lives}")
            print("""
   ________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___      
    """)
        elif lives == 5:
            print(f"Remaining lives: {lives}")
            print(f"""
   ________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___     
    """)
        elif lives == 4:
            print(f"Remaining lives: {lives}")
            print("""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___       
    """)
        elif lives == 3:
            print(f"Remaining lives: {lives}")
            print("""
   ________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___      
    """)
        elif lives == 2:
            print(f"Remaining lives: {lives}")
            print("""
   ________              
    |/   |                     
    |   (_)                     
    |   /|\         
    |    |                       
    |                             
    |                            
    |___       
    """)
        elif lives == 1:
            print(f"Remaining lives: {lives}")
            print("""
   ________                  
    |/   |                         
    |   (_)                      
    |   /|\         
    |    |                          
    |   /                            
    |                                  
    |___    
    """)
        else:
            print(f"Remaining lives: {lives}")
            print("""
    GAME OVER
   ________
    |/   |     
    |   (_)    
    |   /|\       
    |    |        
    |   / \       
    |               
    |___      
    """)
    else:
        if lives == 3:  #nivel hard
            print(f"Remaining lives: {lives}")
            print("""
   ____
    | /
    |
    |
    |
    |
    |
    | ____
    """)
        elif lives == 2:
             print(f"Remaining lives: {lives}")
             print("""
   ________              
    |/   |                     
    |   (_)                     
    |   /|\         
    |    |                       
    |                             
    |                            
    |___       
    """)
        elif lives == 1:
              print(f"Remaining lives: {lives}")
              print("""
   ________                  
    |/   |                         
    |   (_)                      
    |   /|\         
    |    |                          
    |   /                            
    |                                  
    |___    
    """)
        elif lives == 0:
                 print(f"Remaining lives: {lives}")
                 print("""
    GAME OVER
   ________
    |/   |     
    |   (_)    
    |   /|\       
    |    |        
    |   / \       
    |               
    |___      
    """)

          




def game_state():
    print_hangman(lives)
    print(" ".join(player_state))


def guess():    #functie ghicit cuvant

    global lives
    found = False
    for i in range(len(list_of_letters)):
        letter = list_of_letters[i]

        if letter.upper() == player_guess.upper():
            found = True
            player_state[i] = letter
  
    if not found:
        lives -= 1
    game_state()

game_state()

history = [] #lista cuvinte ghicite

while lives > 0 and player_state != list_of_letters: 
    
    player_guess = input()
    if player_guess.lower() == "quit":  #playerul poate introduce in orice moment cuvantul quit si o sa fie scos din joc
        sys.exit("Good bye")  
    
    while len(player_guess) != 1 or not(player_guess[0].isalpha()):  #daca playerul nu introduce un input de 1 caracter sau nu e litera afiseaza mesaj
        print("Incorrect input, please try again...")
        player_guess = input()
    
    if player_guess in history:    #daca e gasit in istoric, afiseaza mesaj
        print("Found in history")
        continue
    else:   
        history.append(player_guess)
      
    guess()
    print("\n Already used letters:")
    print()
    print(" ".join(history))

if lives <= 0:
    print("GAME OVER")
else:
    print("Congrats! You WIN!!!")
