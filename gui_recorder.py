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
        # below are the imported modules or dependencies required for running the program
        import numpy as np
        import cv2
        from PIL import ImageGrab
        import datetime
		

		# encoding the video in mp4 format
        fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
        #saving the current time at which the recording started
        time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        # saving the final encoded video and defining frame rate , codec , resolution
        captured_video = cv2.VideoWriter("test {}.mp4".format(time), fourcc, 20.0, (1920, 1080))

        while True:
		    # taking screen shot of the screen and defined the resolutionof it
            img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
			# taking those screenshot and arranging them in a array
            img_np = np.array(img)
			# converting the array of ss into its correct rgb color
            img_FINAL = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            #capturing video from webcam
            webcam = cv2.VideoCapture(1)
			#capturing and reading frames from webcam
            _, frame = webcam.read()
		    # defining it size
            fr_height, fr_width, _ = frame.shape
			# embedding the webcam image over the screen
            img_FINAL[0:fr_height, 0:fr_width] = frame[0: fr_height, 0: fr_width, :]
            # showing the final capture
            cv2.imshow("capture", img_FINAL)
			# encoding the frames after completing one loop
            captured_video.write(img_FINAL)
			# waitkey means the time interval in milli second and creating if condition to stop recording by
            # pressing q key on the keyboard while being in the imshow screen
            if cv2.waitKey(50) == ord('q'):
                exit()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
	