#Saar Haber
#Program 31
#Date: March 19th 2018

import pandas as pd
import matplotlib.pyplot as plt

FileName=input("Enter name of input file: ")
OutputFile=input("Enter name of output file: ")
homeless = pd.read_csv(FileName)
homeless['Fraction Children'] = homeless['Total Children in Shelter']/homeless['Total Individuals in Shelter']

homeless.plot(x="Date of Census", y="Fraction Children")

plt.savefig(OutputFile)
