import matplotlib.pyplot as plt
import pandas as pd

# Load data
data = pd.read_csv('data/ufo_sightings.csv')

# Plot
plt.figure(figsize=(6.8, 4.4))
x = range(len(data['Day']))
plt.plot(x, data['March'])
plt.xticks(x, data['Day'])
plt.xlabel('Day')
plt.ylabel('March')
plt.show()
