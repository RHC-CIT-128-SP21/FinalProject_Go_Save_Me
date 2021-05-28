# FinalProject_Go_Save_Me
* Jean Lira
* CIT 128
* CRN 37902

## Info

This program is a finacial saving program. 
It will take in user input such as generated revenue as well as expenditures. 
All storage of data will be placed upon an inaccessible excel file.
After the data is stored, the user can then request a report of exepnditures as percentages and the program will return where high expenditures are made.  

## Code Structure
The code will be broken into 3 main sections. 
1. The program receives user input
2. The program appends to storage
3. The program calls and calculates the percentage reports

## Testing 

Testing will be done using a professor approved unit test and must pass all tests to be considered to be complete. 
The unit test will use good data, bad data, and data that may just need a data type change. 

## Rubric / Grading Scale
* Working Python Code
  * Code follows the structure and actions(60 Points)
  * Code appends and updates excel file (20 points)
  * Code passes the Unit Test(120)
 
 Total: 200 Points
 
## Instructions To Use Code
 # Code starts and terminal screen shows up giving 5 options:
  * Option 1: Add an expense to your report
  * Option 2: Add income to your report
  * Option 3: Get a percentage report
  * Option 4: Show entirety of expense and income report
  * Option 5: Exit program

 # Option 1 Steps:
  * Enter amount of expenditure
  * Select category of expense(Food, Gas, or Other)
  * Code will automatically save it to the report

 # Option 2 Steps:
  * Enter amount of income
  * Code will automatically save it to the report

 # Option 3 steps:
  * Code will automatcally return percentage report of all spending categories
  * Code will also highlight the highest percentage and give a tip to save money
