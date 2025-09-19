from tkinter import Toplevel, RIGHT, LEFT, Label, Scale, Button, HORIZONTAL, CENTER, TOP
import cv2
import numpy as np


def xep_anh(scale, mang_anh):
    hang = len(mang_anh)
    cot = len(mang_anh[0])
    hang_co_san = isinstance(mang_anh[0], list)
    rong = mang_anh[0][0].shape[1]
    cao = mang_anh[0][0].shape[0]
    if hang_co_san:
        for x in range(0, hang):
            for y in range(0, cot):
                if mang_anh[x][y].shape[:2] == mang_anh[0][0].shape[:2]:
                    mang_anh[x][y] = cv2.resize(mang_anh[x][y], (0, 0), None, scale, scale)
                else:
                    mang_anh[x][y] = cv2.resize(mang_anh[x][y], (mang_anh[0][0].shape[1], mang_anh[0][0].shape[0]),
                                                None, scale, scale)
                if len(mang_anh[x][y].shape) == 2: mang_anh[x][y] = cv2.cvtColor(mang_anh[x][y], cv2.COLOR_GRAY2BGR)
        anh_trang = np.zeros((cao, rong, 3), np.uint8)
        ngang = [anh_trang] * hang
        for x in range(0, hang):
            ngang[x] = np.hstack(mang_anh[x])
        doc = np.vstack(ngang)
    else:
        for x in range(0, hang):
            if mang_anh[x].shape[:2] == mang_anh[0].shape[:2]:
                mang_anh[x] = cv2.resize(mang_anh[x], (0, 0), None, scale, scale)
            else:
                mang_anh[x] = cv2.resize(mang_anh[x], (mang_anh[0].shape[1], mang_anh[0].shape[0]), None, scale,
                                         scale)
            if len(mang_anh[x].shape) == 2: mang_anh[x] = cv2.cvtColor(mang_anh[x], cv2.COLOR_GRAY2BGR)
        doc = np.hstack(mang_anh)
    return doc


class PhatHienBien(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)
        self.da_hoan_thanh = False
        self.anh = None
        self.may_quay = None

        self.anh_goc = self.master.anh_dang_xu_ly

        self.nut_bat_dau = Button(master=self, text="Open Camera")
        self.nut_phat_hien = Button(master=self, text="Face-Mask Detection")
        self.nut_ket_thuc = Button(master=self, text="Finish Process")
        self.wm_title("Phát Hiện Biên")
        self.nhan_tham_so_nguong = Label(self, text="Threshold Parameter")
        self.thanh_tham_so_nguong = Scale(self, from_=0, to=255, length=300, resolution=0.1, activebackground="gray",
                                          cursor="arrow", orient=HORIZONTAL)
        self.thanh_tham_so_nguong.set(40)

        self.nhan_tham_so_nguong_2 = Label(self, text="Other Threshold Parameter")
        self.thanh_tham_so_nguong_2 = Scale(self, from_=0, to=255, length=300, resolution=0.1, activebackground="gray",
                                           cursor="arrow", orient=HORIZONTAL)

        self.nhan_tham_so_dien_tich = Label(self, text="Area Parameter")
        self.thanh_tham_so_dien_tich = Scale(self, from_=300, to=10000, length=300, resolution=1, activebackground="gray",
                                     cursor="arrow", orient=HORIZONTAL)

        self.nut_bat_dau.bind("<ButtonRelease>", self.nut_bat_dau_nhan)
        self.nut_phat_hien.bind("<ButtonRelease>", self.nut_phat_hien_nhan)
        self.nut_ket_thuc.bind("<ButtonRelease>", self.nut_ket_thuc_nhan)

        self.nhan_tham_so_nguong.pack()
        self.thanh_tham_so_nguong.pack(anchor=CENTER)
        self.nhan_tham_so_nguong_2.pack()
        self.thanh_tham_so_nguong_2.pack(anchor=CENTER)
        self.nhan_tham_so_dien_tich.pack()
        self.thanh_tham_so_dien_tich.pack()
        self.nut_bat_dau.pack(side=RIGHT)
        self.nut_phat_hien.pack(side=TOP)
        self.nut_ket_thuc.pack(side=LEFT)

    def nut_bat_dau_nhan(self, event):
        self.quay_video()

    def nut_phat_hien_nhan(self, event):
        self.phat_hien_mat_na()

    def nut_ket_thuc_nhan(self, event):
        self.master.chuc_nang_giao_dien.xoa_canvas()
        if self.master.anh_dang_xu_ly is not None:
            self.master.chuc_nang_giao_dien.hien_thi_anh()
        self.da_hoan_thanh = True

    def hien_thi_anh(self):
        self.master.chuc_nang_giao_dien.hien_thi_anh(anh=self.anh)

    def lay_duong_vien(self, anh, anh_duong_vien):
        # Sửa: OpenCV 4.x+ chỉ trả về 2 giá trị (bỏ image)
        duong_vien, cau_truc = cv2.findContours(anh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # etrafta çok fazla öge varsa ve en çok alana sahip olanların yakalanmasını istiyorsanız bu yorum satırını açın
        # duong_vien = sorted(duong_vien, key=cv2.contourArea, reverse=True)[:5]
        for duong in duong_vien:
            dien_tich = cv2.contourArea(duong)
            print(dien_tich)
            dien_tich_min = self.thanh_tham_so_dien_tich.get()
            if dien_tich > dien_tich_min:
                cv2.drawContours(anh_duong_vien, duong, -1, (255, 0, 0), 3)
                chu_vi = cv2.arcLength(duong, True)
                gan = cv2.approxPolyDP(duong, 0.02 * chu_vi, True)
                print(len(gan))
                so_goc = len(gan)
                x, y, w, h = cv2.boundingRect(gan)

                if so_goc == 3:
                    loai_doi_tuong = "Triangle"
                elif so_goc == 4:
                    ty_le = w / float(h)
                    if 0.98 < ty_le < 1.03:
                        loai_doi_tuong = "Square"
                    else:
                        loai_doi_tuong = "Rectangle"
                elif so_goc > 10:
                    loai_doi_tuong = "Circles"
                else:
                    loai_doi_tuong = "Polygon"

                cv2.rectangle(anh_duong_vien, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(anh_duong_vien, loai_doi_tuong,
                            (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                            (0, 0, 0), 2)
                cv2.putText(anh_duong_vien, "Area: " + str(dien_tich),
                            (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                            (0, 0, 0), 2)

    def quay_video(self):
        self.may_quay = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while True:
            self.cap_nhat()  # Sửa: self.cap_nhat() thay vì self.master.cap_nhat()
            if self.da_hoan_thanh:
                self.dong()
                break

            thanh_cong, anh = self.may_quay.read()
            if not thanh_cong:  # Thêm: Bỏ qua nếu không đọc được frame
                continue

            anh_duong_vien = anh.copy()
            anh_lam_mo = cv2.GaussianBlur(anh, (7, 7), 1)
            anh_xam = cv2.cvtColor(anh_lam_mo, cv2.COLOR_BGR2GRAY)

            nguong_1 = self.thanh_tham_so_nguong.get()
            nguong_2 = self.thanh_tham_so_nguong_2.get()
            anh_canny = cv2.Canny(anh_xam, nguong_1, nguong_2)

            nhan = np.ones((5, 5))
            anh_gian_no = cv2.dilate(anh_canny, nhan, iterations=1)

            self.lay_duong_vien(anh_gian_no, anh_duong_vien)

            self.anh = xep_anh(0.8, ([anh, anh_xam, anh_canny],
                                            [anh_gian_no, anh_duong_vien, anh_duong_vien]))

            self.hien_thi_anh()
            self.master.update()

    def phat_hien_mat_na(self):
        try:
            # Opencv versiyonu "pip install opencv-contrib-python"
            mang = cv2.dnn.readNet("dnn_model/yolov4-tiny-custom_best.weights", "dnn_model/yolov4-tiny-custom.cfg")
            mo_hinh = cv2.dnn_DetectionModel(mang)
            mo_hinh.setInputParams(size=(320, 320), scale=1 / 255)

            lop = ['with_mask', 'without_mask']
            mau = [[0, 0, 255], [255, 0, 0]]
            self.may_quay = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            self.may_quay.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
            self.may_quay.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

            while True:
                self.cap_nhat()  # Sửa: self.cap_nhat() thay vì self.master.cap_nhat()
                if self.da_hoan_thanh:
                    self.dong()
                    break

                thanh_cong, khung = self.may_quay.read()
                if not thanh_cong:  # Thêm: Bỏ qua nếu không đọc được frame
                    continue

                # Phát hiện đối tượng
                (id_lop, diem, hinh_vu) = mo_hinh.detect(khung, confThreshold=0.6, nmsThreshold=.4)
                for id_lop_, diem_, hinh_vu_ in zip(id_lop, diem, hinh_vu):
                    (x, y, w, h) = hinh_vu_
                    ten_lop = lop[id_lop_]
                    mau_ = mau[id_lop_]

                    if ten_lop in lop:
                        cv2.putText(khung, ten_lop + '  ' + str(format(diem_, '0.2')), (x, y - 10),
                                    cv2.FONT_HERSHEY_PLAIN, 3, mau_, 2)
                        cv2.rectangle(khung, (x, y), (x + w, y + h), mau_, 3)

                self.anh = khung
                self.hien_thi_anh()
                self.master.update()

        except Exception as e:  # Thêm: Xử lý lỗi load model hoặc khác
            print(f"Lỗi phát hiện mask: {e}")
            self.dong()

    def cap_nhat(self):
        self.master.update()

    def dong(self):
        if self.may_quay is not None:
            self.may_quay.release()
        self.destroy()