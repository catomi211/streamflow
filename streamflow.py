### Import Statements

import matplotlib.pyplot as plt
import numpy as np

### Part 3 - Provo River Streamflow Data

### Numpy Array Creation & Slicing

# imports data from the file into an array
array1 = np.genfromtxt('June-2021-Provo-River-Streamflow-Rates.csv', delimiter=',',dtype=str,skip_header=1)

# creates seperate arrays for seperate data types found in each column. Use as type to make sure the formatting is right
x = array1[:, 0].astype("datetime64")
y_1 = array1[:,1].astype(float)
y_2 = array1[:,2].astype(float)
y_3 = array1[:,3].astype(float)
y_4 = array1[:,4].astype(float)
y_5 = array1[:,5].astype(float)

### Graphing the Data Plot 
### x, y_1, y_2, y_3, y_4, and y_5 with the elements shown in the instructions in the code block below.

plt.plot(x,y_1,label = "10163000")
plt.plot(x,y_2, label = "10155200")
plt.plot(x,y_3, label = "10155500")
plt.plot(x,y_4, label = "10154200")
plt.plot(x,y_5, label = "10155000")

# creates a legend
plt.legend(title = "Site Numbers", loc = "upper right")
plt.xlabel("Date")

# rotates the x labels 45 degrees
plt.xticks(rotation = 45)
plt.ylabel("Flowrate (cfs)")
plt.title("Provo River Streamflow Data (2021)")

plt.grid()
plt.show()