# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class WindowUI(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1176, 390)
        self.showTomada1 = QtWidgets.QPushButton(Dialog)
        self.showTomada1.setGeometry(QtCore.QRect(40, 280, 101, 51))
        self.showTomada1.setObjectName("showTomada1")
        self.showTomada2 = QtWidgets.QPushButton(Dialog)
        self.showTomada2.setGeometry(QtCore.QRect(150, 280, 101, 51))
        self.showTomada2.setObjectName("showTomada2")
        self.showTomada4 = QtWidgets.QPushButton(Dialog)
        self.showTomada4.setGeometry(QtCore.QRect(370, 280, 101, 51))
        self.showTomada4.setObjectName("showTomada4")
        self.showTomada3 = QtWidgets.QPushButton(Dialog)
        self.showTomada3.setGeometry(QtCore.QRect(260, 280, 101, 51))
        self.showTomada3.setObjectName("showTomada3")
        self.showTomada8 = QtWidgets.QPushButton(Dialog)
        self.showTomada8.setGeometry(QtCore.QRect(810, 280, 101, 51))
        self.showTomada8.setObjectName("showTomada8")
        self.showTomada6 = QtWidgets.QPushButton(Dialog)
        self.showTomada6.setGeometry(QtCore.QRect(590, 280, 101, 51))
        self.showTomada6.setObjectName("showTomada6")
        self.showTomada7 = QtWidgets.QPushButton(Dialog)
        self.showTomada7.setGeometry(QtCore.QRect(700, 280, 101, 51))
        self.showTomada7.setObjectName("showTomada7")
        self.showTomada5 = QtWidgets.QPushButton(Dialog)
        self.showTomada5.setGeometry(QtCore.QRect(480, 280, 101, 51))
        self.showTomada5.setObjectName("showTomada5")
        self.showTomada10 = QtWidgets.QPushButton(Dialog)
        self.showTomada10.setGeometry(QtCore.QRect(1030, 280, 101, 51))
        self.showTomada10.setObjectName("showTomada10")
        self.showTomada9 = QtWidgets.QPushButton(Dialog)
        self.showTomada9.setGeometry(QtCore.QRect(920, 280, 101, 51))
        self.showTomada9.setObjectName("showTomada9")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(840, 20, 261, 241))
        self.groupBox.setObjectName("groupBox")
        self.dhcp = QtWidgets.QCheckBox(self.groupBox)
        self.dhcp.setGeometry(QtCore.QRect(16, 20, 70, 17))
        self.dhcp.setObjectName("dhcp")
        self.btSaveEthernet = QtWidgets.QPushButton(self.groupBox)
        self.btSaveEthernet.setGeometry(QtCore.QRect(10, 210, 241, 23))
        self.btSaveEthernet.setObjectName("btSaveEthernet")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(6, 50, 61, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(6, 100, 47, 13))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(6, 150, 101, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(140, 50, 47, 13))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(140, 100, 91, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(140, 150, 101, 16))
        self.label_14.setObjectName("label_14")
        self.hostname = QtWidgets.QLineEdit(self.groupBox)
        self.hostname.setGeometry(QtCore.QRect(6, 70, 113, 20))
        self.hostname.setObjectName("hostname")
        self.gateway = QtWidgets.QLineEdit(self.groupBox)
        self.gateway.setGeometry(QtCore.QRect(140, 70, 113, 20))
        self.gateway.setObjectName("gateway")
        self.ip = QtWidgets.QLineEdit(self.groupBox)
        self.ip.setGeometry(QtCore.QRect(6, 120, 113, 20))
        self.ip.setObjectName("ip")
        self.dns1 = QtWidgets.QLineEdit(self.groupBox)
        self.dns1.setGeometry(QtCore.QRect(140, 120, 113, 20))
        self.dns1.setObjectName("dns1")
        self.mask = QtWidgets.QLineEdit(self.groupBox)
        self.mask.setGeometry(QtCore.QRect(6, 170, 113, 20))
        self.mask.setObjectName("mask")
        self.dns2 = QtWidgets.QLineEdit(self.groupBox)
        self.dns2.setGeometry(QtCore.QRect(140, 170, 113, 20))
        self.dns2.setObjectName("dns2")
        self.ipField = QtWidgets.QLineEdit(Dialog)
        self.ipField.setGeometry(QtCore.QRect(70, 20, 113, 20))
        self.ipField.setObjectName("ipField")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 21, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.userField = QtWidgets.QLineEdit(Dialog)
        self.userField.setGeometry(QtCore.QRect(70, 50, 113, 20))
        self.userField.setObjectName("userField")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(190, 50, 47, 13))
        self.label_3.setObjectName("label_3")
        self.passField = QtWidgets.QLineEdit(Dialog)
        self.passField.setGeometry(QtCore.QRect(230, 50, 113, 20))
        self.passField.setObjectName("passField")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 160, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 190, 71, 16))
        self.label_6.setObjectName("label_6")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(610, 110, 191, 151))#self.groupBox_2.setGeometry(QtCore.QRect(610, 140, 181, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label_7.setObjectName("label_7")
        self.nomeTomadaField = QtWidgets.QLineEdit(self.groupBox_2)
        self.nomeTomadaField.setGeometry(QtCore.QRect(60, 50, 113, 20))
        self.nomeTomadaField.setObjectName("nomeTomadaField")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 50, 47, 13))
        self.label_8.setObjectName("label_8")
        self.btRenamePort = QtWidgets.QPushButton(self.groupBox_2)
        self.btRenamePort.setGeometry(QtCore.QRect(10, 120, 171, 23))#self.btRenamePort.setGeometry(QtCore.QRect(4, 80, 171, 23))
        self.btRenamePort.setObjectName("btRenamePort")
        self.cbTomada = QtWidgets.QComboBox(self.groupBox_2)
        self.cbTomada.setGeometry(QtCore.QRect(60, 20, 69, 22))
        self.cbTomada.setObjectName("cbTomada")

        self.cbHabilitaTomada = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbHabilitaTomada.setGeometry(QtCore.QRect(10, 80, 70, 17))
        self.cbHabilitaTomada.setObjectName("cbHabilitaTomada")

        self.btConnect = QtWidgets.QPushButton(Dialog)
        self.btConnect.setGeometry(QtCore.QRect(380, 50, 75, 23))
        self.btConnect.setObjectName("btConnect")
        self.uptimeField = QtWidgets.QLineEdit(Dialog)
        self.uptimeField.setGeometry(QtCore.QRect(100, 130, 113, 20))
        self.uptimeField.setObjectName("uptimeField")
        self.tempField = QtWidgets.QLineEdit(Dialog)
        self.tempField.setGeometry(QtCore.QRect(100, 160, 113, 20))
        self.tempField.setObjectName("tempField")
        self.dataHoraField = QtWidgets.QLineEdit(Dialog)
        self.dataHoraField.setGeometry(QtCore.QRect(100, 190, 113, 20))
        self.dataHoraField.setObjectName("dataHoraField")

        self.nt1 = QtWidgets.QLineEdit(Dialog)
        self.nt1.setGeometry(QtCore.QRect(40, 340, 101, 20))
        self.nt1.setReadOnly(True)
        self.nt1.setObjectName("nt1")
        self.nt2 = QtWidgets.QLineEdit(Dialog)
        self.nt2.setGeometry(QtCore.QRect(150, 340, 101, 20))
        self.nt2.setReadOnly(True)
        self.nt2.setObjectName("nt2")
        self.nt3 = QtWidgets.QLineEdit(Dialog)
        self.nt3.setGeometry(QtCore.QRect(260, 340, 101, 20))
        self.nt3.setReadOnly(True)
        self.nt3.setObjectName("nt3")
        self.nt4 = QtWidgets.QLineEdit(Dialog)
        self.nt4.setGeometry(QtCore.QRect(370, 340, 101, 20))
        self.nt4.setReadOnly(True)
        self.nt4.setObjectName("nt4")
        self.nt5 = QtWidgets.QLineEdit(Dialog)
        self.nt5.setGeometry(QtCore.QRect(480, 340, 101, 20))
        self.nt5.setReadOnly(True)
        self.nt5.setObjectName("nt5")
        self.nt6 = QtWidgets.QLineEdit(Dialog)
        self.nt6.setGeometry(QtCore.QRect(590, 340, 101, 20))
        self.nt6.setReadOnly(True)
        self.nt6.setObjectName("nt6")
        self.nt7 = QtWidgets.QLineEdit(Dialog)
        self.nt7.setGeometry(QtCore.QRect(700, 340, 101, 20))
        self.nt7.setReadOnly(True)
        self.nt7.setObjectName("nt7")
        self.nt8 = QtWidgets.QLineEdit(Dialog)
        self.nt8.setGeometry(QtCore.QRect(810, 340, 101, 20))
        self.nt8.setReadOnly(True)
        self.nt8.setObjectName("nt8")
        self.nt9 = QtWidgets.QLineEdit(Dialog)
        self.nt9.setGeometry(QtCore.QRect(920, 340, 101, 20))
        self.nt9.setReadOnly(True)
        self.nt9.setObjectName("nt9")
        self.nt10 = QtWidgets.QLineEdit(Dialog)
        self.nt10.setGeometry(QtCore.QRect(1030, 340, 101, 20))
        self.nt10.setReadOnly(True)
        self.nt10.setObjectName("nt10")

        self.retranslateUi(Dialog)
        self.initHandlers(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.showTomada1.setText(_translate("Dialog", "TOMADA1"))
        self.showTomada2.setText(_translate("Dialog", "TOMADA2"))
        self.showTomada4.setText(_translate("Dialog", "TOMADA4"))
        self.showTomada3.setText(_translate("Dialog", "TOMADA3"))
        self.showTomada8.setText(_translate("Dialog", "TOMADA8"))
        self.showTomada6.setText(_translate("Dialog", "TOMADA6"))
        self.showTomada7.setText(_translate("Dialog", "TOMADA7"))
        self.showTomada5.setText(_translate("Dialog", "TOMADA5"))
        self.showTomada10.setText(_translate("Dialog", "TOMADA10"))
        self.showTomada9.setText(_translate("Dialog", "TOMADA9"))
        self.groupBox.setTitle(_translate("Dialog", "Configuração de Rede"))
        self.dhcp.setText(_translate("Dialog", "DHCP"))
        self.btSaveEthernet.setText(_translate("Dialog", "Salvar"))
        self.label_9.setText(_translate("Dialog", "Hostname"))
        self.label_10.setText(_translate("Dialog", "IP"))
        self.label_11.setText(_translate("Dialog", "Máscara de rede"))
        self.label_12.setText(_translate("Dialog", "Gateway"))
        self.label_13.setText(_translate("Dialog", "DNS Primário"))
        self.label_14.setText(_translate("Dialog", "DNS Secundário"))
        self.label.setText(_translate("Dialog", "IP:"))
        self.label_2.setText(_translate("Dialog", "Usuário:"))
        self.label_3.setText(_translate("Dialog", "Senha:"))
        self.label_4.setText(_translate("Dialog", "Uptime:"))
        self.label_5.setText(_translate("Dialog", "Temperatura:"))
        self.label_6.setText(_translate("Dialog", "Data e Hora:"))
        self.groupBox_2.setTitle(_translate("Dialog", "Configurar Tomada"))#self.groupBox_2.setTitle(_translate("Dialog", "Renomear porta"))
        self.label_7.setText(_translate("Dialog", "Porta"))
        self.label_8.setText(_translate("Dialog", "Nome"))
        self.btRenamePort.setText(_translate("Dialog", "Salvar"))
        self.cbHabilitaTomada.setText(_translate("Dialog", "Habilitada"))
        self.btConnect.setText(_translate("Dialog", "Conectar"))
        self.cbTomada.addItems(['','1','2','3','4','5','6','7','8','9','10'])

        self.ipField.setText('192.168.0.91')
        self.userField.setText('admin')
        self.passField.setText('voltvolt')

    def initHandlers(self, Dialog):
        self.btConnect.clicked.connect(Dialog.login);
        self.showTomada1.clicked.connect(lambda: Dialog.controlTomada(1))
        self.showTomada2.clicked.connect(lambda: Dialog.controlTomada(2))
        self.showTomada3.clicked.connect(lambda: Dialog.controlTomada(3))
        self.showTomada4.clicked.connect(lambda: Dialog.controlTomada(4))
        self.showTomada5.clicked.connect(lambda: Dialog.controlTomada(5))
        self.showTomada6.clicked.connect(lambda: Dialog.controlTomada(6))
        self.showTomada7.clicked.connect(lambda: Dialog.controlTomada(7))
        self.showTomada8.clicked.connect(lambda: Dialog.controlTomada(8))
        self.showTomada9.clicked.connect(lambda: Dialog.controlTomada(9))
        self.showTomada10.clicked.connect(lambda: Dialog.controlTomada(10))
        self.cbTomada.currentIndexChanged.connect(Dialog.selectTomada)
        self.btRenamePort.clicked.connect(Dialog.configTomada)
        self.btSaveEthernet.clicked.connect(Dialog.saveEthernet)
            
    def enableComponents(self, enable):
        self.uptimeField.setEnabled(enable)
        self.tempField.setEnabled(enable)
        self.dataHoraField.setEnabled(enable)
        self.showTomada1.setEnabled(enable)

        self.showTomada2.setEnabled(enable)
        self.showTomada3.setEnabled(enable)
        self.showTomada4.setEnabled(enable)
        self.showTomada5.setEnabled(enable)
        self.showTomada6.setEnabled(enable)
        self.showTomada7.setEnabled(enable)
        self.showTomada8.setEnabled(enable)
        self.showTomada9.setEnabled(enable)
        self.showTomada10.setEnabled(enable)
        self.hostname.setEnabled(enable)
        self.ip.setEnabled(enable)
        self.gateway.setEnabled(enable)
        self.mask.setEnabled(enable)
        self.dns1.setEnabled(enable)
        self.dns2.setEnabled(enable)
        self.dhcp.setEnabled(enable)

    def updateUI(self, vd):
        colorVerde = 'rgb(0,255,102)'
        print(vd.updateInfo())
        print('Atualiza ui')
        if(vd.lastInfo != 0):
            self.enableComponents(True)
            self.uptimeField.setText(vd.getUptime())
            self.tempField.setText(vd.lastInfo['temp']+' °C')
            self.dataHoraField.setText(vd.getDate()+'-'+vd.getTime())
            self.showTomada1.setStyleSheet("background-color:"+("gray" if vd.getRmac(1) == 'false' else (colorVerde if vd.getAc(1) == '0' else "red"))+"");

            self.showTomada2.setStyleSheet("background-color:"+("gray" if vd.getRmac(2) == 'false' else (colorVerde if vd.getAc(2) == '0' else "red"))+"");
            self.showTomada3.setStyleSheet("background-color:"+("gray" if vd.getRmac(3) == 'false' else (colorVerde if vd.getAc(3) == '0' else "red"))+"");
            self.showTomada4.setStyleSheet("background-color:"+("gray" if vd.getRmac(4) == 'false' else (colorVerde if vd.getAc(4) == '0' else "red"))+"");
            self.showTomada5.setStyleSheet("background-color:"+("gray" if vd.getRmac(5) == 'false' else (colorVerde if vd.getAc(5) == '0' else "red"))+"");
            self.showTomada6.setStyleSheet("background-color:"+("gray" if vd.getRmac(6) == 'false' else (colorVerde if vd.getAc(6) == '0' else "red"))+"");
            self.showTomada7.setStyleSheet("background-color:"+("gray" if vd.getRmac(7) == 'false' else (colorVerde if vd.getAc(7) == '0' else "red"))+"");
            self.showTomada8.setStyleSheet("background-color:"+("gray" if vd.getRmac(8) == 'false' else (colorVerde if vd.getAc(8) == '0' else "red"))+"");
            self.showTomada9.setStyleSheet("background-color:"+("gray" if vd.getRmac(9) == 'false' else (colorVerde if vd.getAc(9) == '0' else "red"))+"");
            self.showTomada10.setStyleSheet("background-color:"+("gray" if vd.getRmac(10) == 'false' else (colorVerde if vd.getAc(10) == '0' else "red"))+"");
            self.hostname.setText(vd.lastInfo['devhost'])
            self.ip.setText(vd.lastInfo['devip'])
            self.gateway.setText(vd.lastInfo['devgtw'])
            self.mask.setText(vd.lastInfo['devmask'])
            self.dns1.setText(vd.lastInfo['devdns1'])
            self.dns2.setText(vd.lastInfo['devdns2'])
            self.dhcp.setChecked(True if vd.lastInfo['devdhcp'] == 'true' else False)

            self.nt1.setText(vd.getNomeAC(1))
            self.nt2.setText(vd.getNomeAC(2))
            self.nt3.setText(vd.getNomeAC(3))
            self.nt4.setText(vd.getNomeAC(4))
            self.nt5.setText(vd.getNomeAC(5))
            self.nt6.setText(vd.getNomeAC(6))
            self.nt7.setText(vd.getNomeAC(7))
            self.nt8.setText(vd.getNomeAC(8))
            self.nt9.setText(vd.getNomeAC(9))
            self.nt10.setText(vd.getNomeAC(10))
        else: self.enableComponents(False)
            


    def alert(self, window, title, message):
        QMessageBox.about(window, title, message)