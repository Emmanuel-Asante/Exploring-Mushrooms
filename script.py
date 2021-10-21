# Import modules
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import codecademylib3

# load in the data
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# list of all column headers
columns = df.columns.tolist()

# What type(s) of variables does mushroom_data.csv contain?
print("Every single variable of \'mushroom_data.csv\' is a categorical variable\n")

# How many of the variables can we visualize effectively with a bar graph?
print("We can create bar charts for the counts of every variable in the csv file\n")

# Output the columns of the csv file

# Iterate through columns to create a barchart for each categorical variable
for column in columns:
  #print(column)
  sns.countplot(df[column], order=df[column].value_counts().index, palette=['green'])
  plt.title(column + " Value Counts")
  plt.xticks(rotation=30, fontsize=10)
  plt.xlabel(column, fontsize=12)
  plt.show()
  plt.clf()

# What variables have an obvious mode?
print("From the Barcharts, all the variables have an obvious mode\n")

# Do any of them have a notably diverse array of values?
print("Values are widely varied\n")

# What habitat are you most likely to find mushrooms in?
print("Mushrooms are mostly found in Woods Habitat")

# Create the proportions for the "Veil Color" variable in df. Assign the result to a variable named veil_proportion
veil_proportions  = df["Veil Color"].value_counts(normalize=True)

# Display a pie chart of "Veil Color" variable
explode = (0.5, 0.1, 0.2, 0.4)
fig1, ax1 = plt.subplots()
ax1.pie(veil_proportions, explode=explode, labels=["White", "Orange", "Brown", "Yellow"])
plt.axis("equal")
plt.title("Veil Color Distribution")
plt.show()
plt.clf()

# Create a function called graph which will plot the data
def graph(column):
  sns.countplot(df[column], order=df[column].value_counts().index, palette=['red'])
  # Rotates the value labels slightly so the don’t overlap, also slightly increases font size
  plt.xticks(rotation=30, fontsize=10)
  # Increases the variable label font size slightly to increase readability
  plt.xlabel(column, fontsize=12)
  plt.title(column + ' Value Counts')
  plt.show()
  plt.clf()

# Create your bar charts using a list comprehension instead of a for loop
results = [graph(column) for column in columns]