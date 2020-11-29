# Desktop Battery Notifier
A simple program that notifies the user when the battery goes beyond the specified limit

![](https://i.imgur.com/dLFg9A5.png)

![](https://i.imgur.com/IC6rEbu.png)

## About the project  

### User-specified limit
The user can specify the upper and lower battery limit.  

### Notification
The program will check the battery every 5 minutes. Appropriate notification will be sent when the battery hits or goes beyond the limit.

### Background app
The program runs in the background. To quit the program, go to System Tray > right-click the program, press Quit.

## Project Setup

### Requirements
* Python3
```
pip install pyqt5
pip install psutil
```

### Source Code
The source can be found in desktopBatteryNotifier.py