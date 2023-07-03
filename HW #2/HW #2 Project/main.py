# Name: Brittany Zimmerman
# PSID: 2219602

import datetime

month_def = {                                           # Dictionary of months and associated numbers.
        "January": "1",
        "February": "2",
        "March": "3",
        "April": "4",
        "May": "5",
        "June": "6",
        "July": "7",
        "August": "8",
        "September": "9",
        "October": "10",
        "November": "11",
        "December": "12"
    }

date = ""                                               # Initialized date variable.
if __name__ == "__main__":
    new_date_list = ['']                                # Initialized new dates list for use after for loop.
    f = open('inputDates.txt').readlines()

    for date in f:
        if date == '-1\n':
            break                                       # Breaks loop if -1 detected
        else:

            date = date.strip('\n')                     # Deleting newlines
            date_list = date.split(" ")                 # Split input on space
            comma_true = 0                              # For comma testing (ensure formatting correct)

            if len(date_list) >= 3:                     # Check input values then assign them to positions
                month = date_list[0]
                day = date_list[1]
                year = date_list[2]
                year_len = len(year)                    # Four-digit year check

                if month in month_def:                  # Grab month number from month dictionary
                    month_num = month_def[month]

                    if day.find(",") >= 0:              # Full comma check
                        comma_true = 1
                        day = day.replace(',', '')      # Delete comma to make data more workable
                        day_num = int(day)
                        if year.isdigit():              # Ensure year is num
                            year_num = int(year)
                            date_string = year + "-" + month_num + "-" + day   # Place data into comparable format
                            date_date = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()  # Get actual date

                            if date_date <= datetime.date.today() and year_len == 4:   # Date comparison and year length
                                full_date = str(month_num) + '/' + day + '/' + year    # Grab back date data
                                new_date_list.append(full_date)                        # Add date to new list

                    else:
                        continue

    new_date_list.pop(0)  # Deletes list initialization value
    w = open('parsedDates.txt', 'w')    # Open and write to new file
    for dates in new_date_list:
        w.write(dates+'\n')
    w.close()


