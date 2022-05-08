from abc import ABC, ABCMeta, abstractmethod

class ICustomer(metaclass = ABCMeta):
    def __init__(self, name):      
        self.name =  name   

    def isNull():
        pass

    def getName():
        pass


class RealCustomer(ICustomer):
    def __init__(self, name):
        super().__init__(name)
    
    def isNull(self):
        return False

    def getName(self):
        return self.name


class NullCustomer(ICustomer):
    def isNull(self):
        return True
    
    def getName(self):
        return "Not Available !!!!"


class Factory():
    
    def build(name):
        names = ["bach", "cuong", "phung"]
        for i in names:
            if(name == i):
                return RealCustomer(name)
        
        return NullCustomer(name)


if __name__ == "__main__":
    cus1 = Factory.build("bach")
    cus2 = Factory.build("phung")
    cus3 = Factory.build("cuong")
    cus4 = Factory.build("Bach")

    print(25*"-")
    print(cus1.getName(),cus1.isNull())
    print(cus2.getName(),cus2.isNull())
    print(cus3.getName(),cus3.isNull())
    print(cus4.getName(),cus4.isNull())
