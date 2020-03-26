from new8.ui_and_function2 import Ui_MainWindow
import sys
from PyQt5 import QtWidgets, QtCore, QtGui

#--------------------------------실행------------------------------#
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # import한 qt위젯 실행문
    app.setStyle('Fusion')
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15,15,15))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)

    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142,45,197).lighter())
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)

    MainWindow = QtWidgets.QMainWindow()    # 위젯을 윈도우화
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)  #ui메인윈도우 인스턴스실행
    MainWindow.show()   #윈도우 창 켜기

    sys.exit(app.exec_())   #윈도우창이 자동으로 종료되지않도록 기다리기


