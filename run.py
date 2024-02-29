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

def get_data(data_type):
    """
    Get data for variable , validate data and return in string form
    """
    print(f"Please enter {data_type} for the relevant employee below.")
    print("This should be in numerical form.")
    emma = input("Emma: ")
    charlie = input("Charlie: ")
    darren = input("Darren: ")
    george = input("George: ")
    conor = input("Conor: ")
    data_str = [str(holidays_emma), str(holidays_charlie), str(holidays_darren), str(holidays_george), str(holidays_conor)]
    validate_data(data_str)
    return data_str


def validate_data(values):
    """
    This function validates the data 
    """
    try:
        [int(value) for value in values]
    except ValueError as e:
        print(f'Invalid answer: {e}. Please try again\n')

def main():
    """
    Calls the main functions
    """
    get_data("holidays taken")
    get_data("over hours worked")

