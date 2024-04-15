import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Define the vertices of a unit tesseract
tesseract_vertices = np.array([
    [0, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
])

# Define the edges of the tesseract
tesseract_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7),
    (8, 9), (9, 10), (10, 11), (11, 8),
    (12, 13), (13, 14), (14, 15), (15, 12),
    (8, 12), (9, 13), (10, 14), (11, 15),
    (0, 8), (1, 9), (2, 10), (3, 11),
    (4, 12), (5, 13), (6, 14), (7, 15)
]

# Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Function to update the plot for each frame of the animation
def update(frame):
    ax.clear()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    ax.set_title(f"Tesseract Rotation Frame {frame}")
    rotated_vertices = np.dot(tesseract_vertices, rotation_matrix(frame * np.pi / 180))
    for edge in tesseract_edges:
        ax.plot3D(rotated_vertices[edge, 0], rotated_vertices[edge, 1], rotated_vertices[edge, 2], color='blue')



# Function to generate rotation matrix for 4D rotation around XY plane
def rotation_matrix(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [c, -s, 0, 0],
        [s, c, c, s],
        [0, 0, 1, c],
        [0, s, -c, c]
    ])

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 5), interval=50)

# Show the animation
plt.show()
