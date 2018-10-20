#Saar Haber
#March 8th
#Lab 6

import matplotlib.pyplot as plt

import pandas as pd
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

print('enter a borough name: ')
bo=str(input())
print('enter output file name: ')
ofn=str(input())

#Compute the fraction of the population in the Bronx, and save as new column:
pop['Fraction'] = pop[bo]/pop['Total']

#Create a plot of year versus fraction of pop. in Bronx (with labels):
pop.plot(x = 'Year', y = 'Fraction')

#Save to the file:  fractionBX.png
fig = plt.gcf()
fig.savefig(ofn)
