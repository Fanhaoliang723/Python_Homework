import sys
from pathlib import Path, PurePath
from use_case import reader as reader
from use_case import joseph as joseph
from UI.UI import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class UiDialog(object):
    def __init__(self):
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.click_buttom_start()
        self.click_buttom_close()
        self.click_buttom_setconf()
        self.click_buttom_choose_file()
        self.click_buttom_read_file()
        self.click_buttom_write_file()
        self.cwd = Path.cwd()
        MainWindow.show()
        sys.exit(app.exec_())
        
    def click_buttom_start(self):
        self.ui.start.clicked.connect(self.start_joseph)

    def click_buttom_close(self):
        self.ui.close.clicked.connect(QCoreApplication.instance().quit)
    
    def click_buttom_setconf(self):
        self.ui.button_conf.clicked.connect(self.setconf)

    def click_buttom_choose_file(self):
        self.ui.button_choose.clicked.connect(self.choose_file)

    def click_buttom_read_file(self):
        self.ui.button_read.clicked.connect(self.read_file)

    def click_buttom_write_file(self):
        self.ui.button_write.clicked.connect(self.write_file)

    def read_file(self):
        map = {".txt":reader.TxtReader, ".csv":reader.CsvReader, ".xlsx":reader.XlsxReader, ".zip":reader.ZipReader}
        suffix = PurePath(self.path).suffix
        new_reader = map[suffix](self.path)
        self.person_lst = new_reader.create_lst()
        self.ui.file_show.clear()
        for person in self.person_lst:
              self.ui.file_show.append(person.__str__())

    def choose_file(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)
        dlg.exec_()
        filenames= dlg.selectedFiles()
        self.path = filenames[0]
        if self.path:
            msg_box = QMessageBox(QMessageBox.Information, '通知', '文件选择成功',QMessageBox.Ok)
            msg_box.exec_()

    def write_file(self):
         write_str = self.ui.file_input.toPlainText()
         with open(self.path, "a", encoding="UTF-8") as file:
             file.write("\n")
             file.write(write_str)
         with open(self.path, "r", encoding="UTF-8") as file:
             self.ui.file_show.clear()
             for line in file:
                 line = line.strip("\n")
                 self.ui.file_show.append(line)
        
    def setconf(self):
        self.start = self.ui.line_start.text()
        self.step = self.ui.line_step.text()
        if int(self.start) < 1:
            msg_box = QMessageBox(QMessageBox.Warning, '错误', 'start设置应大于0')
            msg_box.exec_()
    
    def start_joseph(self):
        josepher_iter = joseph.JosephIter(self.person_lst,int(self.start),int(self.step))
        result_lst = []
        self.ui.result_show.clear()
        for out_person in josepher_iter:
            result_lst.append(out_person)
            self.ui.result_show.append(out_person.__str__())

            
if __name__ == "__main__":
     UiDialog()