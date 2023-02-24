from PyQt5.QtWidgets import *
from hw1_python import Ui_MainWindow
from PyQt5.QtGui import QPixmap, QImage
import cv2
import numpy as np
import icons_rc
from matplotlib import pyplot as plt

class gui(QMainWindow):
    def __init__(self):
        super().__init__()
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


    def hist(self):

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
        else:
            self.ui.lineEdit_2.setText("The image is a greyscale image!")
            self.ui.label_2.setVisible(False)
            self.ui.label_8.setVisible(True)


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
            self.img[:, :, 2] = output3[:, :]
            self.setPhoto(self.img)

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





app=QApplication([])
window=gui()
window.show()
app.exec_()
