import pyshorteners
import os
import colorama
from colorama import Fore,Back,Style
colorama.init()

os.system("clear")
print(Fore.LIGHTGREEN_EX +"""

   _____ _                _
  / ____| |              | |
 | (___ | |__   ___  _ __| |_ ___ _ __   ___ _ __
  \___ \| '_ \ / _ \| '__| __/ _ \ '_ \ / _ \ '__|
  ____) | | | | (_) | |  | ||  __/ | | |  __/ |
 |_____/|_| |_|\___/|_|   \__\___|_| |_|\___|_|

                                                """)
print("                created by BLU3N1N3S              ")
link=input("\n enter you links: ")
print(".............please wait.................")
cont=input(" press enter to continue ")
shortener=pyshorteners.Shortener()
final=shortener.tinyurl.short(link)
print(" your link is :"+ final)
print(" thank you for using my tool:) ")
