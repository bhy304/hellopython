# 리스트 : 여러 가지 자료를 저장할 수 있는 자료
# 생성 방법 : [<요소(element)>,<요소>,<요소>...]
# 예) [1, 2, 3, 4, 5]
list_a = []
list_b = [1, 2, 3, 4, 5, 6, 7]
list_c = [1, "반복문", 3, True]
list_d = [[1,2,3], [4,5,6], [7,8,9]]

# 접근 연산자
print(list_b[0])
print(list_b[1])
print(list_b[-1])
print(list_b[-2])

print(list_c[1])
print(list_c[1][0])

print(list_d[1])
print(list_d[1][1])

# 결합/연결 연결자
print(list_b + list_c)

# 반복 연산자
print(list_b * 3)