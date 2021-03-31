from lxml import html
import requests
import datetime
import sys
import math
import time
import json
import os

print("Unless told otherwise, answer questions with whole numbers, like 42.")
print("The resultant file will be in the same directory that the script is located in.")
time.sleep(0.25)
topicID = int(input("What's the Topic ID of the topic? (The 'id' part of the url) >"))
time.sleep(0.25)
filename = input("What should the name of the output file be? >")
if (filename == ""): filename = "tbgs_export_id" + str(topicID) + "_t" + str(int(time.time()))
filename = filename.split(" ")
filename = "_".join(filename)
time.sleep(0.25)

print("\n\n\nFinding page count...")
apage = requests.get('https://tbgforums.com/forums/viewtopic.php?id=' + str(topicID))
atree = html.fromstring(apage.content)

pageCountEl = atree.xpath('//*[@id="brdmain"]/div[1]/div/div[1]/p[1]/a')
try:
    pageCountEl = pageCountEl[-2]
    pageCount = pageCountEl.attrib["href"]
except IndexError:
    pageCount = "?p=1"
pageCount = int(pageCount.split("=")[-1])
time.sleep(0.5)
print("Found a page count of " + str(pageCount) + ".")

i = 0
postContents = {}

sys.stdout.write("\rGetting data from pages... [0/" + str(pageCount) + "]")
sys.stdout.flush()
if (pageCount >= 100): updateSep = 9
elif (pageCount >= 50): updateSep = 7
elif (pageCount >= 20): updateSep = 5
else: updateSep = 3

while (i < pageCount):
    if ((i != 0) and (i%updateSep == 0)):
        sys.stdout.write("\rGetting data from pages... [" + str(i) + "/" + str(pageCount) + "]")
        sys.stdout.flush()
        #print("Getting data from pages... [" + str(i) + "/" + str(pageCount) + "]")
    j = 0
    k = ""
    postContents[str(i+1)] = []
    bpage = requests.get('https://tbgforums.com/forums/viewtopic.php?id=' + str(topicID) + '&p=' + str(i+1))
    btree = html.fromstring(bpage.content)
    x = btree.xpath('//div[contains(@class, "blockpost")]/div/div[1]/div/div[2]/div[1]')
    while (j < len(x)):
        k = html.tostring(x[j]).decode("utf-8")[28:-18]
        postContents[str(i+1)].append(k)
        j += 1
    i += 1
sys.stdout.write("\rGetting data from pages... [" + str(pageCount) + "/" + str(pageCount) + "]")
sys.stdout.flush()
time.sleep(0.25)
#print(postContents)
#print(json.dumps(postContents))
#print(sys.path[0])

print("\nSaving file...")
filenameFull = filename + ".json"
with open(os.path.join(sys.path[0], filenameFull), "w") as l:
    l.write(json.dumps(postContents, indent=4))
    l.close()
time.sleep(0.5)

print("\nDone! The output can be found at " + str(sys.path[0]) + "\\" + filenameFull)
time.sleep(7.5)

#mostRecentPage = int(mostRecentPage[0])
#
#recentPage = 'https://tbgforums.com/forums/viewtopic.php?id=' + str(topicID) + '&p=' + str(mostRecentPage)
#
#bpage = requests.get(recentPage)
#btree = html.fromstring(bpage.content)
#
#postNums = btree.xpath('//span[@class="conr"]/text()')
#
#mostRecentPost = postNums[-1]
#mostRecentPost = mostRecentPost[1:]
#mostRecentPost = int(mostRecentPost)
