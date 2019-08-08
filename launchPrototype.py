#For linux on raspberry
#Dit al wel als alles is geïnstalleerd
#!/usr/bin/python
import os
import platform


def linuxPosix():
    pth = "/home/pi/prototype/build"
    if os.path.exists(pth):
        os.chdir(pth)
        Cmd = "node main.js"
        os.system(Cmd)
    else:
        print('There is not yet the right files')

Environment = platform.system()
OperatingSystem = os.name
print(Environment)
print(OperatingSystem)
if Environment == 'Linux':
    if OperatingSystem == 'posix':
        linuxPosix()