# cau3.py - Xử lý dữ liệu sách bằng pandas + matplotlib
import os

import matplotlib
matplotlib.use("Agg")  # Chỉ lưu file, không mở cửa sổ hiển thị
import matplotlib.pyplot as plt
import pandas as pd

FILE_SACH = "sach.csv"
FILE_BIEUDO = "bieudo.png"
FILE_CANH_BAO = "canh_bao_sach.csv"

NOI_DUNG_CSV = """MaSach,TenSach,Gia,SoLuong
S001,Lap trinh Python co ban,95000,40
S002,Cau truc du lieu va giai thuat,120000,6
S003,Nhap mon tri tue nhan tao,150000,25
S004,Co so du lieu nang cao,135000,4
S005,Tieng Anh chuyen nganh CNTT,70000,80
"""


def tao_file_csv():
    """Tạo file sach.csv với nội dung theo đề (nếu chưa có)."""
    if not os.path.exists(FILE_SACH):
        with open(FILE_SACH, "w", encoding="utf-8", newline="") as f:
            f.write(NOI_DUNG_CSV)
        print(f"Đã tạo file {FILE_SACH}")


# a) Đọc dữ liệu
def doc_du_lieu():
    return pd.read_csv(FILE_SACH, encoding="utf-8")


# b) Thống kê
def thong_ke(df):
    tong_dau_sach = len(df)
    gia_trung_binh = df["Gia"].mean()
    sach_dat_nhat = df.loc[df["Gia"].idxmax(), "TenSach"]

    print("===== THỐNG KÊ =====")
    print(f"Tổng số đầu sách       : {tong_dau_sach}")
    print(f"Giá trung bình         : {gia_trung_binh:,.0f} đ")
    print(f"Sách có giá cao nhất   : {sach_dat_nhat}")


# c) Vẽ biểu đồ cột số lượng tồn kho
def ve_bieu_do(df):
    plt.figure(figsize=(8, 5))
    cot = plt.bar(df["MaSach"], df["SoLuong"], color="steelblue")
    plt.bar_label(cot)  # Hiện số lượng trên đầu mỗi cột
    plt.title("Số lượng tồn kho của từng cuốn sách")
    plt.xlabel("Mã sách")
    plt.ylabel("Số lượng")
    plt.tight_layout()
    plt.savefig(FILE_BIEUDO, dpi=150)
    plt.close()
    print(f"Đã lưu biểu đồ vào {FILE_BIEUDO}")


# d) Lọc sách sắp hết (SoLuong < 10) và xuất file
def xuat_canh_bao(df):
    sap_het = df[df["SoLuong"] < 10]
    sap_het.to_csv(FILE_CANH_BAO, index=False, encoding="utf-8")
    print(f"\nCó {len(sap_het)} sách sắp hết (SoLuong < 10):")
    print(sap_het.to_string(index=False))
    print(f"Đã xuất danh sách vào {FILE_CANH_BAO}")


def main():
    tao_file_csv()
    df = doc_du_lieu()
    thong_ke(df)
    ve_bieu_do(df)
    xuat_canh_bao(df)


if __name__ == "__main__":
    main()