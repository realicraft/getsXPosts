from lxml import html
import requests
import datetime
import sys
import math
import time

print("Unless told otherwise, answer questions with whole numbers, like 42.")
time.sleep(0.25)
topicID = int(input("What's the Topic ID of the topic? (The 'id' part of the url) >"))
time.sleep(0.25)
goal = int(input("How many posts needed to complete the thread? (Total, not remaining) >"))
time.sleep(0.25)

apage = requests.get('https://tbgforums.com/forums/viewtopic.php?id=' + str(topicID))
atree = html.fromstring(apage.content)

mostRecentPage = atree.xpath('//*[@id="brdmain"]/div[1]/div/div[1]/p[1]/a[3]/text()')
mostRecentPage = int(mostRecentPage[0])

adate = atree.xpath('//*[@id="brdmain"]/div[2]/h2/span/a/text()')
adate = adate[0]
aday = int(adate[9:11])
amonth = adate[5:8]
ayear = int(adate[0:4])
if (amonth == "Jan"): amonth = 1
elif (amonth == "Feb"): amonth = 2
elif (amonth == "Mar"): amonth = 3
elif (amonth == "Apr"): amonth = 4
elif (amonth == "May"): amonth = 5
elif (amonth == "Jun"): amonth = 6
elif (amonth == "Jul"): amonth = 7
elif (amonth == "Aug"): amonth = 8
elif (amonth == "Sep"): amonth = 9
elif (amonth == "Oct"): amonth = 10
elif (amonth == "Nov"): amonth = 11
elif (amonth == "Dec"): amonth = 12
else: sys.exit("It looks like the date isn't valid. This may be caused by the first post being too recent.")
adate = datetime.date(ayear, amonth, aday)

recentPage = 'https://tbgforums.com/forums/viewtopic.php?id=' + str(topicID) + '&p=' + str(mostRecentPage)

bpage = requests.get(recentPage)
btree = html.fromstring(bpage.content)

postNums = btree.xpath('//span[@class="conr"]/text()')

mostRecentPost = postNums[-1]
mostRecentPost = mostRecentPost[1:]
mostRecentPost = int(mostRecentPost)

bdate = datetime.date.today()
time.sleep(0.25)
print("So, the first post's date is " + datetime.date.isoformat(adate) + ", and today's date is " + datetime.date.isoformat(bdate) + ". If this is incorrect, run the program again.")
time.sleep(0.25)
print("So... the number of posts so far is...")
time.sleep(2)
print(str(mostRecentPost) + "!")
time.sleep(0.25)
diff = bdate - adate
diff = diff.days
print("And there have been " + str(diff) + " days since the first post.")
ppd = mostRecentPost / diff
time.sleep(0.25)
print("That's about... " + str(round(ppd, 5)) + " posts per day.")
time.sleep(0.25)
until = math.ceil(goal / ppd)
print("So that means it will have been around... " + str(until) + " days since the first post, when you reach the goal.")

cdate = adate + datetime.timedelta(days=until)
print("That means the end date is on " + datetime.date.isoformat(cdate) + "!")
time.sleep(5)
