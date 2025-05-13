import random 
import matplotlib.pyplot as plt
import numpy as np

valid_directions = ['L', 'R', 'U', 'D']

def generate_room(width, height, dirt_prob=0.5):
    '''
    Generate random height x width grid space where each cell has a
    dirt_prob probability of being a 1.
    '''
    # Error handling
    if not isinstance(width, int) or width <= 0:
        raise ValueError("Width must be a positive integer.")
    if not isinstance(height, int) or height <= 0:
        raise ValueError("Height must be a positive integer.")
    if not 0 <= dirt_prob <= 1:
        raise ValueError("Probability must be between 0 and 1.")
    
    # Create room and update each cell based on probability 
    room = [[0 for x in range(width)] for y in range(height)]
    for y in range(height):
        for x in range(width):
            r = random.random()
            if r <= dirt_prob:
                room[y][x] = 1
    return room

def generate_start(width, height):
    '''
    Generate random starting point (x, y) in height x width grid space
    '''
    # Error handling
    if not isinstance(width, int) or width <= 0:
        raise ValueError("Width must be a positive integer.")
    if not isinstance(height, int) or height <= 0:
        raise ValueError("Height must be a positive integer.")
    
    # Uniformly random integer coordinate
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    return (x, y)

def generate_directions(length, distrib):
    '''
    Generate random sequence of directions with given length and 
    distribution for directions.
    '''
    # Error handling
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length of list must be a positive integer.")
    if set(distrib.keys()) != set(valid_directions):
        raise ValueError("Distribution must include all and only valid directions: " +
                         ", ".join(valid_directions))
    probs = distrib.values()
    if not abs(sum(probs) - 1) < 1e-9:
        raise ValueError("Probabilities must sum to 1.")
    if not all(0 <= p <= 1 for p in probs):
        raise ValueError("Probabilities must be between 0 and 1.")
        
    return random.choices(valid_directions, 
                          weights=[distrib[d] for d in valid_directions], 
                          k=length)
    
def clean_room(room, start, directions):
    '''
    Given a grid, starting point and sequence of directions, begins at
    start and follows the direction, cleaning any dirty cell along
    the way.
    '''
    # Error handling
    if not room or not all(isinstance(row, list) for row in room):
        raise ValueError("Room must be a non-empty list of lists.")
    height, width = len(room), len(room[0])
    if not all(len(row) == width for row in room):
        raise ValueError("All rows in room must have the same length.")
    if not (isinstance(start, tuple) and len(start) == 2):
        raise ValueError("Start must be a tuple of (x, y).")
    x, y = start
    if not (0 <= x < width and 0 <= y < height):
        raise ValueError(f"Start {start} is outside room bounds ({width}, {height}).")
    if not all(d in valid_directions for d in directions):
        raise ValueError("Invalid direction(s), please try again.")
    
    # Deep copy of the grid and counter for cleaned cells
    cleaned_room = [row[:] for row in room]
    clean_counter = 0
    path = [(x, y)]  # Track path for visualization
    
    # Check starting point
    if cleaned_room[y][x] == 1:
        cleaned_room[y][x] = 0
        clean_counter += 1
    
    for d in directions:
        # Update coordinates, go to other side if out of bounds
        if d == 'L':
            x = x - 1 if x > 0 else width - 1
        elif d == 'R':
            x = x + 1 if x < width - 1 else 0
        elif d == 'U':
            y = y - 1 if y > 0 else height - 1
        elif d == 'D':
            y = y + 1 if y < height - 1 else 0
        
        # Stores coordinate and cleans if dirty
        path.append((x, y))
        if cleaned_room[y][x] == 1:
            cleaned_room[y][x] = 0
            clean_counter += 1
    
    return cleaned_room, clean_counter, path

def plot_room(room, path, title):
    room_array = np.array(room)
    plt.imshow(room_array, cmap='Greys', interpolation='none')
    path_x, path_y = zip(*path)
    plt.plot(path_x, path_y, 'r.-', linewidth=1, markersize=10)
    plt.title(title)
    plt.show()

# Test with visualization
# random.seed(100)
width = 5
height = 3
path_length = 6

my_room = generate_room(width, height, 0.3)
print(f"Current {height}x{width} room:")
for row in my_room:
    print(row)
    
start = generate_start(width, height)

my_distrib = {'L': 0.25, 'R': 0.25, 'U': 0.25, 'D': 0.25}
my_directions = generate_directions(path_length, my_distrib)
print(f"\nStarting at {start}, vacuum cleaner follows path:")
print(my_directions)
    
try:
    result, count, path = clean_room(my_room, start, my_directions)
    print("\nCleaned room:")
    for row in result:
        print(row)
    print(f"Cleaned {count} cells.")
    plot_room(my_room, path, f"Vacuum Path from {start}")
except ValueError as ve:
    print(f"ValueError: {ve}")
    
Nine = 9
Ten = 12

