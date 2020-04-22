# -*- coding: utf-8 -*-
# add pict display and save file

# pict = Image.open("C:/Users/Jon/Downloads/20200421.jpg")
# pict.show()
import sys
from PIL import Image
import time
import threading
import queue

from stopThreading import stop_thread

class PictDisplay(self):
    def pict_start(self):
        self.path = None
        # # print('PictDisplay start!')
        # self.save_display_th = None
        # self.detail_pict_queue = queue.Queue(maxsize=128);
        # # 创建线程
        # self.save_display_th = threading.Thread(target=self.pict_thread, args=(self.detail_pict_queue,))
        # self.save_display_th.setDaemon(True)
        # self.save_display_th.start()

    def pict_thread(self, queue):
        # 线程等待
        while True:
            pict_info = self.detail_pict_queue.get(block=True, timeout=None)
            # print(pict_info)
            if 'jpg' in pict_info:
                pict = Image.open(pict_info)
                pict.show()
            elif 'pcm' in pict_info:
                continue

    def pict_save(self, path):
        # self.path = path
        # pict = Image.open(self.path)
        spath = path
        self.detail_pict_queue.put(spath)

        # print(spath)
        # pict.save(spath)
        # pict.show()

    def pict_exit(self):
        stop_thread(self.save_display_th)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = TcpLogic(1)
    sys.exit(app.exec_())

