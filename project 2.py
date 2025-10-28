print("Hello")

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        print(name)
        print(age)

p1 = Student("John", 20)
p2 = Student("JAMIL", 20)

print(p1.name, p1.age)
print(p2.name, p2.age)
