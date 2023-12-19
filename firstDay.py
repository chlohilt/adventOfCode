def checkLetters(input_array):
    word = ''
    for letter in reversed(input_array):
        word = letter + word

        if 'one' in word:
            return '1'
        elif 'two' in word:
            return '2'
        elif 'three' in word:
            return '3'
        elif 'four' in word:
            return '4'
        elif 'five' in word:
            return '5'
        elif 'six'in word:
            return '6'
        elif 'seven' in word:
            return '7'
        elif 'eight' in word:
            return '8'
        elif 'nine' in word:
            return '9'
    return None


file = open("firstDayInput.txt", "r")

sum = 0

for x in file:
    lineSum = ''
    firstNum = '0'
    secondNum = '0'
    firstLetters = []
    secondLetters = []
    for i in x:
        if firstNum == '0' and i.isalpha():
            firstLetters.append(i)
            checkLettersResult = checkLetters(firstLetters)
            if checkLettersResult != None:
                firstNum = checkLettersResult
        elif i.isalpha():
            secondLetters.append(i)
            checkLettersResult = checkLetters(secondLetters)
            if checkLettersResult != None:
                secondNum = checkLettersResult
                secondLetters = secondLetters[-1:]

        if i.isdigit() and firstNum == '0':
            firstNum = i
        elif i.isdigit():
            secondNum = i
    if secondNum == '0' or secondNum == None:
        secondNum = firstNum
    lineSum += firstNum
    lineSum += secondNum
    sum += int(lineSum)

print(sum)