from abc import ABCMeta, abstractclassmethod

class ICash(metaclass=ABCMeta):
    
    def __init__(self, money):      
        self.money =  money

    @abstractclassmethod
    def cash_method():
        "Interface"


class Cash(ICash):                      #Real Object

    def cash_method(self):
        print(f"So tien trong bank: {self.money}")


    def checkThanhtoan(self):
        self.money = self.money - 1000
        return self.money


class Credit_card(ICash):               #Proxy
    def __init__(self, money):
        super().__init__(money)
        self.cash = Cash(money)

    def cash_method(self):
        print("Thuc hien thanh toan gi do")
        self.cash.checkThanhtoan()
        self.cash.cash_method()

    

n = 10000
p1 = Cash(n)
p1.cash_method()
print("-------------------------")
p2 = Credit_card(n)
p2.cash_method()



