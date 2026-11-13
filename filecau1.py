

danh_sach_sach = []

def them_sach(danh_sach, ma, ten, gia, soluong):
    sach = {
        "MaSach": ma,
        "Tensach": ten,
        "Gia": float(gia),
        "SoLuong": int(soluong)
    }
    danh_sach.append(sach)

def tim_kiem_theo_ten(danh_sach, tu_khoa):
    ket_qua = []
    for s in danh_sach:
        if tu_khoa.lower() in s["Tensach"].lower():
            ket_qua.append(s)
    return ket_qua

def tong_gia_tri_kho_sach(danh_sach):
    tong = 0
    for s in danh_sach:
        tong = tong + (s["Gia"] * s["SoLuong"])
    return tong

them_sach(danh_sach_sach, "S001", "Lập trình Python cơ bản", 95000, 40)
them_sach(danh_sach_sach, "S002", "Cấu trúc dữ liệu và giải thuật", 120000, 6)
them_sach(danh_sach_sach, "S003", "Nhập môn trí tuệ nhân tạo", 150000, 25)

while True:
    print("\n--- QUẢN LÝ THƯ VIỆN SÁCH ---")
    print("1. Thêm sách")
    print("2. Tìm kiếm sách theo tên")
    print("3. Xem tổng giá trị kho sách")
    print("4. Thoát chương trình")
    
    chon = input("Nhập lựa chọn của bạn (1-4): ")
    
    if chon == "1":
        ma = input("Nhập mã sách: ")
        ten = input("Nhập tên sách: ")
        gia = input("Nhập giá sách: ")
        soluong = input("Nhập số lượng: ")
        
        them_sach(danh_sach_sach, ma, ten, gia, soluong)
        print("-> Thêm sách thành công!")
        
    elif chon == "2":
        tu_khoa = input("Nhập từ khóa tên sách cần tìm: ")
        kq = tim_kiem_theo_ten(danh_sach_sach, tu_khoa)
        
        if len(kq) > 0:
            print(f"-> Tìm thấy {len(kq)} cuốn sách:")
            for s in kq:
                print(f"   Mã: {s['MaSach']} | Tên: {s['Tensach']} | Giá: {s['Gia']} | SL: {s['SoLuong']}")
        else:
            print("-> Không tìm thấy cuốn sách nào phù hợp.")
            
    elif chon == "3":
        tong = tong_gia_tri_kho_sach(danh_sach_sach)
        print(f"-> Tổng giá trị kho sách là: {tong} VNĐ")
        
    elif chon == "4":
        print("-> Thoát chương trình. Tạm biệt!")
        break
    else:
        print("-> Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 4.")