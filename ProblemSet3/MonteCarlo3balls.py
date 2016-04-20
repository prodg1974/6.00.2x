import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    success = 0
    for trials in range(numTrials):
        c = draw_1()
        if draw_2(c) == c:
#            print "two" + c
            if draw_3(c) == c:
#                print "three" + c
                success +=1
    return success/float(numTrials)

def draw_1():
        if random.random() > 0.5:
            color = 'red'
        else:
            color = 'green'
        return color
def draw_2(color):
        if color == 'red':
            c2 = random.choice(['red','red','green','green','green'])
        else:
            c2 = random.choice(['red','red','red','green', 'green'])
        return c2
def draw_3(color):
        if color == 'red':
            c3 = random.choice(['red','green','green','green'])
        else:
            c3 = random.choice(['red','red','red','green'])
        return c3


for x in range(50):
    noReplacementSimulation(10000)
