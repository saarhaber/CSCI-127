#Saar Haber
#Date: March 19th 2018
#Program 32

arr=str(input("Enter a list of words"))

if arr[-1]=="s":
    n=1
else:
    n=0

words = arr.count(" ")+1
plural = arr.count("s ")+n

print ("number of words: " , words)
print ("Fraction of your list that is plural is: " ,plural/words) 


