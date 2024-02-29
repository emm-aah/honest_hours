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

holidays_taken = SHEET.worksheet('holidays_taken')

data = holidays_taken.get_all_values()

def get_holidays_taken():
    """
    Get data for holidays taken that month
    """
    print("Please enter holidays taken for the relevant employee below")
    print("This should be in numerical form")
    holidays_emma = input("Emma: ")
    holidays_charlie = input("Charlie: ")
    holidays_darren = input("Darren: ")
    holidays_george = input("George: ")
    holidays_conor = input("Conor: ")
    
    print(f"Emma took {holidays_emma}. Charlie took {holidays_charlie}. Darren took {holidays_darren}. George took {holidays_george}. Conor took {holidays_conor}.")
    holidays_str = [str(holidays_emma), str(holidays_charlie), str(holidays_darren), str(holidays_george), str(holidays_conor)]
    validate_data(holidays_str)
    return holidays_str

def get_over_hours():
    """
    Get data for over hours worked this month
    """
    print("Please enter the over hours worked by the relevant employee below")
    print("This should be in numerical form")
    hours_emma = input("Emma: ")
    hours_charlie = input("Charlie: ")
    hours_darren = input("Darren: ")
    hours_george = input("George: ")
    hours_conor = input("Conor: ")
    
    print(f"Emma worked {hours_emma}.\n Charlie worked {hours_charlie}.\n Darren worked {hours_darren}.\n George worked {hours_george}.\n Conor worked {hours_conor}.")
    hours_str = [str(hours_emma), str(hours_charlie), str(hours_darren), str(hours_george), str(hours_conor)]
    validate_data(hours_str)
    return hours_str


def validate_data(values):
    try:
        [int(value) for value in values]
    except ValueError as e:
        print(f'Invalid answer: {e}. Please try again\n')


get_holidays_taken()
get_over_hours()

