#name Saar Haber
#date 22 February 2018
#This program ask the user for a binary number and print out the corresponding decimal number.

binString = input ('enter a binary number')
decNum = 0
for c in binString:
    n=int(c)
    decNum = 2*decNum + n
print (decNum)
