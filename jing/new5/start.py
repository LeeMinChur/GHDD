from new5.ui_and_function import Ui_MainWindow
import sys
from PyQt5 import QtWidgets

#--------------------------------실행------------------------------#
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # import한 qt위젯 실행문
    MainWindow = QtWidgets.QMainWindow()    # 위젯을 윈도우화
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)  #ui메인윈도우 인스턴스실행
    MainWindow.show()   #윈도우 창 켜기

    sys.exit(app.exec_())   #윈도우창이 자동으로 종료되지않도록 기다리기


