from gen_barcode import MyGenBarcode
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox
from PySide2.QtUiTools import QUiLoader
from ui_main import Ui_MainWindow
import os
from pic2docx import gen_docx


class MyWindows(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        # self.ui = QUiLoader().load('ui_main.ui')
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button.clicked.connect(self.click_button)
        self.pic_paths = []

    # def show_windows(self):
    #     self.ui.show()
    #     self.app.exec_()

    def click_button(self):
        self.pic_paths = []
        #写入参数
        code_text = self.ui.textEdit.toPlainText()
        if code_text == '':
            raise ValueError('Input can not be None')
        module_width = float(self.ui.line_Edit_module_width.text(
        )) if self.ui.line_Edit_module_width.text() != '' else 0.3
        module_height = float(self.ui.lineEdit_module_height.text(
        )) if self.ui.lineEdit_module_height.text() != '' else 10
        quiet_zone = float(self.ui.lineEdit_quiet_zone.text()
                           ) if self.ui.lineEdit_quiet_zone.text() != '' else 0
        font_size = int(self.ui.lineEdit_font_size.text()
                        ) if self.ui.lineEdit_font_size.text() != '' else 9
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
        # if len(code_text_split) > 18:
        #     self.ui.textEdit.setPlainText('单次最多18个，请重新输入')
        #     return 0
        extra_text = []
        for i, code_text in enumerate(code_text_split):
            if code_text == '':
                continue
            if 't' not in code_text:
                extra_text.append('')
            if 't' in code_text:
                code_text, tmp_text = code_text.split('t')
                extra_text.append(tmp_text)
            write_path_local = str(i + 1) + '-' + code_text
            pic_path = os.path.join(write_path_global, write_path_local)
            pic_path.replace('\\', "\\\\")
            pic_path = pic_path + '.png'
            self.pic_paths.append(pic_path)
            gen_barcode.gen_barcode(code_text, write_path_local)
                
        #生成word
        my_gen_docx = gen_docx(self.pic_paths, extra_text)
        my_gen_docx.put_pic_in_word()

app = QApplication([])
test = MyWindows()
test.show()
app.exec_()
# test.show_windows()
