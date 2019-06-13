# 문자열로 바꾸기

# - str() 함수
# str(<다른 자료형>)
str_int_a = str(52)
str_float_a = str(52.273)
print(str_int_a, type(str_int_a))
print(str_float_a, type(str_float_a))

# - format() 함수 
# "{}".format(10)
# "{} {}".format(10, 20)
str_a = "{} {}".format(10, 20)
print(str_a)
print(type(str_a))