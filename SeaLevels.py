import pandas as pd
import matplotlib.pyplot as plt

ser = pd.read_csv('data.csv')
year = ser['Year']
sea_level = ser['CSIRO Adjusted Sea Level']
plt.scatter(year, sea_level, edgecolors='g')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sealevel')
plt.grid(which = 'major')
plt.show()