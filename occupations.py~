from random import random

##def readFile():
##    file_ = open('occupations.csv')
##    instream = file_.readlines()

def readFile():
    try:
        with open('occupations.csv') as file_:
            instream = file_.readlines()
        classPercentages = {}
        for line in instream[1:]:
            line = line.strip('\r\n')
            percentage = float(line[line.rfind(',') + 1:])
            jobClass = line[:line.rfind(',')]
            classPercentages[jobClass] = percentage
        classPercentages['Unemployed']  = .2
        del classPercentages['Total']
        return classPercentages
    except (OSError, IOError) as e:
        print "File not found..."
    except Exception:
        print "Unknown error occured"
        
def getOccupation():
    classPercentages = readFile()
    if classPercentages is None:
        print "Error generating dictionary"
        raise SystemExit(0)
    choice = 100 * random()
    beginningValue = 0
    for i in classPercentages:
        value = classPercentages[i]
        if choice > beginningValue and choice < (beginningValue + value):
            return i
        beginningValue += value

if __name__ == '__main__':
    result = {}
    for i in xrange(100):
        occupation = getOccupation()
        if occupation in result:
            result[occupation] +=1
        else:
            result[occupation] = 1
    classPercentages = readFile()
    for i in classPercentages:
        print i, classPercentages.get(i), result.get(i)
