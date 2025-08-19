from data_module import (graphInflation,graphCrime,tableCrime,tableInflation,filterDataCrime,filterDataInflation)
import time
def main_menu():
    time.sleep(1)
    print("For educational purposes the key is: U+1F511")
    time.sleep(1)
    permission = input("Do you have permission - What is your key?")
    
    Value = True
    if permission ==  "U+1F511":
        Value = True
        access = 1
    else:
        pass
        #Value = False
        #access = 0
    
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
        print("5. Filter Crime Dataset")
        time.sleep(0.1)
        print("6. Filter Inflation Dataset")
        time.sleep(0.1)
        print("7. Exit")        

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
            query = str(input("What year do you want to query, eg: 2013–14 - "))
            filterDataCrime(query)
        elif choice == '6':
            query = str(input("What year do you want to query, eg: 16 for 2016 - "))
            filterDataInflation(query)
        elif choice == '7':
            Value = False
    
        else:
            print("Invalid selection. Please choose a number between 1 and 6.")

    if Value == False and access == 1:
        print("Program Ended, Conclusions made")
    elif Value == False and access == 0:
        print("No access")
        
if __name__ == "__main__":
    main_menu()