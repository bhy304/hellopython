arr = []
for i in range(0,20,2):
    arr.append(i)
    print(i)

# 위와 동일한 결과를 내는 코드를 한 줄로 작성하세요.

#방법1
xs = list(range(0,20,2))
print(xs)

#방법2
print(list([i for i in range(0,20,2)]))