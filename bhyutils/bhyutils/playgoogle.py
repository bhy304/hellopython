from bs4 import BeautifulSoup
import requests
# from Game import Game
from bhyutils.Game import Game

url = 'https://play.google.com/store/apps/category/GAME/collection/topselling_paid'
res = requests.get(url)
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
card_list = soup.select('div.card-list')
# print(card_list)

# print(">>>>>>", type(card_list), type(card_list[0]))
games = []
isTest = True # QQQ: 배포시 False로 할 것!
for i in card_list:
    cards = i.select('div.card')
    # print("len(cards): ", len(cards))
    tmpi = 0
    for c in cards:
        if isTest:
            tmpi += 1
            if tmpi > 10 : break
        games.append(Game(c))

# QQQ
for i in games:
    print(i)

with open("games.csv", "w", encoding="utf8") as file:
    file.write("게임명\t제조사\t가격\t평점\n")
    for i in games:
        file.write(str(i) + "\n")

# 문제2) 각 게임의 상세페이지로 가서 출시일 등 기타정보 수집