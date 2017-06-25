# ctypes練習

from ctypes import *

myUser32 = windll.user32
myUser32.MessageBoxA( 0, "Hello, World!", "Welcom to IDAPython world!", 0x40)
