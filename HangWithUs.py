import random


word_lista = open("countries-and-capitals.txt", "r").readlines()
countries = []
capitals = []
for I in word_lista:
    c_and_c = I.split(" | ")
    countries.append(c_and_c[0])
    capitals.append(c_and_c[1].strip())


def play(word, lives):
    good_guess = True
    bad_guess = False
    lives = 6
    word_competition = "_" * len(word_lista)
    while bad_guess in word:
        print("Bad guess! ")
        lives -= 1
    if good_guess in word:
        print("Good guess! ")





def level(word):
    short_list = word_lista
    long_list = word_lista
    for word in countries:
        if len(word) <= 6:
            short_list.append(word)



def Choose():            
    print("Please choose a level! ")
    if input == "1":
        return short_list.random.upper()
    if input == "2":
        return long_list.random.upper()

    


        


#def display():
 #   txt = word_lista
  #  x = txt.replace(world_lista,)