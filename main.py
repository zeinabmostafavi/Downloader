import sys
import os
import urllib.request

from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QDir


class mainwindow(QWidget):
    def __init__(self):
        super(mainwindow, self).__init__()

        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.ui.dnbtn.clicked.connect(self.download)
        self.ui.brbtn.clicked.connect(self.browse)

    def browse(self):
        save = QFileDialog.getSaveFileName(
            self, caption="Save File As", filter="All Files (*.*)", dir=".")
        self.ui.bredit.setText(save[0])

    def download(self):
        url = self.ui.dnedit.text()
        save_url = self.ui.bredit.text()
        try:
            urllib.request.urlretrieve(url, save_url, self.report)
        except Exception:
            QMessageBox.warning(self, "Warning", "The download failed!")
            return

        QMessageBox.information(self, "Information",
                                "The download is complete!")
        self.ui.prb.setValue(0)
        self.ui.dnedit.setText('')
        self.ui.bredit.setText('')

    def report(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize

        if totalsize > 0:
            percent = readsofar * 100 / totalsize
            self.ui.prb.setValue(int(percent))


if __name__ == "__main__":
    app = QApplication([])
    window = mainwindow()
    sys.exit(app.exec_())
