import tkinter as tk
from tkinter import Frame, Button, Label, Entry, filedialog, Scale, HORIZONTAL
from LocAnh import LocAnh
from ChinhSuaAnh import ChinhSuaAnh
from PhatHienBien import PhatHienBien
from PIL import Image
import numpy as np
import cv2


class GiaoDien(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master=master, bg='gray', width=1280, height=100)

        self.nhan_am_nhac = Label(self, text="Music Volume", bg='gray', font="ariel 11 bold")
        self.thanh_am_nhac = Scale(self, from_=0.0, to_=1.0, length=100, resolution=0.01,
                                   orient=HORIZONTAL)
        self.thanh_am_nhac.set(0.7)
        self.thanh_am_nhac.bind("<ButtonRelease-1>", self.am_luong_nhac)

        self.nut_moi = Button(self, text="New", bg='gold', fg='black', width=10, font="ariel 13 bold")
        self.nut_luu = Button(self, text="Save", bg='black', fg='gold', width=10, font="ariel 13 bold")
        self.nut_luu_thanh = Button(self, text="Save As", bg="magenta", fg='yellow', width=10, font="ariel 13 bold")
        self.nut_loc = Button(self, text="Filter", bg="black", fg='white', width=10, font="ariel 13 bold")
        self.nut_chinh_sua = Button(self, text="Adjust", bg="black", fg='white', width=10, font="ariel 13 bold")
        self.nut_xoa = Button(self, text="Clear", bg="cyan", fg='red', width=10, font="ariel 13 bold")
        self.nut_xu_ly_video = Button(self, text="Shape Detection on Webcam", bg="black", fg='red', width=25,
                                      font="ariel 13 bold")
        self.nut_ve = Button(self, text="Draw", bg="black", fg='white', width=10, font="ariel 13 bold")
        self.nut_hoi_quay_lai = Button(self, text="Undo", bg="blue", fg='white', width=6, font="ariel 13 bold")
        self.nut_tien = Button(self, text="Forward", bg="blue", fg='white', width=7, font="ariel 13 bold")
        self.nut_cat = Button(self, text="Crop", bg="black", fg='white', width=10, font="ariel 13 bold")
        self.nut_xoay = Button(self, text="Xoay", bg="black", fg='white', width=5, font="ariel 10 bold")
        self.nut_luu_xoay = Button(self, text="Lưu\nXoay", bg="black", fg='white', width=8,
                                   font="ariel 8 bold")
        self.nhan_xoay = Label(text="Nhập góc xoay", font="Arial 8 bold")
        self.o_nhap_xoay = Entry(width=15)
        self.nut_thay_doi_kich_thuoc = Button(self, text="Resize", bg="black", fg='white', width=10, font="ariel 13 bold")
        self.nhan_thay_doi_kich_thuoc = Label(text="Nhâp size X và Y", font="Arial 8 bold")
        self.o_nhap_x_kich_thuoc = Entry(width=8)
        self.o_nhap_y_kich_thuoc = Entry(width=8)
        self.nut_them_anh = Button(self, text="Thêm ảnh\ndán lên",
                                   bg='red', fg='blue', width=15, font="ariel 12 bold")
        self.nut_lat = Button(self, text="Flipping", bg="black", fg='white', width=10, font="ariel 13 bold")
        self.nut_tang_tuong_phan = Button(self, text="Increase\nContrast", bg="black", fg='white', width=10,
                                          font="ariel 13 bold")

        # Thay thế Music/Control bằng 2 nút: Music + Clear Canvas
        self.nut_music = Button(self, text="Music", bg="black", fg='gold',
                                width=12, font="ariel 13 bold")
        self.nut_clear_canvas = Button(self, text="Clear Canvas", bg="black", fg='red',
                                       width=13, font="ariel 13 bold")

        # Gán sự kiện
        self.nut_moi.bind("<ButtonRelease>", self.nut_moi_nhan)
        self.nut_luu.bind("<ButtonRelease>", self.nut_luu_nhan)
        self.nut_luu_thanh.bind("<ButtonRelease>", self.nut_luu_thanh_nhan)
        self.nut_loc.bind("<ButtonRelease>", self.nut_loc_nhan)
        self.nut_chinh_sua.bind("<ButtonRelease>", self.nut_chinh_sua_nhan)
        self.nut_xoa.bind("<ButtonRelease>", self.nut_xoa_nhan)
        self.nut_xu_ly_video.bind("<ButtonRelease>", self.nut_xu_ly_video_nhan)
        self.nut_ve.bind("<ButtonRelease>", self.nut_ve_nhan)
        self.nut_hoi_quay_lai.bind("<ButtonRelease>", self.nut_hoi_quay_lai_nhan)
        self.nut_tien.bind("<ButtonRelease>", self.nut_tien_nhan)
        self.nut_cat.bind("<ButtonRelease>", self.nut_cat_nhan)
        self.nut_xoay.bind("<ButtonRelease>", self.nut_xoay_nhan)
        self.nut_luu_xoay.bind("<ButtonRelease>", self.nut_luu_xoay_nhan)
        self.nut_thay_doi_kich_thuoc.bind("<ButtonRelease>", self.nut_thay_doi_kich_thuoc_nhan)
        self.nut_them_anh.bind("<ButtonRelease>", self.nut_them_anh_nhan)
        self.nut_lat.bind("<ButtonRelease>", self.nut_lat_nhan)
        self.nut_tang_tuong_phan.bind("<ButtonRelease>", self.nut_tang_tuong_phan_nhan)

        self.nut_music.bind("<ButtonRelease>", self.nut_music_nhan)
        self.nut_clear_canvas.bind("<ButtonRelease>", self.nut_clear_canvas_nhan)

        # Đặt vị trí các nút
        self.nut_moi.place(x=0, y=0)
        self.nut_luu.place(x=0, y=35)
        self.nut_luu_thanh.place(x=120, y=35)
        self.nhan_am_nhac.place(x=10, y=70)
        self.thanh_am_nhac.place(x=120, y=60)
        self.nut_xoa.place(x=120, y=0)
        self.nut_loc.place(x=240, y=0)
        self.nut_chinh_sua.place(x=240, y=45)
        self.nut_xu_ly_video.place(x=1020, y=10)
        self.nut_ve.place(x=360)
        self.nut_cat.place(x=360, y=45)
        self.nhan_xoay.place(x=490)
        self.o_nhap_xoay.place(x=490, y=25)
        self.nut_xoay.place(x=475, y=45)
        self.nut_luu_xoay.place(x=525, y=45)
        self.nhan_thay_doi_kich_thuoc.place(x=608)
        self.o_nhap_x_kich_thuoc.place(x=600, y=25)
        self.o_nhap_y_kich_thuoc.place(x=660, y=25)
        self.nut_thay_doi_kich_thuoc.place(x=600, y=45)
        self.nut_them_anh.place(x=720)
        self.nut_hoi_quay_lai.place(x=720, y=55)
        self.nut_tien.place(x=800, y=55)
        self.nut_lat.place(x=885)
        self.nut_tang_tuong_phan.place(x=885, y=45)

        # 2 nút Music và Clear Canvas cạnh nhau, ngang hàng với nhau
        self.nut_music.place(x=1020, y=45)
        self.nut_clear_canvas.place(x=1160, y=45)

    def am_luong_nhac(self, event):
        self.master.mixer.music.set_volume(float(self.thanh_am_nhac.get()))

    def kiem_tra_trang_thai(self):
        if self.master.da_chon_anh:
            if self.master.dang_cat:
                self.master.chuc_nang_giao_dien.tat_cat()
            if self.master.dang_ve:
                self.master.chuc_nang_giao_dien.tat_ve()
            if self.master.dang_dan:
                self.master.chuc_nang_giao_dien.tat_dan()
            return True
        return False

    def nut_moi_nhan(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.nut_moi:
            if self.master.dang_ve:
                self.master.chuc_nang_giao_dien.tat_ve()
            if self.master.dang_cat:
                self.master.chuc_nang_giao_dien.tat_cat()
            if self.master.dang_dan:
                self.master.chuc_nang_giao_dien.tat_dan()

            ten_tap_tin = filedialog.askopenfilename()
            anh = cv2.cvtColor(np.array(Image.open(ten_tap_tin)), cv2.COLOR_BGR2RGB)

            if anh is not None:
                self.master.ten_tap_tin = ten_tap_tin
                self.master.anh_goc = anh.copy()
                self.master.anh_dang_xu_ly = anh.copy()
                self.master.chuc_nang_giao_dien.hien_thi_anh()
                self.master.da_chon_anh = True
                self.master.so_hang, self.master.so_cot = self.master.anh_dang_xu_ly.shape[:2]
                self.master.bo_nho_anh.append(self.master.anh_dang_xu_ly.copy())

    def nut_luu_nhan(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.nut_luu:
            if self.kiem_tra_trang_thai():
                anh_luu = self.master.anh_dang_xu_ly
                ten_tap_tin_anh = self.master.ten_tap_tin
                cv2.imwrite(ten_tap_tin_anh, anh_luu)

    def nut_luu_thanh_nhan(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.nut_luu_thanh:
            if self.kiem_tra_trang_thai():
                loai_tap_tin_goc = self.master.ten_tap_tin.split('.')[-1]
                ten_tap_tin = filedialog.asksaveasfilename()
                ten_tap_tin = ten_tap_tin + "." + loai_tap_tin_goc

                anh_luu = self.master.anh_dang_xu_ly
                cv2.imwrite(ten_tap_tin, anh_luu)

                self.master.ten_tap_tin = ten_tap_tin

    def nut_loc_nhan(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.nut_loc:
            if self.kiem_tra_trang_thai():
                self.master.khung_loc = LocAnh(master=self.master)
                self.master.khung_loc.grab_set()

    def nut_chinh_sua_nhan(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.nut_chinh_sua:
            if self.kiem_tra_trang_thai():
                self.master.khung_chinh_sua = ChinhSuaAnh(master=self.master)
                self.master.khung_chinh_sua.grab_set()

    def nut_xoa_nhan(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.nut_xoa:
            if self.kiem_tra_trang_thai():
                self.master.bo_nho_anh.clear()
                self.master.chuc_nang_giao_dien.bo_nho_tien.clear()
                self.master.anh_dang_xu_ly = self.master.anh_goc.copy()
                self.master.chuc_nang_giao_dien.hien_thi_anh()

    def nut_xu_ly_video_nhan(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.nut_xu_ly_video:
            if self.kiem_tra_trang_thai():
                print("There will be the amount of area and the approximate number of "
                      "edges of the objects detected by the camera in console.")

            self.master.khung_phat_hien_bien = PhatHienBien(master=self.master)
            self.master.khung_phat_hien_bien.grab_set()

    def nut_ve_nhan(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.nut_ve:
            if self.kiem_tra_trang_thai():
                self.master.chuc_nang_giao_dien.kich_hoat_ve()

    def nut_hoi_quay_lai_nhan(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.nut_hoi_quay_lai:
            self.master.chuc_nang_giao_dien.hoi_quay_anh()

    def nut_tien_nhan(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.nut_tien:
            self.master.chuc_nang_giao_dien.tien_anh()

    def nut_cat_nhan(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.nut_cat:
            if self.kiem_tra_trang_thai():
                self.master.chuc_nang_giao_dien.kich_hoat_cat()

    def nut_xoay_nhan(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.nut_xoay:
            if self.kiem_tra_trang_thai():
                self.master.chuc_nang_giao_dien.xoay(self.o_nhap_xoay.get())

    def nut_luu_xoay_nhan(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.nut_luu_xoay:
            if self.kiem_tra_trang_thai():
                self.master.anh_dang_xu_ly = self.master.anh_dang_xoay

    def nut_thay_doi_kich_thuoc_nhan(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.nut_thay_doi_kich_thuoc:
            if self.kiem_tra_trang_thai():
                self.master.chuc_nang_giao_dien.thay_doi_kich_thuoc(self.o_nhap_x_kich_thuoc.get(),
                                                                     self.o_nhap_y_kich_thuoc.get())

    def nut_them_anh_nhan(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.nut_them_anh:
            if self.kiem_tra_trang_thai():
                ten_tap_tin = filedialog.askopenfilename()
                anh = cv2.cvtColor(np.array(Image.open(ten_tap_tin)), cv2.COLOR_BGRA2RGBA)

                if anh is not None:
                    self.master.ten_tap_tin_anh_them = ten_tap_tin
                    self.master.anh_them = anh.copy()
                    self.master.chuc_nang_giao_dien.kich_hoat_dan()

    def nut_lat_nhan(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.nut_lat:
            if self.kiem_tra_trang_thai():
                self.master.chuc_nang_giao_dien.lat_anh()

    def nut_tang_tuong_phan_nhan(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.nut_tang_tuong_phan:
            if self.kiem_tra_trang_thai():
                self.master.chuc_nang_giao_dien.tang_tuong_phan()

    # Popup Music
    def nut_music_nhan(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.nut_music:
            win = tk.Toplevel(self)
            win.title("Music Control")
            win.geometry("250x120")

            def toggle_music():
                if self.master.mixer.music.get_busy():
                    self.master.mixer.music.stop()
                    print("Music stopped.")
                else:
                    bai_hat = self.master.ds_nhac[self.master.chi_so_nhac]
                    self.master.mixer.music.load(bai_hat)
                    self.master.mixer.music.play()
                    print("Music playing:", bai_hat)

            btn_toggle = Button(win, text="Play/Stop", width=15, command=toggle_music)
            btn_toggle.pack(pady=10)

            def next_song():
                if hasattr(self.master, "ds_nhac") and self.master.ds_nhac:
                    self.master.chi_so_nhac = (self.master.chi_so_nhac + 1) % len(self.master.ds_nhac)
                    bai_hat = self.master.ds_nhac[self.master.chi_so_nhac]
                    self.master.mixer.music.load(bai_hat)
                    self.master.mixer.music.play()
                    print("Now playing:", bai_hat)

            btn_next = Button(win, text="Next Song", width=15, command=next_song)
            btn_next.pack(pady=10)

    # Clear Canvas
    def nut_clear_canvas_nhan(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.nut_clear_canvas:
            self.master.anh_dang_xu_ly = None
            self.master.chuc_nang_giao_dien.xoa_canvas()
            print("Cleared current image.")
