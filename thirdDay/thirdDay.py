def getNum(row, col):
    num = ''
    if 0 <= col - 1 < len(matrix[0]) and matrix[row][col - 1].isdigit():
        num += matrix[row][col - 1]
        num += matrix[row][col]
        if 0 <= col - 2 < len(matrix) and matrix[row][col - 2].isdigit():
            matrix[row][col - 2] += num
            return num
        elif 0 <= col + 1 < len(matrix[0]) and matrix[row][col + 1].isdigit():
            num += matrix[row][col + 1]
            return num
        else:
            return num

    if 0 <= col + 1 < len(matrix[0]) and matrix[row][col + 1].isdigit():
        num += matrix[row][col]
        num += matrix[row][col + 1]
        if 0 <= col + 2 < len(matrix) and matrix[row][col + 2].isdigit():
            num += matrix[row][col + 2]
            return num
        elif 0 <= col - 1 < len(matrix[0]) and matrix[row][col - 1].isdigit():
            matrix[row][col - 1] += num
            return num
        else:
            return num
    else:
        return matrix[row][col]


def checkForSecondPart(originalRow, originalCol, currentNumber):
    if 0 <= originalRow - 1 < len(matrix):
        row = originalRow - 1
        col = originalCol - 1
        if 0 <= col < len(matrix[0]):
            charAtCheckPosition = matrix[originalRow - 1][originalCol - 1]  # left and left
            if (charAtCheckPosition.isdigit()):
                if currentNumber != getNum(row, col):
                    return getNum(row, col)

        if matrix[originalRow - 1][originalCol].isdigit():
            if currentNumber != getNum(row, originalCol):
                return getNum(row, originalCol)

        col = originalCol + 1
        charAtCheckPosition = matrix[row][col]
        if 0 <= col < len(matrix[0]):
            if (charAtCheckPosition.isdigit()):
                if currentNumber != getNum(row, col):
                    return getNum(row, col)

    if (0 <= originalCol + 1 < len(matrix[0]) and
            matrix[originalRow][originalCol + 1].isdigit()):
        if currentNumber != getNum(originalRow, originalCol + 1):
            return getNum(originalRow, originalCol + 1)
    if (0 <= originalCol - 1 < len(matrix[0]) and
            not matrix[originalRow][originalCol - 1].isdigit()):
        if currentNumber != getNum(originalRow, originalCol - 1):
            return getNum(originalRow, originalCol - 1)

    if 0 <= originalRow + 1 < len(matrix):
        row = originalRow + 1
        col = originalCol + 1
        if 0 <= col < len(matrix[0]):
            charAtCheckPosition = matrix[row][col]
            if charAtCheckPosition.isdigit():
                if currentNumber != getNum(row, col):
                    return getNum(row, col)

        if (matrix[row][originalCol] != '.' and
                not matrix[row][originalCol].isdigit()):
            if currentNumber != getNum(row, originalCol):
                return getNum(row, originalCol)

        if 0 <= originalCol - 1 < len(matrix[0]):
            col = originalCol - 1
            charAtCheckPosition = matrix[row][col]
            if charAtCheckPosition.isdigit():
                if currentNumber != getNum(row, col):
                    return getNum(row, col)


def checkMatrix(checkPositions, currentNumber):
    for checkPosition in checkPositions:
        originalRow = checkPosition[0]
        originalCol = checkPosition[1]
        # check for diagonal positions
        if 0 <= originalRow - 1 < len(matrix):
            row = originalRow - 1
            col = originalCol - 1
            if 0 <= col < len(matrix[0]):
                charAtCheckPosition = matrix[originalRow - 1][originalCol - 1] # left and left
                if (charAtCheckPosition != '.' and
                        not charAtCheckPosition.isdigit()):
                    return checkForSecondPart(row, col, currentNumber)

            if (matrix[originalRow - 1][originalCol] != '.' and # left and none
                    not matrix[originalRow - 1][originalCol].isdigit()):
                return checkForSecondPart(row, originalCol, currentNumber)

            col = originalCol + 1
            if 0 <= col < len(matrix[0]):
                if (charAtCheckPosition != '.' and # left and right
                        not charAtCheckPosition.isdigit()):
                    return checkForSecondPart(row, col, currentNumber)

        if (0 <= originalCol + 1 < len(matrix[0]) and
                not matrix[originalRow][originalCol + 1].isdigit() and
                matrix[originalRow][originalCol + 1] != '.'):
            return checkForSecondPart(originalRow, originalCol + 1, currentNumber)
        if (0 <= originalCol - 1 < len(matrix[0]) and
                not matrix[originalRow][originalCol - 1].isdigit() and
                matrix[originalRow][originalCol - 1] != '.'):
            return checkForSecondPart(originalRow, originalCol - 1, currentNumber)

        if 0 <= originalRow + 1 < len(matrix):
            row = originalRow + 1
            col = originalCol + 1
            if 0 <= col < len(matrix[0]):
                charAtCheckPosition = matrix[originalRow + 1][originalCol + 1]
                if (charAtCheckPosition != '.' and
                        not charAtCheckPosition.isdigit()):
                    return checkForSecondPart(row, col, currentNumber)

            if (matrix[originalRow + 1][originalCol] != '.' and
                    not matrix[originalRow + 1][originalCol].isdigit()):
                return checkForSecondPart(row, originalCol, currentNumber)

            if 0 <= originalCol - 1 < len(matrix[0]):
                col = originalCol - 1
                charAtCheckPosition = matrix[originalRow + 1][originalCol - 1]
                if (charAtCheckPosition != '.' and  # diagonal right lower
                        not charAtCheckPosition.isdigit()):
                    return checkForSecondPart(row, col, currentNumber)


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

# calculate what are numbers and see what is all around them
file.seek(0)
sumOfPartNums = 0
for indexLine, line in enumerate(file):
    currentNumber = ''
    checkPositions = []
    alreadyChecked = []
    for indexChar, char in enumerate(line):
        if char.isdigit():
            currentNumber += char
            checkPositions.append((indexLine, indexChar))
        elif currentNumber != '':
            if checkMatrix(checkPositions, currentNumber) is not None:
                sumOfPartNums += (int(currentNumber) * int(checkMatrix(checkPositions)))
                alreadyChecked.append(checkMatrix(checkPositions))
            currentNumber = ''
            checkPositions.clear()

print(sumOfPartNums)
file.close()
