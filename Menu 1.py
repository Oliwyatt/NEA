import time
import calendar
import Data

def ValueException():
    try:
        val = int(input(": "))
        return val
    except ValueError:
        print("Error that is not an accepted input.")


def main():
    choice = 0
    while choice != 9:
        print("Enter\n1) To view your calendar.\n2) To view your relaxation area.\n9) To exit.")
        while not(choice == 1 or choice == 2 or choice == 9):
            choice = ValueException()
        if choice == 1:
            calendar()
            choice = 0
        elif choice == 2:
            relaxation()
            choice = 0
        elif choice == 9:
            print("Goodbye !")
        else:
            print("Error, not an option.")

def calendar():
    print("Yay! Calendar!")
    #table.view()
    #personal or work or all
    #view, update or delete your calendar
    #search for specific day or show today

def relaxation():
    print("Mmmm, Relaxation")
    # view top shows (possibly)
    # view shows watching
    # upadte and delete shows watching
    # rate a show
    # maybe link account? (API?)
    


if __name__ == "__main__":
    Data.Initialise
    main()
