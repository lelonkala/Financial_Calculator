# Financial_Calculator
This Python program allows users to perform financial calculations for bonds and investments. Users can choose between calculating bond repayments and investment returns with either simple or compound interest. The program is designed to handle user input case-insensitively and provides appropriate error messages for invalid inputs.

# Features
Bond Calculation: Calculate monthly repayments on a home loan.
Investment Calculation: Calculate the total amount after a given period with simple or compound interest.
Case-insensitive Input: The program handles user input case-insensitively for ease of use.
Loop for Multiple Calculations: Users can choose to perform multiple calculations in a single session.
***New line***

# Usage
Clone the repository:
git clone https://github.com/lelonkala/financial_calculator.git
cd financial_calculator
# Run the program:
python financial_calculator.py

# Calculation Details
Bond Calculation
Inputs:
        Present value of the house.
        Annual interest rate (percentage).
        Number of months to repay the bond.
        Formula:
repayment
=
𝑖
⋅
𝑃
1
−
(
1
+
𝑖
)
−
𝑛
repayment= 
1−(1+i) 
−n
 
i⋅P

 

where:
𝑃
P is the present value of the house.
𝑖
i is the monthly interest rate (annual interest rate divided by 12).
𝑛
n is the number of months to repay the bond.


Investment Calculation
Inputs:
Amount of money deposited.
Annual interest rate (percentage).
Number of years for investment.
Type of interest (simple or compound).
Formulas:
Simple Interest:
𝐴
=
𝑃
⋅
(
1
+
𝑟
⋅
𝑡
)
A=P⋅(1+r⋅t)
Compound Interest:
𝐴
=
𝑃
⋅
(
1
+
𝑟
)
𝑡
A=P⋅(1+r) 
t
 
where:
𝑃
P is the amount deposited.
𝑟
r is the annual interest rate (entered as a percentage and divided by 100).
𝑡
t is the number of years for investment.
𝐴
A is the total amount after the interest has been applied.
# Example
Bond Calculation
Choose a calculation:
1. Bond
2. Investment
Enter your choice (Bond/Investment): bond
Enter the present value of the house: 100000
Enter the annual interest rate (percentage): 7
Enter the number of months to repay the bond: 120
The monthly repayment amount is: 1160.46

Investment Calculation
Choose a calculation:
1. Bond
2. Investment
Enter your choice (Bond/Investment): investment
Enter the amount of money you are depositing: 10000
Enter the interest rate (percentage): 8
Enter the number of years you plan on investing for: 20
Enter the type of interest (simple/compound): compound
The total amount after 20 years with compound interest is: 46609.57

# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Contributing
Contributions are welcome! Please open an issue or submit a pull request.

# Author
Nombulelo Prudence Nkala
lelonkala
