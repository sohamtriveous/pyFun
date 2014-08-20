import sys
import random


def sortByCount(countTuple):
    '''
    Returns the current count in the countTuple
    :param countTuple: the tuple, that contains the current count
    :return: the current count in the tuple
    '''
    return countTuple[-1]


def wordCalc(filepath):
    '''
    Calculates the word frequency and then creates a next word dictionary
    Post that, it will create a random sentence based on the dictionary
    :param filepath: The path of the file that needs to be processed
    '''
    # open a file
    file = open(filepath, 'rU')
    # initialize the dictionaries
    fileDictionary = {}
    nextWordDictionary = {}
    for line in file:
        wordList = line.split()
        for word in wordList:
            word = word.lower()
            if fileDictionary.get(word) == None:
                # this is when you have to create a new dictionary entry for the word
                fileDictionary[word] = 1
                nextWordDictionary[word] = []
            else:
                # dictionary entry already exists, populate the next word dictionary
                fileDictionary[word] = fileDictionary[word] + 1
                nextWordDictionary.setdefault(lastWord, []).append(word)
            lastWord = word;
    # sort the dictionary items into a tuple
    tupleList = sorted(fileDictionary.items(), key=sortByCount, reverse=True)
    # print the sorted list of dictionary items
    print tupleList
    # list the next word dictionary items
    print nextWordDictionary.items()
    # generate the random text
    generateText(nextWordDictionary)
    return


def generateText(nextWordDictionary={}):
    '''
    Generates some random sentences based on the nextWordDicionary created in the last stage
    :param nextWordDictionary: the dictionary where the words that are post the current word are mentioned
    :return:
    '''

    size = len(nextWordDictionary)
    # choose a random starting word
    index = random.randint(0, size)
    # find the word that is at this position
    word = nextWordDictionary.keys()[index]
    print word,
    while (nextWordDictionary[word]):
        size = len(nextWordDictionary[word])
        if (size > 0):
            # select a random next word in the nextWordDictionary
            index = random.randint(0, size - 1)
            word = nextWordDictionary.setdefault(word, [])[index]
            print word,
        else:
            break
    return


wordCalc(sys.argv[1])