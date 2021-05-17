import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Test Screen Recorder")
        Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 380, 280))

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 149, 151, 31))
        self.label.setText("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.pushButton.clicked.connect(self.screen_recorder)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Start"))

    def screen_recorder(self):
        import numpy as np
        import cv2
        from PIL import ImageGrab
        import datetime
		

		
        fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")

        time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

        captured_video = cv2.VideoWriter("test {}.mp4".format(time), fourcc, 20.0, (1920, 1080))

        while True:
		
            img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
			
            img_np = np.array(img)
			
            img_FINAL = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

            webcam = cv2.VideoCapture(1)
			
            _, frame = webcam.read()
			
            fr_height, fr_width, _ = frame.shape
			
            img_FINAL[0:fr_height, 0:fr_width] = frame[0: fr_height, 0: fr_width, :]

            cv2.imshow("capture", img_FINAL)
			
            captured_video.write(img_FINAL)
			
            if cv2.waitKey(50) == ord('q'):
                exit()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
	