#from PyQt5 import QtGui
#from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication,QPushButton, QMainWindow
from main_ui import *
from voltdevice import VoltDevice
import sys
class Window(QMainWindow):
    def __init__(self, parent=None):
        self.colorVerde = 'rgb(0,255,102)'
        QtWidgets.QTabWidget.__init__(self, parent)

        self.ui = WindowUI()
        self.ui.setupUi(self)

        self.vd = VoltDevice('192.168.0.90','admin','voltvolt')
        if self.vd.lastInfo !=0:
            self.ui.updateUI(self.vd)
 
    def login(self):
        if(self.ui.btConnect.text() == "Conectar"):
            
            self.vd = VoltDevice(self.ui.ipField.text(), self.ui.userField.text(), self.ui.passField.text())
            if self.vd.lastInfo !=0:
                print('Login sucesso!!')
                self.ui.alert(self, 'Sucesso','Login efetuado com sucesso!!')
                self.ui.btConnect.setText("Desconectar")
                self.ui.updateUI(self.vd)
            else: 
                print('Falha login')
                self.ui.alert(self, 'Falha','Falha de Login!!')
        else:
            self.ui.btConnect.setText("Conectar")
            self.ui.enableComponents(False)

    def controlTomada(self, tomada):
        if(self.vd.lastInfo !=0 and self.vd.getRmac(tomada)):
            resp = self.vd.ctrlAc(tomada,0,True,'')
            if hasattr(resp, 'status_code') and resp.status_code == 200:
                print("comando enviado com sucesso")
            else:
                self.ui.alert(self,"Erro","Falha ao enviar o comando")

            self.ui.updateUI(self.vd)

    def saveEthernet(self):
        if(self.vd.lastInfo !=0):
            resp = self.vd.configEthernet(self.ui.dhcp.isChecked(), self.ui.hostname.text(), self.ui.ip.text(),self.ui.gateway.text(),self.ui.mask.text(),self.ui.dns1.text(), self.ui.dns2.text())        
            if(hasattr(resp, 'status_code') and resp.status_code == 200):
                self.ui.alert(self, 'Sucesso','Configuração executada com sucesso!!')
            else: self.ui.alert(self, 'Falha','Falha!!')

    def selectTomada(self):
        if(self.ui.cbTomada.currentIndex() > 0 and self.vd.lastInfo !=0):
            nome = self.vd.getNomeAC(int(self.ui.cbTomada.currentText()))
            self.ui.nomeTomadaField.setText(nome)
            self.ui.cbHabilitaTomada.setChecked(self.vd.getRmac(int(self.ui.cbTomada.currentText())) == 'true')

    def configTomada(self):
        if(self.ui.cbTomada.currentIndex() > 0 and self.vd.lastInfo !=0):           
            resp = self.vd.ctrlAc(self.ui.cbTomada.currentIndex(), 1,self.ui.cbHabilitaTomada.isChecked() , self.ui.nomeTomadaField.text())
            print(resp.status_code)
            if(hasattr(resp, 'status_code') and resp.status_code == 200):
                self.ui.alert(self, 'Sucesso','Configuração executada com sucesso!!')
            else: self.ui.alert(self, 'Falha','Falha!!')
            self.ui.updateUI(self.vd)

    def alert(self, msg):
        print(msg)

App = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(App.exec())

