#Name: Saar Haber
#Date: January 31st 2018
#This program prompts the user for a DNA string, and then prints the length and GC-content.

print("Enter a DNA string")

n=input() 

T=0

print(len(n))

m=len(n)
c='C'
g='G'

for i in n:
    if i==c or i==g:
        T+=1;
        
print (T/len(n)+100)
