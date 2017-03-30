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
# target = "JohnIaconianni"

print(target + "'s Twitter Feed!\n")
for i in [[[y.text.strip().split() for y in x.findAll("p", {"class": "TweetTextSize"})],
           [y.text.strip().replace("Verified account", "").replace("@", "\033[36m@") + "\033[1m" for y in
            x.findAll("a", {"class": "account-group"})],
           [y.text.strip()[y.text.strip().find([s for s in y.text.strip() if not s.isdigit()][0]):] for y in
            x.findAll("small", {"class": "time"})]] for x in
          BeautifulSoup(urllib.request.urlopen("https://twitter.com/" + target).read(), "lxml").find("ol", {
              "class": "stream-items"}).findAll("li", {"class": "stream-item"})][:-2]:
    if i[2][0][1].isdigit():
        i[2][0] = "About " + i[2][0][1:]
    else:
        i[2][0] = "On " + i[2][0]
    tt = ''
    z = 1
    for n in i[0][0]:
        if n[0] == '#':
            n = "\033[92m" + n + "\033[0m"
        elif n[0] == '@':
            n = "\033[36m" + n + "\033[0m"
        tt += (n + " " + ("\n" if not z % 8 else ""))
        z += 1
    tt = "\t\033[0m| " + tt.replace("http", "\nhttp").replace("pic.twitter.com",
                                                     "\n\033[94mimage at http://pic.twitter.com").replace(
        "\n", "\n\t\033[0m| ") + "\033[0m\n"
    print("\033[1m" + i[2][0] + ",", i[1][0], "said:\033[0m")
    print("\t ___________________________________________\n\t/\n" + tt + "\t\\\n\t --------------------------------------------\n")
