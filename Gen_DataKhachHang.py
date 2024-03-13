import random

listTenDuong = [hex(i)[2:].upper() for i in range(0, 2000)]
listChar = [chr(ord('A') + i) for i in range(0, 26)]

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

id = 1
print("use quan_ly_khach_san")
print("go")
print(f"insert into Khach_hang(First_name,Last_name,ID_Khach_hang,Dia_chi,Ngay_sinh,Gioi_tinh) values")
for i in ho_tieu_viet_khong_dau:
    for j in ten_nam_khong_dau:
        tinh = random.choice(tinh_viet_nam)
        date = f'{random.randint(1, 29)}/{random.randint(1, 12)}/{random.randint(1950, 2000)}'
        print(f"('{j}','{i}','{'kh' + '{:03d}'.format(id)}','{tinh}','{date}','male'),")
        id += 1

for i in ho_tieu_viet_khong_dau:
    for j in ten_nu_khong_dau:
        tinh = random.choice(tinh_viet_nam)
        date = f'{random.randint(1, 29)}/{random.randint(1, 12)}/{random.randint(1950, 2000)}'
        print(f"('{j}','{i}','{'kh' + '{:03d}'.format(id)}','{tinh}','{date}','female'),")
        id += 1
