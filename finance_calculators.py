#financial calculator of a small company that allows the user to access two calculators by Nombulelo Nkala, July 2024.
import math

#main function with a while loop, while the user still wants to calculate 
def main():
    while True:
        print("Choose a calculation:")
        print("1. Bond")
        print("2. Investment")
        
        #user input converted to lower case
        choice = input("Enter your choice (Bond/Investment): ").strip().lower()

#user validation
        if choice == "bond":
            calculate_bond()                    #calling the bond calculator
        elif choice == "investment":
            calculate_investment()              #calling the investment calculator
        else:
            print("Invalid input. Please enter 'Bond' or 'Investment'.") #error message output

#checking if the user wants to do another calculation
        calc_again = input("Do you want to perform another calculation? (yes to continue, any other key to exit): ").strip().lower()
        if calc_again != "yes":
            break
        
#function to calculate bond
def calculate_bond():
    try:
        P = float(input("Enter the present value of the house: "))
        annual_interest_rate = float(input("Enter the annual interest rate (percentage): "))
        n = int(input("Enter the number of months to repay the bond: "))
        
        i = (annual_interest_rate / 100) / 12
        repayment = (i * P) / (1 - math.pow(1 + i, -n))
        
        print(f"The monthly repayment amount is: {repayment:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for the present value, interest rate, and number of months.")

#function to calculate investment
def calculate_investment():
    try:
        P = float(input("Enter the amount of money you are depositing: "))
        annual_interest_rate = float(input("Enter the interest rate (percentage): "))
        t = int(input("Enter the number of years you plan on investing for: "))
        
        interest_type = input("Enter the type of interest (simple/compound): ").strip().lower()
        
        r = annual_interest_rate / 100
        
        if interest_type == "simple":
            A = P * (1 + r * t)
            print(f"The total amount after {t} years with simple interest is: {A:.2f}")
        elif interest_type == "compound":
            A = P * math.pow((1 + r), t)
            print(f"The total amount after {t} years with compound interest is: {A:.2f}")
        else:
            print("Invalid input. Please enter 'simple' or 'compound' for the type of interest.")
    except ValueError:
        print("Invalid input. Please enter numeric values for the deposit amount, interest rate, and number of years.")

if __name__ == "__main__":
    main()
