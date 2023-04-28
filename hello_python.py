# for x in range (1 , 4, 2):
#     print (x)


   
# word= "FINTECH STICKS"
# for x in word:
#     print (x.lower())


# shopping_spree_charges = [ 100 , 200 , 300 , 400 , 500 , 600 , 700 , 800 , 900 , 1000 ]
# spending_total= 0

# for x in shopping_spree_charges:
#     spending_total += x
#     print (spending_total)

# def process_claims(claims):
#     total_claims= sum(claims)
#     total_payout= total_claims * 0.3
#     return total_payout

# weekly_claims = [5000, 1000, 8000, 10000, 3000, 3500]
# print(process_claims(weekly_claims))
# HINT: Present Value = Future Value (Face Value of the Loan) / (1 + annual_discount_rate/12) ** remaining_months 
# def price_this_home (home_price, expected_sale_price,hurdle_rate,holding_months):
#     present_value= expected_sale_price/(1+(hurdle_rate/12))**holding_months
#     if present_value>home_price:
#         print("Buy this one, junior analyst! It's worth more than it's selling for.")
#         # Otherwise, take a pass:
#     elif present_value < home_price:
#         print("Don't buy this, as it's offered at a price higher than what it's worth.")
#     # Bonus! The edge case:
#     elif present_value == home_price:
#         print(
#             "Breakeven case! You can expect to earn exactly your hurdle rate on this deal."
#         )
#     net_present_value = present_value - home_price
#     return net_present_value
    

# npv = price_this_home(
#     home_price=100000, expected_sale_price=120000, hurdle_rate=0.10, holding_months=36
# )

# # Print the npv
# print(f"The Expected Profit is: {npv}")

# principle = 103208.56
# interest_rates = [.103, .067, .099, .10]
# interest_rates_total= 0

# for rate in interest_rates:
#     interest = rate * principle
#     interest_rates_total= interest_rates_total + interest
#     print("Your interest will be: ", interest)
# print("Your total interest will be: ", interest_rates_total)    

# stock_price = 30
# dividend_yields = [0.035, 0.040, 0.072, 0.012, 0.052]

# total_dividend_income = 0

# for dividend_yield in dividend_yields:
#     total_dividend_income += stock_price * dividend_yield
    
# print (total_dividend_income)

# import csv
# import pathlib

# csvpath = pathlib.Path("quarterly_data.csv")

# with open(csvpath) as csvfile:
#     data= csv.reader(csvfile)
#     counter= 0
#     for row in data:
#         counter += 1
#         print(counter)
#         print(row)


# equity_funding = [
#     {"Company": "CryptoVisors", "Amount": 200000, "Series": "A"},
#     {"Company": "Flutterwave", "Amount": 65000000, "Series": "D"},
#     {"Company": "nCino", "Amount": 80000000, "Series": "D"},
#     {"Company": "Privacy.com", "Amount": 10000000, "Series": "B"},
# ]

# big_raisers = []

# for equity in equity_funding:
#     if equity["Amount"]> 50000000:
#         big_raisers.append(equity.values())

# header = ["Company", "Amount", "Series"]

# csvpath= pathlib.Path("big_raisers.csv")
# with open(csvpath,"w", newline='') as csvfile:
#     csvwriter= csv.writer(csvfile)
#     csvwriter.writerow(header)
#     for row in big_raisers:
#         csvwriter.writerow(row)
    

# Initial imports
# import csv
# from pathlib import Path


# # This function loads a CSV file from the filepath defined in `csvpath`
# def load_csv(csvpath):
#     with open(csvpath, "r") as csvfile:
#         data = []
#         csvreader = csv.reader(csvfile, delimiter=",")

#         # Skip the CSV Header
#         next(csvreader)

#         # Read the CSV data
#         for row in csvreader:
#             data.append(row)
#     return data


# # This function loads a CSV file with the list of banks and available loans information
# # from the file defined in `file_path`
# def load_bank_data(file_path):
#     csvpath = Path(file_path)
#     return load_csv(csvpath)


# # This function implements the following user story:
# # As a lender,
# # I want to calculate the monthly debt-to-income ratio
# # so that we can assess the ability to pay of the borrower
# def calculate_monthly_debt_ratio(monthly_debt_payment, monthly_income):
#     monthly_debt_ratio = int(monthly_debt_payment) / int(monthly_income)
#     return monthly_debt_ratio


# # @TODO Define a function that implements the following user story:
# # As a lender,
# # I want to calculate the loan-to-value ratio
# # so that we can evaluate the risk of lending money to the borrower
# # @TODO Implement loan_to_value_ratio calculation
# def calculate_loan_to_value_ratio(loan_amount, home_value):
#     if loan_amount<= 0 or home_value<= 0:
#         return "Please enter a positive number"
#     else:
#         loan_to_value_ratio= loan_amount/home_value

#     return loan_to_value_ratio

    



# # This function is the main execution point of the application. It triggers all the business logic.
# def run():
#     # Set the file path of the CSV file with the banks and loans information
#     file_path = Path("./data/daily_rate_sheet.csv")
#     # Load the latest Bank data
#     bank_data = load_bank_data(file_path)

#     # This print statement will display all of the bank data that is provided.
#     # print(f"bank_data: {bank_data}")

#     # The following lines, set the applicant's information and implements the following user story:
#     # As a customer,
#     # I want to provide my financial information
#     # so that I can apply for a loan
# from utils import fileio
# credit_score = 750
# debt = 5000
# income = 20000
# loan_amount = 100000
# home_value = 210000

#     # Calculate the Monthly Debt Ratio
# monthly_debt_ratio = fileio.calculate_monthly_debt_ratio(debt, income)

#     print(f"The monthly deb to income ratio is {monthly_debt_ratio:.02f}.")

#     # Calculate the Loan to Value
# loan_to_value_ratio = fileio.calculate_loan_to_value_ratio(loan_amount, home_value)

#     print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")



# run()

# Initial imports
# import csv
# from pathlib import Path


# # This function loads a CSV file from the filepath defined in `csvpath`
# def load_csv(csvpath):
#     with open(csvpath, "r") as csvfile:
#         data = []
#         csvreader = csv.reader(csvfile, delimiter=",")

#         # Skip the CSV Header
#         next(csvreader)

#         # Read the CSV data
#         for row in csvreader:
#             data.append(row)
#     return data


# # This function loads a CSV file with the list of banks and available loans information
# # from the file defined in `file_path`
# def load_bank_data(file_path):
#     csvpath = Path(file_path)
#     return load_csv(csvpath)


# # As a lender,
# # I want to calculate the monthly debt-to-income ratio
# # so that we can assess the ability to pay of the borrower
# def calculate_monthly_debt_ratio(monthly_debt_payment, monthly_income):
#     monthly_debt_ratio = int(monthly_debt_payment) / int(monthly_income)
#     return monthly_debt_ratio


# # As a lender,
# # I want to calculate the loan-to-value ratio
# # so that we can evaluate the risk of lending money to the borrower
# def calculate_loan_to_value_ratio(loan_amount, home_value):
#     loan_to_value_ratio = int(loan_amount) / int(home_value)
#     return loan_to_value_ratio

# # @TODO Define a function that implements the following user story:
# # As a lender,
# # I want to filter the bank list by checking the customer's desired loan against the bank's maximum loan size
# # so that we can know which banks offer the loan amount requested by the customer
# def filter_max_loan_size(loan_amount, bank_list):
#     approved_banks_loan_size=[]
#     for bank in bank_list:
#         if loan_amount<= int(bank[1]):
#             approved_banks_loan_size.append(bank)




# # @TODO Define a function that implements the following user story:
# # As a lender,
# # I want to filter the bank list by checking if the customer's credit score is equal to or greater than the minimum allowed credit score defined by the bank
# # so that we can know which banks are willing to offer a loan to the customer
# def filter_credit_score(credit_score, bank_list):
#  approved_banks_credit_size=[]
#  for bank in bank_list:
#   if credit_score>= int(bank[4]):
#    approved_banks_credit_size.append(bank)


# # @TODO Define a function that implements the following user story:
# # As a lender,
# # I want to filter the bank list by comparing if the customer's debt-to-income is equal to or less than the maximum debt-to-income ratio allowed by the bank
# # so that we can assess if the customer will have payment capacity according to the bank's criteria
# def filter_debt_to_income(monthly_debt_ratio, bank_list):
#  approved_banks_dt_size=[]
#  for bank in bank_list:
#   if monthly_debt_ratio<= int(bank[3]):
#    approved_banks_dt_size.append(bank)



# # @TODO Define a function that implements the following user story:
# # As a lender,
# # I want to filter the bank list by checking if the customer's loan-to-value is equal to or less than the maximum loan-to-value ratio allowed by the bank
# # so that we assess if the customer's home value is worth as an asset to secure the loan
# def filter_loan_to_value(loan_to_value_ratio, bank_list):
#  approved_banks_ltv_size=[]
#  for bank in bank_list:
#   if loan_to_value_ratio<= int(bank[2]):
#    approved_banks_ltv_size.append(bank)


# # This function implements the following user story:
# # As a customer,
# # I want to know what are the best loans in the market according to my financial profile
# # so that I can choose the best option according to my needs
# def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
#     # Calculate the monthly debt ratio
#     monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
#     print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

#     # Calculate loan to value ratio
#     loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
#     print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

#     # Run qualification filters
#     bank_data_filtered = filter_max_loan_size(loan, bank_data)
#     bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
#     bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
#     bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

#     print(f"Found {len(bank_data_filtered)} qualifying loans")

#     return bank_data_filtered


# # This function is the main execution point of the application. It triggers all the business logic.
# def run():
#     # Set the file path of the CSV file with the banks and loans information
#     file_path = Path("./data/daily_rate_sheet.csv")
#     # Load the latest Bank data
#     bank_data = load_bank_data(file_path)

#     # This print statement will display all of the bank data that is provided.
#     # print(f"bank_data: {bank_data}")

#     # The following lines, set the applicant's information and implements the following user story:
#     # As a customer,
#     # I want to provide my financial information
#     # so that I can apply for a loan
#     credit_score = 750
#     debt = 5000
#     income = 20000
#     loan_amount = 100000
#     home_value = 210000

#     # Find qualifying loans
#     qualifying_loans = find_qualifying_loans(
#         bank_data, credit_score, debt, income, loan_amount, home_value
#     )

#     # Print the list of qualifying loans
#     print(qualifying_loans)


# run()

# san_francisco = {
#     "has_multiple_bridges": True,
#     "state": "California",
#     "tallest_building": "SalesForce Building",
#     "median_house_price": 1610000,
#     "notable_attractions": ["Alcatraz", "Golden Gate Bridge", "Fisherman's Wharf"],
# }

# Re-create the content of the commented out `san_francisco` dictionary by using bracket notation to manually add each of the key-value pairs (including nested objects).
# san_francisco = {

# }

# san_francisco["state"] = "California"
# san_francisco["has_multiple_bridges"] = True
# san_francisco["tallest_building"] = "SalesForce Building"
# san_francisco["median_house_price"] = 1610000
# san_francisco["notable_attractions"] = ["Alcatraz", "Golden Gate Bridge", "Fisherman's Wharf"]

# # Print the manually modified `san_francisco` dictionary and confirm the contents match the commented out version.
# print(san_francisco)


# # Use the `from` keyword to import the `shows` dictionary from the `show_data.py` file
# from show_data import shows
# drama = shows["genre"]["drama"]
# comedy = shows["genre"]["comedy"]
# talk = shows["genre"]["talk"]


# # QUESTION 1: Is the Walking Dead still running?
# print(drama["the_walking_dead"]["still_running"])

# # QUESTION 2: Who hosts the Daily Show (talk)?
# print(talk["the_daily_show"]["host"])

# # QUESTION 3: Who does Will Arnett play in Arrested Development (comedy)
# print(comedy["arrested_development"]["cast"][2]["character"])

# # QUESTION 4: Who does Peter Dinklage play in Game of Thrones (drama)?
# print()

# # QUESTION 5: Who plays Dexter in Dexter (drama) and who plays Dexter in Dexter's Lab (kids)?
# # HINT: You can print multiple items at once by using a comma like this: print(thing1, thing2)
# print()

# # QUESTION 6: Who are the main characters of the Office (comedy) (not the actors, but the actual character names)?
# # YOUR CODE HERE!

# # QUESTION 7: List the main cast of Dexter (drama) (the actors, not the characters)
# # YOUR CODE HERE!


# # QUESTION : List the American Idol Judges
# # YOUR CODE HERE!

# # QUESTION 9: What are the show names of the Impractical Jokers (comedy)
# # Hint: You will need to use a loop for this one. You may not simply log the entire list, but must log each name individually
# # YOUR CODE HERE!

# # We've declared this list for you
# # num_list = [2, 65, 3, 7, 39, 22, 11, 94, 299, 9, 20, 21, 51, 37]

# # # Iterate through the provided `num_list` and print out every number in the list
# # for num in num_list:
# #     print(num)
# # print("All numbers")
# # # YOUR CODE HERE!

# # # Iterate through the provided `num_list` and create an if statement to print every number greater than 50
# # print("Numbers greater than 50:")

# # # YOUR CODE HERE!

# # # Iterate through the provided `num_list` to print the index of the first occurrence of the number 11.
# # print("Index of first occurrence of the number 11:")
# # index = 0
# # # YOUR CODE HERE!

# # # Iterate through the provided `num_list` and print the sum of all the numbers.
# # print("Sum of all numbers:")
# # sum = 0
# # # YOUR CODE HERE!

# # fruits = [
# #   "Apple", "Orange", "Banana", "Pomelo", "Apple", "Kiwi", "Peach", "Banana", "Grape", "Tomato",
# #   "Kiwi", "Apple", "Watermelon", "Lemon", "Pomelo", "Apple", "Banana", "Peach", "Apricot", "Grape"]

# # # Iterate through the provided `fruits` list and print the number of times "Apple" appears in the list.
# # print("Number of times 'Apple' appears in the list:")
# # for fruit in fruits:
# #     print(fruit)
# # count = 0
# # # YOUR CODE HERE!


# # Define a function "warble" that takes in a string as an argument, adds " arglebargle" to the end of it, and returns the result.
# def warble(word) :
#     print(word + "arglebargle")

# # Print the result of calling your "warble" function with the argument "hello".
# warble("hello")

# # Define a function "wibble" that takes a string as an argument, prints the argument, prepends "wibbly " to the argument, and returns the result


# # Print the result of calling your "wibble" function with the argument "bibbly"


# # Define a function "print_sum" that takes in two numbers as arguments and prints the sum of those two numbers.
# def print_sum(num1,num2):
#     print(num1 + num2)

# Define a function "return_sum" that takes in two numbers as arguments and returns the sum of those two numbers


# Define a function "triple_sum" that takes in 3 arguments and returns the sum of those 3 numbers.


"""
Define a function "dance_party" that takes in a string as an argument,
then prints "dance!", then updates the string by calling "wibble" function
with that argument, followed by "warble" function with that argument,
then returns the updated stringdef dance_party(string_param):

"""

# Print the result of calling your "dance_party" function with your name as the argument


"""This is a basic ATM Application.

This is a program consists of the basic actions of an ATM.

Example:
    $ python app.py
"""

# accounts = [
#     {
#     "pin": 123456,
#     "balance" : 1436.19},
#     {
#     "pin" : 246802,
#     "balance": 3571.87},
#     {
#     "pin": 135791,
#     "balance" : 543.79},
#     {
#     "pin" : 123987,
#     "balance": 25.89},
#     {
#     "pin" : 269731,
#     "balance": 3278.42}
# ]

# # Create the `login` function for the ATM application.
# # The login function will take in a user PIN.
# # The function should validate the PIN against this list of `accounts`.
# # If the PIN is validated, the function should return the account's balance.

# def login(pin):
#     for account in accounts:
#         if int(pin) == account["pin"]:
#             account_balance = account['balance']
#             print(f"Your account balance is ${account_balance}")
#     return account_balance


# # Create the `check_balance` function for the ATM application.
# # WRITE YOUR LOGIC HERE!
# # YOUR CODE HERE!
# def check_balance(pin):
#     for account in accounts:
#         if int(pin) == account["pin"]:
#             account_balance = account['balance']
#             if account_balance>0:
#              print(f"Your account balance is ${account_balance}")
#             else:
#              print("Your account balance is $0.00")
#     return account_balance



# # Create the `make_deposit` function for the ATM application.
# # WRITE YOUR LOGIC HERE!
# # YOUR CODE HERE!
# def make_deposit(pin,amount):
#     for account in accounts:
#         if int(pin) == account["pin"]:
#             account["balance"]= account["balance"] + int(amount)
#             print(account["balance"])
#             return account["balance"]





# # Create the `make_withdrawal` function for the ATM application.
# # WRITE YOUR LOGIC HERE!
# # YOUR CODE HERE!

# def make_withdrawal(pin,amount):
#     for account in accounts:
#         if int(pin) == account["pin"]:
#             account["balance"]= account["balance"] - int(amount)
#             print(account["balance"])
#             return account["balance"]

# make_withdrawal(123456,100)


# import pandas as pd
# from pathlib import Path

# cvspath= Path("../Python_Project/sales.csv")
# sales_dataframe= pd.read_csv(cvspath)
# print(sales_dataframe.head())

# import pandas as pd
# import numpy as np

# apple_df = pd.DataFrame({"AAPL": [72.27, np.nan, 74.39, np.nan, 75.94, 76.93,np.nan, 78.74, np.nan, 79.81, np.nan, 79.53, np.nan, 79.56, 79.49]})

# print(apple_df.isnull().sum())

# import pandas as pd
# stock_abc = pd.DataFrame({"close" : [11.25, 11.98, 10.74, 11.16, 12.35, 12.87, 13.03, 13.14, 13.37, 12.99]})

# daily_returns= stock_abc.pct_change()
# print(daily_returns.sum())


# # Import the required libraries and dependencies
# import pandas as pd
# import requests
# import json

# # Set the Ripple endpoint
# ltc_url = "https://api.alternative.me/v2/ticker/Litecoin/"

# # Fetch the current Ripple price
# ltc_response = requests.get(ltc_url).json()

# # Display response data
# print(json.dumps(ltc_response, indent=4, sort_keys=True))

import fire
import questionary
import sqlalchemy
import pandas as pd
from pathlib import Path

# Create a temporary sqlite database
database_connection_string = 'sqlite:///cruddy_database.db'

# Create an engine to interact with the database
engine = sqlalchemy.create_engine(database_connection_string)


"""CREATE

The CREATE operation creates a new table in the database using the given DataFrame.
The table is replaced by the new data if it already exists.
"""


def create_table(engine, table_name, table_data_df):
    table_data_df.to_sql(table_name, engine, index=False, if_exists='replace')


"""READ

The READ operation will read the entire table from the database into a new DataFrame.
Then it will print the DataFrame.
"""


def read_table(engine, table_name):
    results_dataframe = pd.read_sql_table(table_name, con=engine)
    print(f"{table_name} Data:")
    print(results_dataframe)


"""UPDATE

In this section, you will complete the UPDATE operation.

1. Under the “UPDATE” docstring, create a function named `update_data` that accepts the following parameters: `engine`, `table_name`, `column`, `old_value`, and `new_value`.

2. Inside the `update-data` function, write a SQL `UPDATE` statement in the form of an f-string. This statement should use the function parameters to update data in the table in the database. Be sure to do the following:

    * In the `UPDATE` statement, include the `UPDATE`, `SET`, and `WHERE` SQL keywords.

    * Include the statement that calls the engine to execute the `UPDATE` statement.
"""

def update_data(engine, table_name, column, old_value, new_value):
    update_query= """
    UPDATE {table_name}
    SET {column} = {new_value}
    WHERE {column}= {old_value};

    """
    engine.execute(update_query)




"""DELETE

In this section, you will complete the DELETE operation.

3. Under the “DELETE” docstring, create a function named `delete_data` that accepts the following parameters: `engine`, `table_name`, `column`, and `value`.

4. Inside the `delete_data` function, create a SQL `DELETE` statement in the form of an f-string. This statement should use the function parameters to delete data from the table in the database. Be sure to do the following:

    * In the `DELETE` statement, include the `DELETE FROM` and `WHERE` SQL keywords.

    * Include the statement that calls the engine to execute the `DELETE` statement.
"""

def delete_data(enigne, table_name, column, value):
    delete_query= """
    DELETE FROM {table_name}
    WHERE {column}={value};

    """
    engine.execute(delete_query)


def run():
    print("Generating test data for the database...")
    # Create a test DataFrame
    stocks_dataframe = pd.DataFrame({'AAPL': [1, 2], 'GOOG': [3, 4]})
    # Create the database table called 'stocks'
    create_table(engine, 'stocks', stocks_dataframe)

    cruddy_cli_running = True

    while cruddy_cli_running:
        choice = questionary.select(
            "What do you want to do?",
            choices=["Read", "Update", "Delete", "Quit"]
        ).ask()

        if choice == "Read":
            print(f"Available Tables: {engine.table_names()}")
            table_name = questionary.text("Which table would you like to read?").ask()
            read_table(engine, table_name)
        elif choice == "Update":
            # 1. Prompt the user for a table to update.
            table_name = questionary.text("What table would you like to update?").ask()
            # 2. Prompt the user for column to update.
            column = questionary.text("What column would you like to update?").ask()
            # 3. Prompt the user for the old value to find.
            old_value = questionary.text("What is the old value that you want to update?").ask()
            # 4. Prompt the user for the new value.
            new_value = questionary.text("What is the new value that you want to update?").ask()
            # 5. Call the UPDATE operation
            update_data(engine, table_name, column, old_value, new_value)
        elif choice == "Delete":
            # 1. Prompt the user for a table.
            table_name = questionary.text("What table would you like to delete data from?").ask()
            # 2. Prompt the user for the column.
            column = questionary.text("What column is the data in?").ask()
            # 3. Prompt the user for  value to find.
            value = questionary.text("What is the value to delete?").ask()
            # 4. Call the delete operation
            delete_data(engine, table_name, column, value)
        elif choice == "Quit":
            cruddy_cli_running = False
            print("Thank you for using the CRUDdy CLI! Goodbye!")


if __name__ == "__main__":
    fire.Fire(run)
