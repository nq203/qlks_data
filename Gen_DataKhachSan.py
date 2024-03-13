import random

listTenDuong = [hex(i)[2:].upper() for i in range(0, 2000)]
listChar = [chr(ord('A') + i) for i in range(0, 26)]


def convertToHex(num):
    ans = ""
    st = str(num)
    if len(st) < 3:
        st = '0' * (3 - len(st)) + st
    for i in st:
        ans += chr(ord('A') + int(i))
    return ans


print(f"use quan_ly_khach_san\ngo\ninsert into Khach_san(ID_Khachsan, Ten_KS, Dia_chi) values")
for i in range(1, 50):
    print(
        f"('{'ks' + '{:03d}'.format(i)}','Khach san {convertToHex(i)}','{int(listTenDuong[i], 16)} Duong {listTenDuong[i] + random.choice(listChar)}'),")
