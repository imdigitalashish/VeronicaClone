import eel
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)


print(screensize)


eel.init("web")





eel.start("index.html", size=screensize)