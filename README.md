# Honest Hours

Honest hours is a command line program created for employees to keep track and manage their overtime work and holiday days. The program is aimed at taking the burden of work from the employer and allowing the staff to imput their own hours which will update the main google document. It also aims to place the ability to decide how they would like to receive their overtime with the employee. They can take it in either pay or extra holiday days and this

## User Stories

The main user of the program would be employees for the company and they would want to:
- Enter data easily 
- Gain insight into their holiday days left
- Gain insight into how much they have earned in overtime
- Allow them control over how they distribute their overtime
- Allow conversion of overtime to holidays or real money

for the employer:
- Data updated regularly for each staff member
- Access to their spreadsheet for spotchecks
- Validation on holidays taken
- The year befores information can be carried over to a new sheet

## Flowchart


## Existing Features

### Welcome Screen

The program introduces itself here with the name and a brief description of how the program is works so that it as user friendly as can be. There is an example of the type of data that will be looked for to also guide the user.

### Data input 

Each question appears individually and allows the user to input the data step by step. At each point if the data is not valid then the user will be told and it will be explained why it did not valid. They will then be given the opportunity to enter the data again.

### Google Spreadsheet

The spreadsheet is built of individual employee worksheets. Each worksheet contains the information for the year so far. The from the year previous can be input by the employer at the start of the new year if they allow for the carry over of holidays and overtime pay. Each sheet is seperate so the personal data of each employee would be private if the employer needed to speak to anyone about their particular worksheet. This worksheet is updated once all the data is entered correctly. This will be balanced then if the employee decides to cash out their overtime by taking away the equivalant 

### Holiday data returned

This section will feed back the data to the user about how many holiday days they have left and if they decide to convert their overtime hours to holidays how much that would leave them. 

### Pay out data returned

The overtime converted to cash for the month and for the total since January not paid out will be given to the user here to allow them to see their options.

### Option Menu

The options will be then displayed to the user and they will be allowed to decide then how they use their overtime and if they don't want to decide now they can leave the program. 


## Features which could be implented in the future

- Creation of new employee page from the program without having to update the spreadsheet manually. This would need to be looked at further as there would be issues around whether
- Quit button - work out how much the company owes you from holidays not taken and overtime owed.


## Deployment 

 1. I created a list of requirements by getting together the dependencies and saving them in requirements.txt
 2. I then opened my Heroku account and went to create new app.
 3. I picked a name for the app "Honest Hours".
 4. I set the config vars for the cred.json file.
 5. I then added built packs for python and node.js and made sure that python was added first.

## Testing
### Validation
I used the PEP8 validator to ensure the code was correct and it came up with no errors.

| **Test Category** | **Steps**| **Expected Outcome**| **Result**|
|----------|--------|----------|------------|---------|
|Welcome page | Run program and should appear| ---- WELCOME TO HONEST HOURS! ----
Please enter your personal holidays taken
and personal hours overtime for the
last month in the form of the example below
Example: 
Name: Emma, Month: January
Holidays taken: 5, Over hours worked: 18


   ---- Enter details here: ---- | pass|
|Name invalid | Enter a name that was not available
John is not in the list of employees.
Please check the spelling and try again.
The employee names available are:
['Emma', 'Charlie', 'Darren', 'George', 'Conor', 'Lia'] | Pass |
|Name - valid but lowercase |Enter valid name lowercase and uppercase |Name: 
emma
Month: 
(next question appears when first is answered with valid data)| Pass |
Name - valid
Enter valid name
Name: 
Emma
Month: 
Pass
Month - invalid spelling
Enter month spelled wrong
Jan is not in months of the year..
Please check the spelling and try again.

How many holiday days taken in 6: 


Pass
Data already entered for month
Enter month already used by user
Data has been entered for June already.


Pass
Month valid
Enter valid month
Month: 
August
How many holiday days taken in August: 
Pass
Holidays invalid string
Enter word instead of number
How many holiday days taken in August: 
two
Please make sure your answer is given as a number.
Try again.


pass
Holidays valid
Enter number
How many holiday days taken in August: 
2
How many overtime hours worked in August: 
pass
Overtime invalid string
Enter word instead of number
eight
Please make sure your answer is given as a number.
Try again.
pass
Overtime valid
Enter number
How many overtime hours worked in August: 
8
Calculating holidays left...
pass
Data update on sheet
Runs itself once all data entered
Google sheet updated with new row of data
pass
Holiday days left calculation
Runs itself
Holidays left for the month minus holidays taken
pass
Holiday days to convert calculation
Runs itself
Overtime found in full shifts by dividing by 8 hours
pass
Month pay calculation
Runs itself
Overtime hours by hourly rate
pass
Full pay calculation
Runs itself
All pay due added together
pass
Add data row to convert overtime to holidays
Enter 1
Data row added to balance the holiday days converted
pass
Add data row to pay out one month of overtime
Enter 2
Data row added to Google sheets that balances sheet for last month of overtime to be paid. Message about how much gross to expect and goodbye message
pass













### Debugging

| **Bug** | **Fix** |
|---|---|
| Welcome page was coming up again when the name invalid. | Took the welcome page out of the while true loop.|
| When holidays converted it removed full pay due and full overtime to balance but still hours that didn’t make full shifts were to be left. | Changed to work backwards from holidays converted instead of adding full pay due together.|
| Month validation was giving true for month spelled wrong | Put one validation inside the other so that both had to work to return true |
| Overtime available to convert did not include the overtime just entered for that month | Added the current month overtime to calculation |
| Data row appended had an empty string that could not be added together later | Changed to zero |




## Credits








