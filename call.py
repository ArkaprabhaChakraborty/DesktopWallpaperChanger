import os
import random
import ctypes
import time

t = os.getcwd()
path = t+"\images"
x = os.listdir(path)

while(True):
    X = ""
    l = random.choice(x)
    X = ('%s\%s'%(path,l))
    print(X)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, X , 0)
    time.sleep(5) #this is for 5 secs.... So for 2 minutes it will be 120... and so on
