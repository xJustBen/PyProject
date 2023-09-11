#Settings

#Either True or False
#If UseBoth is set to True, disable the others.

UseBoth = True 
UseBrowser = False
BrowserURL = 'https://outlook.office365.com/mail/inbox/'
UseCMDWindows = False
DebuggingMode = False #Set to False for this to actually work - True for testing
DebuggingTimes = 5 #If debugging mode is on, how many times should it loop

# End Of Settings












































# Do Not Edit Below






















# Loading Important Stuff
import time
import ctypes
import ctypes.wintypes as w
import os
import webbrowser
MB_ICONQUESTION = 0x00000020
MB_ICONWARNING = 0x00000030
MB_YESNO = 0x00000004
terminated = 'It appears you hit cancel on a prompt, so this instance has automatically ended. Re-run the program to continue.'
# Loaded

print("Please wait...")
time.sleep(3)


if DebuggingMode == False:
        response = ctypes.windll.user32.MessageBoxW(None, 'Status: You are using the most up to date version!\n\nAre you sure you want to continue? It can be tricky to stop (unless you just restart your PC)', 'The Big Shay', MB_ICONWARNING | MB_YESNO)
        
        if response == 6:  # User clicked "Yes"
            if UseBoth == True:
                while True:
                    webbrowser.open_new_tab(BrowserURL)
                    os.system("start")

            if UseBrowser == True:
                while True:
                    webbrowser.open_new_tab(BrowserURL)

            if UseCMDWindows == True:
                while True:
                    os.system("start")
        else:
            print(terminated)


if DebuggingMode == True:
        response = ctypes.windll.user32.MessageBoxW(None, 'Status: You are using the most up to date version!\n\nConfig: Debugging Mode - (Will not loop forever)\n\nAre you sure you want to continue?', 'Debugging', MB_ICONQUESTION | MB_YESNO)
        
        if response == 6:  # User clicked "Yes"
            if UseBoth == True:
                for _ in range(DebuggingTimes):
                    webbrowser.open_new_tab(BrowserURL)
                    os.system("start")

            if UseBrowser == True:
                for _ in range(DebuggingTimes):
                    webbrowser.open_new_tab(BrowserURL)

            if UseCMDWindows == True:
                for _ in range(DebuggingTimes):
                    os.system("start")
        else:
            print(terminated)
