from datetime import datetime
from fpdf import FPDF

#Program : Decimal converter
#Python 3.10.11



#Function declaration

def decimalToBinary(number):
	return bin(number)[2:].zfill(32)

from datetime import date

def decimalToHexazecimal(number):
    return hex(number)[2:].zfill(32)
    
def decimalToOctal(number):
    return oct(number)[2:].zfill(32)

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
    print("The number {} in binary is {} on 64 bit".format(numberToBeConverted,decimalToBinary(numberToBeConverted)))
    print()
    print("The number {} in hexazecimal is {} on 64 bit".format(numberToBeConverted,decimalToHexazecimal(numberToBeConverted)))
    print()
    print("The number {} in octal is {} on 64 bit".format(numberToBeConverted,decimalToOctal(numberToBeConverted)))

    #Write to log file
    
    logFile.write("Date : {} and Time {} | The number {} in binary is {} on 64 bit\n".format(currentDay, currentTime, numberToBeConverted, decimalToBinary(numberToBeConverted)))
    logFile.write("Date : {} and Time {} | The number {} in hexazecimal is {} on 64 bit\n".format(currentDay, currentTime, numberToBeConverted, decimalToHexazecimal(numberToBeConverted)))
    logFile.write("Date : {} and Time {} | The number {} in octal is {} on 64 bit\n".format(currentDay, currentTime, numberToBeConverted, decimalToOctal(numberToBeConverted)))
    
    #Set FPDF

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 6)

    readTxtLogFile = open("log.txt", "r")

    for x in readTxtLogFile:
        pdf.cell(500, 15, txt = x, ln = 1, align = 'L')
    
    #Save the PDF with name .pdf
    pdf.output("log_pdf.pdf")
    
    #close TXT File Object 
    
    logFile.close()
    
    print("The ouput is saved in txt and pdf format. Please check the output where is the script !")
    
except ValueError:
    print("Wrong Input! Only Integers")

