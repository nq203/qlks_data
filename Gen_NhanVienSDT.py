import random

print("use quan_ly_khach_san")
print("go")
print(f"insert into Nhan_vien_So_dien_thoai(So_dien_thoai,ID_Nhan_vien) values")
list_dau_so = ["086", "096", "097", "098", "039", "038", "037", "036", "035", "034", "033", "032", "031", "090", "093",
               "089", "070", "079", "077", "076", "078", "088", "091", "094", "083", "084", "085", "081", "082", "092",
               "056", "058", "099", "059", "095", "052", "032", "033", "034", "035", "036", "037", "038", "039", "070",
               "076", "077", "078", "079", "081", "082", "083", "084", "085", "086", "088", "089", "090", "091", "092",
               "093", "094", "095", "096", "097", "098", "099"]
listSDT = []
for i in range(9357000, 9359000):
    listSDT.append(str(i))
for i in range(1, 1000):
    sdt = random.choice(listSDT)
    listSDT.remove(sdt)
    sdt = random.choice(list_dau_so) + sdt
    id = "nv" + '{:03d}'.format(i)
    print(f"('{sdt}','{id}'),")
