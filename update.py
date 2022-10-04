import requests, os, shutil, colorama, sys
from colorama import Fore
colorama.init()

print(Fore.YELLOW + "Updating..." + Fore.BLACK)
try:
     os.remove("rverflow.exe")
except FileNotFoundError:
     pass
os.mkdir("temp")
with open(f"temp/temp.py", "bw+") as temp:
     r = requests.get("https://raw.githubusercontent.com/RiverCheet/fart/main/update/launcher.py")
     temp.write(r.content)
with open("temp/temp.ico", "bw+") as icon:
     r = requests.get("https://raw.githubusercontent.com/RiverCheet/fart/main/update/rverflow.ico")
     icon.write(r.content)
os.system("pyinstaller --onefile --i=temp/temp.ico temp/temp.py")
os.remove("temp.spec");shutil.rmtree("temp");shutil.rmtree("build");os.rename("dist/temp.exe", "rverflow.exe");shutil.rmtree("dist")
os.system("cls");print(Fore.GREEN + f"Updated/Reinstalled!")
os.system("pause")
     
          
