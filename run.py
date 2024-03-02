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

def get_employee_name():
    """
    Get name from the user so we have whos data
    """
    while True:
        print("Please enter the details below:\n")
        employee_name = input("Name: \n")
        worksheet_name = employee_name.capitalize()
        if validate_employee_name(worksheet_name):
            print(f"Entered {worksheet_name} ")
            break

    return worksheet_name
    

def validate_employee_name(name):
    """
    Validate name by checking it against employee names
    """
    try:
        if not name in employees:
            print(f'{name} is not an employee name.\n Please check the spelling and try again.\n')
            return False
    except ValueError as e:
        print(f"Invalid data: {e}")
        return False
    
    return True
        





get_employee_name()


