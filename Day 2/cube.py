import regex

text = open("Day 2\\cubeInput.txt", "r")
data = text.read()

handsList=[]
game = 0
splitData = data.split("\n")
for x in splitData:
    game += 1
    formattedData = x[5:]
    formattedData = formattedData.split(":")
    set = formattedData[1].split(";")
    for x in set:
        hands = x.split(",")
        handsList += hands
    handColor = regex.split("a-m", hands)
    handAmount = regex.split("1-9", hands)
    for x in handsList:
        if handColor == "blue" and handAmount <= 14:
            blueValid = "true"
        else:
            blueValid = "false"
    
    handsList=[]
