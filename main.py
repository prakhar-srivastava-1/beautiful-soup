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


