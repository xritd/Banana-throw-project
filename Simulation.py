import matplotlib.pyplot as plt
import numpy as np
'''
Simulate distance between two random points in a unit circle
'''
# Number of iterations
N = 250

# Generate list of distances
dist_lst = [None]*N

# For-loop to simulate average distance between two points
for k in range(N):
    # Plot unit circle
    phi = np.linspace(0, 2*np.pi, 100)
    plt.plot(np.cos(phi), np.sin(phi))
    
    # Generate two random polar coordinates (r, theta)
    r1 = np.sqrt(np.random.uniform(0, 1))
    theta1 = np.random.uniform(0, 2*np.pi)
    
    r2 = np.sqrt(np.random.uniform(0, 1))
    theta2 = np.random.uniform(0, 2*np.pi)
    
    # Construct x-, y-coordinates from r and theta
    [x1, x2] = [r1*np.cos(theta1), r2*np.cos(theta2)]
    [y1, y2] = [r1*np.sin(theta1), r2*np.sin(theta2)]
    
    # Calculate distance between the two points
    d = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    # Plot the two points and the line segment between them
    plt.plot([x1, x2], [y1, y2], 'b-', label=f'Distance = {d}')  # Line segment
    plt.plot(x1, y1, 'ro', label=f'Point 1: ({x1}, {y1})')  # Point 1
    plt.plot(x2, y2, 'go', label=f'Point 2: ({x2}, {y2})')  # Point 2
    
    # Legend should be updated outside the loop
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    
    # Show the plot
    plt.axis('equal')  # Set equal aspect ratio
    plt.title(f'Iteration {k + 1}')
    plt.grid()
    plt.show()
    
    # Assign value corresponding to the distance
    dist_lst[k] = d
    
    # Calculate the average distance
    average_dist = sum(filter(lambda x: x is not None, dist_lst))/(k+1)
    
    # Print information
    print(f"Iteration {k+1}:")
    print(f"Average distance = {average_dist} \n")

# Print conclusion
print(f"After {N} iterations, the average distance between two random "
      f"points in the unit circle is: {average_dist}")
print(f"Error: {np.abs(average_dist - 128/(45*np.pi))}")