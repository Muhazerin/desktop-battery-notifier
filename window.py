# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(232, 77)
        Dialog.setMaximumSize(QtCore.QSize(232, 77))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/battery.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.upperBatteryPercentageLimitLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.upperBatteryPercentageLimitLabel.setFont(font)
        self.upperBatteryPercentageLimitLabel.setObjectName("upperBatteryPercentageLimitLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.upperBatteryPercentageLimitLabel)
        self.lowerBatteryPercentageLimitLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lowerBatteryPercentageLimitLabel.setFont(font)
        self.lowerBatteryPercentageLimitLabel.setObjectName("lowerBatteryPercentageLimitLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lowerBatteryPercentageLimitLabel)
        self.upperBatteryPercentageLimitSpinBox = QtWidgets.QSpinBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.upperBatteryPercentageLimitSpinBox.setFont(font)
        self.upperBatteryPercentageLimitSpinBox.setObjectName("upperBatteryPercentageLimitSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.upperBatteryPercentageLimitSpinBox)
        self.lowerBatteryPercentageLimitSpinBox = QtWidgets.QSpinBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lowerBatteryPercentageLimitSpinBox.setFont(font)
        self.lowerBatteryPercentageLimitSpinBox.setObjectName("lowerBatteryPercentageLimitSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lowerBatteryPercentageLimitSpinBox)
        self.saveBtn = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.saveBtn.setFont(font)
        self.saveBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.saveBtn.setIconSize(QtCore.QSize(12, 12))
        self.saveBtn.setObjectName("saveBtn")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.saveBtn)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Desktop Battery Notifier"))
        self.upperBatteryPercentageLimitLabel.setText(_translate("Dialog", "Upper Battery Percentage Limit: "))
        self.lowerBatteryPercentageLimitLabel.setText(_translate("Dialog", "Lower Battery Percentage Limit:"))
        self.saveBtn.setText(_translate("Dialog", "Save"))
import resources_rc
