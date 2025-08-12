import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms



Inflation = pd.read_csv('Inflation.csv')
Inflation[['Quarter', 'Annual change (%)']]


Crime = pd.read_csv('Crime_Rate.csv')
Crime[['Years', 'Crime(%)/House']]


def graphInflation():
    global Inflation
    Inflation.plot(
        kind='bar',
        x='Quarter',
        y='Annual change (%)',
        color='blue',
        alpha=0.1,
        title='Inflation across the years in Australia',
        yticks=(0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10),
        ylabel= 'Annual Change (%)',
        xlabel= 'Date per Quarters',
               )
    plt.xlim(-1, 37)
    plt.show()



def graphCrime():
    global Crime
    Crime.plot(
            kind='bar',
            x='Years',
            y='Crime(%)/House',
            color='blue',
            alpha=0.1,
            title='Percentage of Victimisation From Total Housholds in Australia',
            )
    plt.show()
def tableCrime():
    print(Crime)

def tableInflation():
    print(Inflation)
    
