from abc import ABCMeta, abstractmethod


class IShapeImplementer(metaclass=ABCMeta):
    "Shape Implementer"

    @staticmethod
    @abstractmethod
    def draw_implementation():
        "The method that the refined abstractions will implement"


class IShape(metaclass=ABCMeta):
    "The Shape Abstraction Interface"

    def __init__(self, canh, implementer : IShapeImplementer):
        self.implementer = implementer
        self.canh = canh

    @staticmethod
    @abstractmethod
    def draw():
        "The method that will be handled at the shapes implementer"
        

class SquareImplementer(IShapeImplementer):
    
    def draw_implementation(self):
        print("**************")
        print("*            *")
        print("*            *")
        print("*            *")
        print("*            *")
        print("*            *")
        print("*            *")
        print("**************")

class TriangleImplementer(IShapeImplementer):
    
    def draw_implementation(self):
        print("*")
        print("**")
        print("* *")
        print("*  *")
        print("*   *")
        print("*    *")
        print("*     *")
        print("*      *")
        print("*       *")
        print("*        *")
        print("*         *")
        print("************")


class Square(IShape):
    
    def __init__(self, canh, implementer : IShapeImplementer):
        super().__init__(canh, implementer)
        self.implementer = implementer()

    def draw(self):
        print(f"Hinh vuong co {self.canh} canh")
        self.implementer.draw_implementation()


class Triangle(IShape):
    
    def __init__(self, canh, implementer : IShapeImplementer):
        super().__init__(canh, implementer)
        self.implementer = implementer()

    def draw(self):
        print(f"Hinh tam giac co {self.canh} canh")
        self.implementer.draw_implementation()



canh = input("Nhap so canh (3 hoac 4):")
print("------------------------------")
if canh == "3":
    hinh = Triangle(canh, TriangleImplementer)
    hinh.draw()
elif canh == "4":
    hinh = Square(canh, SquareImplementer)
    hinh.draw()
else: 
    print("Nhap sai")


