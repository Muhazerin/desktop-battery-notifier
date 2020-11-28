from PyQt5.QtGui import QIcon
from PyQt5.QtCore import (QThread, pyqtSignal, pyqtSlot)
from PyQt5.QtWidgets import (QApplication, QDialog, QSystemTrayIcon, 
                            QMenu, QVBoxLayout, QAction, QMessageBox)
from PyQt5.QtSql import (QSqlDatabase, QSqlQuery)
import sys
import psutil
import window

class Worker(QThread):
    batInfo = pyqtSignal(int, bool)

    def __init__(self):
        QThread.__init__(self)
    
    def __del__(self):
        self.wait()

    def run(self):
        while True:
            battery = psutil.sensors_battery()
            self.batInfo.emit(battery.percent, battery.power_plugged)
            self.sleep(300) # let the thread sleep for 5 minutes before continue

class Window(QDialog, window.Ui_Dialog):
    def __init__(self):
        super(Window, self).__init__()

        # These 3 functions will also launch a system tray in the background.
        # The app will not close unless the user closes the system tray.
        self.createAction()
        self.createSystemTray()
        self.setSystemTrayIcon()
        self.trayIcon.activated.connect(self.restoreApp)
        self.trayIcon.show()

        # Worker thread to check battery life
        self.batteryWorker = Worker()
        self.batteryWorker.batInfo.connect(self.on_batInfo_emitted)
        self.batteryWorker.start()

        self.setupUi(self)
        self.saveBtn.setEnabled(False)
        self.upperBatteryPercentageLimitSpinBox.valueChanged.connect(self.checkOriginal)
        self.lowerBatteryPercentageLimitSpinBox.valueChanged.connect(self.checkOriginal)
        self.saveBtn.clicked.connect(self.saveNewValue)

        # open the database to retrieve the information
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("database/db.sqlite3")
        self.db.open()

        query = QSqlQuery()
        query.exec("SELECT * FROM info LIMIT 1;")
        while query.next():
            self.originalUpperBatteryPercentageLimit = query.value(0)
            self.originalLowerBatteryPercentageLimit = query.value(1)
            self.upperBatteryPercentageLimitSpinBox.setValue(query.value(0))
            self.lowerBatteryPercentageLimitSpinBox.setValue(query.value(1))
        
        self.db.close() # close the connection after using it

    def saveNewValue(self):
        if self.upperBatteryPercentageLimitSpinBox.value() > self.lowerBatteryPercentageLimitSpinBox.value():
            self.saveBtn.setEnabled(False)
            self.originalUpperBatteryPercentageLimit = self.upperBatteryPercentageLimitSpinBox.value()
            self.originalLowerBatteryPercentageLimit = self.lowerBatteryPercentageLimitSpinBox.value()

            self.db.open()

            query = QSqlQuery()
            statement = f"UPDATE info SET upperBatLimit={self.originalUpperBatteryPercentageLimit}, lowerBatLimit={self.originalLowerBatteryPercentageLimit};"
            query.exec(statement)

            self.db.close()
        elif self.upperBatteryPercentageLimitSpinBox.value() == self.lowerBatteryPercentageLimitSpinBox.value():
            QMessageBox.critical(None, "Error", "The upper battery limit cannot be equal to the lower battery limit")
        else:
            QMessageBox.critical(None, "Error", "The upper battery limit cannot be lower than the lower battery limit")


    def checkOriginal(self, placeholder):
        if self.originalUpperBatteryPercentageLimit == self.upperBatteryPercentageLimitSpinBox.value() and self.originalLowerBatteryPercentageLimit == self.lowerBatteryPercentageLimitSpinBox.value():
            self.saveBtn.setEnabled(False)
        else:
            self.saveBtn.setEnabled(True)

    @pyqtSlot(int, bool)
    def on_batInfo_emitted(self, batPercent, powerPlugged):
        if powerPlugged and batPercent >= self.originalUpperBatteryPercentageLimit:
            self.trayIcon.showMessage("Battery Notifier", 
                f"Battery is at {batPercent}%. Unplug your power",
                self.icon, 2000)
        elif not powerPlugged and batPercent <= self.originalLowerBatteryPercentageLimit:
            self.trayIcon.showMessage("Battery Notifier", 
                f"Battery is at {batPercent}%. Please plug in your power",
                self.icon, 2000)

    def setSystemTrayIcon(self):
        self.trayIcon.setIcon(QIcon(":/battery.png"))

    def closeApp(self):
        self.batteryWorker.quit()
        QApplication.instance().quit()

    def restoreApp(self, activationReason):
        if activationReason == 3:
            self.showNormal()

    def createAction(self):
        self.restoreAction = QAction("&Restore", self,
            triggered=self.showNormal)
        self.quitAction = QAction("&Quit", self,
            triggered=self.closeApp)

    def createSystemTray(self):
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)

        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    QApplication.setQuitOnLastWindowClosed(False)

    window = Window()
    window.show()
    sys.exit(app.exec_())