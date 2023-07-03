# Name: Brittany Zimmerman
# PSID: 2219602

import datetime

month_def = {
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
f = open('inputDates.txt')
values = f.readline()


date = ""
if __name__ == "__main__":
    new_date_list = ['']
    f = open('inputDates.txt').readlines()

    for date in f:
        if date == '-1\n':
            break
        else:

            date = date.strip('\n')
            date_list = date.split(" ")
            comma_true = 0

            if len(date_list) >= 3:
                month = date_list[0]
                day = date_list[1]
                year = date_list[2]
                year_len = len(year)

                if month in month_def:
                    month_num = month_def[month]

                    if day.find(",") >= 0:
                        comma_true = 1
                        day = day.replace(',', '')
                        day_num = int(day)
                        if year.isdigit():
                            year_num = int(year)
                            date_string = year + "-" + month_num + "-" + day
                            date_date = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()

                            if date_date <= datetime.date.today() and year_len == 4:
                                full_date = str(month_num) + '/' + day + '/' + year
                                new_date_list.append(full_date)

                    else:
                        continue

    new_date_list.pop(0)
    for date in new_date_list:
        print(date)
