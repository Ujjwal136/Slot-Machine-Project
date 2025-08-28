''''Slot Machine'''

import random

MAX_ROWS = 3
MAX_COLS = 3
MAX_BETS = 3
MIN_BETS = 1

symbol_count = {
    "@": 6,
    "#": 8,
    "$": 4,
    "&": 8
}

def get_Slot_values():
    symbols = []
    for symbol,count in symbol_count.items():
        for _ in range(count):
            symbols.append(symbol)
    
    row = MAX_ROWS
    col = MAX_COLS
    matrix = []

    for _ in range(col):
        column = [] 
        for _ in range(row):
            column.append(random.choice(symbols))
        matrix.append(column)
    return matrix

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i , column in enumerate(columns):
            if i < (len(columns)-1):
                print(column[row], end = "|")
            else:
                print(column[row], end = "")    
        print()

def deposit():
    
    while True:
        amount = input("Enter The Amount you want to Deposit! $")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 500:
                break
            else: 
                print("Amount must be greater than $500 ")
        else:
            print("Enter the Valid Amount! ")
    return amount

def lines():
    while True:
        lines = input(f"Enter the Number of Lines you want to Bet on between {MIN_BETS}-{MAX_BETS} ")
        if lines.isdigit():
            lines = int(lines)
            if MAX_BETS >= lines >= MIN_BETS:
                break
            else:
                print("Please Enter the Valid Amount of Lines you want to Bet on! ")
        else:
            print("Please Enter Number of lines only! ")
    return lines

def bet_amount(Amount,line):
    while True:
        bets = input(f"Enter the Amount of bet on each line! $")
        if bets.isdigit():
            bets = int(bets)
            if 1 <= bets <= Amount/line:
                break
            else:
                print(f"Please Enter the Amount between $1 to ${round(Amount/line,1)}  ")
        else:
            print("Please Enter valid Amount! ")
    return bets

def lines_win(values):
    data = values
    list1, list2, list3 = data
    line_win = []
    # a = list1[0]
    # for i in list1[1:]:
    #     if a != i:
    #         break
    #     return True
    # We can also convert into sets
    a = list(set(list1))
    b = list(set(list2))
    c = list(set(list3))
    if len(a) == 1:
        line_win.append(1)
    if len(b) == 1:
        line_win.append(1)
    if len(c) == 1:
        line_win.append(1)

    return len(line_win)

def winings(line,bet,balance):
    # if line == MAX_BETS:
    #     print(f"Congrats!, You win all the lines. You won total ${bet * MAX_BETS}")
    # elif (line == (MAX_BETS - 1)):
    #     print(f"Congrats!, You win {MAX_BETS-1} lines. You won total ${bet * (MAX_BETS - 1)}")
    # else:
    total_amount = 0
    if line > 0:
        print(f"You win ${bet * line} :). Amount is debited in your Account.")
        total_amount += (bet * line)
        print(f"{total_amount} added to your Wallet!")
    else:
        print("Better Luck Next Time :(")
        return total_amount

def main():
    balance = deposit()
    line = lines()
    print(f"Total Amount you deposited is ${balance}")
    print(f"Number of Lines you choose to Bet are {line}")
    while True:
        bet = bet_amount(balance,line)
        if (bet*line) <= balance:
            print(f"Your Total Bet is ${bet * line}")
            break
        else :
            print("Your Betting amount is Larger than Your Deposit!")
            break
    value = get_Slot_values()
    print_slot_machine(value)
    win = lines_win(value)
    print(f"You won Total {lines_win(value)} Lines!")
    amount_win = winings(win,bet,balance)
    new_balance = balance - (bet*line)
    new_balance += amount_win
    print(f"Updated amount in your Wallet is, ${new_balance}")

    
main()