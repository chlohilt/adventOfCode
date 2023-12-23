file = open('fourthDay.txt', 'r')

sumScratchcards = 0

def process_cards(counts, first_card_count):
    for card in first_card_count:
        # TODO: have to recurse on each card copy and add more copies
    # Check if there are any cards to process
    if counts == first_card_count:
        return counts

    # Recursively process the next set of cards
    return process_cards(cards, counts)


def total_cards():
    # Initialize counts with 0 for each number of copies
    games = sum(1 for line in file)
    file.seek(0)
    counts = [0] * games

    first_card_count = original_cards(counts)
    # Process the original set of cards
    process_cards(counts, first_card_count)

    # Calculate the total number of cards
    total = sum(counts)
    #return total


def original_cards(counts):
    for line in file:
        indexSpace = line.find(' ')
        indexColon = line.find(':')
        substringAfterGameNumber = line[indexColon + 2:].strip()
        gameNumber = line[indexSpace + 1: indexColon].strip()

        indexLine = substringAfterGameNumber.find('|')
        winningNumbersLine = substringAfterGameNumber[:indexLine]
        possibleNumbersLine = substringAfterGameNumber[indexLine + 1:]

        winningNumbers = winningNumbersLine.split()
        possibleNumbers = possibleNumbersLine.split()

        matchingNumbers = 0
        for possibleNumber in possibleNumbers:
            if possibleNumber in winningNumbers:
                matchingNumbers += 1

        for x in range(matchingNumbers):
            counts[int(gameNumber) + x] += 1

    return counts

total_cards()
file.close()