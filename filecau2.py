import tkinter as tk
from tkinter import messagebox

danh_sach = []

root = tk.Tk()
root.title("Quản lý sách thư viện")
root.geometry("600x450")

# Tiêu đề
lbl_title = tk.Label(root, text="PHẦN MỀM QUẢN LÝ SÁCH", font=("Arial", 12, "bold"))
lbl_title.pack(pady=5)

# a) Form nhập liệu
frame_form = tk.Frame(root)
frame_form.pack(pady=5)

tk.Label(frame_form, text="Mã sách:").grid(row=0, column=0, sticky="w", padx=5, pady=3)
txt_ma = tk.Entry(frame_form, width=30)
txt_ma.grid(row=0, column=1, padx=5, pady=3)

tk.Label(frame_form, text="Tên sách:").grid(row=1, column=0, sticky="w", padx=5, pady=3)
txt_ten = tk.Entry(frame_form, width=30)
txt_ten.grid(row=1, column=1, padx=5, pady=3)

tk.Label(frame_form, text="Giá sách:").grid(row=2, column=0, sticky="w", padx=5, pady=3)
txt_gia = tk.Entry(frame_form, width=30)
txt_gia.grid(row=2, column=1, padx=5, pady=3)

tk.Label(frame_form, text="Số lượng:").grid(row=3, column=0, sticky="w", padx=5, pady=3)
txt_sl = tk.Entry(frame_form, width=30)
txt_sl.grid(row=3, column=1, padx=5, pady=3)

lb_hien_thi = tk.Listbox(root, width=70, height=10)
lb_hien_thi.pack(pady=10)

def xu_ly_them():
    ma = txt_ma.get()
    ten = txt_ten.get()
    str_gia = txt_gia.get()
    str_sl = txt_sl.get()
    
    if ma == "" or ten == "":
        messagebox.showerror("Lỗi", "Mã sách và Tên sách không được để trống!")
        return
        
    try:
        gia = float(str_gia)
        soluong = int(str_sl)
    except ValueError:
        messagebox.showerror("Lỗi", "Giá và số lượng phải nhập số hợp lệ!")
        return
    
    sach = {"MaSach": ma, "Tensach": ten, "Gia": gia, "SoLuong": soluong}
    danh_sach.append(sach)
    
    chuoi_hien_thi = ma + " - " + ten + " - " + str(gia) + "đ - SL: " + str(soluong)
    lb_hien_thi.insert(tk.END, chuoi_hien_thi)
    
    txt_ma.delete(0, tk.END)
    txt_ten.delete(0, tk.END)
    txt_gia.delete(0, tk.END)
    txt_sl.delete(0, tk.END)
    
    messagebox.showinfo("Thông báo", "Thêm sách thành công!")

def xu_ly_tim():
    tu_khoa = txt_tim.get().lower()
    lb_hien_thi.delete(0, tk.END) 
    
    for s in danh_sach:
        if tu_khoa in s["Tensach"].lower():
            chuoi = s["MaSach"] + " - " + s["Tensach"] + " - " + str(s["Gia"]) + "đ - SL: " + str(s["SoLuong"])
            lb_hien_thi.insert(tk.END, chuoi)

frame_nut = tk.Frame(root)
frame_nut.pack(pady=5)
btn_them = tk.Button(frame_nut, text="Thêm sách", command=xu_ly_them, bg="lightgreen")
btn_them.pack(side="left", padx=5)

tk.Label(frame_nut, text="Từ khóa:").pack(side="left", padx=5)
txt_tim = tk.Entry(frame_nut, width=15)
txt_tim.pack(side="left", padx=5)

btn_tim = tk.Button(frame_nut, text="Tìm kiếm", command=xu_ly_tim)
btn_tim.pack(side="left", padx=5)

root.mainloop()