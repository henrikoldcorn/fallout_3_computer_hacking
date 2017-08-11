from functools import reduce
def lettersCorrect(guess, word):
                 # string, string
                 
    correct = 0
    for i in range(len(guess)):
        if guess[i] == word[i]:
            correct += 1
    return correct
def matchesAll(word, triedWords):
            #  string, dict
            
    for test in triedWords:
        if lettersCorrect(word, test) != int(triedWords[test]):
            return False
    return True
        
def solve(triedWords, allWords):
    #     dict,       list
    # triedWords: {words1:letterscorrect} etc
    
    results = []
    for word in allWords:
        if matchesAll(word, triedWords):
            results.append(word)
    return results

def run():
    allWords = []
    triedWords = {}
    word = input("Please enter [word] or [word matches]:\n")
    while word:
        splitWord = word.split(" ")
        allWords.append(splitWord[0])
        if len(splitWord) > 1:
            triedWords[splitWord[0]] = splitWord[1]
        word = input()
    print(solve(triedWords, allWords))
    while True:
        word = input("add more words:\n")
        while word:
            splitWord = word.split(" ")
            allWords.append(splitWord[0])
            if len(splitWord) > 1:
                triedWords[splitWord[0]] = splitWord[1]
            word = input()
        print(solve(triedWords, allWords))
"""
F5 to run, Crtl-C to cancel or close

Example: given words "one", "two", "six"
try two words at random, or beter, choose different words (i.e. not both ending -"ing"
here if solution is "six", and you tried "one" and "two", both will give scores of 0
run program, using IDLE or Spyder or bash or whatever
enter:
one 0
two 0
six

i.e. enter each word, followed by a space and a number if the word has been tried, followed by the enter key
when all words are entered, press enter twice
possible matches will be given
if more than one is available, pick one, and then enter the word again but this time with its score

I've found 2 initial guesses on the computer to work best, more than one possible answer is unusual

"""
run()
