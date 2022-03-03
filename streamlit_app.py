# Load libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the data
students = pd.read_csv('test_data.csv')

# Write equation for a line
y = 9.85 * students.hours_studied + 43

# Create the plot here: 


#plt.plot(students.hours_studied, y)
plt.show()
