''''Slot Machine'''

import random

MAX_ROWS = 3
MAX_COLS = 3
MAX_BETS = 3
MIN_BETS = 1

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
                print("Please Enter the Correct Amount of Lines you want to Bet on! ")
        else:
            print("Please Enter Number of lines only! ")
    return lines

def bet_amount():
    while True:
        bets = input(f"Enter the Amount of bet on each line! ")
        if bets.isdigit():
            bets = int(bets)
            if 1 <= bets <= 100:
                break
            else:
                print("Please Enter the Amount between [$1 to $100] ")
        else:
            print("Please Enter valid Amount! ")
    return bets

def main():
    balance = deposit()
    line = lines()
    print(f"Total Amount you deposited is ${balance}")
    print(f"Number of Lines you choose to Bet are {line}")
    while True:
        bet = bet_amount()
        if (bet*line) <= balance:
            print(f"Your Total Bet is ${bet * line}")
            break
        else :
            print("Your Betting amount is Larger than Your Deposit!")
            break

main()