import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

def main():
    user_score = 0
    computer_score = 0

    print("🎮 Welcome to Rock-Paper-Scissors Game!")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'exit' to quit the game.\n")

    while True:
        user_choice = input("Enter your choice: ").lower()

        if user_choice == "exit":
            print("\n🎯 Final Score")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice! Please try again.\n")
            continue

        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("🤝 It's a tie!\n")

        elif result == "win":
            print("🎉 You win!\n")
            user_score += 1

        else:
            print("😢 You lose!\n")
            computer_score += 1

        # Score हर round के बाद दिखेगा
        print(f"Score -> You: {user_score} | Computer: {computer_score}\n")


if __name__ == "__main__":
    main()