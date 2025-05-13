import random

def Guessing_game(a, b, k):
    i = random.randint(a, b)
    c = k
    print(f"I'm thinking of a whole number between {a} and {b}. You have {k} guesses.")
    while True:
        try:
            guess = input("")
            g = int(guess)
            if g < a:
                raise IndexError
            if g > b:
                raise IndexError
            else:
                if g == i:
                    if c != k:
                        print(f"Correct! You got it in {k-c+1} guesses! Can you"
                          f" get it in {k-c} next time?")
                        return
                    elif c == k:
                        print("Correct! You got it on the first try! Well done!")
                        return
                elif g > i:
                    c -= 1
                    if c > 0:
                        print(f"Too high. You have {c} guesses remaining.")
                    else:
                        print("Too high. Better luck next time.")
                        return
                elif g < i:
                    c -= 1
                    if c > 0:
                        print(f"Too low. You have {c} guesses remaining.")
                    else:
                        print("Too low. Better luck next time.")
                        return
        except IndexError:
            print("The number is outside the range.")
        except ValueError:
            print("Please input a whole number.")
           
a = 1
b = 100
k = 10
if __name__ == "__main__":
    Guessing_game(a, b, k)
                    




