import string
import ps1_pkgtest
import pylab
PATH_TO_FILE = '/Users/paulr/Documents/Courses/6.00.2x/ProblemSet1/julyTemps.txt'

def loadData():
       
        highs = []
        lows = []
        extremes = ()
        print PATH_TO_FILE
	inFile = open(PATH_TO_FILE, 'r', 0)
	for rec in inFile:
	    data=rec.split()
	    if len(data) == 3 and data[0] != 'Boston' and data[0] !="" and data[0] !="Day":
	       highs.append(int(data[1]))
	       lows.append(int(data[2]))
	extremes = (highs,lows)
	#extremes[1] = lows
	return extremes
	#print "  ", len(wordlist), "records loaded."
	#return wordlist
def producePlot(lowTemps,highTemps):
    ctr = None
    diffTemps = []
    for t in highTemps:
        if ctr == None:ctr=0
        diffTemps.append(highTemps[ctr] - lowTemps[ctr])
        ctr += 1
    pylab.plot(range(1,32),diffTemps)
#inFile=file.open('julyTemps.txt',r)
temps=loadData()
producePlot(temps[1],temps[0])