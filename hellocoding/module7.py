# urllib 모듈
# URL : Uniform Resource Locator, 웹브라우저에 치는 주소
from urllib import request
target = request.urlopen("https://google.com")
output = target.read()
print(output)