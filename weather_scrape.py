# Below is a link to a 10-day weather forecast at weather.com
url = "https://weather.com/weather/tenday/l/USIL0225:1:US"
# Use urllib and BeautifulSoup to scrape data from the weather table.
import urllib.request
from bs4 import BeautifulSoup

# Print a brief synopsis of the weather for the next 10 days.
# Include the day, date, high temp, low temp, and chance of rain.
# You can customize the text as you like, but it should be readable
# for the user.  You will need to target specific classes or other
# attributes to pull some parts of the data.
# (e.g.  Wednesday, March 22: the high temp will be 48 with a low of 35, and a 20% chance of rain). (25pts)
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "lxml")
if soup.find("table"):
    data_list = [[y.text.strip() for y in x.findAll("td")][1:] for x in soup.find("table").findAll("tr")][1:]
    data_list[0][0] = "Now" + data_list[0][0][5:]
    for day in data_list:
        print(day[0][:3] + ", " + day[0][3:] + ": will be " + day[1] + ". The high temp will be " +
              day[2].split("°")[0] + " with a low of " +
              day[2].split("°")[0] + ", and a " + day[3] + " chance of rain.")
else:
    print("Try again -- your connection is bad.")
