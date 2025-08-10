#102727265A SHWUNLEIWIN

import random

# Prices ranges for minerals
MINERAL_PRICES = {
    'copper': (1, 3),
    'silver': (5, 8),
    'gold': (10, 18),
}

# main menu

def main_menu():
    print("""
---------------- Welcome to Sundrop Caves! ----------------
You spent all your money to get the deed to a mine, a small
backpack, a simple pickaxe and a magical portal stone.

How quickly can you get the 500 GP you need to retire
and live happily ever after?
-----------------------------------------------------------

--- Main Menu ----
(N)ew game
(L)oad saved game
(Q)uit
------------------ Your choice?""")

def town_menu(player):
    print(f"""
DAY {player['day']}
----- Sundrop Town -----
(B)uy stuff
See Player (I)nformation
See Mine (M)ap
(E)nter mine
Sa(V)e game
(Q)uit to main menu
------------------------ Your choice?""")

# selling of minerals

def sell_minerals(player):
    if not player['inventory']:
        return
    print("You have minerals to sell. Selling all...")
    total_sale = 0
    for mineral, count in player['inventory'].items():
        if count > 0:
            price_range = MINERAL_PRICES.get(mineral, (0, 0))
            sale_price = random.randint(*price_range)
            sale_value = sale_price * count
            print(f" Sold {count} {mineral} ore at {sale_price} GP each for {sale_value} GP.")
            total_sale += sale_value
            player['inventory'][mineral] = 0
    player['gp'] += total_sale
    player['load'] = 0
    print(f"Total GP earned from selling: {total_sale}")
    print(f"Current GP: {player['gp']}")
#shop menu 

def buy_stuff_menu(player):
    while True:
        backpack_price = player['backpack_capacity'] * 2
        print(f"""
----------------------- Shop Menu ------------------------- 
(P)ickaxe upgrade to Level 2 to mine silver ore for 50 GP
(B)ackpack upgrade to carry {player['backpack_capacity'] + 2} items for {backpack_price} GP
(L)eave shop
-----------------------------------------------------------
GP: {player['gp']}
-----------------------------------------------------------
Your choice?""")
        choice = input().strip().lower()
        if choice == 'p':
            if player['pickaxe_level'] >= 2:
                print("You already have the silver pickaxe or better.")
            elif player['gp'] >= 50:
                player['gp'] -= 50
                player['pickaxe_level'] = 2
                print("Congratulations! You upgraded to pickaxe level 2 (silver)!")
            else:
                print("You don't have enough GP for the pickaxe upgrade.")
        elif choice == 'b':
            if player['gp'] >= backpack_price:
                player['gp'] -= backpack_price
                player['backpack_capacity'] += 2
                print(f"Congratulations! You can now carry {player['backpack_capacity']} items!")
            else:
                print("You don't have enough GP for the backpack upgrade.")
        elif choice == 'l':
            break
        else:
            print("Invalid choice, please enter P, B, or L.")

def print_player_info(player):
    pickaxe_name = {1: "copper", 2: "silver"}.get(player['pickaxe_level'], "unknown")
    print(f"""
----- Player Information -----
Name: {player['name']}
Portal position: {player['portal_pos']}
Pickaxe level: {player['pickaxe_level']} ({pickaxe_name})
------------------------------
Load: {player['load']} / {player['backpack_capacity']}
------------------------------
GP: {player['gp']}
Steps taken: {player['steps']}
------------------------------
""")
    
# for mine map 
def see_mine_map():
    print("\n+------------------------------+")
    print("|M     C    ???????????????????|")
    print("|      CP   ???????????????????|")
    print("|????CCCC   ???????????????????|")
    print("|??????????????????????????????|")
    print("|??????????????????????????????|")
    print("|??????????????????????????????|")
    print("|??????????????????????????????|")
    print("|??????????????????????????????|")
    print("|??????????????????????????????|")
    print("|??????????????????????????????|")
    print("+------------------------------+")

# for saving the game to text file - the format
def save_game(player):
    with open("save_player.txt", "w") as f:
        f.write(f"{player['name']}\n")
        f.write(f"{player['day']}\n")
        f.write(f"{player['backpack_capacity']}\n")
        f.write(f"{player['load']}\n")
        f.write(f"{player['gp']}\n")
        f.write(f"{player['steps']}\n")
        f.write(f"{player['pickaxe_level']}\n")
        f.write(f"{player['portal_pos'][0]} {player['portal_pos'][1]}\n")
        f.write(f"{player['inventory']['copper']} {player['inventory']['silver']} {player['inventory']['gold']}\n")
    print("Game saved.")

# to read the saved file when load game is chosen
def load_game():
    try:
        with open("save_player.txt", "r") as f:
            name = f.readline().strip()
            day = int(f.readline())
            backpack_capacity = int(f.readline())
            load = int(f.readline())
            gp = int(f.readline())
            steps = int(f.readline())
            pickaxe_level = int(f.readline())
            portal_x, portal_y = map(int, f.readline().split())
            copper, silver, gold = map(int, f.readline().split())

        player = {
            'name': name,
            'day': day,
            'backpack_capacity': backpack_capacity,
            'load': load,
            'gp': gp,
            'steps': steps,
            'pickaxe_level': pickaxe_level,
            'portal_pos': (portal_x, portal_y),
            'inventory': {
                'copper': copper,
                'silver': silver,
                'gold': gold,
            },
        }

        print(f"Welcome back, {name}!")
        return player

    except FileNotFoundError:
        print("No save file found.")
        return None

def new_game(player=None):
    if not player:
        name = input("Greetings, miner! What is your name? ").strip()
        print(f"Pleased to meet you, {name}. Welcome to Sundrop Town!")
        player = {
            'name': name,
            'day': 1,
            'backpack_capacity': 10,
            'load': 0,
            'gp': 0,
            'steps': 0,
            'pickaxe_level': 1,
            'portal_pos': (0, 0),
            'inventory': {'copper': 0, 'silver': 0, 'gold': 0},
        }

    while True:
        sell_minerals(player)
        town_menu(player)
        choice = input("Your choice? ").strip().lower()
        if choice == 'q':
            break
        elif choice == 'b':
            buy_stuff_menu(player)
        elif choice == 'i':
            print_player_info(player)
        elif choice == 'm':
            see_mine_map()
        elif choice == 'e':
            mine_map = load_mine()  # DONT load the mine map from file
            enter_mine(player, mine_map)

        elif choice == 'v':
            save_game(player)
        else:
            print("Invalid choice, try again.")

# map map making of the moving in the map

MINERAL_PRICES = {
    'copper': (1, 3),
    'silver': (5, 8),
    'gold': (10, 18),
}

MINERAL_ORE_RANGES = {
    'C': (1, 5),  # copper
    'S': (1, 3),  # silver
    'G': (1, 2),  # gold
}

MINERAL_NAMES = {
    'C': 'copper',
    'S': 'silver',
    'G': 'gold',
}


def show_viewport(mine_map, x, y):
    print("+---+")
    for dy in range(-1, 2):
        row = "|"
        for dx in range(-1, 2):
            nx, ny = x + dx, y + dy
            if nx == x and ny == y:
                row += "M"
            elif 0 <= ny < len(mine_map) and 0 <= nx < len(mine_map[0]):
                row += mine_map[ny][nx]
            else:
                row += " "  # outside map bounds
        row += "|"
        print(row)
    print("+---+")


def load_mine():
    with open(r"C:\Users\Shwun\OneDrive\Desktop\2. PRG 1\ASSIGNMENT\PRG1Assignment\level1.txt", "r") as f:
        return [list(line.rstrip("\n")) for line in f]

def enter_mine(player, mine_map):
    x, y = player.get('mine_pos', player['portal_pos'])

    turns_left = 20
    player['steps'] = player.get('steps', 0)

    while turns_left > 0:
        print(f"\nDAY {player['day']}")
        show_viewport(mine_map, x, y)
        print(f"Turns left: {turns_left}    Load: {player['load']} / {player['backpack_capacity']}    Steps: {player['steps']}")
        print("(WASD) to move")
        print("(M)ap, (I)nformation, (P)ortal, (Q)uit to main menu")
        action = input("Action? ").strip().lower()

        if action == 'q':
            print("Quitting to main menu...")
            player['mine_pos'] = (x, y)
            break
        elif action == 'm':
            print("Full mine map display is not implemented yet.")
            continue
        elif action == 'i':
            print_player_info(player)
            continue
        elif action == 'p':
            print("Using portal to return to town...")
            player['portal_pos'] = (x, y)
            player['mine_pos'] = (0, 0)
            player['day'] += 1
            break
        elif action in ['w', 'a', 's', 'd']:
            dx, dy = 0, 0
            if action == 'w': dy = -1
            elif action == 'a': dx = -1
            elif action == 's': dy = 1
            elif action == 'd': dx = 1

            new_x, new_y = x + dx, y + dy

            if not (0 <= new_y < len(mine_map) and 0 <= new_x < len(mine_map[0])):
                print("You can't move past the edge of the mine.")
                continue

            target_cell = mine_map[new_y][new_x]

            if target_cell in MINERAL_NAMES:
                if player['load'] >= player['backpack_capacity']:
                    print("Your backpack is full. You cannot step onto a mineral node.")
                    continue
                ore_name = MINERAL_NAMES[target_cell]
                min_ore, max_ore = MINERAL_ORE_RANGES[target_cell]
                mined_amount = random.randint(min_ore, max_ore)
                space_left = player['backpack_capacity'] - player['load']
                if mined_amount > space_left:
                    print(f"You mined {mined_amount} piece(s) of {ore_name}.")
                    print(f"...but you can only carry {space_left} more piece(s)!")
                    mined_amount = space_left
                else:
                    print(f"You mined {mined_amount} piece(s) of {ore_name}.")
                player['inventory'][ore_name] += mined_amount
                player['load'] += mined_amount
                mine_map[new_y][new_x] = ' '

            if target_cell == 'T':
                print("You stepped on the Town portal. Returning to town...")
                player['mine_pos'] = (0, 0)
                player['portal_pos'] = (0, 0)
                player['day'] += 1
                break

            x, y = new_x, new_y
            player['steps'] += 1
            turns_left -= 1

        else:
            print("Invalid action.")

    else:
        print("can't carry any more, so you can't go that way. You are exhausted. You place your portal stone here and zap back to town. ")
        player['mine_pos'] = (x, y)
        player['day'] += 1



def main():
    while True:
        main_menu()
        choice = input().strip().lower()
        if choice == 'n':
            new_game()
        elif choice == 'l':
            player = load_game()
            if player:
                new_game(player)
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter N, L, or Q.")

if __name__ == "__main__":
    main()
