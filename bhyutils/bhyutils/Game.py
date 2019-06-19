# 문제1) 플레이스토어 유료 게임 랭킹 60위까지 스크래핑 후, csv 파일로 저장

class Game:
    def __init__(self, tag):
        # self.title = tag.select('a.title')[0].text.strip()
        # self.comp = c.select('a.subtitle')[0].get('title')
        self.title = self.get_text(tag, 'a.title')
        self.comp = self.get_attr(tag, 'a.subtitle', 'title')
        self.price = self.get_text(tag, 'span.display-price')
        self.rating = self.get_rating(tag, 'div.current-rating', 'style')
        # print("cr_style>> ", cr_style)

    def get_rating(self, parent_tag, selector, attr_name):
        percent_strs = self.get_attr(parent_tag, selector, attr_name).split(':')[1]
        return float(percent_strs.replace('%', ''))

    def get_text(self, parent_tag, selector):
        tag = self.get_tag(parent_tag, selector)
        # return "" if tag == None or len(tag) == 0 else t[0].text.strip()
        # if tag == None or len(tag) == 0:
        #     return ""
        # else:
        #     return tag.text.strip()
        return tag.text.strip()

    def get_attr(self, parent_tag, selector, attr_name):
        tag = self.get_tag(parent_tag, selector)
        if tag != None:
            return tag.get(attr_name).strip()
        else:
            return ""

    def get_tag(self, parent_tag, selector):
        # print(parent_tag)
        tag = parent_tag.select(selector)
        if tag == None or len(tag) == 0:
            return None
        else:
            return tag[0]

    def __str__(self):
        # return self.to_str()
        return "{}\t{}\t{}\t{:.2f}".format(self.title, self.comp, self.price, self.rating)

    # def to_str(self):
    #     return "{}\t{}\t{}\t{:.2f}".format(self.title, self.comp, self.price, self.rating)

if __name__ == "__main__":
    print("=========================", __name__)