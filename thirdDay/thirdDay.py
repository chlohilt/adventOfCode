# read in file and put contents in a matrix
file = open("thirdDayInput.txt", "r")
firstLine = file.readline()

columns = len(firstLine.strip())
file.seek(0)
rows = sum(1 for line in file)
matrix = [[0] * columns for _ in range(rows)]

file.seek(0)
for indexLine, line in enumerate(file):
    for index, char in enumerate(line.strip()):
        matrix[indexLine][index] = char


def checkMatrix(checkPositions):
    for checkPosition in checkPositions:
        # check for diagonal positions
        if 0 <= checkPosition[0] - 1 < len(matrix):
            if 0 <= checkPosition[1] - 1 < len(matrix[0]):
                if (matrix[checkPosition[0] - 1][checkPosition[1] - 1] != '.' and
                        not matrix[checkPosition[0] - 1][checkPosition[1] - 1].isdigit()):
                    return True
            if (matrix[checkPosition[0] - 1][checkPosition[1]] != '.' and
                    not matrix[checkPosition[0] - 1][checkPosition[1]].isdigit()):
                return True
            if 0 <= checkPosition[1] + 1 < len(matrix[0]):
                if (matrix[checkPosition[0] - 1][checkPosition[1] + 1] != '.' and
                        not matrix[checkPosition[0] - 1][checkPosition[1] + 1].isdigit()):
                    return True

        if (0 <= checkPosition[1] + 1 < len(matrix[0]) and
                not matrix[checkPosition[0]][checkPosition[1] + 1].isdigit() and
                matrix[checkPosition[0]][checkPosition[1] + 1] != '.'):
                return True
        if (0 <= checkPosition[1] - 1 < len(matrix[0]) and
                not matrix[checkPosition[0]][checkPosition[1] - 1].isdigit() and
                matrix[checkPosition[0]][checkPosition[1] - 1] != '.'):
                return True

        if 0 <= checkPosition[0] + 1 < len(matrix):
            if 0 <= checkPosition[1] + 1 < len(matrix[0]):
                if (matrix[checkPosition[0] + 1][checkPosition[1] + 1] != '.' and
                        not matrix[checkPosition[0] + 1][checkPosition[1] + 1].isdigit()):
                    return True
            if (matrix[checkPosition[0] + 1][checkPosition[1]] != '.' and
                    not matrix[checkPosition[0] + 1][checkPosition[1]].isdigit()):
                return True
            if 0 <= checkPosition[1] - 1 < len(matrix[0]):
                if (matrix[checkPosition[0] + 1][checkPosition[1] - 1] != '.' and # diagonal right lower
                        not matrix[checkPosition[0] + 1][checkPosition[1] - 1].isdigit()):
                    return True

# calculate what are numbers and see what is all around them
file.seek(0)
sumOfPartNums = 0
for indexLine, line in enumerate(file):
    currentNumber = ''
    checkPositions = []
    for indexChar, char in enumerate(line):
        if char.isdigit():
            currentNumber += char
            checkPositions.append((indexLine, indexChar))
        elif currentNumber != '':
            if checkMatrix(checkPositions):
                sumOfPartNums += int(currentNumber)
            currentNumber = ''
            checkPositions.clear()

print(sumOfPartNums)
file.close()