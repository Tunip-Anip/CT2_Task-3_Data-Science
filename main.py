from data_module import (graphInflation,graphCrime,tableCrime,tableInflation,filterDataCrime,filterDataInflation,graphBoth)
import time
#Imports the modules to run the graphs
def main_menu():
    #Checks for access
    print("For educational purposes the key is: U+1F511")
    #This is the unicode for the Key Emoji 🔑
    time.sleep(1)
    permission = input("Do you have permission - What is your key? ")
    
    
    Value = True
    if permission ==  "U+1F511":
        Value = True
        access = 1
    else:
        pass

        #Value = False
       # access = 0
    #Checks access

    while Value == True:
        print("\n=== Data Viewer Interface ===")
        print("1. View Crime dataset")
        time.sleep(0.1)
        print("2. View Inflation dataset")
        time.sleep(0.1)      
        print("3. View Crime visualisation")
        time.sleep(0.1)
        print("4. View Inflation visualisation")
        time.sleep(0.1)
        print("5. View Both visualisations")
        time.sleep(0.1)
        print("6. Filter Crime Dataset")
        time.sleep(0.1)
        print("7. Filter Inflation Dataset")
        time.sleep(0.1)
        print("8. Exit")        
    # Prints the options for the user
        time.sleep(1)

        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            tableCrime()
            time.sleep(1)
        elif choice == '2':
            tableInflation()
            time.sleep(1)
        elif choice == '3':
           graphCrime()
        elif choice == '4':
            graphInflation()
        elif choice == '5':
            graphBoth()
        elif choice == '6':
            try:
                query = str(input("What year do you want to query, eg: 2013–14 - "))
                #Enters the year as shown in the example
                filterDataCrime(query)
            except:
                print("Invalid query")
                #checks if the value can be inputted without error; if it can't then it tries again
        elif choice == '7':
            try:
                query = str(input("What year do you want to query, eg: 16 for 2016 - "))
                #Enters the year as shown in the example
                filterDataInflation(query)
            except:
                print("Invalid query")
                #checks if the value can be inputted without error; if it can't then it tries again

        elif choice == '8':
            Value = False
        # Checks which option the User picks and  runsthe respective function
        else:
            print("Invalid selection. Please choose a number between 1 and 6.")
        # if the user inputs an incorrect character it retries

    if Value == False and access == 1:
        print("Program Ended, Conclusions made")
    elif Value == False and access == 0:
        print("No access")
    #If the user doesnt have access ends the program
if __name__ == "__main__":
    main_menu()
    #If the file is being run directly (e.g., python main.py), then __name__ is set to "__main__").
    #If the file is being imported as a module (e.g., import main), then __name__ is set to "main" (the file name, without .py).