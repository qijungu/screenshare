## Description

For some reasons, I wanted to share my computer screen to other computers in the same local network (LAN or WLAN). I could not find an easy way to do it. All free and pricey screen sharing services need the computers in the same local network to connect to the Internet. They incur tremendous network traffic on my Internet connection.

So, I created this small screen sharing tool in Python. All computers in the same local network only need local network connections for screen sharing. Now, I have zero Internet access concerns while I share my screen to all other computers in my network.

In short, the computer to share screen runs this Python script that captures screenshots periodically and hosts screenshots as a streaming web service. Other computers then browse the screenshots with any web browser.

Of course, if you want to share your screen on the Internet, all you need to do is offering this service on the Internet as any other regular services.

**Security reminder** Do not run this service if you do not need to share screen.

## Requirements

This tool can run on Linux, Windows and MAC.

+ Python 2.x or 3.x

+ Know issue: In Linux, this tool does not work with Wayland because of a <a href="https://fedoraproject.org/wiki/How_to_debug_Wayland_problems#Screen_capture_is_not_available_with_usual_apps">security reason</a>. You must use Xorg (by selecting Xorg on login).

## Install and Run

1. pip install flask-bootstrap pyscreenshot

2. In a directory, run "**git clone https://github.com/qijungu/screenshare.git**". You will have a new directory "screenshare" with code inside.

3. To start the screen sharing service, run "**python screenshare.py [port]**".

	The default service port is 18331. Example commands are below.

	\# host screenshots on port 18331  
	python screenshare.py

	\# host screenshots on port 80  
	python screenshare.py 80

4. On other computers, open a web browser and browse "**http://serverip:port**".

	For example, if the server ip is 192.168.0.101 and the service port is 18331, then the URL to browse is "http://192.168.0.101:18331".
