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
print(f"insert into Nguoi_than_khach_hang(ID_Nguoi_than,Ten,Tuoi,Dia_chi,ID_Khach_hang) values")
ten = []

for i in ho_tieu_viet_khong_dau:
    for j in ten_nam_khong_dau:
        ten.append(f"{i} {j}")
    for j in ten_nu_khong_dau:
        ten.append(f"{i} {j}")

for i in range(1, 1000):
    id_nguoi_than = f'ntkh{"{:03d}".format(i)}'
    t = random.choice(ten)
    tuoi = random.randint(18, 80)
    dia_chi = random.choice(tinh_viet_nam)
    id_kh = "kh" + '{:03d}'.format(i % 710 if i % 710 != 0 else 710)
    print(f"('{id_nguoi_than}','{t}','{tuoi}','{dia_chi}','{id_kh}'),")
