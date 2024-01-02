#importing necessary libraries
import pandas as pd #pandas is a data manipulation library
import matplotlib.pyplot as plt # matplotlib is a plotting library for creating visualization

# Read the data from a csv file into a dataframe
grow_data = pd.read_csv('Inputs/GrowLocations.csv')

# Data Cleaning  Rename the wrongly named columns for clarity
grow_data.rename(columns={"Latitude": "Longitude", "Longitude": "Latitude"}, inplace=True)

# Data Cleaning Filtering the necessary boundary from the data
cleaned_grow_data = grow_data[
    (grow_data['Latitude'] >= 50.681) & (grow_data['Latitude'] <= 57.985) & (grow_data['Longitude'] >= -10.592) & (grow_data['Longitude'] <= 1.6848)
]

# Creating variables for the plot  (x, y and area of plot)
x_axis = cleaned_grow_data['Latitude']
y_axis = cleaned_grow_data['Longitude']
figure, ax = plt.subplots() # creating figure and axis for the plot

# Reading the UK image and plotting the cleaned data on the UK map, and saving output
scatter = ax.scatter(y_axis, x_axis, c='green', label='Sensor Data') #scatter plot with green color for sensor data
ukmap = plt.imread('Inputs/map.png') #reading the uk map which is in resources folder
plt.title("Plotting Grow Sensor Data") # title on the output
plt.xlabel('Longitude') # name on the x_axis
plt.ylabel('Latitude') # name on the y_axis
ax.imshow(ukmap, extent=(-10.5, 1.8, 50.6, 57.8)) # Displaying the as the background for the plot

# Adding a legend to the plot
ax.legend()

figure.savefig('YashashGrowLocationsMaps.png') # helping to save the output file
plt.show() # a screen will pop to show the output of the program
