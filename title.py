class Title(object):

    def __init__(self, news_title, link, score):
        self.news_title = news_title
        self.link = link
        self.score = score

    def print_title(self):
        print(self.news_title, "->", self.link, "|", self.score)

