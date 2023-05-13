#Program : Decimal converter
#Python 3.10.11



#Function declaration

def decimalToBinary(number):
	return bin(number)[2:].zfill(64)

from datetime import date

def decimalToHexazecimal(number):
    return hex(number)[2:].zfill(64)
    
def decimalToOctal(number):
    return oct(number)[2:].zfill(64)

#Get date for log file

currentDay = date.today()

#Creating log FIle

logFile = open("log.txt", "a")

#Prompt

print("Enter a decimal number to be converted in:\n")
print(7*"=" + " Binary | Hexazecimal | Octal" + 7*"=")
print()
numberToBeConverted = int(input("Enter a number to be converted: "))
print()
print("The number {} in binary is {} on 64 bit".format(numberToBeConverted,decimalToBinary(numberToBeConverted)))
print()
print("The number {} in hexazecimal is {} on 64 bit".format(numberToBeConverted,decimalToHexazecimal(numberToBeConverted)))
print()
print("The number {} in octal is {} on 64 bit".format(numberToBeConverted,decimalToOctal(numberToBeConverted)))

#Write to log file

logFile.write("Date : {} | The number {} in binary is {} on 64 bit\n".format(currentDay, numberToBeConverted, decimalToBinary(numberToBeConverted)))
logFile.write("Date : {} | The number {} in hexazecimal is {} on 64 bit\n".format(currentDay, numberToBeConverted, decimalToHexazecimal(numberToBeConverted)))
logFile.write("Date : {} | The number {} in octal is {} on 64 bit\n".format(currentDay, numberToBeConverted, decimalToOctal(numberToBeConverted)))
