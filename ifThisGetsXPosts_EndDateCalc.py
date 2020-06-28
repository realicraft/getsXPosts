import datetime
import sys
import math
import time

print("Please use whole numbers (such as 42) for all inputs unless specified.")

goal = int(input("What is the goal number of posts? "))

ayear = int(input("What year was the first post? "))
amonth = int(input("What month in that year was the first post? "))
aday = int(input("What day in that month was the first post? "))
adate = datetime.date(ayear, amonth, aday)
bdate = datetime.date.today()
print("So, the first post's date is " + datetime.date.isoformat(adate) + ", and today's date is " + datetime.date.isoformat(bdate) + ". Is this correct? (Y/N)")

isCorrect = input("> ")
if isCorrect == "Y" :
    pass
else:
    sys.exit("Please enter the correct date and make sure your computer's date is properly set.")

diff = bdate - adate
diff = diff.days
print("So that means there have been " + str(diff) + " days since the first post.")
posts = int(input("How many posts have been made so far, including the first? "))
ppd = posts / diff
print("That's " + str(round(ppd, 5)) + " posts per day!")
print("You need to get to post " + str(goal) + " to win.")
until = math.ceil(goal / ppd)
print("At this rate, it will be around " + str(until) + " days since the first post.")

cdate = adate + datetime.timedelta(days=until)
print("The end date comes out to be:")
print(datetime.date.isoformat(cdate))

mid = math.ceil((goal / 2) / ppd)
if (posts > (goal / 2)):
    phrase = "was "
else:
    phrase = "will be "
print("At this rate, the midpoint " + phrase + str(mid) + " days since the first post.")

ddate = adate + datetime.timedelta(days=mid)
print("So the midpoint will be on:")
print(datetime.date.isoformat(ddate))

time.sleep(5)
