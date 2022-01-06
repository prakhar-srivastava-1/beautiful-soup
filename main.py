from bs4 import BeautifulSoup
import requests
from title import Title

# url to hit - https://news.ycombinator.com/
response = requests.get("https://news.ycombinator.com/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

all_titles = soup.select(".titlelink")
scores = soup.select(".score")

list_of_titles = list()

for i in range(len(all_titles)):
    if scores[i].text:
        title = Title(all_titles[i].text, all_titles[i].get("href"), scores[i].text)
    else:
        title = Title(all_titles[i].text, all_titles[i].get("href"), "0")
    list_of_titles.append(title)

# titles = [title.text for title in all_titles]
# links = [link.get("href") for link in all_titles]
# points = [point.text for point in ]

for each_news_item in list_of_titles:
    each_news_item.print_title()
