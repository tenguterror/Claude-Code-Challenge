low = 1

high = 750

def guess_number(low, high):
    guess = (low + high) // 2
    return guess

while True:
    guess = guess_number(low, high)
    print(f"Is this your number {guess}")
    answer = input("Higher lower or correct:").lower().strip()

    if answer == "higher":
        low = guess + 1
    elif answer == "lower":
        high = guess - 1
    elif answer == "correct":
        print("Yay I guessed it!")
        break
    else:
        print("Please enter higher, lower, or correct.")
