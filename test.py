import matplotlib.pyplot as plt
import numpy as np

# Size of your array in pixels
width_pixels = 150
height_pixels = 125
data = np.random.random((150,125))

# Size of one pixel in centimeters
pixel_size_cm = 0.1

# Calculate the limits in centimeters
x_min_cm = 0  # Starting at 0 cm
x_max_cm = width_pixels * pixel_size_cm
y_min_cm = 0  # Starting at 0 cm
y_max_cm = height_pixels * pixel_size_cm


# Create the plot and set the axis limits in centimeters
plt.imshow(data, cmap="hot", interpolation="nearest", extent=[x_min_cm, x_max_cm, y_min_cm, y_max_cm])
plt.title("Scaled Plot in Centimeters")
plt.colorbar()

# Show the plot
plt.show()
