#Name: Saar Haber
#Date: January 31st 2018
#This program prompts the user for a DNA string, and then prints the length and GC-content.

print("Enter a DNA string") 

n=input() #User enter a string

T=0 #the counter of C's or G's

print(len(n)) #printing the length of the string

c='C'
g='G'

for i in n: #loop
    if i==c or i==g: #if there is a C or a G it counts them at T.
        T+=1;
        
print (T/len(n))   #printing the percent of C's or G's in the DNA string
