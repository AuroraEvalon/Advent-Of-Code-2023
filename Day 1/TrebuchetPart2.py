import regex
import math

finalNumber = 0
data = open("Day 1\Trebuchet_input.txt", "r")
fileData = data.read()
splitData = fileData.split()
for x in splitData:
    x = x.replace("twone", "21")
    x = x.replace("nineight", "98")
    x = x.replace("threeight", "38")
    x = x.replace("oneight", "18")
    x = x.replace("fiveight", "58")
    x = x.replace("sevenine", "79")
    x = x.replace("eighthree", "83")
    x = x.replace("eightwo", "82")
    x = x.replace("one", "1")
    x = x.replace("two", "2")
    x = x.replace("three", "3")
    x = x.replace("four", "4")
    x = x.replace("five", "5")
    x = x.replace("six", "6")
    x = x.replace("seven", "7")
    x = x.replace("eight", "8")
    x = x.replace("nine", "9")
    numberData = regex.sub("[a-z]", "", x)
    firstNumber = numberData[:1]
    lastNumber = numberData[-1]
    fusedNumber = int(firstNumber + lastNumber)
    print(fusedNumber)
    finalNumber = finalNumber + fusedNumber
print(finalNumber)
data.close()