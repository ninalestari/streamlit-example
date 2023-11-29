# my_web_page.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from your_animation_script import create_animation  # Import the function that creates the animation


# Title for the app
st.title('Interactive Function Plot')
st.write('Welcome to my web page!')

# Function to create and display the animation
create_animation()

# Define the function
def f(x):
    return x**2 + 3*x + 5

# Generate x values
x = np.linspace(-10, 10, 400)

# Create a figure and axis
fig, ax = plt.subplots()

# Set up the plot
line, = ax.plot(x, f(x), 'r-', linewidth=2)
ax.grid(True)
plt.title('Graph of f(x) = x^2 + 3x + 5')

# Define the animation function
def animate(i):
    ax.set_xlim(-10, 10)
    ax.set_ylim(0, 100)
    ax.fill_between(x, 0, f(x), where=(x < i), color='blue', alpha=0.3)

# Create the animation
ani = FuncAnimation(fig, animate, frames=np.linspace(-10, 10, 100), interval=100)

# Show the animation
plt.show()


# Add more Streamlit commands to create your web page

