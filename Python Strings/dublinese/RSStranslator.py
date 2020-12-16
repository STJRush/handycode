from urllib.request import urlopen
from xml.dom import minidom
import collections

# THIS IS CONFUSING. MAYBE SCROLL DOWN.
# extract the headlines from the feed
def extractString(doc):
   str = ""
   for node in doc.getElementsByTagName('channel'):
      for title in node.getElementsByTagName('title'):
         str = str + title.firstChild.data + "\n"
   return str

# KEEP SCROLLING
# extract the feed from the url
def getRSSString(url):
    results = []
    rssString = ""
    results.append(minidom.parse(urlopen(url)))
    for webDoc in results:
        rssString = rssString + extractString(webDoc)
    return rssString



# OKAY START HERE ...

# Reads the RSS feed from the URL provided
feed = getRSSString("http://www.rte.ie/news/rss/news-headlines.xml")

# Display the results
# Here it replaces the word "the" with "da bleedin". 
feed=feed.replace(" the "," da bleedin ")
feed=feed.replace(" to "," ta ")
feed=feed.replace(" of "," ah da ")
feed=feed.replace(" for "," fur da ladz and fur ")
feed=feed.replace(" in "," in feck'n ")
feed=feed.replace("Dublin"," da ci-ee ")
feed=feed.replace(" on "," an da feck'n ")
feed=feed.replace(" a "," ableed'n ")
feed=feed.replace("after "," aftur goin'n ")
feed=feed.replace(" over "," cos ah da bleedin  ")
feed=feed.replace(" can "," mite as well ya know ")
feed=feed.replace(" man "," lad ")
feed=feed.replace(" Sinn Féin "," da Shinners ")
feed=feed.replace(" changes "," feck'n around with ")
feed=feed.replace(" today "," today of all bleed'n dayz ladz ")
feed=feed.replace(" suspect "," feck'n ganster mad lad ")
feed=feed.replace(" investigation ","  investigaaaahin by da Gardee shicka lonnies ")
feed=feed.replace(" need "," need some bleed'n whatcha call'm...  ")
feed=feed.replace(" into "," inta whatchama call its...  ")
feed=feed.replace(" migrant"," fardinner")

words=feed.split()
print(collections.Counter(words).most_common(5))



print(feed)
# Display the number of lines
print("There are %d lines in this feed" %feed.count("\n"))

