from tkinter import Toplevel, Label, Scale, Button, HORIZONTAL
import cv2
import numpy as np


class ChinhSuaAnh(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master, width=255, height=765)

        self.da_ap_dung = False
        self.tu_dien_hinh_thai = {
            "isGetHistogram": [False, self.nut_bieu_do_nhan],
            "isGetErosion": [False, True, cv2.MORPH_ERODE],
            "isGetDilation": [False, True, cv2.MORPH_DILATE],
            "isGetOpen": [False, True, cv2.MORPH_OPEN],
            "isGetClose": [False, True, cv2.MORPH_CLOSE],
            "isGetGradient": [False, True, cv2.MORPH_GRADIENT],
            "isGetTopHat": [False, True, cv2.MORPH_TOPHAT],
            "isGetBlackHat": [False, True, cv2.MORPH_BLACKHAT],
            "isGetEllipse": [False, True, cv2.MORPH_ELLIPSE],
            "isGetRect": [False, True, cv2.MORPH_RECT],
            "isGetCross": [False, True, cv2.MORPH_CROSS],
            "isGetLogged": [False, self.nut_log_nhan],
            "isGetPowerLaw": [False, self.nut_luy_thua_nhan]
        }
        self.gia_tri_do_sang = 0
        self.gia_tri_do_sang_truoc = 0

        self.anh_goc = self.master.anh_dang_xu_ly
        self.anh_dang_xu_ly = self.master.anh_dang_xu_ly
        height, width, channels = self.anh_dang_xu_ly.shape
        self.nhan_do_sang = Label(self, text="Brightness Scale")
        self.thanh_do_sang = Scale(self, from_=0, to_=2, length=250, resolution=0.1,
                                      orient=HORIZONTAL)
        self.nhan_do = Label(self, text="Red Scale")
        self.thanh_do = Scale(self, from_=-100, to_=100, length=250, resolution=1,
                             orient=HORIZONTAL)
        self.nhan_xanh_la = Label(self, text="Green Scale")
        self.thanh_xanh_la = Scale(self, from_=-100, to_=100, length=250, resolution=1,
                             orient=HORIZONTAL)
        self.nhan_xanh_duong = Label(self, text="Blue Scale")
        self.thanh_xanh_duong = Scale(self, from_=-100, to_=100, length=250, resolution=1,
                             orient=HORIZONTAL)
        self.nhan_kich_thuoc_nhan = Label(self, text="Kernel Grid Size")
        self.thanh_kich_thuoc_nhan = Scale(self, from_=1, to_=np.gcd(width, height), length=250, resolution=1,
                                      orient=HORIZONTAL)
        self.nhan_kich_thuoc_gamma = Label(self, text="Gamma Size")
        self.thanh_kich_thuoc_gamma = Scale(self, from_=0.1, to_=10.0, length=250, resolution=0.1,
                                     orient=HORIZONTAL)
        self.nhan_gioi_han_cat = Label(self, text="Clip Limit Size")
        self.thanh_gioi_han_cat = Scale(self, from_=2.0, to_=15.0, length=250, resolution=0.1,
                                         orient=HORIZONTAL)

        self.nut_bieu_do = Button(self, text="Histogram Equalization", width=20, font="ariel 11 bold")
        self.nut_xoi_mon = Button(self, text="Erosion", width=10, font="ariel 11 bold")
        self.nut_gian_no = Button(self, text="Dilation", width=10, font="ariel 11 bold")
        self.nut_mo = Button(self, text="Opening", width=10, font="ariel 11 bold")
        self.nut_dong = Button(self, text="Closing", width=10, font="ariel 11 bold")
        self.nut_do_tu = Button(self, text="Gradient", width=10, font="ariel 11 bold")
        self.nut_top_hat = Button(self, text="Top Hat", width=10, font="ariel 11 bold")
        self.nut_black_hat = Button(self, text="Black Hat", width=10, font="ariel 11 bold")
        self.nut_ellipse = Button(self, text="Ellipse", width=10, font="ariel 11 bold")
        self.nut_hinh_chu_nhat = Button(self, text="Rect", width=10, font="ariel 11 bold")
        self.nut_chu_hoa = Button(self, text="Cross", width=10, font="ariel 11 bold")
        self.nut_log = Button(self, text="Log Transformation", width=20, font="ariel 11 bold")
        self.nut_luy_thua = Button(self, text="Power-Law (Gamma)", width=20, font="ariel 11 bold")
        self.nut_ap_dung = Button(self, text="Apply")
        self.nut_xem_truoc = Button(self, text="Preview")
        self.nut_huy = Button(self, text="Cancel")
        self.nut_xoa = Button(self, text="Clear")
        self.thanh_do_sang.set(1)
        self.thanh_kich_thuoc_nhan.set(8)
        self.thanh_kich_thuoc_gamma.set(0.5)
        self.thanh_gioi_han_cat.set(2.0)

        self.nut_bieu_do.bind("<ButtonRelease>", self.nut_bieu_do_nhan)
        self.nut_xoi_mon.bind("<ButtonRelease>", self.nut_xoi_mon_nhan)
        self.nut_gian_no.bind("<ButtonRelease>", self.nut_gian_no_nhan)
        self.nut_mo.bind("<ButtonRelease>", self.nut_mo_nhan)
        self.nut_dong.bind("<ButtonRelease>", self.nut_dong_nhan)
        self.nut_do_tu.bind("<ButtonRelease>", self.nut_do_tu_nhan)
        self.nut_top_hat.bind("<ButtonRelease>", self.nut_top_hat_nhan)
        self.nut_black_hat.bind("<ButtonRelease>", self.nut_black_hat_nhan)
        self.nut_ellipse.bind("<ButtonRelease>", self.nut_ellipse_nhan)
        self.nut_hinh_chu_nhat.bind("<ButtonRelease>", self.nut_hinh_chu_nhat_nhan)
        self.nut_chu_hoa.bind("<ButtonRelease>", self.nut_chu_hoa_nhan)
        self.nut_log.bind("<ButtonRelease>", self.nut_log_nhan)
        self.nut_luy_thua.bind("<ButtonRelease>", self.nut_luy_thua_nhan)
        self.nut_ap_dung.bind("<ButtonRelease>", self.nut_ap_dung_nhan)
        self.nut_xem_truoc.bind("<ButtonRelease>", self.nut_xem_truoc_nhan)
        self.nut_huy.bind("<ButtonRelease>", self.nut_huy_nhan)
        self.nut_xoa.bind("<ButtonRelease>", self.nut_xoa_nhan)

        self.nhan_do_sang.place(x=95, y=0)
        self.thanh_do_sang.place(x=0, y=20)
        self.nhan_do.place(x=100, y=60)
        self.thanh_do.place(x=0, y=80)
        self.nhan_xanh_la.place(x=100, y=120)
        self.thanh_xanh_la.place(x=0, y=140)
        self.nhan_xanh_duong.place(x=100, y=180)
        self.thanh_xanh_duong.place(x=0, y=200)
        self.nhan_kich_thuoc_nhan.place(x=90, y=240)
        self.thanh_kich_thuoc_nhan.place(x=0, y=255)
        self.nut_xoi_mon.place(x=0, y=300)
        self.nut_gian_no.place(x=120, y=300)
        self.nut_mo.place(x=0, y=340)
        self.nut_dong.place(x=120, y=340)
        self.nut_do_tu.place(x=0, y=380)
        self.nut_top_hat.place(x=120, y=380)
        self.nut_black_hat.place(x=0, y=420)
        self.nut_ellipse.place(x=120, y=420)
        self.nut_hinh_chu_nhat.place(x=0, y=460)
        self.nut_chu_hoa.place(x=120, y=460)
        self.nut_log.place(x=20, y=500)
        self.nhan_gioi_han_cat.place(x=90, y=540)
        self.thanh_gioi_han_cat.place(x=0, y=560)
        self.nut_bieu_do.place(x=20, y=600)
        self.nhan_kich_thuoc_gamma.place(x=95, y=640)
        self.thanh_kich_thuoc_gamma.place(x=0, y=660)
        self.nut_luy_thua.place(x=20, y=700)
        self.nut_huy.place(x=0, y=740)
        self.nut_xoa.place(x=90, y=740)
        self.nut_xem_truoc.place(x=140, y=740)
        self.nut_ap_dung.place(x=200, y=740)

    def nut_bieu_do_nhan(self, event):
        self.tu_dien_hinh_thai["isGetHistogram"][0] = True
        anh_ycrcb = cv2.cvtColor(self.anh_dang_xu_ly, cv2.COLOR_RGB2YCrCb)
        anh_ycrcb[:, :, 0] = cv2.equalizeHist(anh_ycrcb[:, :, 0])

        clahe = cv2.createCLAHE(clipLimit=float(self.thanh_gioi_han_cat.get()),
                                tileGridSize=(int(self.thanh_kich_thuoc_nhan.get()), int(self.thanh_kich_thuoc_nhan.get())))
        anh_ycrcb[:, :, 0] = clahe.apply(anh_ycrcb[:, :, 0])
        self.anh_dang_xu_ly = cv2.cvtColor(anh_ycrcb, cv2.COLOR_YCrCb2RGB)

    def lay_nhan(self, ten_hinh_thai):
        nhan = None
        kich_thuoc = int(self.thanh_kich_thuoc_nhan.get())

        try:
            nhan = cv2.getStructuringElement(shape=self.tu_dien_hinh_thai[ten_hinh_thai][2], ksize=(kich_thuoc, kich_thuoc))
        except cv2.error:
            nhan = cv2.getStructuringElement(shape=cv2.MORPH_ELLIPSE, ksize=(kich_thuoc, kich_thuoc))
        finally:
            return nhan

    def nut_xoi_mon_nhan(self, event):
        self.tu_dien_hinh_thai["isGetErosion"][0] = True

    def nut_gian_no_nhan(self, event):
        self.tu_dien_hinh_thai["isGetDilation"][0] = True

    def nut_mo_nhan(self, event):
        self.tu_dien_hinh_thai["isGetOpen"][0] = True

    def nut_dong_nhan(self, event):
        self.tu_dien_hinh_thai["isGetClose"][0] = True

    def nut_do_tu_nhan(self, event):
        self.tu_dien_hinh_thai["isGetGradient"][0] = True

    def nut_top_hat_nhan(self, event):
        self.tu_dien_hinh_thai["isGetTopHat"][0] = True

    def nut_black_hat_nhan(self, event):
        self.tu_dien_hinh_thai["isGetBlackHat"][0] = True

    def nut_ellipse_nhan(self, event):
        self.tu_dien_hinh_thai["isGetEllipse"][0] = True

    def nut_hinh_chu_nhat_nhan(self, event):
        self.tu_dien_hinh_thai["isGetRect"][0] = True

    def nut_chu_hoa_nhan(self, event):
        self.tu_dien_hinh_thai["isGetCross"][0] = True

    def nut_log_nhan(self, event):
        self.tu_dien_hinh_thai["isGetLogged"][0] = True
        c = 255 / (np.log(1 + np.max(self.anh_dang_xu_ly)))
        anh_log = c * np.log(1 + self.anh_dang_xu_ly)

        self.anh_dang_xu_ly = np.array(anh_log, dtype=np.uint8)

    def nut_luy_thua_nhan(self, event):
        self.tu_dien_hinh_thai["isGetPowerLaw"][0] = True
        self.anh_dang_xu_ly = np.array(255 * (self.anh_dang_xu_ly / 255) ** float(self.thanh_kich_thuoc_gamma.get()),
                                         dtype='uint8')

    def nut_xem_truoc_nhan(self, event):
        self.anh_dang_xu_ly = cv2.convertScaleAbs(self.anh_goc, alpha=self.thanh_do_sang.get())
        b, g, r = cv2.split(self.anh_dang_xu_ly)

        for gia_tri_b in b:
            cv2.add(gia_tri_b, self.thanh_xanh_duong.get(), gia_tri_b)
        for gia_tri_g in g:
            cv2.add(gia_tri_g, self.thanh_xanh_la.get(), gia_tri_g)
        for gia_tri_r in r:
            cv2.add(gia_tri_r, self.thanh_do.get(), gia_tri_r)

        self.anh_dang_xu_ly = cv2.merge((b, g, r))

        for khoa, gia_tri in self.tu_dien_hinh_thai.items():
            if gia_tri[0]:
                if gia_tri[1] is True:
                    self.anh_dang_xu_ly = cv2.morphologyEx(self.anh_dang_xu_ly, gia_tri[2], self.lay_nhan(khoa))
                else:
                    gia_tri[1](event)
        self.hien_thi_anh(self.anh_dang_xu_ly)
        self.da_ap_dung = True

    def nut_ap_dung_nhan(self, event):
        if not self.da_ap_dung:
            self.nut_xem_truoc_nhan(event)
        self.master.bo_nho_anh.append(self.master.anh_dang_xu_ly.copy())
        self.master.anh_dang_xu_ly = self.anh_dang_xu_ly
        self.dong(event)

    def nut_huy_nhan(self, event):
        self.dong(event)

    def hien_thi_anh(self, anh=None):
        self.master.chuc_nang_giao_dien.hien_thi_anh(anh=anh)

    def nut_xoa_nhan(self, event):
        for gia_tri in self.tu_dien_hinh_thai.values():
            gia_tri[0] = False
        self.thanh_xanh_duong.set(0)
        self.thanh_do.set(0)
        self.thanh_xanh_la.set(0)
        self.thanh_do_sang.set(1.0)
        self.thanh_kich_thuoc_nhan.set(8)
        self.thanh_kich_thuoc_gamma.set(0.5)
        self.thanh_gioi_han_cat.set(2.0)
        self.anh_dang_xu_ly = self.anh_goc.copy()
        self.hien_thi_anh(self.anh_dang_xu_ly)

    def dong(self, event):
        self.hien_thi_anh()
        self.destroy()