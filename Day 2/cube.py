text = open("Day 2\\cubeInput.txt", "r")
data = text.read()

game = 0
splitData = data.split("\n")
for x in splitData:
    game += 1
    formattedData = x[5:]
    set = formattedData.split(";")
    print(game)
    print(set)
