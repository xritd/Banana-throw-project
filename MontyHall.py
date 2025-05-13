import random

def Pick_remaining(a, b):
    if (a == 1 and b == 2):
        return 3
    if (a == 1 and b == 3):
        return 2
    if (a == 2 and b == 1):
        return 3
    if (a == 2 and b == 3):
        return 1
    if (a == 3 and b == 1):
        return 2
    if (a == 3 and b == 2):
        return 1

def Open_door(a, b):
    if a == b:
        if a == 1:
            return random.choice([2, 3])
        if a == 2:
            return random.choice([1, 3])
        if a == 3:
            return random.choice([1, 2])
    else:
        return Pick_remaining(a, b)

def Monty_Hall():
    c = random.randint(1, 3)
    print("Welcome to the Monty Hall show!")
    print("Here you will be met with three doors, behind two of "
          "which there's a goat, but the third hides a treasure.")
    print("Which door 1-3 do you choose?")
    while True:
        try:
            guess = input("")
            g = int(guess)
            if (g < 1 or g > 3):
                raise IndexError
            else:
                o = Open_door(g, c)
                print(f"Before I tell you the answer, I'm "
                          "going to open door number {o} "
                          , "and show that this door has a goat. Now, "
                          "I will let you either switch to the other door "
                          "I did not open, or stay with your first choice.")
                print("Will you switch or stay?")
                while True:
                    try:
                        choice = input("")
                        if choice in ["Switch", "switch"]:
                            g = Pick_remaining(g, o)
                            print(f"You chose to switch to door number {g} "
                                  "and that is...")
                            if g == c:
                                print("Correct! You win the treasure!")
                                return
                            else:
                                print(f"Incorrect! The correct answer was {c}. "
                                      "Better luck next time.")
                                return
                        if choice in ["stay", "Stay"]:
                            print("You chose to stay with your first choice, "
                                  f"which was door number {g} and that is...")
                            if g == c:
                                print("Correct! You win the treasure!")
                                return
                            else:
                                print(f"Incorrect! The correct answer was {c}. "
                                      "Better luck next time.")
                                return
                        else:
                            raise TypeError
                    except TypeError:
                        print('Please enter "Switch" or "Stay".')
        except ValueError:
            print("Please enter an integer 1-3.")
        except IndexError:
            print("The number is outside of the bounds.")

if __name__ == "__main__":
    Monty_Hall()