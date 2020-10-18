# DesktopWallpaperChanger
A desktop wallpaper changer for windows 10.

# How to run
-> run wallpaper.py first.  
-> type your preffered image genre.  
-> run call.py to see it work.  
alternatively:  
call.py can be scheduled using task scheduler, in that case the call.py has to be modified and the sleep time has to be hardcoded.   
# Requirements
-> python 3  
# Approach  
At first I just needed to retrive the images from the API. So I use requests to get the json and filter out the full image links.
Then I download it using urllib.retrieve() into the images dirctory. This is done in the wallpaper.py.  
The call.py script iteratively chooses a random image from the images directory and changes the wallpaper using ctypes.  
The script uses ctypes to load user32.dll and call SystemParametersInfoW().   
# Some default images has been added but the image folder can be deleted

# how to run
-> run wallpaper.py first.  
-> type your preffered image genre.  
-> run call.py to see it work.  
# requirements
-> python 3  
# some default images has been added but the image folder can be deleted

