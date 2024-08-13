import random

print("Welcome to the amazing Snake-water-gun game made by Akshay Mehta")
print("You have 10 chances")

def determine_winner(player_choice, computer_choice):
    rules = {
        'snake': 'water',
        'water': 'gun',
        'gun': 'snake'
    }

    if player_choice == computer_choice:
        return "It's a tie!"
    elif rules[player_choice] == computer_choice:
        return "You win!"
    else:
        return "Computer wins!"

def main():
    choices = ['snake', 'water', 'gun']
    player_score = 0
    computer_score = 0

    for _ in range(10):
        player_choice = input("Enter your choice (snake, water, gun): ").lower()

        if player_choice not in choices:
            print("Invalid choice! Please choose from snake, water, gun.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1

    print("\nGame Over!")
    print(f"Your score: {player_score}")
    print(f"Computer's score: {computer_score}")

if __name__ == "__main__":
    main()
