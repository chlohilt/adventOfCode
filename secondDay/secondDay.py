file = open("secondDayInput.txt", "r")

totalPowers = 0

for line in file:
    index = line.find(':')
    indexFirstSpace = line.find(' ')
    substringAfterGameNumber = line[index + 2:]

    setSections = substringAfterGameNumber.split(';')
    numRedCubes = 0
    numGreenCubes = 0
    numBlueCubes = 0
    numCubes = ''

    for section in setSections:
        if section == setSections[-1]:
            lastCheck = True
        for setChar in section:
            if setChar.isdigit():
                numCubes += setChar
            elif setChar.isalpha():
                if setChar == 'r':
                    if numCubes != '':
                        if int(numCubes) > numRedCubes:
                            numRedCubes = int(numCubes)
                        numCubes = ''
                elif setChar == 'g':
                    if int(numCubes) > numGreenCubes:
                        numGreenCubes = int(numCubes)
                    numCubes = ''
                elif setChar == 'b':
                    if int(numCubes) > numBlueCubes:
                        numBlueCubes = int(numCubes)
                    numCubes = ''
    powerResult = numBlueCubes * numGreenCubes * numRedCubes
    totalPowers += powerResult

print(totalPowers)
file.close()
