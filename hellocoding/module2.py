# Ref: https://docs.python.org/3/library/index.html

# random 모듈
import random
print(random.random()) # 0부터 1사이
print(random.uniform(10, 20)) # 첫번째 매개변수부터 두번째 매개변수까지 
print(random.randrange(10)) # 10까지의 정수 중에 하나 
print(random.randrange(0, 101, 2)) # 0부터 100까지의 수 중 짝수만 
print(random.choice(['a', 'b', 'c'])) # 리스트 중 하나 
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(a) 
print(a)