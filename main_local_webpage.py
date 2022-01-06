from bs4 import BeautifulSoup

# open the file
with open("website.html", encoding='utf-8') as website_file:
    contents = website_file.read()

soup = BeautifulSoup(contents, 'html.parser')

print(soup.title.name + ":\t" + soup.title.string)
print("First p tag:\n" + str(soup.p))

# get all <a> tags
all_anchor_tags = soup.find_all(name='a')
# list of all anchor tags
print(all_anchor_tags)

# Extract
# 1. text between <a>TEXT</a>
# 2. href link
for anchor_tag in all_anchor_tags:
    print(anchor_tag.string, ":", anchor_tag.get("href"))

# Extract based on attribute value
heading1_with_id_name = soup.find(name="h1", id="name")
print(heading1_with_id_name)

heading3_with_class_heading = soup.find(name="h3", class_="heading")
print(heading3_with_class_heading)

# Extract nested tags
# uses css selector
company_url = soup.select_one(selector="p a")
print(company_url.get("href"))

# use id
name = soup.select_one(selector="#name")
print(name.text)

# use class
heading = soup.select(selector=".heading")
print(heading)