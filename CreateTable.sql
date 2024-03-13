CREATE TABLE Khach_san
(
  Ten_KS VARCHAR(100) NOT NULL,
  Dia_chi VARCHAR(100) NOT NULL,
  ID_Khachsan VARCHAR(100) NOT NULL,
  PRIMARY KEY (ID_Khachsan)
);

CREATE TABLE Nhan_vien
(
  ID_Nhan_vien VARCHAR(100) NOT NULL,
  Cong_viec VARCHAR(100) NOT NULL,
  Gioi_tinh VARCHAR(100) NOT NULL,
  Tennv VARCHAR(100) NOT NULL,
  Luong VARCHAR(100) NOT NULL,
  ID_Khachsan VARCHAR(100) NOT NULL,
  PRIMARY KEY (ID_Nhan_vien),
  FOREIGN KEY (ID_Khachsan) REFERENCES Khach_san(ID_Khachsan)
);

CREATE TABLE Hoa_don
(
  ID_Hoa_don VARCHAR(100) NOT NULL,
  Ngay_den VARCHAR(100) NOT NULL,
  Ngay_di VARCHAR(100) NOT NULL,
  Hinh_thuc_thanh_toan VARCHAR(100) NOT NULL,
  PRIMARY KEY (ID_Hoa_don)
);

CREATE TABLE Khach_hang
(
  First_name VARCHAR(100) NOT NULL,
  Last_name VARCHAR(100) NOT NULL,
  ID_Khach_hang VARCHAR(100) NOT NULL,
  Dia_chi VARCHAR(100) NOT NULL,
  Ngay_sinh VARCHAR(100) NOT NULL,
  Gioi_tinh VARCHAR(100) NOT NULL,
  PRIMARY KEY (ID_Khach_hang)
);
CREATE TABLE Nguoi_than_khach_hang
(
  ID_Nguoi_than VARCHAR(100) NOT NULL,
  Ten VARCHAR(100) NOT NULL,
  Tuoi VARCHAR(100) NOT NULL,
  Dia_chi VARCHAR(100) NOT NULL,
  ID_Khach_hang VARCHAR(100) NOT NULL,
  PRIMARY KEY (ID_Nguoi_than, ID_Khach_hang),
  FOREIGN KEY (ID_Khach_hang) REFERENCES Khach_hang(ID_Khach_hang)
);
CREATE TABLE Nhan_vien_So_dien_thoai
(
  So_dien_thoai VARCHAR(100) NOT NULL,
  ID_Nhan_vien VARCHAR(100) NOT NULL,
  PRIMARY KEY (So_dien_thoai, ID_Nhan_vien),
  FOREIGN KEY (ID_Nhan_vien) REFERENCES Nhan_vien(ID_Nhan_vien)
);

CREATE TABLE Nhan_vien_quan_ly
(
  ID_Nhan_vien VARCHAR(100) NOT NULL,
  Quyen_han VARCHAR(100) NOT NULL,
  PRIMARY KEY (ID_Nhan_vien),
  FOREIGN KEY (ID_Nhan_vien) REFERENCES Nhan_vien(ID_Nhan_vien)
);

CREATE TABLE Le_tan
(
  ID_Nhan_vien VARCHAR(100) NOT NULL,
  Gio_truc VARCHAR(100) NOT NULL,
  PRIMARY KEY (ID_Nhan_vien),
  FOREIGN KEY (ID_Nhan_vien) REFERENCES Nhan_vien(ID_Nhan_vien)
);

CREATE TABLE Phuc_vu_phong
(
  ID_Nhan_vien VARCHAR(100) NOT NULL,
  SL_Phong_da_don VARCHAR(100) NOT NULL,
  PRIMARY KEY (ID_Nhan_vien),
  FOREIGN KEY (ID_Nhan_vien) REFERENCES Nhan_vien(ID_Nhan_vien)
);

CREATE TABLE Phong
(
  Ten_phong VARCHAR(100) NOT NULL,
  Loai_phong VARCHAR(100) NOT NULL,
  Trang_thai_phong VARCHAR(100) NOT NULL,
  ID_Phong VARCHAR(100) NOT NULL,
  Gia_phong VARCHAR(100) NOT NULL,
  ID_Nhan_vien VARCHAR(100) NOT NULL,
  PRIMARY KEY (ID_Phong),
  FOREIGN KEY (ID_Nhan_vien) REFERENCES Phuc_vu_phong(ID_Nhan_vien)
);

CREATE TABLE Khach_hang_SDT
(
  SDT VARCHAR(100) NOT NULL,
  ID_Khach_hang VARCHAR(100) NOT NULL,
  PRIMARY KEY (SDT, ID_Khach_hang),
  FOREIGN KEY (ID_Khach_hang) REFERENCES Khach_hang(ID_Khach_hang)
);

CREATE TABLE Thanh_toan
(
  ID_Khach_hang VARCHAR(100) NOT NULL,
  ID_Hoa_don VARCHAR(100) NOT NULL,
  ID_Phong VARCHAR(100) NOT NULL,
  FOREIGN KEY (ID_Khach_hang) REFERENCES Khach_hang(ID_Khach_hang),
  FOREIGN KEY (ID_Hoa_don) REFERENCES Hoa_don(ID_Hoa_don),
  FOREIGN KEY (ID_Phong) REFERENCES Phong(ID_Phong)
);
