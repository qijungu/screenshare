import threading, time, base64
import pyscreenshot
from io import BytesIO

class Screen():
    def __init__(self):
        self.FPS = 18
        self.buffer = ""
        self.screenfile = BytesIO()
        threading.Thread(target=self.getframes).start()

    def __del__(self):
        self.screenfile.close()

    def getframes(self):
        while True:
            im = pyscreenshot.grab(childprocess=False)
            im.save(self.screenfile, format="jpeg", quality=75, progressive=True)
            self.screenfile.seek(0)
            im.close()
            self.buffer = base64.b64encode(self.screenfile.getvalue())
            time.sleep(1.0/self.FPS)
    
    def gen(self):
        return self.buffer
    
screenlive = Screen()