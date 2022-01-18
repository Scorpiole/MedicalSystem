import sys
from WindowsDesign.medicsystem import *

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from CRUD.CRUD_logic import *



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())