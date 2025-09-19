import tkinter as tk
from tkinter import ttk
from GiaoDien import GiaoDien
from ChucNangGiaoDien import ChucNangGiaoDien
from pygame import mixer


class Chinh(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Khởi tạo mixer
        self.mixer = mixer
        self.mixer.init()

        # Danh sách nhạc
        self.ds_nhac = [
            "./Sample_Images/Beethoven_9.Senfoni.mp3",
            "./Sample_Images/Mozart_Symphony_40.mp3",
            "./Sample_Images/Chopin_Nocturne.mp3"
        ]
        self.chi_so_nhac = 0

        # Phát bài đầu tiên
        self.mixer.music.load(self.ds_nhac[self.chi_so_nhac])
        self.mixer.music.set_volume(0.7)
        self.mixer.music.play(-1)

        # Các biến lưu trữ thông tin ảnh
        self.ten_tap_tin = ""
        self.ten_tap_tin_anh_them = ""
        self.anh_goc = None
        self.anh_dang_xu_ly = None
        self.anh_dang_xoay = None
        self.bo_nho_anh = list()
        self.anh_them = None
        self.da_chon_anh = False
        self.dang_ve = False
        self.dang_cat = False
        self.dang_dan = False
        self.so_hang, self.so_cot = None, None
        self.khung_loc = None
        self.khung_chinh_sua = None
        self.khung_phat_hien_bien = None

        # Cửa sổ chính
        self.title("Image Editor xây dựng bởi Văn Hạnh")

        self.giao_dien = GiaoDien(master=self)
        separator1 = ttk.Separator(master=self, orient=tk.HORIZONTAL)
        self.chuc_nang_giao_dien = ChucNangGiaoDien(master=self)

        self.giao_dien.pack(fill=tk.BOTH)
        separator1.pack(fill=tk.X, padx=10, pady=5)
        self.chuc_nang_giao_dien.pack(fill=tk.BOTH, padx=10, pady=10, expand=1)
