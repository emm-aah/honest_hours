import gspread
from google.oauth2.service_account import Credentials
import math

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSREAD_CLIENT.open("honest_hours")

employees = ["Emma", "Charlie", "Darren", "George", "Conor", "Lia"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def get_employee_name():
    """
    Get name from the user so we have whos data
    """
    while True:
        print("Please enter the details below:\n")
        employee_name = input("Name: ")
        worksheet_name = employee_name.capitalize()
        if validate_employee_name(worksheet_name):
            break

    return worksheet_name

def get_month_of_data(name):
    """
    Get the month from the user which the data corresponds to
    """
    while True:
        month = input("Month: ")
        month = month.capitalize()
        if validate_month(month, name):
            break
        
    return month

def get_holidays_taken():
    """
    Get number of holidays taken for the last month from the user 
    """
    while True:
        holidays_taken = input("Number of holiday days taken in the month given: ")
        if validate_integer(holidays_taken):
            print(f"Entered {holidays_taken} days.\n")
            break

    return holidays_taken


def get_over_hours():
    """
    Get number of holidays taken for the last month from the user 
    """
    while True:
        over_hours = input("Number of hours overtime worked in the month given: ")
        if validate_integer(over_hours):
            print(f"Entered {over_hours} hours.\n")
            break

    return over_hours
    

def validate_employee_name(name):
    """
    Validate name by checking it against employee names
    """
    try:
        if not name in employees:
            print(f'\n{name} is not an employee name.\n Please check the spelling and try again.\n')
            return False
    except ValueError as e:
        print(f"Invalid data: {e}.")
        return False
    
    return True
        
def validate_month(given_month, name):
    """
    Validate name by checking it against employee names
    """
    months_already_entered = SHEET.worksheet(name).col_values(1)
    try:
        if not given_month in MONTHS:
            print(f'\n{given_month} is not a month of the year.\nPlease check the spelling and try again.\n')
            return False
        if given_month in months_already_entered:
            print(f'Data has been entered for {given_month} already. Would you like to continue with a different month? Y/N')
            return False
    except ValueError as e:
        print(f"Invalid data: {e}")
        return False
    
    return True

def validate_integer(nums):
    """
    Validate name by checking it against employee names
    """
    try:
        [int(num) for num in nums]   
    except ValueError as e:
        print(f"Invalid data: {e}. Please make sure its an integer and try again.\n")
        return False
    
    return True


def update_sheet(employee, data, month,):
    """
    Update employees worksheet with the month, holidays and overhours entered.
    """
    print(f"Updating {employee}'s worksheet...")
    worksheet = SHEET.worksheet(employee)
    worksheet.append_row(data)
    print(f"Worksheet updated for {month}.")

def calculate_total_holidays(holidays, hours, employee):
    """
    Takes the holidays taken away from holidays left
    Gets the over time hours in terms of days and adds to holidays left
    returns holidays left
    """
    print("Calculating holidays left...")

    total_hrs_in_days = hours / 8
    worksheet = SHEET.worksheet(employee)
    holidays_column = worksheet.col_values(4)
    last_updated_holidays = holidays_column[-1]
    total_holidays = int(last_updated_holidays) + total_hrs_in_days - holidays
    print(f"You have a total of {total_holidays} left to take.")
    
    return total_holidays


def calculate_pay_for_overtime(data, month):
    """
    Takes over time hours and converts to wages
    """
    pay_out_for_month = data * 11.50
    print(f"Overtime pay for {month} is €{pay_out_for_month}")
    
    return pay_out_for_month

def calculate_all_overtime_owed(employee):
    """
    Adds together all over time owed since start of the year
    """
    worksheet = SHEET.worksheet(employee)
    overtime_values = worksheet.col_values(5)
    overtime_values = overtime_values[1:]
    overtime_integers = [int(overtime_value) for overtime_value in overtime_values]
    full_overtime_pay = sum(overtime_integers)
    print(f"You're overtime pay from January comes to €{full_overtime_pay}")

    return full_overtime_pay


def update_sheet(employee, data, month):
    """
    Update employees worksheet with the month, holidays and overhours entered.
    """
    print(f"Updating {employee}'s worksheet...")
    worksheet = SHEET.worksheet(employee)
    worksheet.append_row(data)
    print(f"Worksheet updated for {month}.")

def cash_out():
    """
    Offers employee chance to cash out their over time
    """
    print("Would you like to cash out your overtime?")
    answer = input("Y/N: ")
    answer.capitalize()
    if answer == "Y":
        print("Would you like to cash it out in full?")
        input("Y/N: ")



def validate_yes_no():
    """
    Validates for yes or no
    """
    

def main():
    """
    Calls the main functions
    """
    employee = get_employee_name()
    month = get_month_of_data(employee)
    holidays_str = get_holidays_taken()
    holidays = int(holidays_str)
    hours_str = get_over_hours()
    hours = int(hours_str)
    total_hols = calculate_total_holidays(holidays, hours, employee)
    total_holidays = int(total_hols)
    pay_out = calculate_pay_for_overtime(hours, month)
    pay = int(pay_out)
    data_str = [month, holidays, hours, total_holidays, pay]
    update_sheet(employee, data_str, month)
    calculate_all_overtime_owed(employee)
    



main()


