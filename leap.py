from datetime import datetime
year = datetime.strptime(input("Enter the date in MM/DD/YYYY format: "), "%m/%d/%Y")
if(year%4==0):
   print("leap")
else:
  print("not leap")
