import numpy as np
import matplotlib.pyplot as plt
import math

# Parameters
k = 0.1 # Air resistance
m = 1 # Mass of banana
g = 9.82 # Gravitational acceleration
h = 0.01 # Timestep size (should be less than tolerance)
tol = 0.1 # Tolerance (or size of target)
d = 5 # Initial distance from target

def F(t, s, A, f): 
    # ds/dt = As + f
    return A@s + f

def Throw_banana(angle, velocity):
    '''
    Numerically calculates the function and plots all iterated points,
    as well as the target.
    '''
    # Initial conditions
    v_x = velocity*math.cos(angle)
    v_y = velocity*math.sin(angle)
    x = 0
    y = 0
    t = 0
    
    s = np.array([v_x, v_y, x, y]) 

    A = np.array([[-k/m, 0, 0, 0],
                  [0, -k/m, 0, 0],
                  [1, 0, 0, 0],
                  [0, 1, 0, 0]])

    f = np.array([0, -g, 0, 0])
    
    s_list = [] # List of solution vectors
    
    while s[3] >= 0: # While y is non-negative
        s_list.append(s.copy())

	# RK2 method
        k1 = F(t, s, A, f)
        k2 = F(t + h/2, s + h*k1/2, A, f)
        s += h*k2 
	
        # Alternative method: Forward Euler
        # s += h*F(t, s, A, f) 

    x_points = [s[2] for s in s_list]
    y_points = [s[3] for s in s_list]
    
    x = x_points[-1]
    y = y_points[-1]
        
    # Distance from last point to center of target
    distance = math.sqrt((x - d)**2 + y**2)
    
    plt.plot(x_points, y_points)
    
    # Constructing circle
    theta = np.linspace(0, math.pi, 100)
    a = tol*np.cos(theta) + d
    b = tol*np.sin(theta)
    # Color of circle depending on hit or miss
    if distance <= tol:
        plt.fill(a, b, color = 'green')
    else:
        plt.fill(a, b, color = 'red')
    
    # Limits of the plot
    plt.xlim(0, d + tol + 1)
    plt.ylim(0, max(y_points) + 1)
    
    # Text with initial angle (in degrees) and velocity
    plt.legend([f'Initial Angle: {angle*180/math.pi:.2f} degrees '
    f'\nInitial Velocity: {velocity:.2f} m/s'], loc='upper right', fontsize=12)
    
    return x, distance

def Suggestion(angle, velocity):
    '''
    Suggests a different angle for a given velocity, and vice versa. 
    Alternatively, if no angle works for the velocity, a new velocity
    is proposed for the entered angle.
    '''
    # Tries finding a velocity for the given angle
    v = velocity
    x, distance = Throw_banana(angle, velocity)
    loop_count = 0
    while distance > tol and loop_count < 500:
        if x > d + tol:
            v = (v + v/2)/2
        elif x < d - tol:
            v = (2*v + v)/2
        x, distance = Throw_banana(angle, v)
        loop_count += 1
    # If no velocity found
    if loop_count == 500: 
        print("It seems that your angle was a bit unsuitable for these "
    "parameters. Try setting a different angle this time.")
        return Throwing_banana_game()
        
    velocity_works = False # Check if velocity works for some angle
    suggested_angle = None # In case no angle is found
    
    # Tries finding an angle for the given velocity
    for theta in np.linspace(0, math.pi/2, num=500):
        dist = Throw_banana(theta, velocity)[-1]
        if dist <= tol:
            velocity_works = True
            suggested_angle = theta
            break
        
    return v, suggested_angle, velocity_works

def Throwing_banana_game():
    '''
    The main menu of the game.
    '''
    plt.clf()  
    print("\nPlease input the initial angle (in degrees) and velocity of "
    "your throw.")
    while True:
        try:
            alpha = input("Angle: ")
            alpha = math.pi*float(alpha)/180 # Conversion to radians
            if alpha >= math.pi/2 or alpha <= 0:
                raise IndexError
            break
        except ValueError:
            print("Could not interpret the input.")
        except IndexError:
            print("Angle must be in range (0, 90).")
    while True:
        try:
            v0 = input("Velocity: ")
            v0 = float(v0)
            if v0 <= 0:
                raise IndexError
            break
        except ValueError:
            print("Could not interpret the input.")
        except IndexError:
            print("Velocity must be positive.")
    x, distance = Throw_banana(alpha, v0)
    plt.show()
    
    # Checks if the target is hit
    if distance <= tol:
        print("Yes! You hit the target, well done!")
        return
    else:
        return Miss(alpha, v0)
    
def Miss(alpha, v0):
    '''
    Runs if the shot missed the target.
    '''
    print("You missed the target! Would you like a suggestion?")
    while True:
        try:
            reply = input("Input: ")
            if reply.lower() == 'yes':
                v, angle, v0_works = Suggestion(alpha, v0)
                if v0_works == False: 
                    print("No angle could be found to work for that "
      "velocity within the given time limit. Instead, try setting your "
      f"velocity to around {v:.2f} m/s.")
                else:
                    print("If you want to maintain your angle of "
      f"{alpha*180/math.pi:.2f} degrees, you may try setting a velocity of "
      f"around {v:.2f} m/s. Alternatively, if you want to keep your velocity "
      f"of {v0:.2f} m/s, try throwing at an angle of around "
      f"{angle*180/math.pi:.2f} degrees.")
                return Throwing_banana_game()
            elif reply.lower() == 'no':
                return Play_again()
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter 'yes' or 'no'.")
        except TypeError:
            return

def Play_again():
    '''
    Runs if user missed the target and did not want a suggestion.
    '''
    print("Okay, do you want to try again?")
    while True:
        try:
            choice = input("Input: ")
            if choice.lower() == 'yes':
                return Throwing_banana_game()
            elif choice.lower() == 'no':
                print("Okay, come back again soon!")
                return
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    print("Welcome to the banana throwing game!")
    print(f"You will throw a banana at a monkey who sits {d} m away. You "
    f"need to hit the target within a distance of {tol} m from its center.")
    Throwing_banana_game()
