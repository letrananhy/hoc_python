class nguoi():
    thongminh = 90
    def __init__(self,cc,cn,gt):
        self.ten = "lê trần an hy"
        self.chieu_cao=cc
        self.can_nang=cn
        self.gioi_tinh=gt

    def hello(self):
        print("tên :", self.ten)
        print("chiều cao:" , self.chieu_cao)
        print("cân nặng:", self.can_nang)
    @classmethod
    def thong_so (cls,s):
        k=s.split("+")
        cc,cn,gt = [j for j in k]
        return  cls(cc,cn,gt)

infor = "1.7m+45kg+male"
sn = nguoi.thong_so(infor)
print(sn.__dict__)
