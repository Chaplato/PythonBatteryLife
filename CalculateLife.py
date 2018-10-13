import time
import datetime

dt = datetime.datetime.now()
dth = datetime.datetime.now().hour
dtm = datetime.datetime.now().minute


potato = 1
seconds = 0
minutes = 0
hours = 0
days = 0


filestring = str(dth)+"-"+str(dtm)+".txt"
print (filestring)
file = open(filestring,"w")

file.write ("A text file written for writing the amount of time the pi has been on for"+"\n")

file.close()
file
print (file)

while (potato == 1):
    time.sleep(5)
    dt = datetime.datetime.now()
    seconds += 5
    if (seconds >= 60):
        seconds -= 60
        minutes += 1
    if (minutes >= 60):
        hours += 1
        minutes -= 60
    if (hours >= 24):
        hours -= 24
        days += 1
    string = (days,' days,',hours,' hours,',minutes,' minutes',seconds,' seconds')
    print (string,)
    file = open (filestring,"a")
    file.write(str(dt))
    file.write(str(string)+ "\n")
    file.close()
    print (str(dt))
    
    
