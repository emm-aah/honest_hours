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
        print("   ---- WELCOME TO HONEST HOURS! ----\n")
        print("Please enter your personal holidays taken")
        print("and personal hours overtime for the")
        print("last month in the form of the example below")
        print("Example: \nName: Emma, Month: January")
        print("Holidays taken: 5, Over hours worked: 18\n")
        print("\n   ---- Enter details here: ----\n")
        employee_name = input("Name: \n")
        employee = employee_name.capitalize()
        if validate_word_in_list(employee, employees, "list of employees"):
            break
        else: 
            print("The employee names available are:")
            print(employees)

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

def get_sum_of_column(name, col_num):
    values = get_column_values(name, col_num)
    values = values[1:]
    values = [int(value) for value in values]
    column_sum = sum(values)

    return column_sum


def validate_month(given_month, name):
    """
    Validate name by checking it against employee names
    """
    months_already_entered = get_column_values(name, 1)
    try:
        validate_word_in_list(given_month, MONTHS, "months of the year")
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


def calculate_holidays_left(name, holidays_taken):
    """
    gets holiday days taken and takes it away from total holidays
    """
    print("Calculating holidays left...\n")
    prev_holidays_left = get_column_values(name, 4)
    prev_holidays_left = prev_holidays_left[-1]
    new_holidays_left = int(prev_holidays_left) - holidays_taken
    print(f"You have {new_holidays_left} holidays left.")

    if new_holidays_left < 0:
        print("You have taken more than your alloted holidays.") 
        print("Please convert overtime to holidays")
        print("or speak to a manager about the issue.\n")
    return new_holidays_left


def calculate_extra_holidays(name):
    """
    Takes the holidays taken away from holidays left
    Gets the over time hours in terms of days and adds to holidays left
    returns holidays left
    """
    all_hour_sum = get_sum_of_column(name, 3)
    extra_days = all_hour_sum / 8
    extra_days = math.floor(extra_days)
    print(f"You have {extra_days} days overtime available to convert to holiday days\n")

    return extra_days


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
    full_overtime_pay = get_sum_of_column(name, 5)
    print(f"Your overtime pay from January comes to €{full_overtime_pay}\n")

    return full_overtime_pay


def update_sheet(employee, data):
    """
    Append the worksheet with a new row
    """
    worksheet = SHEET.worksheet(employee)
    worksheet.append_row(data)


def updating_worksheet(employee, data, month):
    """
    Update employees worksheet with the month, holidays and overhours entered.
    """
    print(f"Updating {employee}'s worksheet...\n")
    update_sheet(employee, data)
    print(f"Worksheet updated for {month}.\n")


def display_option_menu(hours, holidays_left, month_pay, name, full_payout, extra_holidays):
    print("Choose one of the following:")
    print("1. Convert overtime hours to available holidays.")
    print("2. Cash out over time for the last month.")
    print("3. Cash out full overtime since January.")
    print("4. Decide later and leave program")
    answer = input("Please answer with 1, 2, 3, or 4: \n")
    complete_option_choice(answer, hours,holidays_left, month_pay, name, full_payout, extra_holidays)

def complete_option_choice(answer, hours, holidays_left, month_pay, name, full_payout, extra_holidays):
    if answer == "1":
        all_hours = full_payout / 11
        updated_hols = extra_holidays + holidays_left
        converted_hols_str = ["Converted", 0, -int(all_hours), updated_hols, -full_payout]
        update_sheet(name, converted_hols_str)
        print(f"You now have {updated_hols} holidays left to take.\n")
        print("Thank you for using Honest Hours")

    elif answer == "2":
        pay_out_str_month = ["After pay out", 0, - int(hours),
                             holidays_left , - month_pay]
        update_sheet(name, pay_out_str_month)
        print(f"You will be receive €{month_pay} gross")
        print("in your next paycheck\n")
        print(f"\nThank you for using filling out your hours with honesty!")
        quit()
    
    elif answer == "3":
        all_hours = full_payout / 11
        pay_out_str = ["Paid out", 0,  - int(all_hours),
                       holidays_left, - full_payout]
        update_sheet(name, pay_out_str)
        print(f"You will be receive €{full_payout} gross in your next paycheck\n")
        print(f"\nThank you for using Honest Hours")
        quit()
    elif answer == "4":
        print(f"\nThank you for using Honest Hours")
        quit()
    else: 
        print("Please answer with 1, 2, 3 or 4")




    


def main():
    """
    Calls the main functions
    """
    employee = get_employee_name()
    month = get_month_of_data(employee)
    holidays = get_month_data("holiday days taken", month)
    hours = get_month_data("over time hours worked", month)
    holidays_left = calculate_holidays_left(employee, holidays)
    extra_holidays = calculate_extra_holidays(employee)
    month_pay = calculate_pay_for_overtime(hours, month)
    data_str = [month, holidays, hours, holidays_left, month_pay]
    updating_worksheet(employee, data_str, month)
    full_payout = calculate_all_overtime_owed(employee)
    display_option_menu(hours, holidays_left, month_pay, employee, full_payout, extra_holidays)

    #cash_out_answer = cash_out()
    #answer_f_m = cash_out_full_or_month(cash_out_answer)
    #cash_out_payment(answer_f_m, full_payout, pay, employee, hours, total_holidays)


main()



