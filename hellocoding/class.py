# 클래스(https://www.youtube.com/watch?v=Np6Wy5mpyMA&list=PLBXuLgInP-5nbu5s5TuNbD6-4qh3Mgoor&index=64)

# def create_student(name, korean, math, english, science):
#     return {
#         "name" : name,
#         "korean" : korean,
#         "math" : math,
#         "english" : english,
#         "science" : science
#     }

# count = 0
class Student:
    count = 0
    # 생성자
    def __init__(self, name, korean, math, english, science):
        # global count
        Student.count += 1
        self.name = name # self : 객체 자신을 나타내는 것
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())
    
    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

    def __eq__(self, value):
        print("eq 함수가 호출되었습니다.")
        return True

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

@classmethod
def count(cls):
    # global count
    print(Student.count)

# students = [
#     Student("윤인성", 87, 98, 88, 95),
#     Student("연하진", 92, 98, 96, 98),
#     Student("구지연", 76, 96, 94, 90),
#     Student("나선주", 98, 92, 96, 92),
#     Student("윤아린", 95, 98, 98, 99),
#     Student("윤명월", 64, 88, 92, 92),
#     Student("김미화", 82, 86, 98, 88),
#     Student("김연화", 88, 74, 78, 92),
#     Student("박아현", 97, 92, 88, 95),
#     Student("서준서", 45, 52, 72, 78)
# ]

# print("이름", "총점", "평균", sep="\t")
# for student in students:
#     print(student.to_string())

# 어떤 클래스의 인스턴스인지 확인하기
# a = Student("윤인성", 87, 98, 88, 95)
# bool_value = isinstance(a, Student)
# print(bool_value)

# 특수한 이름의 메서드
# print(a.to_string())
# print(str(a))
# print(a == a)

Student("윤인성", 87, 98, 88, 95)
Student("윤인성", 87, 98, 88, 95)
Student("윤인성", 87, 98, 88, 95)
Student("윤인성", 87, 98, 88, 95)
# print(count)
# student_count()
# print(student_count)
Student.count()
