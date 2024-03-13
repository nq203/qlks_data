import random

ho_tieu_viet_khong_dau = ["Nguyen", "Le", "Tran", "Pham", "Vo", "Huong", "Dang", "Bui", "Ho", "Do"]
ten_nam_khong_dau = ["Anh", "Bao", "Binh", "Canh", "Cuong", "Dai", "Danh", "Duc", "Dung", "Duong", "Giang", "Ha", "Hai",
                     "Hieu", "Hoai", "Hung", "Huy", "Khanh", "Khoa", "Lam", "Long", "Luong", "Minh", "Nam", "Nhan",
                     "Phat", "Phong", "Phu", "Phuc", "Quan", "Quang", "Quoc", "Son", "Tam", "Tan", "Thang", "Thien"]

ten_nu_khong_dau = ["Linh", "Hoa", "Thao", "Nhu", "My", "Anh", "Tuyet", "Hanh", "Hong", "Quynh", "Lan", "Mai",
                    "Nga", "Yen", "Hien", "Linh", "Thien", "Huong", "Kieu", "Thu", "Phuong", "Diep", "Tuyet",
                    "Phuc", "Bao", "Tung", "Loan", "Khanh", "Hai", "Hoa", "Lien", "Cam", "Trang", "Thuy"]
tinh_viet_nam = ["An Giang", "Ba Ria-Vung Tau", "Bac Giang", "Bac Kan", "Bac Lieu", "Bac Ninh", "Ben Tre", "Binh Dinh",
                 "Binh Duong", "Binh Phuoc", "Binh Thuan", "Ca Mau", "Cao Bang", "Dak Lak", "Dak Nong", "Dien Bien",
                 "Dong Nai", "Dong Thap", "Gia Lai", "Ha Giang", "Ha Nam", "Ha Tinh", "Hai Duong", "Hau Giang",
                 "Hoa Binh", "Hung Yen", "Khanh Hoa", "Kien Giang", "Kon Tum", "Lai Chau", "Lam Dong", "Lang Son",
                 "Lao Cai", "Long An", "Nam Dinh", "Nghe An", "Ninh Binh", "Ninh Thuan", "Phu Tho", "Phu Yen",
                 "Quang Binh", "Quang Nam", "Quang Ngai", "Quang Ninh", "Quang Tri", "Soc Trang", "Son La", "Tay Ninh",
                 "Thai Binh", "Thai Nguyen", "Thanh Hoa", "Thua Thien-Hue", "Tien Giang", "Tra Vinh", "Tuyen Quang",
                 "Vinh Long", "Vinh Phuc", "Yen Bai", "Phu Quoc"]

print("use quan_ly_khach_san")
print("go")
print(f"insert into Nhan_vien(ID_Nhan_vien,Cong_viec,Gioi_tinh,Tennv,Luong,ID_Khachsan) values")
ten = []

for i in ho_tieu_viet_khong_dau:
    for j in ten_nam_khong_dau:
        ten.append(f"{i} {j}")
    for j in ten_nu_khong_dau:
        ten.append(f"{i} {j}")

list_id_nv_ql = []
list_id_le_tan = []
list_id_phuc_vu_phong = []

for i in range(1, 1000):
    id_nhan_vien = f'nv{"{:03d}".format(i)}'
    cong_viec = ""
    if i % 5 == 0:
        cong_viec = "Quan ly"
    elif i % 5 == 1 or i % 5 == 2:
        cong_viec = "Le tan"
    else:
        cong_viec = "Phuc vu phong"
    id_khach_san = "ks" + '{:03d}'.format(i % 49 if i % 49 != 0 else 49)
    if cong_viec == "Quan ly":
        list_id_nv_ql.append(id_nhan_vien)
    elif cong_viec == "Le tan":
        list_id_le_tan.append(id_nhan_vien)
    else:
        list_id_phuc_vu_phong.append(id_nhan_vien)
    gioi_tinh = random.choice(["male", "female"])
    t = random.choice(ten)
    luong = random.randint(10000000, 20000000)
    print(f"('{id_nhan_vien}','{cong_viec}','{gioi_tinh}','{t}','{luong}','{id_khach_san}'),")

print("use quan_ly_khach_san")
print("go")
print(f"insert into Nhan_vien_quan_ly(ID_Nhan_vien,Quyen_han) values")
for i in list_id_nv_ql:
    quyen_han = random.choice(
        ["Quan ly nhan su", "Quan ly tai chinh", "Quan ly khach san", "Quan ly dich vu khach hang"])
    print(f"('{i}','{quyen_han}'),")

print("use quan_ly_khach_san")
print("go")
print(f"insert into Le_tan(ID_Nhan_vien,Gio_truc) values")
for i in list_id_le_tan:
    gio_truc = random.choice(["Sang", "Chieu", "Toi"])
    print(f"('{i}','{gio_truc}'),")

print("use quan_ly_khach_san")
print("go")
print(f"insert into Phuc_vu_phong(ID_Nhan_vien,SL_Phong_da_don) values")
for i in list_id_phuc_vu_phong:
    sl_phong_da_don = random.randint(1, 10)
    print(f"('{i}','{sl_phong_da_don}'),")

list_phong_da_thanh_toan = []
print("use quan_ly_khach_san")
print("go")
print(f"insert into Phong(Ten_phong,Loai_phong,Trang_thai_phong,ID_Phong,Gia_phong,ID_Nhan_vien) values")
for i in range(1, 1000):
    ten_phong = f"Phong {i}"
    loai_phong = random.choice(["Tong Thong", "VIP", "Gia dinh", "Doi", "Don"])
    trang_thai_phong = random.choice(["true", "false"])
    id_phong = f'ph{"{:03d}".format(i)}'
    if trang_thai_phong == "true":
        list_phong_da_thanh_toan.append(id_phong)
    gia_phong = random.randint(1, 10) * 1000000
    id_nhan_vien = list_id_phuc_vu_phong[i % len(list_id_phuc_vu_phong)]
    print(f"('{ten_phong}','{loai_phong}','{trang_thai_phong}','{id_phong}','{gia_phong}','{id_nhan_vien}'),")

list_id_kh = [(f'kh{"{:03d}".format(i)}') for i in range(1, 711)]
print("use quan_ly_khach_san")
print("go")
print(f"insert into Thanh_toan(ID_Khach_hang, ID_Hoa_don, ID_Phong) values")
for i in range(1, 1000):
    id_Hoa_don = f'hd{"{:03d}".format(i)}'
    id_khach_hang = random.choice(list_id_kh)
    list_id_kh.remove(id_khach_hang)
    if (len(list_id_kh) == 0):
        list_id_kh = [(f'kh{"{:03d}".format(i)}') for i in range(1, 711)]
    id_phong = random.choice(list_phong_da_thanh_toan)
    print(f"('{id_khach_hang}','{id_Hoa_don}','{id_phong}'),")
