from colorama import Fore, Style
import random
import os

# 3x3 grid with random currency sign symbols: USD, GBP, JPY
def generate_ticket():
    symbols = ['$', '£', '¥']
    ticket = [[random.choice(symbols) for _ in range(3)] for _ in range(3)]
    return ticket

# Display the ticket
def display_ticket(ticket):
    for row in ticket:
        print(' '.join(row))

# Clear the screen after a new ticket is requested
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Play
def play_game():
    while True:
        clear_screen()
        print(Fore.YELLOW + "Feeling lucky? \n")
        ticket = generate_ticket()
        display_ticket(ticket)
        play_again = input("\nAnother ticket? (y/n): ")
        if play_again.lower() != 'y':
            break

if __name__ == "__main__":
    play_game()
