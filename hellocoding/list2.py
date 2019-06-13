# 리스트에 요소 추가하기
# <리스트>.append(<요소>)
# <리스트>.insert(<위치>,<요소>)
# <리스트>.extend(<리스트>)

list_a = [1,2,3]
list_a.append(4) # list_a = [1,2,3,4]
print(list_a)
list_a.insert(0, 0) # list_a = [0,1,2,3,4]
print(list_a)
list_a.insert(1, 10) # list_a = [0,10,1,2,3,4]
print(list_a)
list_a.extend([1,2,3,4]) # list_a = [0,10,1,2,3,4,1,2,3,4]
print(list_a)
list_a.append([1,2,3,4]) # list_a = [0,10,1,2,3,4,1,2,3,4,[1,2,3,4]]
print(list_a)

# 리스트의 요소 제거하기
# <리스트>.pop(<인덱스>)
list_a.pop(0)
print(list_a)
list_a.pop() # 가장 마지막 요소 제거
print(list_a)

# 리스트의 요소 모두 제거하기
# <리스트>.clear()
list_a.clear() 
print(list_a)

# del <리스트>[<인덱스>]
list_a = [1,2,3]
list_a.pop(-2)
del list_a[-1]
# del list_a[2]
# del list_a[0]
print(list_a)

# in 연산자
# <요소> in <리스트>
list_a = [1,2,3]
print(1 in list_a)
print("안녕" in "안녕하세요")