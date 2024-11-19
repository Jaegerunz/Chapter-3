# Function:     This program determines if a date entered by the user is valid.  
# Input:        Interactive
# Output:       Valid date is printed or user is alerted that an invalid date was entered.

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

year = None
month = None
day = None

# Get the year, then the month, then the day
year=input("Please input year:")
month=input("Please input month:")
day=input("Please input day:")
# housekeeping()

# Check to be sure date is valid

if int(year) < MIN_YEAR: # invalid year
    validDate = False

if int(month) < MIN_MONTH or int(month) > MAX_MONTH: # invalid month
    validDate = False
#31Days
if month ==1 or month == 3 or month == 5 or month == 7 or month ==9 or month == 10 or month == 12:
    if day <= MIN_DAY or day >= MAX_DAY:
        validDate= False
#30Days
elif month == 4 or month == 6 or month ==9 or month ==11:
    if day < MIN_DAY or day > 30:
        validDate= False
#Feb
elif month ==2: 
    if day < MIN_DAY or day >29:
        validDate= False
# Test to see if date is valid and output date and whether it is valid or not

# endOfJob()
if validDate == True:
    print(month+"/"+ day +"/"+ year+ " is a valid date" )
else:
    print(month+"/"+ day +"/"+ year+ " is an invalid date" )