import regex
import math

finalNumber = 0
data = open("Trebuchet_input.txt", "r")
fileData = data.read()
splitData = fileData.split()
for x in splitData:
    numberData = regex.sub("[a-z]", "", x)
    firstNumber = numberData[:1]
    lastNumber = numberData[-1]
    fusedNumber = int(firstNumber + lastNumber)
    print(fusedNumber)
    finalNumber = finalNumber + fusedNumber
print(finalNumber)
data.close()