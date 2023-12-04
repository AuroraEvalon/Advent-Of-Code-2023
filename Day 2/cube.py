text = open("Day 2\\cubeInput.txt", "r")
data = text.read()

output = 0
game = 0
splitData = data.split("\n")
for x in splitData:
    valid  = True
    formattedData = x[5:]
    formattedData = formattedData.split(":")
    game = int(formattedData[0])
    set = formattedData[1].split(";")
    for x in set:
        hands = x.split(",")
        for cube in hands:
            handColor = cube.strip().split(" ")[1]
            handAmount = cube.strip().split(" ")[0]
            handAmount = int(handAmount)
            if handColor == "blue" and handAmount > 14:
                valid = False
            if handColor == "red" and handAmount > 12:
                valid = False
            if handColor == "green" and handAmount > 13:
                valid = False
    if valid:
        output = output + game  
print(output)