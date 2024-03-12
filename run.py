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
MONTHS = ["January", "February", "March", "April", "May",
          "June", "July", "August", "September", "October",
          "November", "December"]
yes_no = ["y", "n", "yes", "no"]
full_month = ["f", "m", "full", "month"]


def get_employee_name():
    """
    Get name from the user so we have whos data
    """
    while True:
        print("Welcome to Honest Hours!\n")
        print("Please enter the details below:\n")
        print("Example: \nName: Mary, Month: January")
        print("Holidays taken: 5, Over hours worked: 18\n")
        employee_name = input("Name: \n")
        employee = employee_name.capitalize()
        if validate_word_in_list(employee, employees, "list of employees"):
            break

    return employee


def get_month_of_data(name):
    """
    Get the month from the user which the data corresponds to
    """
    while True:
        month = input("Month: \n")
        month = month.capitalize()
        if validate_month(month, name):
            break
    return month


def get_month_data(question, month):
    """
    Get number of holidays taken and
    overhours worked for the last month from the user.
    """
    while True:
        answer = input(f"How many {question} in {month}: \n")
        if validate_integer(answer):
            int_answer = int(answer)
            break

    return int_answer


def validate_word_in_list(word, given_list, list_name):
    """
    Validate by checking if a word and then checking if the word is in the list
    """
    try:
        check = word + ""
        if not word in given_list:
            print(f"{word} is not in {list_name}.")
            print("Please check the spelling and try again.\n")
            return False
    except ValueError:
        print("The answer was not given in the form of a word.")
        print("Please try again")
        return False
    return True


def get_column_values(name, col_num):
    """
    gets list of column values from  employee worksheet
    """
    worksheet = SHEET.worksheet(name)
    data_list = worksheet.col_values(col_num)

    return data_list


def validate_month(given_month, name):
    """
    Validate name by checking it against employee names
    """
    months_already_entered = get_column_values(name, 1)
    try:
        given_month + ""
        if not given_month in MONTHS:
            print(f"{given_month} is not a month of the year.")
            print("Please check the spelling and try again.\n')
            return False
        if given_month in months_already_entered:
            print(f'Data has been entered for {given_month} already.')
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
    except ValueError:
        print(f"Please make sure your answer is given as a number.")
        print("Try again.\n")
        return False

    return True


def calculate_holidays_without_overtime(name, holidays_taken):
    """
    gets holiday days taken and takes it away from total holidays
    """
    taken_holidays = get_column_values(name, 2)
    taken_holidays = taken_holidays[1:]
    all_hols_int = [float(taken_holiday) for taken_holiday in taken_holidays]
    all_taken_holidays = sum(all_hols_int) + holidays_taken
    holidays_left_without_ot = 25 - all_taken_holidays

    return holidays_left_without_ot


def calculate_total_holidays(holidays_taken, hours, name):
    """
    Takes the holidays taken away from holidays left
    Gets the over time hours in terms of days and adds to holidays left
    returns holidays left
    """
    print("Calculating holidays left...\n")

    holidays_left_without_ot =
    calculate_holidays_without_overtime(name, holidays_taken)
    holidays = get_column_values(name, 4)
    total_hrs_in_days = hours / 8
    last_updated_holidays = holidays[-1]
    total_holidays = float(last_updated_holidays)
    + total_hrs_in_days - holidays_taken
    print(f"You have a total of {holidays_left_without_ot} holidays left")
    print("or {total_holidays} holidays with your overtime included.")

    return total_holidays


def calculate_pay_for_overtime(data, month):
    """
    Takes over time hours and converts to wages
    """
    pay_out_for_month = data * 11
    print(f"Overtime pay for {month} is €{pay_out_for_month}\n")

    return pay_out_for_month


def calculate_all_overtime_owed(name):
    """
    Adds together all over time owed since start of the year
    """
    overtime_values = get_column_values(name, 5)
    overtime_values = overtime_values[1:]
    overtime_integers = [int(overtime_value) for
                         overtime_value in overtime_values]
    full_overtime_pay = sum(overtime_integers)
    print(f"Your overtime pay from January comes to €{full_overtime_pay}\n")

    return full_overtime_pay


def update_sheet(employee, data):
    worksheet = SHEET.worksheet(employee)
    worksheet.append_row(data)


def updating_worksheet(employee, data, month):
    """
    Update employees worksheet with the month, holidays and overhours entered.
    """
    print(f"Updating {employee}'s worksheet...\n")
    update_sheet(employee, data)
    print(f"Worksheet updated for {month}.\n")


def cash_out():
    """
    Offers employee chance to cash out their over time
    """
    while True:
        print("Would you like to cash out your overtime?")
        answer = input("Y/N: \n")
        lower_answer = answer.lower()
        if validate_word_in_list(lower_answer, yes_no, "Y/N"):
            break
    return lower_answer


def cash_out_full_or_month(answer):
    """
    Offers employee to cash out their full overtime or just for the last month
    """
    if answer == "y" or answer == "yes":
        while True:
            print("Would you like to cash out your overtime in full")
            print("from January or just for the last month?")
            answer_two = input("Full/ Month: \n")
            answer_two = answer_two.lower()
            if validate_word_in_list(answer_two, full_month, "Full/Month"):
                break
        return answer_two

    else:
        print("\nThank you for filling out your hours with honesty!")
        quit()


def cash_out_payment(answer, pay_out, month_pay_out, employee, hours):
    """
    Creates a data string of what needs to be appended to balance
    the worksheet after payout
    """
    if answer == "full" or answer == "f":
        all_hours = pay_out / 11
        days = all_hours / 8
        pay_out_str = ["Paid out", 0,  - int(all_hours),
                       - int(days), - pay_out]
        update_sheet(employee, pay_out_str)
        print(f"You will be receive €{pay_out} gross in your next paycheck\n")
        print(f"\nThank you for using Honest Hours")
        quit()

    else:
        days = (hours / 8)
        pay_out_str_month = ["Paid out", 0, - int(hours),
                             - int(days), - month_pay_out]
        update_sheet(employee, pay_out_str_month)
        print(f"You will be receive €{month_pay_out} gross")
        print("in your next paycheck\n")
        print(f"\nThank you for using filling out your hours with honesty!")
        quit()


def main():
    """
    Calls the main functions
    """
    employee = get_employee_name()
    month = get_month_of_data(employee)
    holidays = get_month_data("holiday days taken", month)
    hours = get_month_data("over time hours worked", month)
    total_holidays = calculate_total_holidays(holidays, hours, employee)
    pay = calculate_pay_for_overtime(hours, month)
    data_str = [month, holidays, hours, total_holidays, pay]
    updating_worksheet(employee, data_str, month)
    full_payout = calculate_all_overtime_owed(employee)
    cash_out_answer = cash_out()
    answer_f_m = cash_out_full_or_month(cash_out_answer)
    cash_out_payment(answer_f_m, full_payout, pay, employee, hours)


main()



