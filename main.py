''''Slot Machine'''

import random


MAX_ROWS = 3
MAX_COLS = 3
MAX_BETS = 3
MIN_BETS = 1


symbols_count = {
    "@": 2,
    "$": 1,
    "&": 6,
    "#": 5
}

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in range(symbols_count):
        for _ in range(symbol_count):
            all_symbols.append("symbol")
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.appen(column)

def deposit():
    
    while True:
        amount = input("Enter The Amount you want to Deposit! $")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 500:
                break
            else: 
                print("Amount must be greater than $500")
        else:
            print("Enter the Valid Amount!")

def lines():
    while True:
        lines = input(f"Enter the Number of Lines you want to Bet on between {MIN_BETS}-{MAX_BETS}")
        if lines.isdigit():
            lines = int(lines)
            if MAX_BETS >= lines >= MIN_BETS:
                break
            else:
                print("Please Enter the Correct Amount of Lines you want to Bet on!")
        else:
            print("Please Enter Number of lines only!")

def bet_amount():
    while True:
        bets = input(f"Enter the Amount of bet on each line!")
        if bets.isdigit():
            bets = int(bets)
            if 1 <= bets <= 100:
                break
            else:
                print("Please Enter the Amount between [1 to 100]")
        else:
            print("Please Enter valid number!")