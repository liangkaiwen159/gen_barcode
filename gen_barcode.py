import barcode
from barcode.writer import ImageWriter
import os, sys


class MyGenBarcode():

    def __init__(self,
                 module_width: float = 0.3,
                 module_height: float = 15.0,
                 quiet_zone: float = 2,
                 font_size: int = 10,
                 text_distance: float = 5.0,
                 write_text: bool = True,
                 dpi: int = 300,
                 write_path=None) -> None:
        self.module_width = module_width
        self.module_height = module_height
        self.quiet_zone = quiet_zone
        self.font_size = font_size
        self.text_distance = text_distance
        self.write_text = write_text
        self.dpi = dpi
        self.write_path = write_path  #写入路径
        self.ttf_path = None
        self.writer_options = {
            'module_width': self.module_width,  #每个黑竖条的宽度
            'module_height': self.module_height,  #条码高度
            'quiet_zone': self.quiet_zone,  #两边空白宽度
            'font_size': self.font_size,  #字体大小
            'text_distance': self.text_distance,  #文本与条码之间的距离
            'background': 'white',  #背景色
            'foreground': 'black',  #前景色
            'write_text': self.write_text,  #是否显示文本
            'dpi': self.dpi  #分辨率
        }

    def gen_barcode(self, code_text, write_path_local):
        # barcode.generate(name='code128',
        #                  code=self.code_text,
        #                  writer=ImageWriter(),
        #                  output=self.code_text,
        #                  writer_options=self.writer_options,
        #                  text=self.code_text)
        write_path = os.path.join(self.write_path, write_path_local)
        my_writer = ImageWriter()
        try:
            my_writer.font_path = os.path.join(sys._MEIPASS, 'abc.ttf')
        except:
            my_writer.font_path = os.path.join(os.getcwd(), 'abc.ttf')
        self.ttf_path = my_writer.font_path
        generate_code = barcode.get(name='code128',
                                    code=code_text,
                                    writer=my_writer)

        if isinstance(write_path, str):
            fullname = generate_code.save(write_path, self.writer_options,
                                          code_text)
            return fullname
        elif write_path:
            generate_code.write(write_path, self.writer_options, code_text)
        else:
            raise TypeError("'output' cannot be None")
