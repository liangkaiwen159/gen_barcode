from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.shared import Cm, Pt
from docx.document import Document as Doc
import os, sys
import time
import datetime
from docx2pdf import convert


class gen_docx():

    def __init__(self, pic_paths) -> None:
        self.pic_paths = pic_paths
        current_time = datetime.datetime.now()
        current_time = str(current_time).split('.')[0].replace(
            ':', '时')[5:16].replace(' ', '日').replace('-', '月') + '分-条形码输出'
        self.save_docx_path = os.path.join(os.getcwd(), current_time + '.docx')
        self.save_pdf_path = os.path.join(os.getcwd(), current_time + '.pdf')
        self.document = Document()  #创建文档实例
        sections = self.document.sections
        for section in sections:
            section.top_margin = Cm(1.27)
            section.bottom_margin = Cm(1.27)
            section.left_margin = Cm(1.27)
            section.right_margin = Cm(1.27)
        self.pic_numbers = len(self.pic_paths)
        self.table = self.document.add_table(rows=9, cols=2)

    def put_pic_in_word(self):
        for i, pic_path in enumerate(self.pic_paths):
            if i + 1 <= 9:
                cur_cell = self.table.cell(i, 0)
                cur_cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER  # 垂直居中
                cur_cell.paragraphs[
                    0].paragraph_format.alignment = WD_TABLE_ALIGNMENT.CENTER  # 水平居中
                run = cur_cell.paragraphs[0].add_run()  #添加图片的行
                run.add_picture(pic_path, height=Cm(2.25))
            else:
                cur_cell = self.table.cell((i + 1) % 9 - 1, 1)
                cur_cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER  # 垂直居中
                cur_cell.paragraphs[
                    0].paragraph_format.alignment = WD_TABLE_ALIGNMENT.CENTER  # 水平居中
                run = cur_cell.paragraphs[0].add_run()  #添加图片的行
                run.add_picture(pic_path, height=Cm(2.25))
        self.document.save(self.save_docx_path)
        #删除生成的条形码图片
        for pic_path in self.pic_paths:
            os.remove(pic_path)
        convert(self.save_docx_path, self.save_pdf_path)
        os.remove(self.save_docx_path)
