import sys
from pathlib import Path, PurePath
from use_case import reader          
from use_case import joseph 
from UI.UI import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#自检问题部分备注
#不会sys.path因此把主函数都放到了资源文件的上级目录
class UiDialog(object):
    def __init__(self):
        #问题：app入口若放到主函数exit冲突，程序无法弹出文件选择（未解决），因此写在了init
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
        self.path = None  #python熟悉程度不够，想定义判断是否为空（用于用户错误操作检验）
        self.filename = None
        MainWindow.show()
        msg_box = QMessageBox(QMessageBox.Information, '通知', '由于对.text()函数了解不深入，没有写验证是否为空，因此请勿在未设置好步长与初始前点击设置完成，否则UIbreakdown（BUG）',QMessageBox.Ok)
        msg_box.exec_()
        sys.exit(app.exec_())
    #信号    
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
#槽？（定义理解不深）
    def read_file(self):
        if self.path == None:
            msg_box = QMessageBox(QMessageBox.Warning, '错误', '请选择文件')
            msg_box.exec_()
            return

        map = {".txt":reader.TxtReader, ".csv":reader.CsvReader, ".xlsx":reader.XlsxReader, ".zip":reader.ZipReader}
        suffix = PurePath(self.path).suffix

        if suffix == '.zip':
            if self.filename == None:
                msg_box = QMessageBox(QMessageBox.Information, '通知', '请在文件输入框内输入要读取的文件名',QMessageBox.Ok)
                msg_box.exec_()
            self.filename = self.ui.file_input.toPlainText()
            new_reader = map[suffix](self.path,self.filename)
        else:
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

        if self.path == None:
            msg_box = QMessageBox(QMessageBox.Warning, '错误', '请选择文件')
            msg_box.exec_()
            return
        else:
            with open(self.path, "a", encoding="UTF-8") as file:
                 file.write("\n")
                 file.write(write_str)
            with open(self.path, "r", encoding="UTF-8") as file:
                 self.ui.file_show.clear()
                 for line in file:
                     line = line.strip("\n")
                     self.ui.file_show.append(line)
        
    def setconf(self):
        #对于.text()函数了解不深入，没有写验证是否为空，因此未设置点击设置完成，UIbreakdown
        self.start = self.ui.line_start.text()
        self.step = self.ui.line_step.text()

        if int(self.start) < 1:
            msg_box = QMessageBox(QMessageBox.Warning, '错误', 'start设置应大于0')
            msg_box.exec_()
        else:  
            msg_box = QMessageBox(QMessageBox.Information, '通知', '设置成功')
            msg_box.exec_()
    
    def start_joseph(self):
        if self.path == None:
            msg_box = QMessageBox(QMessageBox.Warning, '错误', '请选择文件')
            msg_box.exec_()
            return

        if self.person_lst == []:
            msg_box = QMessageBox(QMessageBox.Information, '错误', '人员信息未读入，请读取文件')
            msg_box.exec_()
            return

        josepher_iter = joseph.JosephIter(self.person_lst,int(self.start),int(self.step))
       
        self.ui.result_show.clear()
        for out_person in josepher_iter:
            self.ui.result_show.append(out_person.__str__())
      
            
if __name__ == "__main__":
     UiDialog()
     