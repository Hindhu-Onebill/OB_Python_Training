import datetime
import calendar


def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])


# Driver program
date = input("enter the date seperated by space in format of dd mm yyyy :")
print(findDay(date))
