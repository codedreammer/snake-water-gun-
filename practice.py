import random

def determine_winner(player_choice, computer_choice):

    rules = {
        'snake' : 'water',
        'water' : 'gun',
        'gun'   : 'snake'
    }

    if player_choice == computer_choice:
        return "It's a tie!"
    elif rules[player_choice] == computer_choice:
        return "You win!"
    else:
        return "Computer wins!"
  
def main():
    choices = ['snake', 'water', 'gun']
    player_choice = input("Enter your choice (snake, water, gun): ").lower()

    if player_choice not in choices:
        print("Invalid choice! Please choose as follow snake, water, gun.")
        return
    
    computer_choice = random.choice(choices)
    print(f"computer chose: {computer_choice}")

    result = determine_winner(player_choice,computer_choice)
    print(result)

if __name__ == "__main__":
        main()
        

    
