# <Crawling 문제>
# 아래 url에서 랭킹 10위까지만 게임명, 제조사, 평점, 가격을 가져오는 문제입니다. 코드는 다음과 같습니다
# 이를 만족하는 Games class와 Game class를 작성하세요.

class Game:
    def __init__(self, tag):
        pass

url = 'https://play.google.com/store/apps/category/GAME/collection/topselling_paid'
response = requests.get(url)

#html 읽음 
html = BeautifulSoup(response.text, 'html.parser')

#tag 가져오기 
card_list_tags = html.select('div.id-card-list.card-list.two-cards')