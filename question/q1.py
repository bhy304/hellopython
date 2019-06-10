# 문제1) fruits = {'오렌지': 400, '사과': 200, '바나나': 300} 일때, 오렌지 3개, 사과 2개, 바나나 5개를 샀다면 총 구매액은??

fruits = {'오렌지':400,'사과':200,'바나나':300}
# print(fruits['오렌지'])

total = fruits['오렌지']*3 + fruits['사과']*2 + fruits['바나나']*5
print(total)

# 문제1_변형
fruits={'orange':200, 'apple':300, 'banana':500}
cart = {'orange':3, 'apple':2, 'banana': 2}

total = fruits['orange']*cart['orange'] + fruits['apple']*cart['apple'] + fruits['banana']*cart['banana']
print(total)