# calculate the growth of a bank account over time with a given interest rate

#Function to calculate the growth of a bank account over time with a given interest rate
def calculate_bank_growth(deposit, interest_rate, years):
    print("Year\tAmount")
    for year in range(1, years+1):
        deposit *= (1 + interest_rate / 100)
        print(f"{year}\t{deposit:.2f} kr")

# Ask the user for the principal, interest rate and number of years
deposit_amount = 100000 #initial deposit
interest_rate = float(input("Enter the interest rate (%): "))
years = 5 #number of years

# Call the function
calculate_bank_growth(deposit_amount, interest_rate, years)
