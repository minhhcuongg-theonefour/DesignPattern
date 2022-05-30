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


class Credit_card(ICash):               #Proxy
    def __init__(self, Cash:Cash):
        self.cash = Cash

    def cash_method(self):
        # print("Thuc hien thanh toan gi do")
        self.cash.cash_method()
