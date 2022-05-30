from abc import ABC, ABCMeta, abstractmethod


ListMH = []

class LopMonHoc(metaclass=ABCMeta):
    def __init__(self, MaGV, TenGV, SLSV, PhongHoc, LichHoc):
        self.MaGV = MaGV
        self.TenGV = TenGV
        self.slsv = SLSV
        self.PhongHoc = PhongHoc
        self.LichHoc = LichHoc

    def TaoLopHoc():
        pass


class MonHoc(metaclass = ABCMeta):
    def __init__(self, LopMonHoc : LopMonHoc):
        # self.id = Id
        # self.TenMon = TenMon
        # self.SoTinchi = SoTinchi
        self.LopMonHoc = LopMonHoc
        # self.NienKhoa = NienKhoa

    def TaoMonHoc():
        pass


class HuongDoiTuong(MonHoc):
    def __init__(self, LopMonHoc: LopMonHoc):
        super().__init__(LopMonHoc)
        self.Id = 1
        self.TenMon = "Lap trinh Huong doi tuong"
        self.SoTinchi = 3
        self.NienKhoa = "2022-2023"
        self.LopMonHoc = LopMonHoc

    def TaoMonHoc(self):
        self.str = self.LopMonHoc.TaoLopHoc()
        

    def __str__(self):
        return "{:<8}| {:<15}| {:<10}| {:<10}".format(self.TenMon, self.SoTinchi, self.NienKhoa, self.str)
        
        
        
class TaoLopHDT(LopMonHoc):
    def __init__(self, MaGV, TenGV, SLSV, PhongHoc, LichHoc):
        super().__init__(MaGV, TenGV, SLSV, PhongHoc, LichHoc)


    def TaoLopHoc(self):
        return "{:<10}| {:<15}| {:<10}| {:<10}".format(self.TenGV, self.slsv, self.PhongHoc, self.LichHoc)
        


class MauThietKe(MonHoc):
    def __init__(self, LopMonHoc: LopMonHoc):
        super().__init__(LopMonHoc)
        self.Id = 2
        self.TenMon = "Mau Thiet ke phan mem"
        self.SoTinchi = 3
        self.NienKhoa = "2022-2023"
        self.LopMonHoc = LopMonHoc

    def TaoMonHoc(self):
        self.str = self.LopMonHoc.TaoLopHoc()
        

    def __str__(self):
        return "{:<25}| {:<15}| {:<10}| {:<10}".format(self.TenMon, self.SoTinchi, self.NienKhoa, self.str)
        
        

class TaoLopMTK(LopMonHoc):
    def __init__(self, MaGV, TenGV, SLSV, PhongHoc, LichHoc):
        super().__init__(MaGV, TenGV, SLSV, PhongHoc, LichHoc)


    def TaoLopHoc(self):
        return "{:<10}| {:<15}| {:<10}| {:<10}".format(self.TenGV, self.slsv, self.PhongHoc, self.LichHoc)



class QLMonHoc:

    def InDanhSachMonHoc():
        if len(ListMH) == 0:
            print("Chua co mon hoc nao")
        else:
            print("{:<25}| {:<15}| {:<10}| {:<10}| {:<15}| {:<10}| {:<10}".format("Ten mon hoc", "So tin chi", "Nien khoa", "Ten GV", "SLSV", "Phong hoc", "Lich hoc"))
            for mh in ListMH:
                print(mh)


    def addMonHoc(name):
        if name == "HDT":
            Lop_HDT1 = HuongDoiTuong(TaoLopHDT(1,"bach",20,"A5-203","thu 2, 12h30"))
            Lop_HDT1.TaoMonHoc()
            Lop_HDT2 = HuongDoiTuong(TaoLopHDT(2,"cuong",20,"A5-203","thu 2, 7h"))
            Lop_HDT2.TaoMonHoc()
            Lop_HDT3 = HuongDoiTuong(TaoLopHDT(3,"tuan",20,"A5-203","thu 3, 12h30"))
            Lop_HDT3.TaoMonHoc()
            ListMH.append(Lop_HDT1)
            ListMH.append(Lop_HDT2)
            ListMH.append(Lop_HDT3)

        if name == "MTK":
            Lop_MTK1 = MauThietKe(TaoLopMTK(1,"bach",30,"A5-403","thu 5, 12h30"))
            Lop_MTK1.TaoMonHoc()
            Lop_MTK2 = MauThietKe(TaoLopMTK(2,"cuong",30,"A5-403","thu 2, 12h30"))
            Lop_MTK2.TaoMonHoc()
            ListMH.append(Lop_MTK1)
            ListMH.append(Lop_MTK2)

        


# if __name__ == "__main__":

# a = QLMonHoc.InDanhSachMonHoc()

# ab = QLMonHoc.addMonHoc("HDT")
# ab = QLMonHoc.addMonHoc("MTK")

# a = QLMonHoc.InDanhSachMonHoc()
    
