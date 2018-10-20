#Saar Haber
#March 19th 2018
#program 39

#import pandas for reading and analyzing CSV data:
import pandas as pd

csvFile = input('Enter CSV file name: ')         #Name of the CSV file
Data1 = pd.read_csv(csvFile)                   #Read in the file to a dataframe

print("Top three contributing factors for collisions:")
print(Data1['CONTRIBUTING FACTOR VEHICLE 1'].value_counts()[:3]) #Print out the dataframe
