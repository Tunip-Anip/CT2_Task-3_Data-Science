import pandas as pd

Inflation = pd.read_csv('Inflation.csv')
print(Inflation)

Inflation[['Quarter', 'Annual change (%)']]


import matplotlib.pyplot as plt
Inflation.plot(
               kind='bar',
               x='Quarter',
               y='Annual change (%)',
               color='blue',
               alpha=0.1,
               title='Inflation across the years in Australia'
              )
plt.show()