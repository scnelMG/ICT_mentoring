## Ex 3-8. 창을 화면의 가운데로.

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget, QLabel, QPushButton,
                             QLineEdit, QGridLayout, QVBoxLayout, QGroupBox,QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QPainter, QPen

#lineedit? 아님 qtextedit?
class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # grid = QGridLayout()
        # self.setLayout(grid)

        label1 = QLabel('기업명/기업코드', self)
        label1.move(100,50)

        qle = QLineEdit(self)
        qle.move(220,45)

        btn = QPushButton('GO', self)
        btn.move(400,45)



        label2 = QLabel('금융 상품 키워드 제공', self)
        label2.move(210,90)
        # label2.setAlignment(Qt.AlignCenter)

        font2 = label2.font()
        font2.setBold(True)
        font2.setPointSize(13)
        label2.setFont(font2)

        label3 = QLabel('당일 기준 지난 24시간 전 기사를 기반으로 제공', self)
        # label3.setAlignment(Qt.AlignCenter)
        label3.move(170,120)
        # label3.move(100, 120)

#https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=smilewhj&logNo=221066451394&parentCategoryNo=&categoryNo=36&viewDate=&isShowPopularPosts=false&from=postView
        pixmap = QPixmap('wordcloud.png')
        lbl_img = QLabel(self)
        lbl_img.resize(400,200)
        lbl_img.setPixmap(QPixmap(pixmap))
        lbl_img.move(170,150)



        label4 = QLabel('TOP 종목', self)
        label4.move(260,390)
        # label2.setAlignment(Qt.AlignCenter)

        font4 = label4.font()
        font4.setBold(True)
        font4.setPointSize(13)
        label4.setFont(font2)

        pixmap = QPixmap('top.png')
        lbl_img = QLabel(self)
        lbl_img.resize(400,200)
        lbl_img.setPixmap(QPixmap(pixmap))
        lbl_img.move(110,400)

        self.setWindowTitle('주가예측 프로그램')
        self.resize(600, 700)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_line(qp)
        qp.end()

    def draw_line(self, qp):
        qp.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        qp.drawLine(100, 370, 500, 370)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())