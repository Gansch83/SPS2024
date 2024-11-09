class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # print without __str__ method
    # <__main__.Person object at 0x104e22120>
    def __str__(self):
        return f"My name is {self.__name}, and I am {self.__age} years old."

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    #Properties sind elegant
    #Name = property(get_name, set_name)
    #Age = property(get_age, set_age)
    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self, name):
        self.__name = name
    @property
    def Age(self):
        return self.__age
    @Age.setter
    def Age(self, age):
        self.__age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self._student_id = student_id

    def __str__(self):
        return f"My name is {self.Name}, and I am {self.Age} years old. My student ID is {self._student_id}."


def main():
    anton = Person("Anton Mueller", 23)
    #geht nicht, weil __name private ist!!!
    anton.__name = "Anton Fake"
    print(anton.Age)
    print(anton.Name)
    anton.Age = 40
    print(anton.Age)
    print(anton)

    student_anton = Student("Michael Jackson", 23, 123456)

    print(student_anton)


if __name__ == "__main__":
    main()