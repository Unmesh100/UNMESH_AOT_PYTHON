import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 0 to 2*pi (one full cycle)
x_values = np.linspace(0, 2 * np.pi, 100)  # 100 points between 0 and 2*pi

# Calculate sine and cosine values
y_sin = np.sin(x_values)
y_cos = np.cos(x_values)

# Plotting the sine and cosine curves
plt.figure(figsize=(10, 6))

# Plot sine curve
plt.plot(x_values, y_sin, label='sin(x)', color='blue')

# Plot cosine curve
plt.plot(x_values, y_cos, label='cos(x)', color='orange')

# Adding labels and title
plt.title('Sine and Cosine Curves')
plt.xlabel('x (radians)')
plt.ylabel('Function value')
plt.axhline(0, color='black', linewidth=0.5, ls='--')  # X-axis
plt.axvline(0, color='black', linewidth=0.5, ls='--')  # Y-axis
plt.grid()
plt.legend()
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], 
           ['0', 'π/2', 'π', '3π/2', '2π'])  # Set x-ticks to show π values

plt.show()
