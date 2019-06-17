# try except 구문 사용
try:
    # 파일 열기
    file = open("file.txt","w")
    # 여러 가지 처리를 수행
    # djska;jf;kj;akdfj;asf

except Exception as e:
    print(e)
finally:
    # 파일 닫기
    file.close()
    
print("# 파일이 제대로 닫혔는 지 확인하기")
print("file.closed:", file.closed)