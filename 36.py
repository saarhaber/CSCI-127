#Saar Haber
#March 19th 2018
#Cprogram 36

#Import pandas for reading and analyzing CSV data:
import pandas as pd

csvFile = input('Enter CSV file name: ')         #Name of the CSV file
tickets = pd.read_csv(csvFile)                   #Read in the file to a dataframe
Attribute = input ('Enter Attribute: ')

print("The 10 worst offenders are:")
print(tickets[Attribute].value_counts()[:10])   #Print out the dataframe
