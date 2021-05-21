# Version 2.0 - 2021 April 29

# work for both Mac, Windows, Linux
# use clear() for clearing terminal
# Method 1
# from clearterminal import * -----> clear()
# import clearterminal -----> clearterminal.clear()
import os
import platform
platform = platform.system()
if platform == 'Darwin':
    text = "clear"
elif platform == 'Windows':
    text = 'cls'


def clear():
    os.system(text)
