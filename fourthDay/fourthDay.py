file = open('fourthDay.txt', 'r')

sumWinningNums = 0

for line in file:
    indexColon = line.find(':')
    substringAfterGameNumber = line[indexColon + 2:].strip()

    indexLine = substringAfterGameNumber.find('|')
    winningNumbersLine = substringAfterGameNumber[:indexLine]
    possibleNumbersLine = substringAfterGameNumber[indexLine + 1:]

    winningNumbers = winningNumbersLine.split()
    possibleNumbers = possibleNumbersLine.split()

    numPoints = 0.5
    for possibleNumber in possibleNumbers:
        if possibleNumber in winningNumbers:
            numPoints *= 2
    if numPoints != 0.5:
        sumWinningNums += numPoints

print(sumWinningNums)

file.close()