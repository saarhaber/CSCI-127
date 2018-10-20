#Name: Saar Haber
#Date: February 8th 2018
#This program Write a program that prompts the user to enter a word and then prints out the word with each letter shifted right by 2.

print("enter a word")
word=input()
word2=""

for i in word:
    word2=word2+chr((ord(i))+2)

print("your word is: "+word2)
    
    
