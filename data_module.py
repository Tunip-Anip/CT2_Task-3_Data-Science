import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms



Inflation = pd.read_csv('Inflation.csv')
print(Inflation)

Inflation[['Quarter', 'Annual change (%)']]


Inflation.plot(
               kind='bar',
               x='Quarter',
               y='Annual change (%)',
               color='blue',
               alpha=0.1,
               title='Inflation across the years in Australia',
               yticks=(1:10)
               )

plt.xlim(-1, 37)

plt.show()