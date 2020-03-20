import sys
from PyQt5.QtWidgets import QApplication, QWidget #라이브러리 임포트

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application') #창의 제목
        self.move(300, 300) #창의 위치 선정
        self.resize(400, 200) #창의 사이즈 조절

        self.show()  # 창을 보여준다.


if __name__ == '__main__':
    app = QApplication(sys.argv) #어플리케이션 객체 생성
    ex = MyApp()

    sys.exit(app.exec_())