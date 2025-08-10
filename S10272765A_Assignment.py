#102727265A SHWUNLEIWIN

import random

# $$$ rng 4 minerals
MINERAL_PRICES = {
    'copper': (1, 3),
    'silver': (5, 8),
    'gold': (10, 18),
}

# main menu scrn
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
(V)iew Top Scores
(Q)uit
------------------ Your choice?""")

# town menu scrn
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

# save player score 2 file
def save_score(player):
    with open("scores.txt", "a") as f:
        line = f"{player['name']},{player['day']},{player['steps']},{player['gp']}\n"
        f.write(line)

# load scores frm file + sort
def load_scores():
    scores = []
    try:
        with open("scores.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    name, days, steps, gp = line.split(",")
                    scores.append({
                        "name": name,
                        "days": int(days),
                        "steps": int(steps),
                        "gp": int(gp)
                    })
    except FileNotFoundError:
        # no scores yet lol
        pass
    
    # sort by day↑, step↑, gp↓
    scores.sort(key=lambda x: (x["days"], x["steps"], -x["gp"]))
    return scores

# show top5 scores scrn
def display_top_scores():
    scores = load_scores()
    print("\n--- Sundrop Mountain Top Scores ---")
    print(f"{'Rank':<5}{'Name':<15}{'Days':<6}{'Steps':<7}{'GP':<5}")
    print("-" * 40)
    for i, score in enumerate(scores[:5], start=1):
        print(f"{i:<5}{score['name']:<15}{score['days']:<6}{score['steps']:<7}{score['gp']:<5}")
    print("-" * 40)
    input("Press Enter to return to the main menu...")

# sell all inv minerals 4 gp
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
    print(f"You now have {player['gp']} GP!")
    
    print(f"Total GP earned from selling: {total_sale}")
    print(f"You now have {player['gp']} GP!")


# check if player hit 500 gp goal yet - time to win!
    if player['gp'] >= 500:
        # show congrats message with player stats
        print(f"""
Woo-hoo! Well done, {player['name']}, you have {player['gp']} GP! 
You now have enough to retire and play video games every day. 
And it only took you {player['day']} days and {player['steps']} steps! You win!
-------------------------------------------------------------  
--- Main Menu ---- 
(N)ew game 
(L)oad saved game 
(V)iew Top Scores
(Q)uit 
------------------ Your choice? 
""")

# loop to get valid menu choice from user
        while True:
            choice = input("Your choice? ").strip().lower()

# start a new game if user types 'n'
            if choice == 'n':
                print("Starting new game...")
                # call your new_game() or reset function here
                break

# load saved game if user types 'l'
            elif choice == 'l':
                print("Loading saved game...")
                # call your load function here

 # show top scores if user types 'v'
            elif choice == 'v':
                print("Showing top scores...")
                break

# quit program if user types 'q'
            elif choice == 'q':
                print("Quitting game...")
                exit()

 # if none of the above, prompt again
            else:
                print("Invalid choice, please enter N, L, V or Q.")


def buy_stuff_menu(player):
    while True:
        # cost based on current backpack capacity
        backpack_price = player['backpack_capacity'] * 2

# show shop menu and current GP
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

# pickaxe upgrade logic
        if choice == 'p':
            if player['pickaxe_level'] >= 2:
                print("You already have the silver pickaxe or better.")
            elif player['gp'] >= 50:
                player['gp'] -= 50
                player['pickaxe_level'] = 2
                print("Congrats! Pickaxe upgraded to level 2 (silver)!")
            else:
                print("Not enough GP for pickaxe upgrade.")

# backpack upgrade logic
        elif choice == 'b':
            if player['gp'] >= backpack_price:
                player['gp'] -= backpack_price
                player['backpack_capacity'] += 2
                print(f"Congrats! Backpack capacity now {player['backpack_capacity']}.")
            else:
                print("Not enough GP for backpack upgrade.")

# leave shop
        elif choice == 'l':
            break

# invalid input catch
        else:
            print("Invalid choice, please enter P, B, or L.")

def print_player_info(player):
# map pickaxe level to name for display
    pickaxe_name = {1: "copper", 2: "silver"}.get(player['pickaxe_level'], "unknown")

# get player's current position in mine or default to (0,0)
    pos = player.get('mine_pos', (0, 0))

 # show player info neatly
    print(f"""
----- Player Information -----
Name: {player.get('name', 'Unknown')}
Current position: {pos}                # where player is now
Pickaxe level: {player.get('pickaxe_level', 1)} ({pickaxe_name})
Gold: {player['inventory'].get('gold', 0)}                  # ore counts
Silver: {player['inventory'].get('silver', 0)}
Copper: {player['inventory'].get('copper', 0)}
------------------------------
Load: {player.get('load', 0)} / {player.get('backpack_capacity', 12)}   # current carry / max
------------------------------
GP: {player.get('gp', 0)}                      # player gold points
Steps taken: {player.get('steps', 0)}          # steps in mine
------------------------------
""")
    
# quick static mine map display for player reference
def see_mine_map():
    print("\n+------------------------------+")
    print("|M     C    ???????????????????|")   # M = player start pos?, C = copper ore spots
    print("|      CP   ???????????????????|")   # P? maybe portal
    print("|????CCCC   ???????????????????|")
    print("|??????????????????????????????|")
    print("|??????????????????????????????|")
    print("|??????????????????????????????|")
    print("|??????????????????????????????|")
    print("|??????????????????????????????|")
    print("|??????????????????????????????|")
    print("|??????????????????????????????|")
    print("+------------------------------+")

# save current player data to text file in order
def save_game(player):
    with open("save_player.txt", "w") as f:
        f.write(f"{player['name']}\n")                              # player name
        f.write(f"{player['day']}\n")                               # current day count
        f.write(f"{player['backpack_capacity']}\n")                # max inventory size
        f.write(f"{player['load']}\n")                              # current load carried
        f.write(f"{player['gp']}\n")                                # player gold points
        f.write(f"{player['steps']}\n")                             # steps taken so far
        f.write(f"{player['pickaxe_level']}\n")                     # pickaxe tier level
        f.write(f"{player['portal_pos'][0]} {player['portal_pos'][1]}\n")   # portal position coords
        f.write(f"{player['inventory']['copper']} {player['inventory']['silver']} {player['inventory']['gold']}\n")  # ore counts
    print("Game saved.")       # confirmation msg

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
    # if no player data loaded, create new player profile
    if not player:
        name = input("Greetings, miner! What is your name? ").strip()   # get player name
        print(f"Pleased to meet you, {name}. Welcome to Sundrop Town!")
        player = {
            'name': name,
            'day': 1,                          # start day 1
            'backpack_capacity': 10,           # start backpack size
            'load': 0,                         # current load empty
            'gp': 0,                           # starting GP
            'steps': 0,                        # no steps taken yet
            'pickaxe_level': 1,                # starting pickaxe level copper
            'portal_pos': (0, 0),              # portal pos at town
            'inventory': {'copper': 0, 'silver': 0, 'gold': 0},   # empty ores
        }

    while True:   # main town loop
        sell_minerals(player)      # sell any minerals automatically when back in town
        town_menu(player)          # show town options menu
        choice = input("Your choice? ").strip().lower()

        if choice == 'q':          # quit to main menu
            break
        elif choice == 'b':        # go to shop menu
            buy_stuff_menu(player)
        elif choice == 'i':        # print player info screen
            print_player_info(player)
        elif choice == 'm':        # see mine map (static)
            see_mine_map()
        elif choice == 'e':        # enter the mine
            mine_map = load_mine() # load mine map file (may want to change if loading from save)
            enter_mine(player, mine_map)
        elif choice == 'v':        # save game option
            save_game(player)
        else:                      # invalid input handler
            print("Invalid choice, try again.")



MINERAL_PRICES = {
    'copper': (1, 3),      # copper ore price range (min, max)
    'silver': (5, 8),      # silver ore price range
    'gold': (10, 18),      # gold ore price range
}

MINERAL_ORE_RANGES = {
    'C': (1, 5),  # copper ore yield range per mining
    'S': (1, 3),  # silver ore yield range
    'G': (1, 2),  # gold ore yield range
}

MINERAL_NAMES = {
    'C': 'copper',   # map char to mineral name
    'S': 'silver',
    'G': 'gold',
}


def show_viewport(mine_map, x, y):
    print("+---+")
    for dy in range(-1, 2):     # vertical -1 to +1 around player
        row = "|"
        for dx in range(-1, 2): # horizontal -1 to +1
            nx, ny = x + dx, y + dy

            if nx == x and ny == y:
                row += "M"       # mark player pos with 'M'
            elif 0 <= ny < len(mine_map) and 0 <= nx < len(mine_map[0]):
                row += mine_map[ny][nx]  # show tile from map
            else:
                row += " "       # outside map bounds
        row += "|"
        print(row)
    print("+---+")


def load_mine(filename):
    with open(filename, "r") as f:
        return [list(line.rstrip("\n")) for line in f]   # load map as 2d list


def create_fog_map(rows, cols, start_pos):
    fog = [["?" for _ in range(cols)] for _ in range(rows)]   # start with all '?'
    r, c = start_pos
    fog[r][c] = "T"    # reveal starting tile as Town
    return fog


def print_fogged_map(fog_map):
    width = len(fog_map[0])
    print("+" + "-" * width + "+")
    for row in fog_map:
        print("|" + "".join(row) + "|")
    print("+" + "-" * width + "+")


def reveal_area(fog_map, full_map, player_pos, radius=1):
    rows, cols = len(full_map), len(full_map[0])
    pr, pc = player_pos

    for r in range(pr - radius, pr + radius + 1):
        for c in range(pc - radius, pc + radius + 1):
            if 0 <= r < rows and 0 <= c < cols:
                fog_map[r][c] = full_map[r][c]    # reveal tiles around player


def print_map(map_data):
    width = len(map_data[0])
    print("+" + "-" * width + "+")
    for row in map_data:
        print("|" + "".join(row) + "|")
    print("+" + "-" * width + "+")


# load full map from file
level_path = r"C:\Users\Shwun\OneDrive\Desktop\2. PRG 1\ASSIGNMENT\PRG1Assignment\level1.txt"
full_map = load_mine(level_path)

# create fog map same size as full map, start at (0,0)
fog_map = create_fog_map(len(full_map), len(full_map[0]), (0, 0))

# reveal starting area around player
reveal_area(fog_map, full_map, (0, 0))

# print the fogged map with revealed tiles
print_map(fog_map)


def load_mine():
    # load mine layout txt into 2d list
    with open(r"C:\Users\Shwun\OneDrive\Desktop\2. PRG 1\ASSIGNMENT\PRG1Assignment\level1.txt", "r") as f:
        return [list(line.rstrip("\n")) for line in f]


def enter_mine(player, mine_map):
    # start pos = saved mine_pos or fallback to portal_pos
    x, y = player.get('mine_pos', player['portal_pos'])

    turns_left = 20    # fixed turns per mine trip
    player['steps'] = player.get('steps', 0)   # init steps if missing

    while turns_left > 0:
        print(f"\nDAY {player['day']}")
        show_viewport(mine_map, x, y)   # show 3x3 area around player
        print(f"Turns left: {turns_left}    Load: {player['load']} / {player['backpack_capacity']}    Steps: {player['steps']}")
        print("(WASD) to move")
        print("(M)ap, (I)nformation, (P)ortal, (Q)uit to main menu")

        action = input("Action? ").strip().lower()

        if action == 'q':     # quit to main menu
            print("Quitting to main menu...")
            player['mine_pos'] = (x, y)   # save current pos
            break

        elif action == 'm':   # show fog of war map
            print("\nCurrent mine map (fog of war):")
            print_fogged_map(fog_map)
            continue

        elif action == 'i':   # show player info screen
            print_player_info(player)
            continue

        elif action == 'p':   # use portal, back to town
            print("Using portal to return to town...")
            player['portal_pos'] = (x, y)   # save portal pos
            player['mine_pos'] = (0, 0)     # reset mine pos to town
            player['day'] += 1               # next day
            break

        elif action in ['w', 'a', 's', 'd']:    # movement keys
            dx, dy = 0, 0

            if action == 'w': dy = -1
            elif action == 'a': dx = -1
            elif action == 's': dy = 1
            elif action == 'd': dx = 1

            new_x, new_y = x + dx, y + dy

            # check boundaries of mine_map
            if not (0 <= new_y < len(mine_map) and 0 <= new_x < len(mine_map[0])):
                print("You can't move past the edge of the mine.")
                continue

            target_cell = mine_map[new_y][new_x]

            # if stepping on mineral node
            if target_cell in MINERAL_NAMES:
                # check backpack full
                if player['load'] >= player['backpack_capacity']:
                    print("Your backpack is full. You cannot step onto a mineral node.")
                    continue

                ore_name = MINERAL_NAMES[target_cell]
                min_ore, max_ore = MINERAL_ORE_RANGES[target_cell]
                mined_amount = random.randint(min_ore, max_ore)

                space_left = player['backpack_capacity'] - player['load']

                # if mined amount > space left, adjust
                if mined_amount > space_left:
                    print(f"You mined {mined_amount} piece(s) of {ore_name}.")
                    print(f"...but you can only carry {space_left} more piece(s)!")
                    mined_amount = space_left
                else:
                    print(f"You mined {mined_amount} piece(s) of {ore_name}.")

                # update inventory + load
                player['inventory'][ore_name] += mined_amount
                player['load'] += mined_amount

                mine_map[new_y][new_x] = ' '   # clear mineral node after mining

            # if stepping on town portal
            if target_cell == 'T':
                print("You stepped on the Town portal. Returning to town...")
                player['mine_pos'] = (0, 0)
                player['portal_pos'] = (0, 0)
                player['day'] += 1
                break

            # update pos, steps, turns left
            x, y = new_x, new_y
            player['steps'] += 1
            turns_left -= 1

            # reveal tiles around new pos on fog map
            reveal_area(fog_map, mine_map, (y, x))

        else:
            print("Invalid action.")

    else:  # runs if while loop not broken (turns run out)
        print("can't carry any more, so you can't go that way. You are exhausted. You place your portal stone here and zap back to town.")
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

        elif choice == 'v':
            display_top_scores()

        else:
            print("Invalid choice, please enter N, L, V or Q.")


if __name__ == "__main__":
    main()

#FINISH CODE KMS KMS KMS