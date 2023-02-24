from PyQt5.QtWidgets import *
from hw1_python import Ui_MainWindow
from PyQt5.QtGui import QPixmap, QImage
import cv2
import numpy as np
import icons_rc

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
        self.ui.label.setPixmap(self.pixmap)



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







app=QApplication([])
window=gui()
window.show()
app.exec_()
