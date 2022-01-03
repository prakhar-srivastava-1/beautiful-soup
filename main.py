from bs4 import BeautifulSoup

# open the file
with open("website.html", encoding='utf-8') as website_file:
    contents = website_file.read()

soup = BeautifulSoup(contents, 'html.parser')

print(soup.title.name + ":\t" + soup.title.string)
print("First p tag:\n" + str(soup.p))


