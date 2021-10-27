import random

def main():
    print(
"""

 __    __   ______   __    __   ______   __       __   ______   __    __ 
|  \  |  \ /      \ |  \  |  \ /      \ |  \     /  \ /      \ |  \  |  \ 
| $$  | $$|  $$$$$$\| $$\ | $$|  $$$$$$\| $$\   /  $$|  $$$$$$\| $$\ | $$
| $$__| $$| $$__| $$| $$$\| $$| $$ __\$$| $$$\ /  $$$| $$__| $$| $$$\| $$
| $$    $$| $$    $$| $$$$\ $$| $$|    \| $$$$\  $$$$| $$    $$| $$$$\ $$
| $$$$$$$$| $$$$$$$$| $$\$$ $$| $$ \$$$$| $$\$$ $$ $$| $$$$$$$$| $$\$$ $$
| $$  | $$| $$  | $$| $$ \$$$$| $$__| $$| $$ \$$$| $$| $$  | $$| $$ \$$$$
| $$  | $$| $$  | $$| $$  \$$$ \$$    $$| $$  \$ | $$| $$  | $$| $$  \$$$
 \$$   \$$ \$$   \$$ \$$   \$$  \$$$$$$  \$$      \$$ \$$   \$$ \$$   \$$

""")

    number_input = input("Please choose a level! Press 1 for easy, 2 for hard: ")
    choose_word(number_input)
    
            
    word_list = open("c_and_c.txt", "r").readlines()
    countries = []
    capitals = []
    for I in word_list:
        c_and_c = I.split(" | ")
        countries.append(c_and_c[0])
        capitals.append(c_and_c[1].strip())

if __name__ == '__main__':
        main()




#def play(word, lives):
    #good_guess = True
    #bad_guess = False
    #lives = 6
    #word_competition = "_" * len(word_lista)
    #while bad_guess in word:
        #print("Bad guess! ")
        #lives -= 1
    #if good_guess in word:
        #print("Good guess! ")

# def lines(word):
#     list_for_lines = []
#     for letter in word



def choose_word(number_input):

    short_list = []
    long_list = []


    if number_input == "1":
        for word in countries:
            if len(word) <= 6:
                short_list.append(word)
        chosen_word = random.choice(short_list)
        return chosen_word

    if number_input == "2":
        for word in countries:
            if len(word) > 6:
                long_list.append(word)
        chosen_word = random.choice(long_list)
        return chosen_word



        


#def display():
 #   txt = word_lista
  #  x = txt.replace(world_lista,)

  