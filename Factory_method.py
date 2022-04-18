from abc import ABCMeta, abstractclassmethod

class IPerson(metaclass=ABCMeta):

    def __init__(self, name):      
        self.name =  name   

    @abstractclassmethod
    def person_method():
        "Interface"
    

class Student(IPerson):

    def __init__(self, name):
        super().__init__(name)
        self.mssv = input("Nhap mssv: ")
        
    def person_method(self):
        print("I'm a Student")
        print(self.mssv, self.name)
        
    

class Teacher(IPerson):

    def __init__(self, name):
        super().__init__(name)      
        self.work = input("Nhap khoa lam viec: ")
    
    def person_method(self):
        print("I'm a Teacher")
        print(self.work, self.name)


class PersonFactory:

    def build_person(person_type, name):
        if person_type =="Student":
            return Student(name)
        if person_type == "Teacher":
            return Teacher(name)
        print("Sai---------------------")
        return -1


if __name__ == "__main__":

    Name = input("Nhap ten: ")
    choice = input("Nhap person type: ")
    person = PersonFactory.build_person(choice, Name)
    person.person_method()


