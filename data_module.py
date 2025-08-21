import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import time
#Imports the required modules for the graphs and datasets

Inflation = pd.read_csv('Inflation.csv')
Inflation[['Quarter', 'Annual change (%)']]


Crime = pd.read_csv('Crime_Rate.csv')
Crime[['Years', 'Crime(%)/House']]
#Sets the datasets as a variable

def graphInflation():
    Inflation
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
#Visuallises the graph when called, specify type of graph, axis and values.


def graphCrime():
    Crime
    Crime.plot(
            kind='bar',
            x='Years',
            y='Crime(%)/House',
            color='blue',
            alpha=0.1,
            title='Percentage of Victimisation From Total Housholds in Australia',
            ylabel= 'Crime(%)/House',
            xlabel= 'Years'
            )
    plt.show()
    #Visuallises the graph when called, specify type of graph, axis and values.
def tableCrime():
    print(Crime)

def tableInflation():
    print(Inflation)
    #Prints the dataset
def filterDataCrime(query):
    num = query[:4]
    #Takes the first four characters of the inputted number which is the year.
    numint = int(num) - 2015
    #The inputed year minus 2013 is the row number
    specific_rows = Crime.iloc[numint,0:2]
    #Sets the filtered row into a variable from the row and column
    time.sleep(0.5)
    print(specific_rows)
    #Prints the variable

def filterDataInflation(query):
    num = int(query[-2:])
    #from the inputted number takes the last two integers (which is also the year)
    floor = (num*4) - 61    
    #Gets the lower range of numbers  from the year as each year contains 4 quarters Tthe 2nd row is the lowest in 2016)
    roof = (num*4) - 57
    #Gets the highest number in the range as each year contains 4 quarters (The 5th row is the highest of 2016)
    specific_rows = Inflation.iloc[floor:roof,0:3]
    #Sets the filtered row into a variable from the row and column
    print(specific_rows)
     #Prints the variable
def graphBoth():
    Inflation = pd.read_csv('Inflation.csv')
    Inflation[['Quarter', 'Annual change (%)']]
    
    Crime = pd.read_csv('Crime_Rate.csv')
    Crime[['Years', 'Crime(%)/House']]
    # Assigns the Crime Dataset and Inflation Dataset to variables
    Crimex = Crime['Years']
    Crimey = Crime['Crime(%)/House']
    Inflationx = Inflation['Quarter']
    Inflationy = Inflation['Annual change (%)']
    #Seperates the X and Y values of both datasets.
    fig=plt.figure()
    Crime=fig.add_subplot(111, label="1")
    Inflation=fig.add_subplot(111, label="2", frame_on=False)
    #Identifies the graphs constrains/ properties
    

    Crime.plot(Crimex,Crimey,color="C0")
    Crime.set_xlabel("Years", color="C0")
    Crime.set_ylabel("Crime(%)/House", color="C0")
    Crime.tick_params(axis='x', colors="C0")
    Crime.tick_params(axis='y', colors="C0")
    Crime.set_title("Affect\n of Inflation \non Crime\n Rates",fontsize = 10)
    ttl = Crime.title
    ttl.set_position([-0.01, 1.05])
    #Sets the properties of the Crime Data Plot
    
    Inflation.plot(Inflationx,Inflationy,color="C1")
    Inflation.xaxis.tick_top()
    Inflation.yaxis.tick_right()
    Inflation.set_xlabel('Date per Quarters', color="C1") 
    Inflation.set_ylabel('Annual Change (%)', color="C1")       
    Inflation.xaxis.set_label_position('top') 
    Inflation.yaxis.set_label_position('right') 
    Inflation.tick_params(axis='x', colors="C1")
    Inflation.tick_params(axis='y', colors="C1")
    Inflation.tick_params(axis='x', labelrotation=90)
    #Sets the properties of the Inflation Data Plot
    


    plt.show()
        