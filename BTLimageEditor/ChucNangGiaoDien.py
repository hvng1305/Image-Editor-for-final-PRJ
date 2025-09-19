from tkinter import Frame, Canvas, CENTER, ROUND
import numpy as np
from PIL import Image, ImageTk, ImageEnhance
import cv2


class ChucNangGiaoDien(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=master, bg="black", width=1280, height=720)

        self.anh_hien_thi = None
        self.x = 0
        self.y = 0
        self.cat_bat_dau_x = 0
        self.cat_bat_dau_y = 0
        self.cat_ket_thuc_x = 0
        self.cat_ket_thuc_y = 0
        self.id_hinh_chu_nhat = 0
        self.ti_le = 0
        self.goc_xoay = 0
        self.bo_nho_tien = list()

        self.canvas = Canvas(self, bg="black", width=1280, height=720)
        self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

    def hien_thi_anh(self, anh=None):
        self.xoa_canvas()

        if anh is None:
            anh = self.master.anh_dang_xu_ly.copy()
        else:
            anh = anh

        anh = cv2.cvtColor(anh, cv2.COLOR_BGR2RGB)
        height, width, channels = anh.shape
        ti_le = height / width

        new_width = width
        new_height = height

        if height > self.winfo_height() or width > self.winfo_width():
            if ti_le < 1:
                new_width = self.winfo_width()
                new_height = int(new_width * ti_le)
            else:
                new_height = self.winfo_height()
                new_width = int(new_height * (width / height))

        self.anh_hien_thi = cv2.resize(anh, (new_width, new_height))
        self.anh_hien_thi = ImageTk.PhotoImage(Image.fromarray(self.anh_hien_thi))

        self.ti_le = height / new_height

        self.canvas.config(width=new_width, height=new_height)
        self.canvas.create_image(new_width / 2, new_height / 2, anchor=CENTER, image=self.anh_hien_thi)

    def tang_tuong_phan(self):
        self.master.bo_nho_anh.append(self.master.anh_dang_xu_ly.copy())
        tuong_phan = (ImageEnhance.Contrast(Image.fromarray(self.master.anh_dang_xu_ly))).enhance(1.1)
        self.master.anh_dang_xu_ly = np.array(tuong_phan)
        self.master.bo_nho_anh.append(self.master.anh_dang_xu_ly.copy())
        self.hien_thi_anh()

    def lat_anh(self):
        self.master.bo_nho_anh.append(self.master.anh_dang_xu_ly.copy())
        anh_lat = Image.fromarray(self.master.anh_dang_xu_ly).copy()
        anh_lat = anh_lat.transpose(Image.FLIP_LEFT_RIGHT)
        self.master.anh_dang_xu_ly = np.array(anh_lat).copy()
        self.master.bo_nho_anh.append(self.master.anh_dang_xu_ly.copy())
        self.hien_thi_anh()

    def thay_doi_kich_thuoc(self, x, y):
        if x or y == '':
            x, y = 500, 500
        else:
            x, y = int(x),  int(y)
        self.master.bo_nho_anh.append(self.master.anh_dang_xu_ly.copy())
        self.master.anh_dang_xu_ly = np.array(Image.fromarray(self.master.anh_dang_xu_ly).resize((x, y)))
        self.master.bo_nho_anh.append(self.master.anh_dang_xu_ly.copy())
        self.hien_thi_anh()

    def xoay(self, goc_xoay_anh):
        if goc_xoay_anh == '':
            goc_xoay_anh = 60
        else:
            goc_xoay_anh = float(goc_xoay_anh)
        self.goc_xoay += goc_xoay_anh
        self.master.anh_dang_xoay = np.array(Image.fromarray(self.master.anh_dang_xu_ly).rotate(self.goc_xoay))
        self.master.bo_nho_anh.append(self.master.anh_dang_xoay.copy())
        self.hien_thi_anh(anh=self.master.anh_dang_xoay)

    def kich_hoat_dan(self):
        self.canvas.bind("<ButtonPress>", self.bat_dau_dan)
        self.canvas.bind("<B1-Motion>", self.dang_dan)
        self.canvas.bind("<ButtonRelease>", self.ket_thuc_dan)

        self.master.dang_dan = True

    def kich_hoat_ve(self):
        self.canvas.bind("<ButtonPress>", self.bat_dau_ve)
        self.canvas.bind("<B1-Motion>", self.ve)

        self.master.dang_ve = True

    def kich_hoat_cat(self):
        self.canvas.bind("<ButtonPress>", self.bat_dau_cat)
        self.canvas.bind("<B1-Motion>", self.cat)
        self.canvas.bind("<ButtonRelease>", self.ket_thuc_cat)

        self.master.dang_cat = True

    def tat_dan(self):
        self.canvas.unbind("<ButtonPress>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease>")

        self.master.dang_dan = False

    def tat_ve(self):
        self.canvas.unbind("<ButtonPress>")
        self.canvas.unbind("<B1-Motion>")

        self.master.dang_ve = False

    def tat_cat(self):
        self.canvas.unbind("<ButtonPress>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease>")

        self.master.dang_cat = False

    def bat_dau_dan(self, event):
        self.master.bo_nho_anh.append(self.master.anh_dang_xu_ly.copy())
        self.x = event.x
        self.y = event.y

    def bat_dau_ve(self, event):
        self.master.bo_nho_anh.append(self.master.anh_dang_xu_ly.copy())
        self.x = event.x
        self.y = event.y

    def dang_dan(self, event):
        global anh
        anh = ImageTk.PhotoImage(file=self.master.ten_tap_tin_anh_them)
        self.canvas.create_image(self.x, self.y, image=anh)
        self.x = event.x
        self.y = event.y

    def ket_thuc_dan(self, event):
        anh_chu = Image.fromarray(self.master.anh_dang_xu_ly).copy()
        anh_dan = Image.fromarray(self.master.anh_them).copy()

        vi_tri = (self.x - int(anh_dan.width/2), self.y - int(anh_dan.height/2))
        anh_chu.paste(anh_dan, vi_tri, anh_dan)

        self.master.anh_dang_xu_ly = np.array(anh_chu)
        self.hien_thi_anh()

    def ve(self, event):
        self.canvas.create_line(self.x, self.y, event.x, event.y, width=2,
                                fill="red", capstyle=ROUND, smooth=True)

        cv2.line(self.master.anh_dang_xu_ly, (int(self.x * self.ti_le), int(self.y * self.ti_le)),
                 (int(event.x * self.ti_le), int(event.y * self.ti_le)),
                 (0, 0, 255), thickness=int(self.ti_le * 2),
                 lineType=8)

        self.x = event.x
        self.y = event.y

    def bat_dau_cat(self, event):
        self.master.bo_nho_anh.append(self.master.anh_dang_xu_ly.copy())
        self.cat_bat_dau_x = event.x
        self.cat_bat_dau_y = event.y

    def cat(self, event):
        if self.id_hinh_chu_nhat:
            self.canvas.delete(self.id_hinh_chu_nhat)

        self.cat_ket_thuc_x = event.x
        self.cat_ket_thuc_y = event.y

        self.id_hinh_chu_nhat = self.canvas.create_rectangle(self.cat_bat_dau_x, self.cat_bat_dau_y,
                                                         self.cat_ket_thuc_x, self.cat_ket_thuc_y, width=1)

    def ket_thuc_cat(self, event):
        if self.cat_bat_dau_x <= self.cat_ket_thuc_x and self.cat_bat_dau_y <= self.cat_ket_thuc_y:
            bat_dau_x = int(self.cat_bat_dau_x * self.ti_le)
            bat_dau_y = int(self.cat_bat_dau_y * self.ti_le)
            ket_thuc_x = int(self.cat_ket_thuc_x * self.ti_le)
            ket_thuc_y = int(self.cat_ket_thuc_y * self.ti_le)
        elif self.cat_bat_dau_x > self.cat_ket_thuc_x and self.cat_bat_dau_y <= self.cat_ket_thuc_y:
            bat_dau_x = int(self.cat_ket_thuc_x * self.ti_le)
            bat_dau_y = int(self.cat_bat_dau_y * self.ti_le)
            ket_thuc_x = int(self.cat_bat_dau_x * self.ti_le)
            ket_thuc_y = int(self.cat_ket_thuc_y * self.ti_le)
        elif self.cat_bat_dau_x <= self.cat_ket_thuc_x and self.cat_bat_dau_y > self.cat_ket_thuc_y:
            bat_dau_x = int(self.cat_bat_dau_x * self.ti_le)
            bat_dau_y = int(self.cat_ket_thuc_y * self.ti_le)
            ket_thuc_x = int(self.cat_ket_thuc_x * self.ti_le)
            ket_thuc_y = int(self.cat_bat_dau_y * self.ti_le)
        else:
            bat_dau_x = int(self.cat_ket_thuc_x * self.ti_le)
            bat_dau_y = int(self.cat_ket_thuc_y * self.ti_le)
            ket_thuc_x = int(self.cat_bat_dau_x * self.ti_le)
            ket_thuc_y = int(self.cat_bat_dau_y * self.ti_le)

        x = slice(bat_dau_x, ket_thuc_x, 1)
        y = slice(bat_dau_y, ket_thuc_y, 1)

        self.master.anh_dang_xu_ly = self.master.anh_dang_xu_ly[y, x]
        self.master.bo_nho_anh.append(self.master.anh_dang_xu_ly.copy())

        self.hien_thi_anh()

    def xoa_canvas(self):
        self.canvas.delete("all")

    def hoi_quay_anh(self):
        if self.master.bo_nho_anh:
            self.master.anh_dang_xu_ly = self.master.bo_nho_anh.pop()
            self.bo_nho_tien.append(self.master.anh_dang_xu_ly)
        self.hien_thi_anh()

    def tien_anh(self):
        if self.bo_nho_tien:
            self.master.anh_dang_xu_ly = self.bo_nho_tien.pop()
            self.master.bo_nho_anh.append(self.master.anh_dang_xu_ly)
        self.hien_thi_anh()