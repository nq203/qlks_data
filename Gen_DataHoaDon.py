import random


def AddMoreDay(date, numberDay):
    date = date.split('/')
    date[0] = int(date[0])
    date[1] = int(date[1])
    date[2] = int(date[2])
    date[0] += numberDay
    if date[0] > 28:
        date[0] -= 28
        date[1] += 1
        if date[1] > 12:
            date[1] -= 12
            date[2] += 1
    return f'{date[0]}/{date[1]}/{date[2]}'


print("use quan_ly_khach_san")
print("go")
print(f"insert into Hoa_don(ID_Hoa_don,Ngay_den,Ngay_di,Hinh_thuc_thanh_toan) values")
for i in range(1, 1000):
    id = "hd" + '{:03d}'.format(i)
    price = random.randint(1000000, 10000000)
    dateIn = f'{random.randint(1, 29)}/{random.randint(1, 12)}/{random.randint(2018, 2022)}'
    dateOut = AddMoreDay(dateIn, random.randint(1, 10))
    hinh_thuc_thanh_toan = random.choice(["Tien mat", "The", "Chuyen khoan"])
    id_khach_hang = random.choice(["kh" + '{:03d}'.format(i) for i in range(1, 711)])
    print(f"('{id}','{dateIn}','{dateOut}','{hinh_thuc_thanh_toan}'),")
