# 바이널 = 이진(0101010101010)과 같은 형태
# 텍스트 파일 : 메모장으로 읽을 수 있다. 
# 바이너리 파일 :메모장으로 읽을 수 없다. 

# 텍스트 파일 처리
# 방법_1
# mode : r 읽기, w 쓰기, a 뒤에 붙여 쓸 때 
# 1. 파일 열기 -> open()
file = open("abcdef.txt", mode="a",encoding="UTF8")
# 2. 파일 읽기 -> file.read()
print(file.read())
# 3. 파일 쓰기 -> file.write()
file.write("abcdef")
# 4. 파일 닫기 -> file.close()
file.close()

# 방법_2
with open("abcdef.txt", mode="a", encoding="UTF8") as file:
    file.write("123456789")