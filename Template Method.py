from abc import ABC, ABCMeta, abstractmethod


class MakeMeal(metaclass = ABCMeta):

    def Make(self):                   #Template method
        self.ChuanBi()
        self.Nau()
        self.An()
        self.Dondep()


    def ChuanBi(self):
        pass
    
    def Nau(self):
        pass

    def An(self):
        pass

    def Dondep(self):
        print("Don dep moi thu!!!!")


class MakePizza(MakeMeal):

    def ChuanBi(self):
        print("Chuan bi nguyen lieu cho mon Pizza")

    def Nau(self):
        print("Nuong Pizza")

    def An(self):
        print("An Pizza")
    

class MakeTea(MakeMeal):

    def Nau(self):
        print("Pha tra")

    def An(self):
        print("Uong tra")




Pizza = MakePizza()
Pizza.Make()

print (25*"-")

Tea = MakeTea()
Tea.Make()