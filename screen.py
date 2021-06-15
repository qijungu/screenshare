# -*- coding: utf-8 -*-

import threading, time, base64
import pyscreenshot as ig

import sys

ver = sys.version_info.major
if ver==2:
    import StringIO
elif ver==3:
    import io

class Screen():
    def __init__(self):
        self.FPS = 10
        self.screenbuf = ""
        if ver==2:
            self.screenfile = StringIO.StringIO()
        elif ver==3:
            self.screenfile = io.BytesIO()
        threading.Thread(target=self.getframes).start()

    def __del__(self):
        self.screenfile.close()

    def getframes(self):
        while True:
            im = ig.grab(childprocess=False,backend="pygdk3")
            self.screenfile.seek(0)
            self.screenfile.truncate(0)
            im.save(self.screenfile, format="jpeg", quality=75, progressive=True)
            self.screenbuf = base64.b64encode(self.screenfile.getvalue())
            time.sleep(1.0/self.FPS)
    
    def gen(self):
        s = ''
        if ver==2:
            s = self.screenbuf
        elif ver==3:
            s = self.screenbuf.decode()
        return s
    
screenlive = Screen()
