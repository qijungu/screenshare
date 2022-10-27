#Copyright (C) 2021  Qijun Gu
#
#This file is part of Screenshare.
#
#Screenshare is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Screenshare is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with Screenshare. If not, see <https://www.gnu.org/licenses/>.

__version__ = "1.1"

import sys
import time
import base64
import threading

version = sys.version_info.major

if version == 2:
    import StringIO as io
elif version == 3:
    import io

if sys.platform in ["win32", "darwin"]:
    from PIL import ImageGrab as ig
else:
    import pyscreenshot as ig
    bkend = "pygdk3"


class Screen():
    def __init__(self):
        self.fps = 10
        self.quality = 75
        self.screenbuf = ""
        self.password = ""

        if version == 2:
            self.screenfile = io.StringIO()
        elif version == 3:
            self.screenfile = io.BytesIO()
        
        threading.Thread(target=self.capture_frames, daemon=True).start()

    def __del__(self):
        self.screenfile.close()

    def capture_frames(self):
        while True:
            if sys.platform in ["win32", "darwin"]:
                im = ig.grab()
            else:
                im = ig.grab(childprocess=False,backend=bkend)
            
            self.screenfile.seek(0)
            self.screenfile.truncate(0)

            im_converted = im.convert("RGB")
            im_converted.save(self.screenfile, format="jpeg", quality=self.quality, progressive=True)

            self.screenbuf = base64.b64encode(self.screenfile.getvalue())

            time.sleep(1.0/self.fps)
    
    def get_frame(self):
        s = ''

        if version == 2:
            s = self.screenbuf
        elif version == 3:
            s = self.screenbuf.decode()
        
        return s
    
screenlive = Screen()
