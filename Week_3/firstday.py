# Firstday 
# Name: Yusuf Hendricks 
# Date: 22nd May 2020

days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'] 

year1 = int(input("Enter year 1: "))
year2 = int(input("Enter year 2: "))

def calc(year1):
  a = year1%4
  b = year1%100
  c = year1%400

  day = (1+5*a+4*b+6*c)%7
  return day
  
while year1 <= year2 :
  d = calc(year1 - 1)
  day = days[d]
  print("The first of january {} falls on a {} .".format(year1, day))
  year1 += 1











