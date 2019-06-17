# 바이너리 데이터
# 텍스트 데이터 : 텍스트로 인식할 수 있는 데이터 

# 텍스트 데이터를 다루는 방법
# file = open("test.py","r")
# textdata = file.read()
# file.close()
# print(type(textdata))

# 바이너리 데이터를 다루는 방법 = 큰 의미: 컴퓨터 내부에 있는 모든 파일
# file = open("test.py","rb")
# textdata = file.read()
# file.close()
# print(type(textdata))
# print(textdata)

# 바이너리 데이터
# 모듈을 읽어들인다.
from urllib import request
# urlopen() 함수로 구글의 메인 페이지를 읽는다.
target = request.urlopen("http://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)
# write binary[바이너리 쓰기] 모드로
file = open("output.png","wb")
file.write(output)


file = open("output.png", "r") # UnicodeDecodeError 발생
data = file.read()
file.close()
print(data)