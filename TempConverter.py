def celsius_to_fahrenheit(c):
    return 9*c/5 + 32

def fahrenheit_to_celsius(f):
    return 5*(f - 32)/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return 5*(f - 32)/9 + 273.15

def kelvin_to_fahrenheit(k):
    return 9*(k - 273.15)/5 + 32
        
def convert(choice):
    if choice == "1":
        print("Enter the temperature in Celsius.")
        while True:
            try:
                c = float(input("Temp: "))
                if c < -273.15:
                    raise IndexError
                f = celsius_to_fahrenheit(c)
                print("Temperature in Fahrenheit:", f)
                return
            except ValueError:
                print("Please enter a float number.")
            except IndexError:
                print("That temperature is impossible.")
    if choice == "2":
        print("Enter the temperature in Fahrenheit.")
        while True:
            try:
                f = float(input("Temp: "))
                if f < -9*273.15/5 + 32:
                    raise IndexError
                c = fahrenheit_to_celsius(f)
                print("Temperature in Celsius:", c)
                return
            except ValueError:
                print("Please enter a float number.")
            except IndexError:
                print("That temperature is impossible.")
    if choice == "3":
        print("Enter the temperature in Celsius.")
        while True:
            try:
                c = float(input("Temp: "))
                if c < -273.15:
                    raise IndexError
                k = celsius_to_kelvin(c)
                print("Temperature in Kelvin:", k)
                return
            except ValueError:
                print("Please enter a float number.")
            except IndexError:
                print("That temperature is impossible.")
    if choice == "4":
        print("Enter the temperature in Kelvin.")
        while True:
            try:
                k = float(input("Temp: "))
                if k < 0:
                    raise IndexError
                c = kelvin_to_celsius(k)
                print("Temperature in Celsius:", c)
                return
            except ValueError:
                print("Please enter a float number.")
            except IndexError:
                print("That temperature is impossible.")
    if choice == "5":
        print("Enter the temperature in Fahrenheit.")
        while True:
            try:
                f = float(input("Temp: "))
                if f < -9*273.15/5 + 32:
                    raise IndexError
                k = fahrenheit_to_kelvin(f)
                print("Temperature in Kelvin:", k)
                return
            except ValueError:
                print("Please enter a float number.")
            except IndexError:
                print("That temperature is impossible.")
    if choice == "6":
        print("Enter the temperature in Kelvin.")
        while True:
            try:
                k = float(input("Temp: "))
                if k < 0:
                    raise IndexError
                f = kelvin_to_fahrenheit(k)
                print("Temperature in Fahrenheit:", f)
                return
            except ValueError:
                print("Please enter a float number.")
            except IndexError:
                print("That temperature is impossible.")

print("Please enter an option 1-6 for converting temperatures:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")
while True:
    try:
        choice = input("You: ")
        if choice not in ["1", "2", "3", "4", "5", "6"]:
            raise ValueError
        else:
            convert(choice)
            break
    except ValueError:
        print("Please enter an option 1-6.")