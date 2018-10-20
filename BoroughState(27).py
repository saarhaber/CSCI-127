#Saar Haber
#March 8th
#BoroughState(27)

import matplotlib.pyplot as plt

import pandas as pd
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

print('enter a borough name: ')
bo=str(input())


#Compute the average of the population in the borough, and print:
Average = pop[bo].mean()
print("Average Population ", Average)
      
#Compute the maximum of the population in the borough, and print:
Maximum = pop[bo].max()
print("Maximum Population ", Maximum)

