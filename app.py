from MainWindow import Ui_MainWindow
from pictures_screen import Ui_Picture_Window
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import zipfile
import datetime
import os
import numpy as np
import cv2

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setStyleSheet('.QWidget {background-image: url(background.png);}')
        self.pushButton_start.clicked.connect(self.start)

    def start(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, "Выбрать архив", '',
                                                      'Архив (*.zip);;Картинка (*.jpg);;Картинка (*.png)')[0]
        self.screen = Picture_Show(fname)
        self.screen.show()


class Picture_Show(QtWidgets.QMainWindow, Ui_Picture_Window):
    def __init__(self, name):
        super(Picture_Show, self).__init__ ()
        self.setupUi(self)
        self.setStyleSheet('.QWidget {background-image: url(background.png);}')
        if name[-3:] == 'zip':
            files = zipfile.ZipFile(name)
            self.name_of_directory = str(datetime.date.today())
            os.mkdir(self.name_of_directory)
            files.extractall(self.name_of_directory)
            self.many_files()
        else:
            self.one_file(name.split('/')[-1])

    def change_photo(self, fname, directory_name):
        img = cv2.imread(fname)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h = hsv[:, :, 0]

        img[h >= 45] = (0, 0, 0)
        img[h <= 19] = (0, 0, 0)

        gray = np.copy(img[:, :, 0])

        thr, wb = cv2.threshold(gray, 3, 255, cv2.THRESH_BINARY)

        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(wb, 4, cv2.CV_32S)

        MAX_W = 70
        MAX_H = 70
        MIN_W = 20
        MIN_H = 20

        labels_to_add = []

        for i, stat in enumerate(stats):
            if stat[cv2.CC_STAT_WIDTH] > MAX_W or stat[cv2.CC_STAT_HEIGHT] > MAX_H:
                continue

            if stat[cv2.CC_STAT_WIDTH] < MIN_W or stat[cv2.CC_STAT_HEIGHT] < MIN_H:
                continue

            labels_to_add.append (i)
            print(f'Added {i}')

        wb[:, :] = 0

        for lbl in labels_to_add:
            print(f'Added {lbl}')
            wb[labels == lbl] = 255

        kernel = np.ones((9, 9), np.uint8)
        eroded = cv2.erode(wb, kernel, iterations = 1)
        dilated = cv2.dilate(eroded, kernel, iterations = 1)
        img[dilated == 255] = [0, 0, 255]

        cv2.imwrite(directory_name, img)
        return directory_name


    def many_files(self):
        directory = os.fsdecode(self.name_of_directory)
        self.files_path = []
        self.name_of_directory_new = self.name_of_directory + '_new'
        os.mkdir(self.name_of_directory_new)
        for file in os.listdir(directory):
            fname = self.name_of_directory + '/' + str(file)
            directory_name = self.name_of_directory_new + '/' + str(file)
            self.files_path.append(self.change_photo(fname, directory_name))
        self.last_ind_of_photo = 0
        self.set_pixmap(self.files_path[self.last_ind_of_photo])
        print(self.files_path)
        self.pushButton_left.setEnabled(False)
        self.pushButton_right.clicked.connect(self.right)
        self.pushButton_left.clicked.connect(self.left)

    def right(self):
        self.last_ind_of_photo += 1
        self.set_pixmap(self.files_path[self.last_ind_of_photo])
        if self.last_ind_of_photo == 1:
            self.pushButton_left.setEnabled(True)
        if self.last_ind_of_photo == len(self.files_path) - 1:
            self.pushButton_right.setEnabled(False)

    def left(self):
        self.last_ind_of_photo -= 1
        self.set_pixmap(self.files_path[self.last_ind_of_photo])
        if self.last_ind_of_photo == 0:
            self.pushButton_left.setEnabled(False)
        if self.last_ind_of_photo == len(self.files_path) - 2:
            self.pushButton_right.setEnabled(True)

    def one_file(self, fname):
        self.pushButton_left.setEnabled(False)
        self.pushButton_right.setEnabled(False)
        print('processing...')
        self.change_photo(fname, fname[:-4] + '_new' + fname[-4:])
        self.set_pixmap(fname[:-4] + '_new' + fname[-4:])

    def set_pixmap(self, fname):
        print('setting photo...')
        pixmap = QtGui.QPixmap(fname)
        pixmap2 = pixmap.scaledToHeight(1024)
        self.label.setPixmap(pixmap2)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icon.png'))
    window = MyWindow()
    window.setWindowIcon(QtGui.QIcon('icon.png'))
    window.show()
    sys.exit(app.exec())
