import matplotlib.pyplot as plt
import numpy as np

# Your data and pixel size (assuming your data is in micrometers)
data = np.random.random((100, 100))  # Replace with your data
pixel_size_um = 1000
print(type(data))
# Calculate the width and height of the plot in micrometers
width_um = data.shape[1] * pixel_size_um
height_um = data.shape[0] * pixel_size_um

# Create the figure with the desired figsize
fig, ax = plt.subplots(figsize=(width_um / 100, height_um / 100))

# Set the extent based on the width and height
extent = [0, width_um, 0, height_um]

# Plot your data with the specified extent
plt.imshow(data, extent=extent, cmap='viridis', interpolation='nearest')

# Set the aspect ratio to ensure correct scaling
ax.set_aspect('equal')

# Add labels and title as needed
plt.xlabel('X (um)')
plt.ylabel('Y (um)')
plt.title('Scaled Plot')

# Display the plot
plt.show()
