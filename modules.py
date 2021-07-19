import getpass
import time

def TimeToday():
    TheTime = time.asctime
    with open("timenow.txt", "w") as to:
        to.write(TheTime)
    with open("timenow.txt", "r") as tr:
        timeread = tr.read()
        print(timeread)

        return timeread

    