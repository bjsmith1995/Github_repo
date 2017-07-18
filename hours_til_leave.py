
# coding: utf-8

from datetime import datetime
currentHour = datetime.now().hour
currentMinute = datetime.now().minute

number_of_times = int(input("How many times have you clocked in/out  "))
hourly_clocks_calc = []
hourly_clocks_hour = []
hourly_clocks_minute = []

#get time using for loop with the number of times clocked in
#if previous minutes is > new minutes then add 12 hours to new minutes (to account for afternoon vs morning)

for i in range(number_of_times):
    time_in_hour = int(input('clock time (hour)?  '))
    time_in_minute = int(input('clock time (minute)?  '))
    
    #checking to see if the time is am or pm
    #the first time is ignored
    #this assumes that they will only enter clock ins for a one day period
    #works by checking to see if the entered hour is smaller than a previous hour
    if hourly_clocks_calc == []:
        print('')
    elif time_in_calc < hourly_clocks_calc[i-1]:
        time_in_hour = time_in_hour + 12
    #calculate the number of minutes (for easier calculations)
    time_in_calc = time_in_hour*60 + time_in_minute
    #store the three time values in lists
    hourly_clocks_calc.insert(i, time_in_calc)
    hourly_clocks_hour.insert(i, time_in_hour)
    hourly_clocks_minute.insert(i, time_in_minute)

# if not clocked in then check current time to see what time you can actually get out
#calculate the total number of hours worked based on subtracting clock out time from clock in time
# if currently clocked in then check current time to use in the previous subtraction
#loop through hourly_clocks to calculate all of the hours
time_remaining = 8*60
for i in range(len(hourly_clocks_calc)):
    sign_change = 1
    if i % 2 != 0:
        sign_change = -1
    time_remaining = time_remaining +sign_change * hourly_clocks_calc[i]

currentTime = currentHour * 60 + currentMinute
if i % 2 == 0:
    time_remaining = time_remaining - currentTime

get_out_hour = (time_remaining + currentTime) // 60
get_out_minute = (time_remaining + currentTime) % 60

print("")
for i in range(number_of_times):
    print("hourly_clock %s %s" %(hourly_clocks_hour[i], str(hourly_clocks_minute[i]).zfill(2)))
print("Minutes remaining ", time_remaining)
pm_or_am = "am"
if get_out_hour > 12:
    get_out_hour = get_out_hour - 12
    pm_or_am = "pm"
print("You will have worked 8 hours at %s:%s %s" %(get_out_hour, str(get_out_minute).zfill(2), pm_or_am))

