#SHWUN LEI WIN S10272765A P12

player = {}
game_map = []
fog = []

# ------------------ MAIN GAME ------------------
print("------------------ Welcome to Sundrop Caves! ------------------")
print("You spent all your money to get the deed to a mine, a small")
print("backpack, a simple pickaxe and a magical portal stone.\n")
print("How quickly can you get the 500 GP you need to retire")
print("and live happily ever after?")
print("--------------------------------------------------------------")

while True:
    print("---- Main Menu ----")
    print("(N)ew game")
    print("(L)oad saved game")
    print("(Q)uit")
    choice = input("------------------ Your choice? ").lower()

    if choice == 'n':
        name = input("Greetings, miner! What is your name? ")
        print(f"Pleased to meet you, {name}. Welcome to Sundrop Town!\n")

        # Initialize player
        player = {
            'name': name,
            'x': 0,
            'y': 0,
            'copper': 0,
            'silver': 0,
            'gold': 0,
            'GP': 0,
            'day': 1,
            'steps': 0,
            'turns': 20
        }

        while True:
            print(f"\nDAY {player['day']}")
            print("----- Sundrop Town -----")
            print("(B)uy stuff")
            print("See Player (I)nformation")
            print("See Mine (M)ap")
            print("(E)nter mine")
            print("Sa(V)e game")
            print("-------- (Q)uit to main menu --------")
            town_choice = input("------------------ Your choice? ").lower()

            if town_choice == 'q':
                break

            elif town_choice == 'i':
                print(f"\n--- {player['name']}'s Info ---")
                print(f"Gold Pieces (GP): {player['GP']}")
                print(f"Ore: {player['copper']} copper, {player['silver']} silver, {player['gold']} gold")
                total_ore = player['copper'] + player['silver'] + player['gold']
                print(f"Total Ore: {total_ore}/10")
                if total_ore >= 10:
                    print("Your backpack is full!")
                print("-------------------------")

            elif town_choice == 'v':
                with open('save_player.txt', 'w') as f:
                    for key in player:
                        f.write(f"{key}:{player[key]}\n")
                print("Game saved.")

            elif town_choice == 'm':
                print("Map view not implemented yet.")
            elif town_choice == 'b':
                print("Shop not implemented yet.")
            elif town_choice == 'e':
                print("Mining not implemented yet.")
            else:
                print("Invalid choice. Try again.")

    elif choice == 'l':
        try:
            with open('save_player.txt', 'r') as f:
                player.clear()
                for line in f:
                    key, value = line.strip().split(':')
                    if key in ['x', 'y', 'copper', 'silver', 'gold', 'GP', 'day', 'steps', 'turns']:
                        player[key] = int(value)
                    else:
                        player[key] = value
            print(f"Pleased to see you again, {player['name']}.\n")

            while True:
                print(f"\nDAY {player['day']}")
                print("----- Sundrop Town -----")
                print("(B)uy stuff")
                print("See Player (I)nformation")
                print("See Mine (M)ap")
                print("(E)nter mine")
                print("Sa(V)e game")
                print("-------- (Q)uit to main menu --------")
                town_choice = input("------------------ Your choice? ").lower()

                if town_choice == 'q':
                    break

                elif town_choice == 'i':
                    print(f"\n--- {player['name']}'s Info ---")
                    print(f"Gold Pieces (GP): {player['GP']}")
                    print(f"Ore: {player['copper']} copper, {player['silver']} silver, {player['gold']} gold")
                    total_ore = player['copper'] + player['silver'] + player['gold']
                    print(f"Total Ore: {total_ore}/10")
                    if total_ore >= 10:
                        print("Your backpack is full!")
                    print("-------------------------")

                elif town_choice == 'v':
                    with open('save_player.txt', 'w') as f:
                        for key in player:
                            f.write(f"{key}:{player[key]}\n")
                    print("Game saved.")

                elif town_choice == 'm':
                    print("Map view not implemented yet.")
                elif town_choice == 'b':
                    print("Shop not implemented yet.")
                elif town_choice == 'e':
                    print("Mining not implemented yet.")
                else:
                    print("Invalid choice. Try again.")
        except:
            print("Failed to load saved game.")

    elif choice == 'q':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
