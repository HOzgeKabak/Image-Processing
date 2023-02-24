import math
#from hw2_image import interpolate,interpolate_pixel
from PyQt5.QtWidgets import *
from hw1_python import Ui_MainWindow
from PyQt5.QtGui import QPixmap, QImage
import cv2
import numpy as np
import icons_rc
from matplotlib import pyplot as plt
#import noises
from skimage.io import imread, imshow
import matplotlib.pyplot as plt
import numpy as np
from skimage.feature import match_template
class gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.img = None
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.enter_image)
        self.ui.pushButton_2.clicked.connect(self.filtering)
        self.ui.verticalSlider.valueChanged.connect(self.visible)
        self.a = None
        self.ui.label_2.setVisible(False)
        self.ui.label_8.setVisible(False)
        self.ui.dial.valueChanged.connect(self.colour)
        self.ui.horizontalSlider_6.valueChanged.connect(self.range_black)
        self.ui.pushButton_4.clicked.connect(self.black_white)
        self.ui.dial_2.valueChanged.connect(self.histogram)
        self.ui.pushButton_5.clicked.connect(self.hist)
        self.ui.dial_3.valueChanged.connect(self.filters)
        self.ui.pushButton_3.clicked.connect(self.rontgen)
        self.ui.horizontalSlider.valueChanged.connect(self.boundry1)
        self.ui.horizontalSlider_2.valueChanged.connect(self.boundry2)
        self.ui.horizontalSlider_6.valueChanged.connect(self.boundryw)
        self.ui.horizontalSlider_5.valueChanged.connect(self.boundryb)
        self.ui.pushButton_8.clicked.connect(self.vertical)
        self.ui.pushButton_9.clicked.connect(self.horizontal)
        self.ui.pushButton_10.clicked.connect(self.resizing)
        self.ui.pushButton_11.clicked.connect(self.crop)
        self.ui.pushButton_12.clicked.connect(self.shift)
        #self.ui.pushButton_13.clicked.connect(self.addnoise)
        self.ui.pushButton_6.clicked.connect(self.covid)
        self.ui.verticalSlider_2.valueChanged.connect(self.kernel)
        self.ui.dial_4.valueChanged.connect(self.mor)
        self.ui.pushButton_13.clicked.connect(self.otsu)
        self.ui.pushButton_14.clicked.connect(self.add)

    def add(self):
        self.image=cv2.add(self.img,self.image)
        self.setPhoto(self.image)

    def otsu(self):

        img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        ret, th = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        self.setPhoto(th)

    def mor(self):
        value=self.ui.dial_4.value()
        if self.ui.horizontalSlider_3.value()==1:

            if value==1:
                self.image = cv2.morphologyEx(self.img, cv2.MORPH_OPEN, self.ker)
                self.setPhoto(self.image)
            elif value==2:
                self.image = cv2.morphologyEx(self.img, cv2.MORPH_CLOSE, self.ker)
                self.setPhoto(self.image)
            elif value==3:
                self.image = cv2.erode(self.img,self.ker,iterations = 1)
                self.setPhoto(self.image)
            elif value==4:
                self.image = cv2.dilate(self.img,self.ker,iterations = 1)
                self.setPhoto(self.image)
            elif value==5:
                self.image = cv2.morphologyEx(self.img, cv2.MORPH_GRADIENT, self.ker)
                self.setPhoto(self.image)
            elif value==6:
                self.image =cv2.morphologyEx(self.img, cv2.MORPH_TOPHAT, self.ker)
                self.setPhoto(self.image)
        elif self.ui.horizontalSlider_3.value()==0:
            if value == 1:
                self.image = cv2.morphologyEx(self.image, cv2.MORPH_OPEN, self.ker)
                self.setPhoto(self.image)
            elif value == 2:
                self.image = cv2.morphologyEx(self.image, cv2.MORPH_CLOSE, self.ker)
                self.setPhoto(self.image)
            elif value == 3:
                self.image = cv2.erode(self.image, self.ker, iterations=1)
                self.setPhoto(self.image)
            elif value == 4:
                self.image = cv2.dilate(self.image, self.ker, iterations=1)
                self.setPhoto(self.image)
            elif value == 5:
                self.image = cv2.morphologyEx(self.image, cv2.MORPH_GRADIENT, self.ker)
                self.setPhoto(self.image)
            elif value == 6:
                self.image = cv2.morphologyEx(self.image, cv2.MORPH_TOPHAT, self.ker)
                self.setPhoto(self.image)


    def kernel(self):
        a=self.ui.verticalSlider_2.value()
        R=self.ui.spinBox_5.value()
        if a==1:
            self.ker= cv2.getStructuringElement(cv2.MORPH_RECT,(R,R))
        elif a==2:
            self.ker=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(R,R))
        elif a == 3:
            self.ker=cv2.getStructuringElement(cv2.MORPH_CROSS,(R,R))


    def covid(self):
        a=self.ui.lineEdit.text()
        img_rgb = imread(a)
        img_rgb = cv2.resize(img_rgb, (256, 256))
        self.setPhoto(img_rgb)
        # Convert it to grayscale
        img_gray = (img_rgb)

        template1 = imread("cropped_cobble/35.jpg")
        template2 = imread("cropped_cobble/120.jpg")
        template3 = imread("cropped_cobble/123.jpg")
        template4 = imread("cropped_cobble/120.jpg")
        template5 = imread("cropped_cobble/125.jpg")
        template6 = imread("cropped_cobble/129.jpg")
        template7 = imread("cropped_cobble/130.jpg")
        template8 = imread("cropped_cobble/189.jpg")
        template9 = imread("cropped_tree/59.jpg")
        template10 = imread("cropped_tree/81.jpg")
        template11 = imread("cropped_tree/92.jpg")
        template12 = imread("cropped_tree/96.jpg")
        template13 = imread("cropped_tree/7.jpg")
        template14 = imread("cropped_tree/39.jpg")
        template15 = imread("cropped_tree/72.jpg")
        template16 = imread("cropped_tree/75.jpg")

        img1 = match_template(img_gray, template1)
        print("done")
        img2 = match_template(img_gray, template2)
        img3 = match_template(img_gray, template3)
        img4 = match_template(img_gray, template4)
        img5 = match_template(img_gray, template5)
        img6 = match_template(img_gray, template6)
        img7 = match_template(img_gray, template7)
        img8 = match_template(img_gray, template8)
        img9 = match_template(img_gray, template9)
        img10 = match_template(img_gray, template10)
        img11 = match_template(img_gray, template11)
        img12 = match_template(img_gray, template12)
        img13 = match_template(img_gray, template13)
        img14 = match_template(img_gray, template14)
        img15 = match_template(img_gray, template15)
        img16 = match_template(img_gray, template16)

        max1 = (img1.max())
        max2 = (img2.max())
        max3 = (img3.max())
        max4 = (img4.max())
        max5 = (img5.max())
        max6 = (img6.max())
        max7 = (img7.max())
        max8 = (img8.max())
        max9 = (img9.max())
        max10 = (img10.max())
        max11 = (img11.max())
        max12 = (img12.max())
        max13 = (img13.max())
        max14 = (img14.max())
        max15 = (img15.max())
        max16 = (img16.max())

        liste = []
        liste.append(max1)
        liste.append(max2)
        liste.append(max3)
        liste.append(max4)
        liste.append(max5)
        liste.append(max6)
        liste.append(max7)
        liste.append(max8)
        liste.append(max9)
        liste.append(max10)
        liste.append(max11)
        liste.append(max12)
        liste.append(max13)
        liste.append(max14)
        liste.append(max15)
        liste.append(max16)

        sum1 = max1 + max2 + max3 + max4 + max5 + max6 + max7 + max8
        mean1 = sum1 / 8
        sum2 = max9 + max10 + max11 + max12 + max13 + max14 + max15 + max16
        mean2 = sum2 / 8


        for i in range(len(liste)):
            print(liste[i])

        max_value = max(liste)
        max_index = liste.index(max_value)

        if max_index < 8:
            self.ui.lineEdit_3.setText("Pattern is Cobblestone.")
        else:
            self.ui.lineEdit_3.setText("Pattern is Tree.")


    def addnoise(self):

        val = self.ui.comboBox_2.currentIndex()
        self.img = cv2.imread(self.a)
        img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        [M, N] = img.shape
        Gframe = np.double(self.img)
        Gframe = Gframe - Gframe.min()
        Gframe = Gframe / Gframe.max()
        if val==1:
            print("done")
            R = noises.salt_papper(img, 0.05)
            self.img = R + Gframe
        elif val==2:
            R=0.1*noises.noises('gaussian', M,N,0,1)
            self.img = R + Gframe
        elif val==3:
            R = 0.3 * noises.noises('uniform', M, N, 0, 1)
            self.img = R + Gframe
        elif val==4:
            R = 0.1 * noises.noises('erlang', M, N, 2, 5)
            self.img = R + Gframe
        elif val==5:
            R = 0.3 * noises.noises('rayleigh', M, N, 0, 1)
            self.img = R + Gframe
        elif val==6:
            R = 0.2 * noises.noises('exponential', M, N, 1, 1)
            self.img = R + Gframe
        elif val==7:
            R = 0.3 * noises.noises('lognormal', M, N, 1, 0.25)
            self.img = R + Gframe
        elif val==8:
            self.img=noises.add_periodic(self.img).astype(int)
        self.setPhoto((self.img))
    def boundryw(self):
        self.ui.lcdNumber_3.display(self.ui.horizontalSlider_6.value())

    def boundryb(self):
        self.ui.lcdNumber_4.display(self.ui.horizontalSlider_5.value())

    def shift(self):
        [a, s, c] = self.img.shape
        b = self.img[:, :, 0]
        g = self.img[:, :, 1]
        r = self.img[:, :, 2]
        w = self.ui.spinBox.value()
        h = self.ui.spinBox.value()
        B1 = np.zeros([a, s])
        B2 = np.zeros([a, s])
        B3 = np.zeros([a, s])
        for i in range(w, a):

            for j in range(h, s):
                B1[i, j] = b[i - w + 1, j - h + 1]
                B2[i, j] = g[i - w + 1, j - h + 1]
                B3[i, j] = r[i - w + 1, j - h + 1]

        self.img[:, :, 0] = B1[:, :]
        self.img[:, :, 1] = B2[:, :]
        self.img[:, :, 2] = B3[:, :]
        self.setPhoto(self.img)

    def crop(self):
        w = self.ui.spinBox.value()
        h = self.ui.spinBox.value()
        w2 = self.ui.spinBox_3.value()
        h2 = self.ui.spinBox_4.value()
        self.img = self.img[w:w2, h:h2, :]
        self.setPhoto(self.img)

    def resizing(self):
        w=self.ui.spinBox.value()
        h=self.ui.spinBox.value()
        img = interpolate(self.img, w, h)
        self.img = np.uint8(img)
        self.setPhoto(self.img)

    def vertical(self):
        b = self.img[:, :, 0]
        g = self.img[:, :, 1]
        r = self.img[:, :, 2]
        # Vertical Reflection-------------------------------------------------------------------------------------------------
        ref1 = r[:, ::-1]
        ref2 = g[:, ::-1]
        ref3 = b[:, ::-1]
        self.img[:, :, 0] = ref3[:, :]
        self.img[:, :, 1] = ref2[:, :]
        self.img[:, :, 2] = ref1[:, :]
        self.setPhoto(self.img)

    def horizontal(self):
        b = self.img[:, :, 0]
        g = self.img[:, :, 1]
        r = self.img[:, :, 2]
        # Horizontal Reflection-------------------------------------------------------------------------------------------------
        ref1 = r[::-1, :]
        ref2 = g[::-1, :]
        ref3 = b[::-1, :]
        self.img[:, :, 0] = ref3[:, :]
        self.img[:, :, 1] = ref2[:, :]
        self.img[:, :, 2] = ref1[:, :]
        self.setPhoto(self.img)

    def boundry1(self):
        self.ui.lcdNumber.display(self.ui.horizontalSlider.value())

    def boundry2(self):
        self.ui.lcdNumber_2.display(self.ui.horizontalSlider_2.value())


    def hist(self):
         if self.channel==1:
            def his(image):
                h = np.zeros(shape=(256, 1))

                [x, y] = image.shape
                for i in range(x):
                    for j in range(y):
                        k = image[i, j]
                        h[k, 0] = h[k, 0] + 1
                return h
            histg=his(self.img)

            plt.plot(histg)
            plt.show()
         elif self.channel==3:
            plt.hist(self.img, bins=10)
            plt.show()

    def range_black(self):
        value=self.ui.horizontalSlider_6.value()
        if value>4:
            self.ui.horizontalSlider_5.setMaximum(value-3)



    def colour(self):
        value=self.ui.dial.value()
        if value==1:
            self.img = cv2.imread(self.a,0)
            self.setPhoto(self.img)
        elif value==2:
            (thresh, blackAndWhiteImage) = cv2.threshold(self.img, 127, 255, cv2.THRESH_BINARY)
            self.setPhoto(blackAndWhiteImage)
        elif value == 3:
            YIQ = np.uint8(np.zeros(self.img.shape))
            [a, s, c] = self.img.shape
            img=self.img
            for i in range(0, a):
                for j in range(0, s):
                    YIQ[i, j, 2] = 0.299 * img[i, j, 2] + 0.5870 * img[i, j, 1] + 0.1140 * img[i, j, 0]
                    YIQ[i, j, 1] = 0.596 * img[i, j, 2] - 0.274 * img[i, j, 1] - 0.322 * img[i, j, 0]
                    YIQ[i, j, 0] = 0.211 * img[i, j, 2] - 0.523 * img[i, j, 1] + 0.312 * img[i, j, 0]
            self.setPhoto(YIQ)
        elif value==0:
            self.img = cv2.imread(self.a)
            self.setPhoto(self.img)

    def visible(self):
        value=self.ui.verticalSlider.value()
        if value==0:
            self.ui.label.setVisible(False)
            self.ui.label_3.setVisible(True)

        elif value == 1:
            self.ui.label.setVisible(True)
            self.ui.label_3.setVisible(False)

    def enter_image(self):
        """fname=QFileDialog.getOpenFileName(self,"Open File","c\\","Image files (*.jpg *.png)")
        path=fname[0]
        self.pixmap = QPixmap(path)
        self.ui.label.setPixmap(QPixmap(self.pixmap))

        #pixmap=QPixmap(path)
        #self.ui.label.setPixmap((pixmap))
        #self.ui.lineEdit.setText(path)
        self.pixmap = QPixmap(self.a)
        self.ui.label.setPixmap(self.pixmap)
        self.img = cv2.imread(sel)

        b=self.img[:,:,0]
        g = self.img[:, :, 1]
        r = self.img[:, :, 2]
        print(path)"""
        self.a = self.ui.lineEdit.text()
        self.pixmap = QPixmap(self.a)
        self.ui.label.setPixmap(self.pixmap)
        self.img = cv2.imread(self.a)
        self.image=self.img
        b, g, r = cv2.split(self.img)

        ### getting differences between (b,g), (r,g), (b,r) channel pixels
        r_g = np.count_nonzero(abs(r - g))
        r_b = np.count_nonzero(abs(r - b))
        g_b = np.count_nonzero(abs(g - b))

        ### sum of differences
        diff_sum = float(r_g + r_b + g_b)

        ### finding ratio of diff_sum with respect to size of image
        self.ratio = diff_sum / self.img.size

        if self.ratio > 0.005:
            self.ui.lineEdit_2.setText("The image is a RGB image!")
            self.ui.label_2.setVisible(True)
            self.ui.label_8.setVisible(False)
            self.channel=3
        else:
            self.ui.lineEdit_2.setText("The image is gray!")
            self.ui.label_2.setVisible(False)
            self.ui.label_8.setVisible(True)
            self.channel = 1


    def setPhoto(self,image):
        frame=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        image=QImage(frame,frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(image)
        self.ui.label.setPixmap(QPixmap(self.pixmap))



    def filtering(self):
        a1 = self.ui.horizontalSlider.value()
        a2 = self.ui.horizontalSlider_2.value()
        filter = np.ones([a1, a2])
        filter = filter / (a1 * a2)
        if self.channel==3:

            self.image=self.img
            b = self.image[:, :, 0]
            g = self.image[:, :, 1]
            r = self.image[:, :, 2]
            [x, y] = b.shape
            output1 = np.zeros([x, y])
            output2 = np.zeros([x, y])
            output3 = np.zeros([x, y])
            extra1 = x % a1
            extra2 = y % a2
            endpoint = x
            endpoint2 = y
            for i in range(0, endpoint - extra1, a1):
                for j in range(0, endpoint2 - extra2, a2):
                    # print(b[i:i+3,j:j+3])
                    filtering1 = np.multiply(b[i:i + (a1), j:j + (a2)], filter)
                    for z in range(0, a1):
                        for z2 in range(0, a2):
                            output1[i + z, j + z2] = filtering1.sum()

                    filtering2 = np.multiply(g[i:i + (a1), j:j + (a2)], filter)
                    for z in range(0, a1):
                        for z2 in range(0, a2):
                            output2[i + z, j + z2] = filtering2.sum()
                    filtering3 = np.multiply(r[i:i + (a1), j:j + (a2)], filter)
                    for z in range(0, a1):
                        for z2 in range(0, a2):
                            output3[i + z, j + z2] = filtering3.sum()

            a3 = extra1
            a4 = a2
            filter2 = np.ones([a3, a4])
            filter2 = filter2 / (a3 * a4)

            if extra1 != 0:
                if extra1 != 1:
                    for i in range(endpoint - extra1, endpoint - a3 + 1, a3):
                        for j in range(0, endpoint2 - a4 + 1, a4):
                            filtering1 = np.multiply(b[i:i + (a3), j:j + (a4)], filter2)
                            for z in range(0, a3):
                                for z2 in range(0, a4):
                                    output1[i + z, j + z2] = filtering1.sum()
                            filtering2 = np.multiply(g[i:i + (a3), j:j + (a4)], filter2)
                            for z in range(0, a3):
                                for z2 in range(0, a4):
                                    output2[i + z, j + z2] = filtering2.sum()
                            filtering3 = np.multiply(r[i:i + (a3), j:j + (a4)], filter2)
                            for z in range(0, a3):
                                for z2 in range(0, a4):
                                    output3[i + z, j + z2] = filtering3.sum()

            a5 = a1
            a6 = extra2
            filter3 = np.ones([a5, a6])
            filter3 = filter3 / (a5 * a6)

            if extra2 != 0:
                if extra2 != 1:
                    for i in range(0, endpoint - a5 + 1, a5):
                        for j in range(endpoint2 - extra2, endpoint2 - a6 + 1, a6):
                            filtering1 = np.multiply(b[i:i + (a5), j:j + (a6)], filter3)
                            for z in range(0, a5):
                                for z2 in range(0, a6):
                                    output1[i + z, j + z2] = filtering1.sum()
                            filtering2 = np.multiply(g[i:i + (a5), j:j + (a6)], filter3)
                            for z in range(0, a5):
                                for z2 in range(0, a6):
                                    output2[i + z, j + z2] = filtering2.sum()
                            filtering3 = np.multiply(r[i:i + (a5), j:j + (a6)], filter3)
                            for z in range(0, a5):
                                for z2 in range(0, a6):
                                    output3[i + z, j + z2] = filtering3.sum()

            if (extra2 != 0 and extra1 != 0):
                if (extra2 != 1 and extra1 != 1):
                    for i in range(endpoint - extra1, endpoint, extra1):
                        for j in range(endpoint2 - extra2, endpoint2, extra2):
                            a5 = extra1
                            a6 = extra2
                            filter3 = np.ones([a5, a6])
                            filter3 = filter3 / (a5 * a6)
                            filtering1 = np.multiply(b[i:i + (a5), j:j + (a6)], filter3)
                            for z in range(0, a5):
                                for z2 in range(0, a6):
                                    output1[i + z, j + z2] = filtering1.sum()
                            filtering2 = np.multiply(g[i:i + (a5), j:j + (a6)], filter3)
                            for z in range(0, a5):
                                for z2 in range(0, a6):
                                    output2[i + z, j + z2] = filtering2.sum()
                            filtering3 = np.multiply(r[i:i + (a5), j:j + (a6)], filter3)
                            for z in range(0, a5):
                                for z2 in range(0, a6):
                                    output3[i + z, j + z2] = filtering3.sum()

            self.image[:, :, 0] = output1[:, :]
            self.image[:, :, 1] = output2[:, :]
            self.image[:, :, 2] = output3[:, :]
            self.setPhoto(self.image)
        elif self.channel==1:
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            self.image=self.img
            [x, y] = self.image.shape
            output1 = np.zeros([x, y])
            extra1 = x % a1
            extra2 = y % a2
            endpoint = x
            endpoint2 = y
            for i in range(0, endpoint - extra1, a1):
                for j in range(0, endpoint2 - extra2, a2):
                    # print(b[i:i+3,j:j+3])
                    filtering1 = np.multiply(self.image[i:i + (a1), j:j + (a2)], filter)
                    for z in range(0, a1):
                        for z2 in range(0, a2):
                            output1[i + z, j + z2] = filtering1.sum()



            a3 = extra1
            a4 = a2
            filter2 = np.ones([a3, a4])
            filter2 = filter2 / (a3 * a4)

            if extra1 != 0:
                if extra1 != 1:
                    for i in range(endpoint - extra1, endpoint - a3 + 1, a3):
                        for j in range(0, endpoint2 - a4 + 1, a4):
                            filtering1 = np.multiply(self.image[i:i + (a3), j:j + (a4)], filter2)
                            for z in range(0, a3):
                                for z2 in range(0, a4):
                                    output1[i + z, j + z2] = filtering1.sum()


            a5 = a1
            a6 = extra2
            filter3 = np.ones([a5, a6])
            filter3 = filter3 / (a5 * a6)

            if extra2 != 0:
                if extra2 != 1:
                    for i in range(0, endpoint - a5 + 1, a5):
                        for j in range(endpoint2 - extra2, endpoint2 - a6 + 1, a6):
                            filtering1 = np.multiply(self.image[i:i + (a5), j:j + (a6)], filter3)
                            for z in range(0, a5):
                                for z2 in range(0, a6):
                                    output1[i + z, j + z2] = filtering1.sum()


            if (extra2 != 0 and extra1 != 0):
                if (extra2 != 1 and extra1 != 1):
                    for i in range(endpoint - extra1, endpoint, extra1):
                        for j in range(endpoint2 - extra2, endpoint2, extra2):
                            a5 = extra1
                            a6 = extra2
                            filter3 = np.ones([a5, a6])
                            filter3 = filter3 / (a5 * a6)
                            filtering1 = np.multiply(self.image[i:i + (a5), j:j + (a6)], filter3)
                            for z in range(0, a5):
                                for z2 in range(0, a6):
                                    output1[i + z, j + z2] = filtering1.sum()



            self.image[:, :] = output1[:, :]

            self.setPhoto(self.image)


    """" filter = np.ones([a1, a2])
            filter = filter / (a1 * a2)

            self.img = cv2.imread(self.a)
            b = self.img[:, :, 0]
            g = self.img[:, :, 1]
            r = self.img[:, :, 2]
            [x, y] = b.shape
            endpoint = x - a1
            endpoint2 = y - a2
            output1 = np.zeros([x, y])
            output2 = np.zeros([x, y])
            output3 = np.zeros([x, y])

            for i in range(0, endpoint):
                for j in range(0, endpoint2):
                    # print(b[i:i+3,j:j+3])
                    filtering1 = np.multiply(b[i:i + (a1), j:j + (a2)], filter)
                    output1[i, j] = filtering1.sum()
                    filtering2 = np.multiply(g[i:i + (a1), j:j + (a2)], filter)
                    output2[i, j] = filtering2.sum()
                    filtering3 = np.multiply(r[i:i + (a1), j:j + (a2)], filter)
                    output3[i, j] = filtering3.sum()
            for i in range(1, x):
                for j in range(1, y):
                    if output1[i, j] == 0:
                        output1[i, j] = self.img[i, j, 0]

                    if output2[i, j] == 0:
                        output2[i, j] = self.img[i, j, 1]

                    if output3[i, j] == 0:
                        output3[i, j] = self.img[i, j, 2]

            self.img[:, :, 0] = output1[:, :]
            self.img[:, :, 1] = output2[:, :]
            self.img[:, :, 2] = output3[:, :]"""


    def black_white(self):
        image = self.img
        white_value = self.ui.horizontalSlider_6.value()
        black_value = self.ui.horizontalSlider_5.value()
        [a, s, c] = image.shape
        formula = 255 / (white_value - black_value)

        def f(x):
            return ((x - white_value) * formula) + 255

        for i in range(a):
            for j in range(s):

                if black_value < image[i, j, 1] and white_value > image[i, j, 1]:
                    new = np.double(image[i, j, 1])
                    image[i, j, 1] = np.uint8(f(new))

                if black_value < image[i, j, 0] and white_value > image[i, j, 0]:
                    new = np.double(image[i, j, 0])
                    image[i, j, 0] = np.uint8(f(new))

                if black_value < image[i, j, 2] and white_value > image[i, j, 2]:
                    new = np.double(image[i, j, 2])
                    image[i, j, 2] = np.uint8(f(new))

                if image[i, j, 0] <= black_value:
                    image[i, j, 0] = 0
                if image[i, j, 0] >= white_value:
                    image[i, j, 0] = 255

                if image[i, j, 1] <= black_value:
                    image[i, j, 1] = 0
                if image[i, j, 1] >= white_value:
                    image[i, j, 1] = 255

                if image[i, j, 2] <= black_value:
                    image[i, j, 2] = 0
                if image[i, j, 2] >= white_value:
                    image[i, j, 2] = 255
        self.img = image
        self.setPhoto(self.img)


    def histogram(self):
        value = self.ui.dial_2.value()
        if value == 1:
            img=self.img
            def hist(image):
                h = np.zeros(shape=(256, 1))
                h1 = np.zeros(shape=(256, 1))
                h2 = np.zeros(shape=(256, 1))
                [x, y, z] = image.shape
                for i in range(x):
                    for j in range(y):
                        k = image[i, j, 0]
                        h[k, 0] = h[k, 0] + 1
                        k1 = image[i, j, 1]
                        h1[k1, 0] = h1[k1, 0] + 1
                        k2 = image[i, j, 2]
                        h2[k2, 0] = h2[k2, 0] + 1
                return h, h1, h2

            histg, histg2, histg3 = hist(img)


            x1 = histg.reshape(1, 256)
            y1 = np.zeros((1, 256))
            x2 = histg2.reshape(1, 256)
            y2 = np.zeros((1, 256))
            x3 = histg3.reshape(1, 256)
            y3 = np.zeros((1, 256))
            for i in range(256):
                if x1[0, i] == 0:
                    y1[0, i] = 0
                else:
                    y1[0, i] = i

                if x2[0, i] == 0:
                    y2[0, i] = 0
                else:
                    y2[0, i] = i

                if x3[0, i] == 0:
                    y3[0, i] = 0
                else:
                    y3[0, i] = i

            min1 = np.min(y1[np.nonzero(y1)])
            max1 = np.max(y1[np.nonzero(y1)])
            min2 = np.min(y2[np.nonzero(y2)])
            max2 = np.max(y2[np.nonzero(y2)])
            min3 = np.min(y3[np.nonzero(y3)])
            max3 = np.max(y3[np.nonzero(y3)])
            strech1 = np.round((255 / (max1 - min1) * (y1 - min1)))
            strech1[strech1 < 0] = 0
            strech1[strech1 > 255] = 255
            strech2 = np.round((255 / (max2 - min2) * (y2 - min2)))
            strech2[strech2 < 0] = 0
            strech2[strech2 > 255] = 255
            strech3 = np.round((255 / (max3 - min3) * (y3 - min3)))
            strech3[strech3 < 0] = 0
            strech3[strech3 > 255] = 255
            [x, y, z] = img.shape
            for i in range(x):
                for j in range(y):
                    k = img[i, j, 0]
                    k1 = img[i, j, 1]
                    k2 = img[i, j, 2]
                    img[i, j, 0] = strech1[0, k]
                    img[i, j, 1] = strech2[0, k1]
                    img[i, j, 2] = strech3[0, k2]

            self.img=img
            self.setPhoto(self.img)
        elif value==2:
            img=self.img
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


            [a, b] = img.shape

            # a=np.double(img)
            def hist(image):
                h = np.zeros(shape=(256, 1))

                [x, y] = image.shape
                for i in range(x):
                    for j in range(y):
                        k = image[i, j]
                        h[k, 0] = h[k, 0] + 1
                return h

            histg = hist(img)



            pdf = (1 / (a * b)) * histg

            cdf = np.zeros(shape=(256, 1))
            cdf[1] = pdf[1]
            for i in range(2, 256):
                cdf[i] = cdf[i - 1] + pdf[i]

            cdf = np.round(255 * cdf)

            ep = np.zeros(shape=(a, b))
            for i in range(1, a):
                for j in range(1, b):  # loop tracing thes columns of image
                    t = (img[i, j] + 1)  # pixel values in image
                    ep[i, j] = cdf[t]  # Making the ouput image using cdf as the transformation function
            img = np.uint8(ep)
            self.img=img
            self.setPhoto(self.img)

    def filters(self):
        val = self.ui.dial_3.value()
        a1 = self.ui.horizontalSlider.value()
        a2 = self.ui.horizontalSlider_2.value()
        self.img = cv2.imread(self.a)
        if self.channel==1:
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            if val == 1:
                [a, b] = self.img.shape
                array = np.zeros(shape=(a + a1-1, b + a2-1))
                array2 = np.zeros(shape=(a + a1-1, b + a2-1))
                array3 = np.zeros(shape=(a + a1 - 1, b + a2 - 1))
                array4 = np.zeros(shape=(a + a1 - 1, b + a2 - 1))
                for i in range(a):
                    for j in range(b):
                        x = self.img[i, j]
                        array[i + a1-2, j + a2-2] = x
                        array2[i + a1 - 2, j + a2 - 2] = x
                        array3[i + a1 - 2, j + a2 - 2] = x
                        array4[i + a1 - 2, j + a2 - 2] = x

                filter = np.ones([a1, a2])
                filter = (filter) / (a1*a2)
                filter = np.double(filter)
                array = np.double(array)
                output1 = np.zeros([a, b])
                for i in range(a -(a1-1)):
                    for j in range(b - (a2-1)):
                        temp1 = np.multiply(array[i:i + a1, j:j + a2], filter)
                        output1[i, j] = temp1.sum()

                img = np.uint8(output1)
                self.setPhoto(img)
            elif val==2:
                [a, b] = self.img.shape
                array = np.zeros(shape=(a + a1 - 1, b + a2 - 1))
                array2 = np.zeros(shape=(a + a1 - 1, b + a2 - 1))
                array3 = np.zeros(shape=(a + a1 - 1, b + a2 - 1))
                array4 = np.zeros(shape=(a + a1 - 1, b + a2 - 1))
                for i in range(a):
                    for j in range(b):
                        x = self.img[i, j]
                        array[i + a1 - 2, j + a2 - 2] = x
                        array2[i + a1 - 2, j + a2 - 2] = x
                        array3[i + a1 - 2, j + a2 - 2] = x
                        array4[i + a1 - 2, j + a2 - 2] = x


                filter2 = np.ones([a1, a2])
                filter2 = np.double(filter2)
                array2 = np.double(array2)
                output2 = np.zeros([a, b])

                output4 = np.zeros([a, b])
                for i in range(a - (a1-1)):
                    for j in range(b - (a2-1)):
                        temp1 = np.multiply(array2[i:i + a1, j:j + a2], filter2)
                        output2[i, j] = np.median(temp1)

                self.image = np.uint8(output2)
                self.setPhoto(self.image)
            elif val==3:
                [a, b] = self.img.shape
                array = np.zeros(shape=(a + 2, b + 2))
                array2 = np.zeros(shape=(a + 2, b + 2))
                array3 = np.zeros(shape=(a + 2, b + 2))
                array4 = np.zeros(shape=(a + 2, b + 2))
                for i in range(a):
                    for j in range(b):
                        x = self.img[i, j]
                        array[i + 1, j + 1] = x
                        array2[i + 1, j + 1] = x
                        array3[i + 1, j + 1] = x
                        array4[i + 1, j + 1] = x

                output3 = np.zeros([a, b])
                for i in range(a - 2):
                    for j in range(b - 2):
                        temp1 = array3[i:i + 3, j:j + 3]
                        output3[i, j] = np.max(temp1)

                image = np.uint8(output3)
                self.setPhoto(image)
            elif val==4:
                [a, b] = self.img.shape
                array = np.zeros(shape=(a + 2, b + 2))
                array2 = np.zeros(shape=(a + 2, b + 2))
                array3 = np.zeros(shape=(a + 2, b + 2))
                array4 = np.zeros(shape=(a + 2, b + 2))
                for i in range(a):
                    for j in range(b):
                        x = self.img[i, j]
                        array[i + 1, j + 1] = x
                        array2[i + 1, j + 1] = x
                        array3[i + 1, j + 1] = x
                        array4[i + 1, j + 1] = x

                output3 = np.zeros([a, b])
                for i in range(a - 2):
                    for j in range(b - 2):
                        temp1 = array3[i:i + 3, j:j + 3]
                        output3[i, j] = np.min(temp1)

                image = np.uint8(output3)
                self.setPhoto(image)
        elif self.channel==3:

            if val == 1:
                [a, b,c] = self.img.shape
                array = np.zeros(shape=(a + a1 - 1, b + a2 - 1))
                array2 = np.zeros(shape=(a + a1 - 1, b + a2 - 1))
                array3 = np.zeros(shape=(a + a1 - 1, b + a2 - 1))

                for i in range(a):
                    for j in range(b):
                        x = self.img[i, j,2]
                        y = self.img[i, j, 1]
                        z= self.img[i, j, 0]
                        array[i + a1 - 2, j + a2 - 2] = x
                        array2[i + a1 - 2, j + a2 - 2] = y
                        array3[i + a1 - 2, j + a2 - 2] = z


                filter = np.ones([a1, a2])
                filter = (filter) / (a1 * a2)
                filter = np.double(filter)
                array = np.double(array)
                output1 = np.zeros([a, b])
                output2 = np.zeros([a, b])
                output3 = np.zeros([a, b])

                for i in range(a - (a1 - 1)):
                    for j in range(b - (a2 - 1)):
                        temp1 = np.multiply(array[i:i + a1, j:j + a2], filter)
                        output1[i, j] = temp1.sum()
                        temp2 = np.multiply(array2[i:i + a1, j:j + a2], filter)
                        output2[i, j] = temp2.sum()
                        temp3 = np.multiply(array3[i:i + a1, j:j + a2], filter)
                        output3[i, j] = temp3.sum()
                self.img[:,:,0]=output3[:,:]
                self.img[:, :, 1] = output2[:,:]
                self.img[:, :, 2] = output1[:,:]
                img = np.uint8(self.img)
                self.setPhoto(img)
            elif val==2:
                [a, b,c] = self.img.shape
                array = np.zeros(shape=(a + a1 - 1, b + a2 - 1))
                array2 = np.zeros(shape=(a + a1 - 1, b + a2 - 1))
                array3 = np.zeros(shape=(a + a1 - 1, b + a2 - 1))
                array4 = np.zeros(shape=(a + a1 - 1, b + a2 - 1))
                for i in range(a):
                    for j in range(b):
                        x = self.img[i, j, 2]
                        y = self.img[i, j, 1]
                        z = self.img[i, j, 0]
                        array[i + a1 - 2, j + a2 - 2] = x
                        array2[i + a1 - 2, j + a2 - 2] = y
                        array3[i + a1 - 2, j + a2 - 2] = z

                    filter2 = np.ones([a1, a2])
                    filter2 = np.double(filter2)
                    array = np.double(array)
                    array2 = np.double(array2)
                    array3 = np.double(array3)
                    output1 = np.zeros([a, b])
                    output2 = np.zeros([a, b])
                    output3 = np.zeros([a, b])
                for i in range(a - (a1-1)):
                    for j in range(b - (a2-1)):
                        temp1 = np.multiply(array[i:i + a1, j:j + a2], filter2)
                        output1[i, j] = np.median(temp1)
                        temp2 = np.multiply(array2[i:i + a1, j:j + a2], filter2)
                        output2[i, j] = np.median(temp2)
                        temp3 = np.multiply(array3[i:i + a1, j:j + a2], filter2)
                        output3[i, j] = np.median(temp3)

                self.img[:, :, 0] = output3[:, :]
                self.img[:, :, 1] = output2[:, :]
                self.img[:, :, 2] = output1[:, :]
                img = np.uint8(self.img)
                self.setPhoto(img)

    def rontgen(self):
        val=self.ui.comboBox.currentIndex()
        self.img = cv2.imread(self.a)
        img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        [a, b] = img.shape
        array = np.zeros(shape=(a + 2, b + 2))
        array2 = np.zeros(shape=(a + 2, b + 2))
        array3 = np.zeros(shape=(a + 2, b + 2))
        for i in range(a):
            for j in range(b):
                x = img[i, j]
                array[i + 1, j + 1] = x
                array2[i + 1, j + 1] = x
                array3[i + 1, j + 1] = x
        array = np.double(array)
        array2 = np.double(array2)
        if val==1:
            filter = [[-0.125, -0.125, -0.125], [-0.125, 1, -0.125], [-0.125, -0.125, -0.125]]
            filter = np.double(filter)


            output1 = np.zeros([a, b])

            for i in range(a - 2):
                for j in range(b - 2):
                    temp1 = np.multiply(array[i:i + 3, j:j + 3], filter)
                    output1[i, j] = temp1.sum()

            self.image_b = np.uint8(output1)
            self.setPhoto(self.image_b)
        elif val==2:
            self.image_c = self.image_b + img
            self.setPhoto(self.image_c)
        elif val==3:
            output2 = np.zeros([a, b])
            for i in range(1, a - 2):
                for j in range(1, b - 2):
                    Gx = ((2 * array2[i + 2, j + 1] + array2[i + 2, j] + array2[i + 2, j + 2]) - (
                                2 * array2[i, j + 1] + array2[i, j] + array2[i, j + 2]))
                    Gy = ((2 * array2[i + 1, j + 2] + array2[i, j + 2] + array2[i + 2, j + 2]) - (
                                2 * array2[i + 1, j] + array2[i, j] + array2[i + 2, j]));
                    output2[i, j] = math.sqrt(pow(Gx, 2) + pow(Gy, 2))

            image_d = np.uint8(output2)
            self.setPhoto(image_d)
        elif val==4:
            filter = np.ones([5, 5])
            filter = (filter) / 25
            filter = np.double(filter)
            array3 = np.double(array3)
            output3 = np.zeros([a, b])
            for i in range(a - 4):
                for j in range(b - 4):
                    temp1 = np.multiply(array3[i:i + 5, j:j + 5], filter)
                    output3[i, j] = temp1.sum()

            self.image_e = np.uint8(output3)
            self.setPhoto(self.image_e)
        elif val==5:
            self.image_f = np.multiply(np.double(self.image_e), np.double(self.image_c))
            self.image_f = self.image_f / 255
            self.image_f = np.uint8(self.image_f)
            self.setPhoto(self.image_f)
        elif val==6:
            self.image_g = self.image_f + img
            self.setPhoto(self.image_g)
        elif val==7:
            image_h = np.double(self.image_g) ** 1.0
            image_h = np.uint8(image_h)
            self.setPhoto(image_h)

app=QApplication([])
window=gui()
window.show()
app.exec_()
