import string
PATH_TO_FILE = 'ProblemSet1/BostonTemp.txt'

def loadData():
	inFile = open(PATH_TO_FILE, 'r', 0)
	for rec in inFile:
		wordlist = string.split(line)
	print "  ", len(wordlist), "records loaded."
	return wordlist

#inFile=file.open('julyTemps.txt',r)
