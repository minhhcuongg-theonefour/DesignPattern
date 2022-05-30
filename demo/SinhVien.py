from asyncio.windows_events import NULL

import MonHoc as MonHoc
import Khoa as KH
import Diem as Diem
import Cash as Cash


List_Sv = []
class SinhVien:

    count = 1
    GPA = 0
    def __init__(self, Name, NgaySinh, Khoa, Nganh, money, QueQuan, NamNhapHoc):
        self.Id = SinhVien.count
        SinhVien.count +=1
        self.name = Name
        self.ngaysinh = NgaySinh
        self.khoa = Khoa
        self.nganh = Nganh
        money1 = Cash.Cash(money)     
        self.money = Cash.Credit_card(money1)
        self.city = QueQuan
        self.nhaphoc = NamNhapHoc
        
    def InTKB(self):
        self.tkb = MonHoc.QLMonHoc.InDanhSachMonHoc()

    def GPA():
        GPA = Diem.GPA()

    def cash_method(self):
        self.money.cash_method()



class NullSinhVien(SinhVien):
    def ThongBao():
        return "Khong co Sinh vien nao !!!!!!!!"


def checkSinhVien(id):
    for sv in List_Sv:
        if(sv.Id == id):
            return sv

    return NullSinhVien


def checkSVKH(Khoa ,idSV):
    for sv in Khoa.List_SV_of_Khoa:
        if(sv.Id == idSV):
            return sv

    return NullSinhVien



class AddSinhVien:
    def AddSinhVien():
        KH.QLKHOA.DsKhoa()
        print(20*"-")
        MaKhoa = int(input("Nhap ma khoa: "))
        Khoa = KH.checkKhoa(MaKhoa)
        if(Khoa != KH.NullKhoa):
            Name = input("Nhap ho ten: ")
            NgaySinh = input("Nhap Ngay sinh: ")
            Tenkhoa = Khoa.Khoa_Method()
            Nganh = input("Nhap Nganh hoc: ")
            money = 2000
            city = input("Nhap que quan: ")
            NamNhapHoc = input("Nam nhap hoc: ")
            sv = SinhVien(Name, NgaySinh, Tenkhoa, Nganh, money, city, NamNhapHoc)
            List_Sv.append(sv)
            Khoa.List_SV_of_Khoa.append(sv)

            print("Da them sinh vien !!!")

        else:
            print(KH.NullKhoa.ThongBao())


class DisplaySinhVien:
    def DisplaySinhVien():
        if(List_Sv != NULL and len(List_Sv) > 0):
            print(30*"-")
            print("{:<8}| {:25}| {:20}| {:25}| {:25}| {:13}| {:20}".format("ID", "Ho Ten", "Ngay sinh", "Ten Khoa",
             "Nganh hoc", "Que quan", "Nam nhap hoc"))

            for sv in List_Sv:
                print("{:<8}| {:25}| {:20}| {:25}| {:25}| {:13}| {:20}".format(sv.Id, sv.name, sv.ngaysinh, sv.khoa,
                 sv.nganh, sv.city, sv.nhaphoc))
        else:
            print("Khong co sinh vien nao !!!!!")

class DeleteSinhVien:
    def DeleteSinhVien():
        print(20*"-")
        MaKhoa = int(input("Nhap ma khoa: "))
        Khoa = KH.checkKhoa(MaKhoa)
        if(Khoa != KH.NullKhoa):
            if(List_Sv != NULL and len(List_Sv) > 0):
                mssv = int(input("Nhap ID sinh vien: "))
                sv = checkSVKH(Khoa, mssv)
                if(sv != NullSinhVien):
                    List_Sv.remove(sv)
                    Khoa.List_SV_of_Khoa.remove(sv)
                    print("Da xoa sinh vien co ID {} !!!".format(sv.Id))
                else:
                    print("Khong tim thay sv trong {} !!!".format(Khoa.TenKhoa))
            else:
                print("Khong co danh sach sv !!!")
        else:
            print("Khong tim thay khoa !!!")


def menu():
    print("----Quan ly sinh vien----");
    print("1.Nhap sinh vien");
    print("2.Hien thi sinh vien");
    print("3.Tim kiem sinh vien");
    print("4.Xoa sinh vien");
    print("0.Quay lai");

    i = int(input("Lua chon: "))
    return i


a = SinhVien("bach","24/02/2001","Khoa Chat luong cao", "cntt", 20000, "vt", "2019")
b = SinhVien("bah","2001","Khoa Cong nghe thong tin", "cntt", 20000, "vt", "2019")
c = SinhVien("bah","2001","Khoa Cong nghe thong tin", "cntt", 20000, "vt", "2019")
List_Sv.append(a)
List_Sv.append(b)
List_Sv.append(c)

# Sv = AddSinhVien.AddSinhVien()
# Dp = DisplaySinhVien.DisplaySinhVien()
# dele = DeleteSinhVien.DeleteSinhVien()
# Dp = DisplaySinhVien.DisplaySinhVien()

a.cash_method()
# i= menu()
# print(i)

print(20*"-")