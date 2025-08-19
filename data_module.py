import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import time



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
    
def filterDataCrime(query):
    num = query[:4]
    numint = int(num) - 2013
    specific_rows = Crime.iloc[numint,0:2]
    time.sleep(0.5)
    print(specific_rows)

def filterDataInflation(query):
    num = int(query[-2:])
    floor = (num*4) - 64    
    print(floor)
    roof = (num*4) - 60
    print(roof)
    
    specific_rows = Inflation.iloc[floor:roof,0:3]
    print(specific_rows)