import calendar
x= int(input("Enter number of years:"))
for i in range (x):
    
    yy= int(input ("Enter year:"))
    mm= int(input ("Enter month:"))
    print(calendar.month(yy,mm))