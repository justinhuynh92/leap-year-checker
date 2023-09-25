
#create function for leap year
def is_leap_year(year):
    #check if the year is evenly divisible by 4 and 100
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('Leap Year')
            else:
                print('Not leap year')
        else:
            print('Leap year')
    else:
        print('Not leap year')

#call function and check if the input is a leap year
is_leap_year(2004)
