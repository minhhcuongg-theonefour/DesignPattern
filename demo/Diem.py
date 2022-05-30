from abc import ABCMeta
from numpy import double


List_diem =[]
class Diem(metaclass = ABCMeta):

    def DiemTongket(self):
        return (self.Quatrinh() + self.DiemThi())/2 + self.DiemBonus()
        
    def Quatrinh(self):
        pass

    def DiemThi(self):
        pass

    def DiemBonus(self):
        pass



class GPAmonMTK(Diem):
    def Quatrinh(self):
        qt = double(input("diem qt mon MTK:"))
        return qt

    def DiemThi(self):
        t = double(input("diem thi:"))
        return t

    def DiemBonus(self):
        b = double(input("Nhap bonus (neu co):"))
        return b


class GPAmonHDT(Diem):

    def Quatrinh(self):
        qt = double(input("diem qt mon HDT:"))
        return qt

    def DiemThi(self):
        t = double(input("diem thi:"))
        return t

    def DiemBonus(self):
        b = double(input("Nhap bonus (neu co):"))
        return b


def GPA():
    gpa =0
    hdt = GPAmonHDT()
    List_diem.append(hdt.DiemTongket())
    mtk = GPAmonMTK()
    List_diem.append(mtk.DiemTongket())

    for diem in List_diem:
        gpa += diem
        
    return round(gpa/len(List_diem),2)


# print(GPA())