# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_template.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.vLayout_1 = QVBoxLayout(self.central_widget)
        self.vLayout_1.setObjectName(u"vLayout_1")
        self.hLayout_1 = QHBoxLayout()
        self.hLayout_1.setObjectName(u"hLayout_1")
        self.app_icon_lbl = QLabel(self.central_widget)
        self.app_icon_lbl.setObjectName(u"app_icon_lbl")

        self.hLayout_1.addWidget(self.app_icon_lbl)

        self.app_title_lbl = QLabel(self.central_widget)
        self.app_title_lbl.setObjectName(u"app_title_lbl")
        self.app_title_lbl.setTextFormat(Qt.MarkdownText)
        self.app_title_lbl.setAlignment(Qt.AlignCenter)

        self.hLayout_1.addWidget(self.app_title_lbl)

        self.hSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hLayout_1.addItem(self.hSpacer_1)


        self.vLayout_1.addLayout(self.hLayout_1)

        self.main_frame = QFrame(self.central_widget)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.main_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.vLayout_3 = QVBoxLayout()
        self.vLayout_3.setObjectName(u"vLayout_3")
        self.info_lbl_2 = QLabel(self.main_frame)
        self.info_lbl_2.setObjectName(u"info_lbl_2")
        self.info_lbl_2.setTextFormat(Qt.MarkdownText)
        self.info_lbl_2.setAlignment(Qt.AlignCenter)

        self.vLayout_3.addWidget(self.info_lbl_2)

        self.generator_settings_frame = QFrame(self.main_frame)
        self.generator_settings_frame.setObjectName(u"generator_settings_frame")
        sizePolicy.setHeightForWidth(self.generator_settings_frame.sizePolicy().hasHeightForWidth())
        self.generator_settings_frame.setSizePolicy(sizePolicy)
        self.generator_settings_frame.setFrameShape(QFrame.StyledPanel)
        self.generator_settings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.generator_settings_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.vSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.vSpacer_2)

        self.hLayout_4 = QHBoxLayout()
        self.hLayout_4.setObjectName(u"hLayout_4")
        self.info_lbl_3 = QLabel(self.generator_settings_frame)
        self.info_lbl_3.setObjectName(u"info_lbl_3")
        self.info_lbl_3.setTextFormat(Qt.MarkdownText)
        self.info_lbl_3.setAlignment(Qt.AlignCenter)

        self.hLayout_4.addWidget(self.info_lbl_3)

        self.psw_length_slider = QSlider(self.generator_settings_frame)
        self.psw_length_slider.setObjectName(u"psw_length_slider")
        self.psw_length_slider.setMinimum(8)
        self.psw_length_slider.setMaximum(64)
        self.psw_length_slider.setPageStep(8)
        self.psw_length_slider.setOrientation(Qt.Horizontal)
        self.psw_length_slider.setInvertedAppearance(False)
        self.psw_length_slider.setInvertedControls(True)
        self.psw_length_slider.setTickPosition(QSlider.NoTicks)

        self.hLayout_4.addWidget(self.psw_length_slider)

        self.psw_length_info_lbl = QLabel(self.generator_settings_frame)
        self.psw_length_info_lbl.setObjectName(u"psw_length_info_lbl")
        self.psw_length_info_lbl.setTextFormat(Qt.MarkdownText)
        self.psw_length_info_lbl.setAlignment(Qt.AlignCenter)

        self.hLayout_4.addWidget(self.psw_length_info_lbl)


        self.verticalLayout.addLayout(self.hLayout_4)

        self.delimiter_line_1 = QFrame(self.generator_settings_frame)
        self.delimiter_line_1.setObjectName(u"delimiter_line_1")
        self.delimiter_line_1.setFrameShape(QFrame.HLine)
        self.delimiter_line_1.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.delimiter_line_1)

        self.lowercase_mode_btn = QCheckBox(self.generator_settings_frame)
        self.lowercase_mode_btn.setObjectName(u"lowercase_mode_btn")

        self.verticalLayout.addWidget(self.lowercase_mode_btn)

        self.uppercse_mode_btn = QCheckBox(self.generator_settings_frame)
        self.uppercse_mode_btn.setObjectName(u"uppercse_mode_btn")

        self.verticalLayout.addWidget(self.uppercse_mode_btn)

        self.special_symbols_mode_btn = QCheckBox(self.generator_settings_frame)
        self.special_symbols_mode_btn.setObjectName(u"special_symbols_mode_btn")

        self.verticalLayout.addWidget(self.special_symbols_mode_btn)

        self.delimiter_line_2 = QFrame(self.generator_settings_frame)
        self.delimiter_line_2.setObjectName(u"delimiter_line_2")
        self.delimiter_line_2.setFrameShape(QFrame.HLine)
        self.delimiter_line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.delimiter_line_2)

        self.vSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.vSpacer_3)

        self.vSpacer_1 = QSpacerItem(20, 93, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.vSpacer_1)

        self.result_frame = QFrame(self.generator_settings_frame)
        self.result_frame.setObjectName(u"result_frame")
        self.hLayout_3 = QHBoxLayout(self.result_frame)
        self.hLayout_3.setObjectName(u"hLayout_3")
        self.psw_le = QLineEdit(self.result_frame)
        self.psw_le.setObjectName(u"psw_le")
        self.psw_le.setMaxLength(64)
        self.psw_le.setEchoMode(QLineEdit.Normal)
        self.psw_le.setAlignment(Qt.AlignCenter)
        self.psw_le.setDragEnabled(False)
        self.psw_le.setReadOnly(True)

        self.hLayout_3.addWidget(self.psw_le)

        self.copy_psw_btn = QPushButton(self.result_frame)
        self.copy_psw_btn.setObjectName(u"copy_psw_btn")

        self.hLayout_3.addWidget(self.copy_psw_btn)


        self.verticalLayout.addWidget(self.result_frame)


        self.vLayout_3.addWidget(self.generator_settings_frame)

        self.hSpacer_3 = QHBoxLayout()
        self.hSpacer_3.setObjectName(u"hSpacer_3")
        self.hSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hSpacer_3.addItem(self.hSpacer_5)

        self.generate_psw_btn = QPushButton(self.main_frame)
        self.generate_psw_btn.setObjectName(u"generate_psw_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.generate_psw_btn.sizePolicy().hasHeightForWidth())
        self.generate_psw_btn.setSizePolicy(sizePolicy1)

        self.hSpacer_3.addWidget(self.generate_psw_btn)

        self.hSpacer_4 = QSpacerItem(79, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hSpacer_3.addItem(self.hSpacer_4)


        self.vLayout_3.addLayout(self.hSpacer_3)


        self.horizontalLayout_3.addLayout(self.vLayout_3)

        self.vLayout_2 = QVBoxLayout()
        self.vLayout_2.setObjectName(u"vLayout_2")
        self.info_lbl_1 = QLabel(self.main_frame)
        self.info_lbl_1.setObjectName(u"info_lbl_1")
        self.info_lbl_1.setTextFormat(Qt.MarkdownText)
        self.info_lbl_1.setAlignment(Qt.AlignCenter)

        self.vLayout_2.addWidget(self.info_lbl_1)

        self.history_list = QListWidget(self.main_frame)
        self.history_list.setObjectName(u"history_list")

        self.vLayout_2.addWidget(self.history_list)

        self.hLayout_2 = QHBoxLayout()
        self.hLayout_2.setObjectName(u"hLayout_2")
        self.hSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hLayout_2.addItem(self.hSpacer_2)

        self.copy_history_psw_btn = QPushButton(self.main_frame)
        self.copy_history_psw_btn.setObjectName(u"copy_history_psw_btn")

        self.hLayout_2.addWidget(self.copy_history_psw_btn)

        self.clear_history_btn = QPushButton(self.main_frame)
        self.clear_history_btn.setObjectName(u"clear_history_btn")

        self.hLayout_2.addWidget(self.clear_history_btn)


        self.vLayout_2.addLayout(self.hLayout_2)


        self.horizontalLayout_3.addLayout(self.vLayout_2)


        self.vLayout_1.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyPasswordGenerator", None))
        self.app_icon_lbl.setText("")
        self.app_title_lbl.setText(QCoreApplication.translate("MainWindow", u"# PyPasswordGenerator", None))
        self.info_lbl_2.setText(QCoreApplication.translate("MainWindow", u"## \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0433\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.info_lbl_3.setText(QCoreApplication.translate("MainWindow", u"### \u0414\u043b\u0438\u043d\u043d\u0430 \u043f\u0430\u0440\u043e\u043b\u044f:", None))
        self.psw_length_info_lbl.setText(QCoreApplication.translate("MainWindow", u"### 8", None))
        self.lowercase_mode_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u043e\u0447\u043d\u044b\u0435 \u0431\u0443\u043a\u0432\u044b", None))
        self.uppercse_mode_btn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u043b\u0430\u0432\u043d\u044b\u0435 \u0431\u0443\u043a\u0432\u044b", None))
        self.special_symbols_mode_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0435 \u0441\u0438\u043c\u0432\u043e\u043b\u044b", None))
        self.copy_psw_btn.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.generate_psw_btn.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0435\u0440\u0438\u0432\u0430\u0442\u044c", None))
        self.info_lbl_1.setText(QCoreApplication.translate("MainWindow", u"## \u0418\u0441\u0442\u043e\u0440\u0438\u044f", None))
        self.copy_history_psw_btn.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.clear_history_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
    # retranslateUi

