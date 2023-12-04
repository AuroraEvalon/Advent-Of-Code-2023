text = open("Day 2\\cubeInput.txt", "r")
data = text.read()

largestBlue = 0
largestRed = 0
largestGreen = 0
output = 0
game = 0
total = 0
splitData = data.split("\n")
for x in splitData:
    valid  = True
    formattedData = x[5:]
    formattedData = formattedData.split(":")
    game = int(formattedData[0])
    set = formattedData[1].split(";")
    largestBlue = 0
    largestRed = 0
    largestGreen = 0
    for x in set:
        hands = x.split(",")
        for cube in hands:
            handColor = cube.strip().split(" ")[1]
            handAmount = cube.strip().split(" ")[0]
            handAmount = int(handAmount) 
            if handAmount > largestBlue and handColor == "blue":
                largestBlue = handAmount
            elif handAmount > largestGreen and handColor == "green":
                largestGreen = handAmount
            elif handAmount > largestRed and handColor == "red":
                largestRed = handAmount
            power = largestBlue*largestGreen*largestRed
    total = power + total
print(total)