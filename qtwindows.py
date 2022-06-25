from gen_barcode import MyGenBarcode
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox
from PySide2.QtUiTools import QUiLoader
from ui_main import Ui_MainWindow
import os


class MyWindows(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        # self.ui = QUiLoader().load('ui_main.ui')
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button.clicked.connect(self.click_button)

    # def show_windows(self):
    #     self.ui.show()
    #     self.app.exec_()

    def click_button(self):
        #写入参数
        code_text = self.ui.textEdit.toPlainText()
        if code_text == '':
            raise ValueError('Input can not be None')
        module_width = float(self.ui.line_Edit_module_width.text(
        )) if self.ui.line_Edit_module_width.text() != '' else 0.3
        module_height = float(self.ui.lineEdit_module_height.text(
        )) if self.ui.lineEdit_module_height.text() != '' else 15.0
        quiet_zone = float(self.ui.lineEdit_quiet_zone.text()
                           ) if self.ui.lineEdit_quiet_zone.text() != '' else 2
        font_size = int(self.ui.lineEdit_quiet_zone.text()
                        ) if self.ui.lineEdit_quiet_zone.text() != '' else 10
        text_distance = float(self.ui.lineEdit_text_distance.text(
        )) if self.ui.lineEdit_text_distance.text() != '' else 5.0
        write_text = True if self.ui.lineEdit_write_text.text(
        ) == '' else False
        dpi = int(self.ui.lineEdit_dpi.text()
                  ) if self.ui.lineEdit_dpi.text() != '' else 300
        # self.write_path = self.ui.lineEdit_write_path.text()  #写入路
        write_path_global = os.getcwd()
        #初始化生成条形码类
        gen_barcode = MyGenBarcode(module_width, module_height, quiet_zone,
                                   font_size, text_distance, write_text, dpi,
                                   write_path_global)
        code_text_split = code_text.split('\n')
        for i, code_text in enumerate(code_text_split):
            if code_text != '':
                write_path_local = str(i) + '-' + code_text
                self.ui.lineEdit_write_path.setText(
                    os.path.join(write_path_global, write_path_local))
                gen_barcode.gen_barcode(code_text, write_path_local)
                # print(write_text)


app = QApplication([])
test = MyWindows()
test.show()
app.exec_()
# test.show_windows()
