import gspread
from google.oauth2.service_account import Credentials

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
            print(f"Entered {worksheet_name}\n")
            break

    return worksheet_name

def get_month_of_data():
    """
    Get the month from the user which the data corresponds to
    """
    while True:
        month = input("Month: ")
        month = month.capitalize()
        if validate_month(month):
            print(f"Entered {month}\n")
            break
        
    return month

def get_holidays_taken():
    """
    Get number of holidays taken for the last month from the user 
    """
    while True:
        holidays_taken = input("Number of holiday days taken in the month given: ")
        if validate_holidays_taken(holidays_taken):
            print(f"Entered {holidays_taken} days.\n")
            break

    return holidays_taken


def get_over_hours():
    """
    Get number of holidays taken for the last month from the user 
    """
    while True:
        over_hours = input("Number of hours overtime worked in the month given: ")
        if validate_over_hours(over_hours):
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
        
def validate_month(given_month):
    """
    Validate name by checking it against employee names
    """
    try:
        if not given_month in MONTHS:
            print(f'\n{given_month} is not a month of the year.\nPlease check the spelling and try again.\n')
            return False
    except ValueError as e:
        print(f"Invalid data: {e}")
        return False
    
    return True

def validate_holidays_taken(nums):
    """
    Validate name by checking it against employee names
    """
    try:
        [int(num) for num in nums]   
    except ValueError as e:
        print(f"Invalid data: {e}. Please make sure its an integer and try again.\n")
        return False
    
    return True

def validate_over_hours(nums):
    """
    Validate name by checking it against employee names
    """
    try:
        [int(num) for num in nums]   
    except ValueError as e:
        print(f"Invalid data: {e}. Please make sure its an integer and try again.\n")
        return False
    
    return True

def update_sheet(employee, data, month):
    """
    Update employees worksheet with the month, holidays and overhours entered.
    """
    print(f"Updating {employee}'s worksheet...")
    worksheet = SHEET.worksheet(employee)
    worksheet.append_row(data)
    print(f"Worksheet updated for {month}.")


    

def main():
    """
    Calls the main functions
    """
    employee = get_employee_name()
    month = get_month_of_data()
    holidays = get_holidays_taken()
    hours = get_over_hours()
    data_str = [month, int(holidays), int(hours)]
    update_sheet(employee, data_str, month)



main()


