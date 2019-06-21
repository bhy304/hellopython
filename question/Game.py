# <Crawling 문제>
# 아래 url에서 랭킹 10위까지만 게임명, 제조사, 평점, 가격을 가져오는 문제입니다. 코드는 다음과 같습니다
# 이를 만족하는 Games class와 Game class를 작성하세요.

from bs4 import BeautifulSoup
import requests

# print(">>>> ", len(card_list_tags), card_list_tags[0].get('class'))
# for i in card_list_tags:
#     cards = i.select('.card')
#     print("len(cards):", len(cards))
#     for c in cards:
#         title = c.select('a.title')[0].text
#         company = c.select('a.subtitle')[0].text
#         rating = c.select('div.current-rating')[0].get('style').split(':')[1].replace("%","")
#         price = c.select('span.display-price')[0].text
#         print("{}\t{}\t{:.2f}\t{}".format(title, company, float(rating), price))

class Game:
    def __init__(self, tag):
        # self.title = c.select('a.title')[0].text
        # self.comp = company = c.select('a.subtitle')[0].text
        self.title = self.get_text(tag, 'a.title')
        self.comp = self.get_attr(tag, 'a.subtitle', 'title')
        self.price = self.get_text(tag, 'span.display-price')
        self.rating = self.get_rating(tag, 'div.current-rating', 'style')

    def get_tag(self, parent_tag, selector):
        return parent_tag.select(selector)

    def get_text(self, parent_tag, selector):
        t = self.get_tag(parent_tag, selector)
        return "" if t == None or len(t) == 0 else t[0].text.strip()
        
    def get_attr(self, parent_tag, selector, attr_name):
        t = self.get_tag(parent_tag, selector)
        return "" if t == None or len(t) == 0 else t[0].get(attr_name).strip()

    def get_rating(self, parent_tag, selector, attr_name):
        percent_strs = self.get_attr(parent_tag, selector, attr_name).split(':')[1]
        return float(percent_strs.replace('%',''))

    def __str__(self):
        return self.to_str()

    def to_str(self):
        return '"{}","{}","{}","{}"'.format(self.title, self.comp, self.rating, self.price)

class Games:
    url = 'https://play.google.com/store/apps/category/GAME/collection/topselling_paid'
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    card_list_tags = html.select('div.id-card-list.card-list.two-cards')
    # print(card_list_tags)

    games = []

    def get_list(self):
        isTest = True
        for i in self.card_list_tags:
            cards = i.select('div.card')
            # print("len(cards):", len(cards))
            tmpi = 0
            for c in cards:
                if isTest:
                    tmpi += 1
                    if tmpi > 10: break
                self.games.append(Game(c))
        # for i in self.games:
        #     print(i)

    def write_csv(self):
        with open("playgoogle.csv", "w", encoding="utf8") as file:
            file.write("title,company,rating,price\n")
            for i in self.games:
                file.write(i.to_str() + "\n")

    def read_csv(self):
        with open("playgoogle.csv", "r", encoding="utf8") as file:
            for line in file:
                print(line, end="")

g = Games()
g.get_list()
g.write_csv()
g.read_csv()