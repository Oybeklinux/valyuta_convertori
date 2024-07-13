# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'konvertortNCoxw.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(429, 212)
        Form.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(147, 147, 147);	\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit {\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(147, 147, 147);	\n"
"	color: white;\n"
"padding: 5px;\n"
"}")
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 140))
        self.frame.setSizeIncrement(QSize(0, 130))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(50, 16777215))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.uzs = QLineEdit(self.frame)
        self.uzs.setObjectName(u"uzs")
        self.uzs.setMinimumSize(QSize(0, 40))
        self.uzs.setMaximumSize(QSize(16777215, 40))
        self.uzs.setFont(font)

        self.gridLayout.addWidget(self.uzs, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(50, 16777215))
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.usd = QLineEdit(self.frame)
        self.usd.setObjectName(u"usd")
        self.usd.setMinimumSize(QSize(0, 40))
        self.usd.setMaximumSize(QSize(16777215, 40))
        self.usd.setFont(font)

        self.gridLayout.addWidget(self.usd, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(290, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.yopish = QPushButton(Form)
        self.yopish.setObjectName(u"yopish")
        self.yopish.setMinimumSize(QSize(112, 40))
        self.yopish.setMaximumSize(QSize(112, 40))
        self.yopish.setFont(font)

        self.gridLayout_2.addWidget(self.yopish, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"UZS", None))
        self.uzs.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"USD", None))
        self.usd.setText("")
        self.yopish.setText(QCoreApplication.translate("Form", u"Yopish", None))
    # retranslateUi

