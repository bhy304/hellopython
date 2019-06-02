class Dog:
    def __init__(self, name):
        self.name = name
        print(self.name, "was Born")

    def speak(self):
        print("YELP!", self.name)

    # def wag(self):
    #     print("Dog's wag tail!")

    def __del__(self):
        print("destroy!!")

# Inheritance 
class Puppy(Dog):
    def __init__(self):
        self.name = "Puppy"
        self.color = "Red"
        print("QQQ> Puppy was Born")

    # Encapsulation 
    def __read_diary(self): #클래스 내에서만 함수 호출 가능, Instance 내에서만 호출할 수 있음
        print("Diary content!!")

    def speak(self):
        print("Bow wow!", self.name)

    def wag(self):
        self.__read_diary()
        print("Puppy's wag tail!")

    def static():
        print("static method on class")

class Calc:
    def plut(a, b):
        return a + b 

d = Dog('puddle')
p = Puppy()
d.speak()
p.speak()
#d.wag()
p.wag()
#p.__read_diary()

print(d.name, p.name, p.color)

Puppy.static()