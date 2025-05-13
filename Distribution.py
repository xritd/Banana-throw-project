import numpy as np
import matplotlib.pyplot as plt
'''
Test the distribution of points using a certain random number generator
'''
# Plot unit circle
phi = np.linspace(0, 2*np.pi, 100)
plt.plot(np.cos(phi), np.sin(phi))

# Number of points
N = 100

# Create lists of x- and y-coordinates
x_lst = [None]*N
y_lst = [None]*N

# for-loop to create 100 points
for k in range(N):
    # Generate random polar coordinates (r, theta)
    r = np.sqrt(np.random.uniform(0, 1))
    theta = np.random.uniform(0, 2*np.pi)
    
    # Assign x, y values to the lists
    x_lst[k] = r*np.cos(theta)
    y_lst[k] = r*np.sin(theta)

# Plot points
plt.plot(x_lst, y_lst, 'ro')

# Add title, grid, axis adjustment
plt.axis('equal') 
plt.title(f'Distribution of {N} random points')
plt.grid()

# Show plot
plt.show()