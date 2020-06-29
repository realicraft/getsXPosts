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
adate = input("What date was the first post made on? (Give it as YYYY-MM-DD) >")
aday = int(adate[8:10])
amonth = int(adate[5:7])
ayear = int(adate[0:4])
adate = datetime.date(ayear, amonth, aday)
bdate = datetime.date.today()
time.sleep(0.25)
print("So, the first post's date is " + datetime.date.isoformat(adate) + ", and today's date is " + datetime.date.isoformat(bdate) + ". If this is incorrect, run the program again.")
time.sleep(0.25)
print("So... the number of posts so far is...")
time.sleep(2)

apage = requests.get('https://tbgforums.com/forums/viewtopic.php?id=' + str(topicID))
atree = html.fromstring(apage.content)

mostRecentPage = atree.xpath('//*[@id="brdmain"]/div[1]/div/div[1]/p[1]/a[3]/text()')
mostRecentPage = int(mostRecentPage[0])

recentPage = 'https://tbgforums.com/forums/viewtopic.php?id=' + str(topicID) + '&p=' + str(mostRecentPage)

bpage = requests.get(recentPage)
btree = html.fromstring(bpage.content)

postNums = btree.xpath('//span[@class="conr"]/text()')

mostRecentPost = postNums[-1]
mostRecentPost = mostRecentPost[1:]
mostRecentPost = int(mostRecentPost)

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
