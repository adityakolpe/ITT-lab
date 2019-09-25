import re
str=input("Enter the string:\n")
pla = input("Enter the string to be replaced:\n")
rep = input("Enter the string to replace:\n")
print (re.sub(pla, rep, str))
