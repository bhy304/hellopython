# Boolean : True 또는 False를 갖는 값

# - 비교연산자(비교할 때 사용하는 연산자)
print(10 == 100) # False
print(10 != 100) # True
print(10 > 100) # False
print(10 < 100) # True
print(10 >= 100) # False
print(10 <= 100) # True
# 문자열비교에도 비교연산자를 사용할 수 있음!
print("가" < "하") # True

# - 논리연산자(불에 적용하는 연산자)
# 단항연산자 -> 피연산자가 하나
# 이항연산자 -> 피연산자가 두 개 

# not -> 단항연산자(True->False, False->True)
print(not True)
print(not False)

x = 10
is_under_30 = x < 30
print(not is_under_30)

# and -> 이항연산자 : 둘 다 참일 때만 참
True and True
False and True
True and False
False and False

# or  -> 이항연산자 : 하나만 참이어도 참
True or True
False or True
True or False
False or False