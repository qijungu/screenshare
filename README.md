## Description

For some reasons, I wanted to share my computer screen to other computers in the same local network (LAN or WLAN). I could not find an easy way to do it. So, I created this small screen sharing tool in Python.

In short, the computer to share screen runs this Python script that captures screenshots periodically and hosts screenshots as a web service. Other computers then browse the screenshots with any web browser.

## Requirements (what I have in my own computer)

+ Fedora 26 + Gnome3 running on Xorg

+ Python 2.7

+ Know issue: This tool does not work with Wayland because of a <a href="https://fedoraproject.org/wiki/How_to_debug_Wayland_problems#Screen_capture_is_not_available_with_usual_apps">security reason</a>. You must use Xorg (by selecting Xorg on login).

## Installation and Run

1. pip install Flask-Bootstrap pyscreenshot

2. In a directory, run "**git clone https://gitlab.com/qijungu/screenshare.git**". You will have a new directory "screenshare" with code inside.

3. The command to run is "**python screenshare.py [port]**". Default port is 18331. Example commands are below.

	python screenshare.py          # host screenshots on port 18331

	python screenshare.py 80       # host screenshots on port 80

4. On other computers, open a web browser and browse "**http://serverip:port**". For example, if the serverip is 192.168.0.101 and the service port is 18331, then other computers should browse "http://192.168.0.101:18331".
