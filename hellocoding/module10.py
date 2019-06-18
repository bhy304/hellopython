# https://www.youtube.com/watch?v=tuKVinbAZow&list=PLBXuLgInP-5nbu5s5TuNbD6-4qh3Mgoor&index=61

# 제어 역전(Inversion of Control) 여부에 따라서 달라짐
# 라이브러리 : 정상적인 제어를 하는 모듈
# 프레임워크 : 제어 역전이 발생하는 모듈

# 제어 정방향
# 우리가 만든 코드 → 모듈[다른 사람이 만든 것] : 라이브러리

# 제어 역방향
# 우리가 만든 코드 ← 모듈[다른 사람이 만든 것] : 프레임워크

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"