from tkinter import Toplevel, Button, RIGHT
import numpy as np
import cv2
from PIL import Image
from PIL.ImageFilter import (
    CONTOUR, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES
)


class LocAnh(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        self.anh_goc = self.master.anh_dang_xu_ly
        self.anh_da_loc = None

        self.nut_am_ban = Button(master=self, text="Negative")
        self.nut_den_trang = Button(master=self, text="Black White")
        self.nut_vang_nhung = Button(master=self, text="Sepia")
        self.nut_noi_khoi = Button(master=self, text="Emboss")
        self.nut_lam_mo_gaussian = Button(master=self, text="Gaussian Blur")
        self.nut_lam_mo_trung_vi = Button(master=self, text="Median Blur")
        self.nut_bien = Button(master=self, text="Edges of Photo")
        self.nut_nghe_thuat_foil = Button(master=self, text="Foil Art")
        self.nut_ve_but_chi = Button(master=self, text="Sharp Paint")
        self.nut_ve_dau = Button(master=self, text="Oil Paint")
        self.nut_pho_ve_nhe = Button(master=self, text="Sketch Light")
        self.nut_huy = Button(master=self, text="Cancel")
        self.nut_ap_dung = Button(master=self, text="Apply")

        self.nut_am_ban.bind("<ButtonRelease>", self.nut_am_ban_nhan)
        self.nut_den_trang.bind("<ButtonRelease>", self.nut_den_trang_nhan)
        self.nut_vang_nhung.bind("<ButtonRelease>", self.nut_vang_nhung_nhan)
        self.nut_noi_khoi.bind("<ButtonRelease>", self.nut_noi_khoi_nhan)
        self.nut_lam_mo_gaussian.bind("<ButtonRelease>", self.nut_lam_mo_gaussian_nhan)
        self.nut_lam_mo_trung_vi.bind("<ButtonRelease>", self.nut_lam_mo_trung_vi_nhan)
        self.nut_bien.bind("<ButtonRelease>", self.nut_bien_nhan)
        self.nut_nghe_thuat_foil.bind("<ButtonRelease>", self.nut_nghe_thuat_foil_nhan)
        self.nut_ve_but_chi.bind("<ButtonRelease>", self.nut_ve_but_chi_nhan)
        self.nut_ve_dau.bind("<ButtonRelease>", self.nut_ve_dau_nhan)
        self.nut_pho_ve_nhe.bind("<ButtonRelease>", self.nut_pho_ve_nhe_nhan)
        self.nut_ap_dung.bind("<ButtonRelease>", self.nut_ap_dung_nhan)
        self.nut_huy.bind("<ButtonRelease>", self.nut_huy_nhan)

        self.nut_am_ban.pack()
        self.nut_den_trang.pack()
        self.nut_vang_nhung.pack()
        self.nut_noi_khoi.pack()
        self.nut_lam_mo_gaussian.pack()
        self.nut_lam_mo_trung_vi.pack()
        self.nut_bien.pack()
        self.nut_nghe_thuat_foil.pack()
        self.nut_ve_but_chi.pack()
        self.nut_ve_dau.pack()
        self.nut_pho_ve_nhe.pack()
        self.nut_huy.pack(side=RIGHT)
        self.nut_ap_dung.pack()

    def nut_am_ban_nhan(self, event):
        self.am_ban()
        self.hien_thi_anh()

    def nut_den_trang_nhan(self, event):
        self.den_trang()
        self.hien_thi_anh()

    def nut_vang_nhung_nhan(self, event):
        self.vang_nhung()
        self.hien_thi_anh()

    def nut_noi_khoi_nhan(self, event):
        self.noi_khoi()
        self.hien_thi_anh()

    def nut_lam_mo_gaussian_nhan(self, event):
        self.lam_mo_gaussian()
        self.hien_thi_anh()

    def nut_lam_mo_trung_vi_nhan(self, event):
        self.lam_mo_trung_vi()
        self.hien_thi_anh()

    def nut_bien_nhan(self, event):
        self.bien()
        self.hien_thi_anh()

    def nut_nghe_thuat_foil_nhan(self, event):
        self.nghe_thuat_foil()
        self.hien_thi_anh()

    def nut_ve_but_chi_nhan(self, event):
        self.ve_but_chi()
        self.hien_thi_anh()

    def nut_ve_dau_nhan(self, event):
        self.ve_dau()
        self.hien_thi_anh()

    def nut_pho_ve_nhe_nhan(self, event):
        self.pho_ve_nhe()
        self.hien_thi_anh()

    def nut_ap_dung_nhan(self, event):
        self.master.bo_nho_anh.append(self.master.anh_dang_xu_ly.copy())
        self.master.anh_dang_xu_ly = self.anh_da_loc
        self.hien_thi_anh()
        self.dong()

    def nut_huy_nhan(self, event):
        self.master.chuc_nang_giao_dien.hien_thi_anh()
        self.dong()

    def hien_thi_anh(self):
        self.master.chuc_nang_giao_dien.hien_thi_anh(anh=self.anh_da_loc)

    def am_ban(self):
        self.anh_da_loc = cv2.bitwise_not(self.anh_goc)

    def den_trang(self):
        self.anh_da_loc = cv2.cvtColor(self.anh_goc, cv2.COLOR_BGR2GRAY)
        self.anh_da_loc = cv2.cvtColor(self.anh_da_loc, cv2.COLOR_GRAY2RGB)

    def vang_nhung(self):
        nhan = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])

        self.anh_da_loc = cv2.filter2D(self.anh_goc, -1, nhan)

    def noi_khoi(self):
        nhan = np.array([[0, -1, -1],
                           [1, 0, -1],
                           [1, 1, 0]])

        self.anh_da_loc = cv2.filter2D(self.anh_goc, -1, nhan)

    def lam_mo_gaussian(self):
        self.anh_da_loc = cv2.GaussianBlur(self.anh_goc, (41, 41), 0)

    def lam_mo_trung_vi(self):
        self.anh_da_loc = cv2.medianBlur(self.anh_goc, 41)

    def bien(self):
        self.anh_da_loc = np.array(Image.fromarray(self.anh_goc).filter(FIND_EDGES))

    def nghe_thuat_foil(self):
        self.anh_da_loc = np.array(Image.fromarray(self.anh_goc).filter(EMBOSS))

    def ve_but_chi(self):
        self.anh_da_loc = np.array(Image.fromarray(self.anh_goc).filter(EDGE_ENHANCE_MORE))

    def ve_dau(self):
        self.anh_da_loc = np.array(Image.fromarray(self.anh_goc).filter(EDGE_ENHANCE))

    def pho_ve_nhe(self):
        self.anh_da_loc = np.array(Image.fromarray(self.anh_goc).filter(CONTOUR))

    def dong(self):
        self.destroy()