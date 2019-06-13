# 문자열 기본함수
# 문자열 기능은 절대로 자기 자신을 변화시키지 않는다. 
print("Hello World".upper()) # 대문자로
print("Hello World".lower()) # 소문자로

string = "Hello World"
returned = string.upper()
print("string:", string)
print("returned:", returned)

# strip() 함수
input_a = '''
    안녕하세요
 문자열의 함수를 알아봅니다   
'''
print("공백 제거 이전>")
print(input_a)
print()
print("공백 제거 이후>")
print(input_a.strip())
print()
# 문자열의 구성을 파악하는 함수
print("hello world".islower())  
print("hello world".isupper())   
# 문자열 찾기 : 특정 문자가 어디에 위치하는 지 확인
output_a = "안녕안녕하세요".find("안녕")
output_b = "안녕안녕하세요".rfind("안녕")
print("find(): ", output_a)
print("rfind(): ", output_b)
# 문자열 in 연산자
print("안녕" in "안녕하세요") # True 
print("가나" in "안녕하세요") # False
# split() 함수
output = "10 20 30 40 50".split(' ')
print(output) 
