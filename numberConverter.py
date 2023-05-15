from datetime import datetime
from fpdf import FPDF

#Program : Decimal converter
#Python 3.10.11

#Function declaration

def decimalToBinary(number):
	return bin(number)[2:]

from datetime import date

def decimalToHexazecimal(number):
    return hex(number)[2:]
    
def decimalToOctal(number):
    return oct(number)[2:]

#Get date and time for log file
now = datetime.now()
currentTime = now.strftime("%H:%M:%S")
currentDay = date.today()

#Creating log File as txt

logFile = open("log.txt", "a")

#Prompt

print("Enter a decimal number to be converted in:\n")
print(7*"=" + " Binary | Hexazecimal | Octal" + 7*"=")
print()
try:
    numberToBeConverted = int(input("Enter a number to be converted: "))
    print()
    print("The number {} in binary is {}".format(numberToBeConverted,decimalToBinary(numberToBeConverted)))
    print()
    print("The number {} in hexazecimal is {}".format(numberToBeConverted,decimalToHexazecimal(numberToBeConverted)))
    print()
    print("The number {} in octal is {}".format(numberToBeConverted,decimalToOctal(numberToBeConverted)))

    #Write to log file
    
    logFile.write("Date : {} and Time {} | The number {} in binary is {}\n".format(currentDay, currentTime, numberToBeConverted, decimalToBinary(numberToBeConverted)))
    logFile.write("Date : {} and Time {} | The number {} in hexazecimal is {}\n".format(currentDay, currentTime, numberToBeConverted, decimalToHexazecimal(numberToBeConverted)))
    logFile.write("Date : {} and Time {} | The number {} in octal is {}\n".format(currentDay, currentTime, numberToBeConverted, decimalToOctal(numberToBeConverted)))
    logFile.close()
    
    print("The ouput is saved in txt format. Please check the output where is the script !")
    
except ValueError:
    print("Wrong Input! Only Integers")

