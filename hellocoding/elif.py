# elif 구문
'''
if <조건A>:
    <조건A가 참일 때 실행할 문장>
elif <조건B>:
    <조건B가 참일 때 실행할 문장>
elif <조건C>:
    <조건C가 참일 때 실행할 문장>
elif <조건D>:
    <조건D가 참일 때 실행할 문장>
else:
    <모든 조건이 거짓일 때 실행할 문장>
'''
import datetime
now = datetime.datetime.now()
month = now.month

# 봄
if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!".format(month)) 
# 여름
elif 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다!".format(month)) 
# 가을
elif 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다!".format(month)) 
# 겨울
else:
    print("이번 달은 {}월로 겨울입니다!".format(month)) 