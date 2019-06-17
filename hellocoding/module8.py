# 조건문 반복문 함수 : 재귀함수
# 모듈 : os 모듈
import os

# for path in os.listdir("."):
#     if os.path.isdir(path):
#         print(path, "은 디렉터리입니다.")
#     else:
#         print(path, "은 파일입니다.")

def read_folder(path):
    for path in os.listdir(path):
        if os.path.isdir(path):
            read_folder(path)
        else:
            print(path)

read_folder(".")