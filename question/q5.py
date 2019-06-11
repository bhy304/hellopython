# 아래의 코드를 한줄로 해보세요.
a = input("입력하시오>> ")
# if a==None or a =='' :
#    print ('none')
# else:
#    print (a)

# 방법1
# print('none') if a == None or a == '' else print(a)

# 방법2
print(a if a else 'none')
# a가 none이거나 길이가 0이면 false로 인식