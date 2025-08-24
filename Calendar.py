import calendar 
year=int(input("Enter any year : "))
cal=calendar.TextCalendar(calendar.SUNDAY)
i=1
while i<=12:
    print(cal.prmonth(year,i))
    i+=1