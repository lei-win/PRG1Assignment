import random

# Prices ranges for minerals
MINERAL_PRICES = {
    'copper': (1, 3),
    'silver': (5, 8),
    'gold': (10, 18),
}

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

def sell_minerals(player):
    if not player['inventory']:
        return
    print("You have minerals to sell. Selling all...")
    total_sale = 0
    for mineral, count in player['inventory'].items():
        if count > 0:
            price_range = MINERAL_PRICES.get(mineral, (0, 0))
            # Random sale price per mineral piece for this visit
            sale_price = random.randint(*price_range)
            sale_value = sale_price * count
            print(f" Sold {count} {mineral} ore at {sale_price} GP each for {sale_value} GP.")
            total_sale += sale_value
            player['inventory'][mineral] = 0  # emptied
    player['gp'] += total_sale
    player['load'] = 0
    print(f"Total GP earned from selling: {total_sale}")
    print(f"Current GP: {player['gp']}")