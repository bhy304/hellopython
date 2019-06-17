# finally 구문이 의미를 갖는 경우

def test():
    print("함수 시작 부분")
    try:
        print("try 구문의 1번 지점")
        # return
        # print("try 구문의 2번 지점")
        djakfj;ksdjf;aksjfk
    except:
        print("except 구문 1번 지점")
        return
        print("except 구문 2번 지점")
    finally:
        print("finally 구문 지점")
    print("함수 끝 부분")

test()