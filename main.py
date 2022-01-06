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

#
# # open the file
# with open("website.html", encoding='utf-8') as website_file:
#     contents = website_file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# print(soup.title.name + ":\t" + soup.title.string)
# print("First p tag:\n" + str(soup.p))
#
# # get all <a> tags
# all_anchor_tags = soup.find_all(name='a')
# # list of all anchor tags
# print(all_anchor_tags)
#
# # Extract
# # 1. text between <a>TEXT</a>
# # 2. href link
# for anchor_tag in all_anchor_tags:
#     print(anchor_tag.string, ":", anchor_tag.get("href"))
#
# # Extract based on attribute value
# heading1_with_id_name = soup.find(name="h1", id="name")
# print(heading1_with_id_name)
#
# heading3_with_class_heading = soup.find(name="h3", class_="heading")
# print(heading3_with_class_heading)
#
# # Extract nested tags
# # uses css selector
# company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))
#
# # use id
# name = soup.select_one(selector="#name")
# print(name.text)
#
# # use class
# heading = soup.select(selector=".heading")
# print(heading)