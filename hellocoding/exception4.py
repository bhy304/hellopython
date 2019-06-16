# 예외 발생시키기
# try:
#     raise NotADirectoryError("메시지")
# except NotADirectoryError as error:
#     print(error)

# ref : https://github.com/keras-team/keras/search?q=raise&unscoped_q=raise

def average_score(scores):
    for score in scores:
        if not 0 <= score <= 100:
            raise ValueError("점수이므로 0점과 100점 사이를 입력해주세요.")
    return sum(scores) / len(scores)

average_score([100, 90, 30, 60, 50, 100])