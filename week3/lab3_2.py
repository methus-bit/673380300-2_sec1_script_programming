def part1_countdown():
    print("=== Part 1: Countdown Timer ===")
    try:
        start = int(input("Enter a starting number for the countdown: "))
        count = start
        while count >= 0:
            print(count)
            count -= 1
        print("Blast off! 🚀")
    except ValueError:
        print("Error: Please enter a valid integer.")

def part2_guessing_game():
    print("\n=== Part 2: Simple Guessing Game ===")
    secret_number = 42
    max_attempts = 5
    attempts = 0
    
    print(f"I am thinking of a secret number. You have {max_attempts} attempts to guess it!")
    
    while attempts < max_attempts:
        try:
            attempts += 1
            guess = int(input(f"Guess the number (Attempt {attempts}/{max_attempts}): "))
            
            if guess == secret_number:
                print("Congratulations! You guessed it! 🎉")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    else:
        # ทำงานเฉพาะเมื่อลูปจบลงโดยไม่ถูก break (ทายไม่ถูกใน 5 ครั้ง)
        print(f"\nSorry, you ran out of attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    part1_countdown()
    part2_guessing_game()