# 문자 선택 연산자 : []
# <문자열>[<숫자>]
print("안녕하세요"[-1])
print("안녕하세요"[-2])
print("안녕하세요"[-3])
print("안녕하세요"[-4])
print("안녕하세요"[-5])

print("안녕하세요[-4:-2]:", "안녕하세요"[-4:-2])
print("안녕하세요[-2:-4]:", "안녕하세요"[-2:-4])

# 에러 발생 : 범위를 넘는 부분을 선택
# IndexError: string index out of range 
# print("안녕하세요"[10]) 

# TypeError
# print("안녕하세요" + 50)

# SyntaxError
# print("안녕하세요"