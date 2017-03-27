# Go to your favorite follow on Twitter.  (not someone who posts explicit materials please)
# Inspect their twitter feed.
# You'll notice that the tweets are stored in a ordered list <ol></ol>,
# and individual tweets are contained as list items <li></li>.
# Use BeautifulSoup and urllib to grab the text contents of the tweets
# located on the twitter page you chose.  The .text attribute will supply the content of a soup object.
# Have fun.  Again, nothing explicit. (15pts)
import urllib.request
from bs4 import BeautifulSoup

target = "Michael_Daalder"

line = "\n--------------------------------------\n"
print(target + "'s Twitter Feed!\n", line)
for i in [[[y.text.strip() for y in x.findAll("p", {"class": "TweetTextSize"})],
           [y.text.strip() for y in x.findAll("a", {"class": "account-group"})],
           [y.text.strip() for y in x.findAll("small", {"class": "time"})]] for x in
          BeautifulSoup(urllib.request.urlopen("https://twitter.com/" + target).read(), "lxml").find("ol", {
              "class": "stream-items"}).findAll("li", {"class": "stream-item"})][:-1]:
    print("\033[1mOn", i[2][0] + ",", i[1][0], "said:\033[0m")
    print(i[0][0] + "\n", line)
