# Honest Hours

Honest hours is a command line program created for employees to keep track and manage their overtime work and holiday days. The program is aimed at taking the burden of work from the employer and allowing the staff to input their own hours which will update the main google document. It also aims to place the ability to decide how they would like to receive their overtime with the employee. They can take it in either pay or extra holiday days or as pay in part or full.

The live project can be found [here](https://honest-hours-4f19aa16e5ff.herokuapp.com/)
Access google sheet [here](https://docs.google.com/spreadsheets/d/1DxJhqyOEBS9VJ2Fa_AfxtH2kQhBHTBNbPNCX3HJ_SLw/edit?usp=sharing)


## User Goals

The main user of the program would be employees for the company and they would want to:
- Enter data easily 
- Gain insight into their holiday days left
- Gain insight into how much they have earned in overtime
- Allow them control over how they distribute their overtime
- Allow conversion of overtime to holidays or real money

for the employer:
- Data updated regularly for each staff member
- Access to their spreadsheet for spot checks
- Validation on holidays taken
- The year befores information can be carried over to a new sheet

## User Stories

- As the user I click run program and a welcome message appears
- I read the instructions and example which show me how the data is expected 
- I see that there is an enter details section where the name question is empty
- I enter my name and it is validated
- I enter the month and it is validated
- I enter the holidays I took for the month entered
- I enter the hours overtime I worked for the month entered
- I then see how many holidays I have left and how many I could covert from my overtime
- I see how much I am owed in euro in overtime for the month and since the start of the year
- I then see a menu which allows me to choose how I wish to handle my overtime
- I press 1 and I see that my overtime hours have been converted to holiday days
- I see a goodbye message that confirms I am finished for this entry

## Flowchart

![Flowchart 1](/documentation/images/flowchart_1.png)
![Flowchart_2](/documentation/images/flowchart_2.png)


## Existing Features

### Welcome Screen

The program introduces itself here with the name and a brief description of how the program works so that it is as user friendly as can be. There is an example of the type of data that will be looked for to also guide the user.
![Welcome Page](/documentation/images/welcome_message.png)

### Data input 

Each question appears individually and allows the user to input the data step by step. At each point if the data is not valid then the user will be told and it will be explained why it did not valid. They will then be given the opportunity to enter the data again.
![Data Input](/documentation/images/details.png)

### Google Spreadsheet

The spreadsheet is built of individual employee worksheets. Each worksheet contains the information for the year so far. The from the year previous can be input by the employer at the start of the new year if they allow for the carry over of holidays and overtime pay. Each sheet is separate so the personal data of each employee would be private if the employer needed to speak to anyone about their particular worksheet. This worksheet is updated once all the data is entered correctly. This will be balanced then if the employee decides to cash out their overtime by taking away the equivalent.

![Google Sheet](/documentation/images/google_sheet.png)

![Google worksheet](/documentation/images/google_worksheets.png)

### Holiday data returned

This section will feed back the data to the user about how many holiday days they have left and if they decide to convert their overtime hours to holidays how much that would leave them. 

### Pay out data returned

The overtime converted to cash for the month and for the total since January not paid out will be given to the user here to allow them to see their options.

### Option Menu

The options will be then displayed to the user and they will be allowed to decide then how they use their overtime and if they don't want to decide now they can leave the program. 

![Option Menu](/documentation/images/menu.png)

### Goodbye Message

A quick line with the brand name to let the user know they have finished their entry.
![Goodbye Message](/documentation/images/goodbye_message.png)


## Features which could be implemented in the future

- Creation of new employee page from the program without having to update the spreadsheet manually. This would need to be looked at further as there would be issues around whether
- Quit button - work out how much the company owes you from holidays not taken and overtime owed.


## Deployment 

I used gitpod to create my site and pushed any changes made to github.

To deploy:

 1. I created a list of requirements by getting together the dependencies and saving them in requirements.txt
 2. I then opened my Heroku account and went to create new app.
 3. I picked a name for the app "Honest Hours".
 4. I set the config vars for the cred.json file.
 5. I then added build packs for python and node.js and made sure that python was added first.

To set up API:
  
  1. Made a google sheet.
  2. Go To Google Cloud Platform and create a new project
  3. Setup API Credentials by:
        - going to 'APIs + Services' then 'Libraries'
        - found Google Drive API, selected and enabled
        - Clicked Create Credentials, then in Credential Type and selected Google Drive from dropdown
        - Clicked Application data and no I'm not using them radio buttons
        - Then gave it the name honest_hours 
        - In the role dropdown I chose editor + skipped the rest pressing done
        - I then created a new key with json and downloaded it to my computer
  4. Enabled Google Sheets API
  5. Drag and drop the json file into repository.
  6. Save it in .gitignore
  7. Install gspread and google auth libraries
  8. Copy client email from json file and go back to google sheets and share to that email


## Testing
### Validation
I used the PEP8 validator to ensure the code was correct and it came up with no errors.

![Pep8 validation](/documentation/images/Validator.png)

![Test table 1](/documentation/images/test_table_1.png)
![test table 2](/documentation/images/test_table_2.png)
![test table 3](/documentation/images/test_table_3.png)

### Debugging

| **Bug** | **Fix** |
|---|---|
| Welcome page was coming up again when the name invalid. | Took the welcome page out of the while true loop.|
| When holidays converted it removed full pay due and full overtime to balance but still hours that didn’t make full shifts were to be left. | Changed to work backwards from holidays converted instead of adding full pay due together.|
| Month validation was giving true for month spelled wrong | Put one validation inside the other so that both had to work to return true |
| Overtime available to convert did not include the overtime just entered for that month | Added the current month overtime to calculation |
| Data row appended had an empty string that could not be added together later | Changed to zero |


## Credits

- _Code institute- Love Sandwiches project_ - I used my knowledge from this completing this to mould my project idea.
- https://github.com/elainebroche-dev/ms3-event-scheduler - I liked the way she used a menu to begin with and implemented something similar for the end of my project
- _Lucid App_ - I used this to create the flowchart

## Acknowledgements

Medale Oluwafemi - my mentor for helping me through each stage of the project with his valuable input.








