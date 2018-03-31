# -*- coding: utf-8 -*-

import threading, StringIO, time, base64
import pyscreenshot as ig

class Screen():
    def __init__(self):
        self.FPS = 10
        self.screenbuf = ""
        self.screenfile = StringIO.StringIO()
        threading.Thread(target=self.getframes).start()

    def __del__(self):
        self.screenfile.close()

    def getframes(self):
        while True:
            im = ig.grab(childprocess=False)
            self.screenfile.truncate(0)
            im.save(self.screenfile, format="jpeg", quality=75, progressive=True)
            self.screenbuf = base64.b64encode(self.screenfile.getvalue())
            time.sleep(1.0/self.FPS)
    
    def gen(self):
        return self.screenbuf
    
screenlive = Screen()