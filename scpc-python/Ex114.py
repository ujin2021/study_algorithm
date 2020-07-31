import sys

inf = sys.stdin 

T = inf.readline()

def getTime(time):
    start = time.split()[0]
    end = time.split()[1]
    hours = int(end.split(":")[0]) - int(start.split(":")[0])
    minutes = int(end.split(":")[1]) - int(start.split(":")[1])
    if minutes < 0:
        minutes = minutes + 60
        hours = hours - 1
    return '%02d:%02d' %(hours, minutes)

for t in range(0, int(T)):
    time = inf.readline()
    Answer = getTime(time)
    print('Case #%d' %(int(t)+1))    
    print(Answer)
inf.close()