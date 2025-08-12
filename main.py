from data_module import (graphInflation,graphCrime,tableCrime,tableInflation)
import time
def main_menu():
    while True:
        print("\n=== Data Viewer Interface ===")
        print("1. View Crime dataset")
        print("2. View Inflation dataset")       
        print("3. View Crime visualisation")
        print("4. View Inflation visualisation")
        print("5. Exit")        


        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            tableCrime()
            time.sleep(1)
        elif choice == '2':
            tableInflation()
        if choice == '3':
           graphCrime()
        elif choice == '4':
            graphInflation()
        elif choice == '5':
            break
        else: print("Invalid selection. Please choose a number between 1 and 6.")
        
if __name__ == "__main__":
    main_menu()