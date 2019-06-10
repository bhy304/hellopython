from functools import reduce

def write_file():
    with open("students.csv","w",encoding="utf8") as file:
        file.write("이름,성별,나이,성적\n")
        file.write("김일수,남,23,80\n")
        file.write("홍길순,여,25,75\n")
        file.write("박길동,남,45,55\n")
        file.write("최순식,남,34,90\n")
        file.write("강감찬,남,90,100\n")
        file.write("갑돌이,남,38,65\n")
        file.write("박삼순,여,31,70\n")
        file.write("김갑순,여,28,85\n")
        file.write("이갑순,여,28,85\n")
        file.write("이순신,남,88,89")

class Student:
    grade = ''
    def __init__(self, line):
        name, gender, age, score = line.strip().split(',')
        self.name = name
        self.gender = gender
        self.age = age
        self.score = int(score)

    def __str__(self):
        return "{}\t{}\t{}\t{}\t{}".format(self.name, self.gender, self.age, self.score, self.grade)

    def make_grade(self):
        g_grades = ['A', 'B', 'C', 'D', 'F']
        g_grades.reverse()       
        if self.score == 100:
            self.grade = 'A+'
        else:
            self.grade = g_grades[self.score // 10 - 5]
        # grade_dict = {10:'A+',9:'A',8:'B',7:'C',6:'D'}
        # grade = grade_dict.get(self.score // 10, 'F')

# write_file()

class Students:
    def __init__(self):
        self.students = []

    def read_students(self):
        with open("students.csv","r",encoding="utf8") as file:
            for i, line in enumerate(file):
                # print(line)
                if i == 0: continue
                self.students.append(Student(line))

    def print_students(self):
        print("1. 학생정보")
        print("이름\t성별\t나이\t성적\t학점")
        print("----\t----\t----\t----\t----")
        for s in self.students:
            print(s)

    # 학생정보를 성적순으로 sorting하는 메소드 (sort)
    def sorting_students(self):
        print("2. Sorting")
        self.students.sort(key=lambda stu: stu.score, reverse=True)
        print("이름\t성별\t나이\t성적\t학점")
        print("----\t----\t----\t----\t----")
        for s in self.students:
            print(s)

    # 학생 성적으로 학점 매기는 메소드 (map, lambda)
    def grading_students(self): 
        m = map(lambda stu: stu.make_grade(), self.students)
        list(m)
    
    
    # 전체 학생의 총점과 평균을 구하는 메소드. (reduce,lambda)
    def get_sum(self): 
        print("3.합계와 평균")
        total = reduce(lambda x, y: (x if type(x) == int else x.score) + y.score, self.students)
        self.avg = total / len(self.students)
        print("합계=", total)
        print("평균=", self.avg)

    # 평균 이상인 학생정보를 출력하는 메소드 (filter, lambda)
    def print_above_avg(self):
        print("4.평균 이상")
        std_avg = filter(lambda x : x.score >= self.avg, self.students)
        for s in std_avg:
            print(s)

s = Students()
s.read_students()
s.print_students()
s.sorting_students()
s.grading_students()
s.print_students()
s.get_sum()
s.print_above_avg()