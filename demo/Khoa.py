from abc import ABC, ABCMeta, abstractmethod


List_Khoa = []
class Khoa(metaclass=ABCMeta):

    Id = 0
    TenKhoa =""
    List_SV_of_Khoa =[]

   
    def Khoa_Method():
        pass


class KHoa_CNTT(Khoa):
    def __init__(self) -> None:
        self.Id = 1
        self.TenKhoa = "Khoa Cong nghe thong tin"
        self.List_SV_of_Khoa = []
    

    def Khoa_Method(self):
        return self.TenKhoa


class KHoa_DDT(Khoa):
    def __init__(self) -> None:
        self.Id = 2
        self.TenKhoa = "Khoa Dien - Dien tu"
        self.List_SV_of_Khoa = []

    def Khoa_Method(self):
        return self.TenKhoa


class KHoa_CLC(Khoa):
    def __init__(self) -> None:
        self.Id = 3
        self.TenKhoa = "Khoa Chat luong cao"
        self.List_SV_of_Khoa = []

    def Khoa_Method(self):
        return self.TenKhoa


class QLKHOA:
    def DsKhoa():

        Khoa1 = KHoa_CNTT()
        Khoa2 = KHoa_DDT()
        Khoa3 = KHoa_CLC()
        List_Khoa.append(Khoa1)
        List_Khoa.append(Khoa2)
        List_Khoa.append(Khoa3)

        print("{:<8} |{} ".format("Ma khoa","Ten khoa"))
        for khoa in List_Khoa:
            print("{:<8} |{} ".format(khoa.Id, khoa.TenKhoa))
            
        
def checkKhoa(id):
    for k in List_Khoa:
        if (id == k.Id):
            return k

    return NullKhoa


class NullKhoa(Khoa):
    def ThongBao():
        return("Khoa khong ton tai !!!!!!")





# a = QLKHOA.DsKhoa()

# print(checkKhoa(0).Khoa_Method())



    
