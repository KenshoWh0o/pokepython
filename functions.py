import random
from variables import *

# Functions obtaining random cards
def random_pokemon1star():
    return random.choice(pokemon1star)
def random_pokemon2star():
    return random.choice(pokemon2star)
def random_pokemon3star():
    return random.choice(pokemon3star)
def random_pokemon4star():
    return random.choice(pokemon4star)
def random_pokemon5star():
    return random.choice(pokemon5star)

# Functions opening a booster

    # Function opening a god pack
def godpack():
    print()
    input("There are the cards you obtained (press Enter to see the next card) :")
    input("GOD PACK !")
    input(random_pokemon3star())
    input(random_pokemon3star())
    input(random_pokemon4star())
    input(random_pokemon4star())
    input(random_pokemon5star())
    input()
    menu()

    # Function opening a base pack
def basepack():
    print()
    input("There are the cards you obtained (press Enter to see the next card) :")
    input(random_pokemon1star())
    if random.randint(1, 2) == 1 :
        input(random_pokemon1star())
    else :
        input(random_pokemon2star())
    if random.randint(1, 2) == 1 :
        input(random_pokemon2star())
    else :
        input(random_pokemon3star())
    input(random_pokemon3star())
    if random.randint(1, 50) == 1 :
        input(random_pokemon5star())
    elif random.randint(1, 10) == 1 :
        input(random_pokemon4star())
    else :
        input(random_pokemon3star())
    input()
    menu()

    # Function choosing if opening a god pack or a base pack
def booster():
    if random.randint(1, 100) == 1:
        godpack()
    else:
        basepack()

# Function displaying every pokemon
def showallpokemons():
    print()
    print("There is the list of every pokemon (press Enter to go back to menu) :")
    print()
    for pokemon in pokemons:
        print(pokemon)
    input()
    menu()

# Function displaying the menu
def menu():
    print("====")
    print("Menu")
    print("====")
    print()
    print("1. Open a booster")
    print("2. Display every pokemon")
    print("3. Leave")
    choice = input("Your choice : ")
    if choice == "1":
        booster()
    elif choice == "2":
        showallpokemons()
    elif choice == "3":
        print()
        print("Thanks for playing !")
    else:
        print("Incorrect choice. Please try again.")
        menu()

# Function launching the game
def launch():
    print("=======================")
    print("Welcome to PokePython !")
    print("=======================")
    print()
    print("To see the menu, please press Enter")
    input()
    menu()