#SHWUN LEI WIN S10272765A P12

# 1. Display Main Menu
print("------------------ Welcome to Sundrop Caves! ------------------")
print("You spent all your money to get the deed to a mine, a small")
print("backpack, a simple pickaxe and a magical portal stone.\n")
print("How quickly can you get the 500 GP you need to retire")
print("and live happily ever after?")
print("--------------------------------------------------------------")

#1.1 New Game (N) 
while True:
    print("---- Main Menu ----")
    print("(N)ew game")
    print("(L)oad saved game")
    print("(Q)uit")
    choice = input("------------------ Your choice? ").lower()

    if choice == 'n':
        # New game
        name = input("Greetings, miner! What is your name? ")
        print(f"Pleased to meet you, {name}. Welcome to Sundrop Town!\n")
        day = 1

        
        while True:
            print(f"DAY {day}")
            print("----- Sundrop Town ----- (B)uy stuff")
            print("See Player (I)nformation")
            print("See Mine (M)ap")
            print("(E)nter mine")
            print("Sa(V)e game")
            print("-------- (Q)uit to main menu --------")
            town_choice = input("------------------ Your choice? ").lower()

            if town_choice == 'q':
                # Exit back to main menu
                break

            
            print()  #blank line for spacing :]

    elif choice == 'l':
        print("Loading saved game... (Not yet implemented)")
    elif choice == 'q':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
d