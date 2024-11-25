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

elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: # invalid month
    validDate = False
#31Days
else:
    if int(month) in {1,3,5,7,10,12}:
        if int(day) < MIN_DAY or int(day) > 31:
            validDate=False

    elif int(month) in {4,6,9,11}:
        if int(day) < MIN_DAY or int(day) >30:
            validDate=False
    
    elif int(month)==2:
        if int(day) < MIN_DAY or int(day) >= 29:
            validDate = False
# Test to see if date is valid and output date and whether it is valid or not

# endOfJob()
if validDate == True:
    print(month+"/"+ day +"/"+ year+ " is a valid date" )
else:
    print(month+"/"+ day +"/"+ year+ " is an invalid date" )