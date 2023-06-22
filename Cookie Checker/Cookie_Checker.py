import requests
from colorama import Fore, Style
from colorama import init
import os
init(autoreset=True)
cookie = input(f"{Style.BRIGHT}{Fore.GREEN}Enter Cookie: ")
try:
 os.system("cls")
 r=requests.get("https://accountsettings.roblox.com/v1/email", cookies={'.ROBLOSECURITY': cookie}).json()
 if "verified" in r:
    print(f"Email:{Fore.BLUE} Verified")
 else:print(f'Email:{Fore.RED} Unverified')
 r=requests.get("https://users.roblox.com/v1/birthdate", cookies={'.ROBLOSECURITY': cookie}).json()
 BIRTH = f"{r['birthYear']}-{r['birthMonth']}-{r['birthDay']}"
 print(f"{Style.BRIGHT}{Fore.GREEN}{BIRTH}")
 r=requests.get("https://users.roblox.com/v1/users/authenticated", cookies={'.ROBLOSECURITY': cookie}).json()
 ID = r["id"]
 print(f"{Style.BRIGHT}{Fore.GREEN}https://www.roblox.com/users/{ID}/profile")
 r=requests.get("https://economy.roblox.com/v1/user/currency", cookies={'.ROBLOSECURITY': cookie}).json()
 ROBUX = r["robux"]
 print(f"{Style.BRIGHT}{Fore.GREEN}Robux: {Fore.BLUE}{ROBUX}")
 r=requests.get(f"https://premiumfeatures.roblox.com/v1/users/{ID}/validate-membership", cookies={'.ROBLOSECURITY': cookie}).json()
 if bool(r):PREMIUM = print(f"{Style.BRIGHT}{Fore.GREEN}Premium:{Fore.BLUE} True")
 else:print(f"{Style.BRIGHT}{Fore.GREEN}Premium:{Fore.RED} False")
 r=requests.get(f'https://inventory.roblox.com/v1/users/{ID}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100', cookies={".ROBLOSECURITY": cookie}).json()
 collectibles = r["data"]
 for collectible in collectibles:
  name = collectible["name"]
  value = collectible["recentAveragePrice"]
  print(f"{Style.BRIGHT}{Fore.GREEN}{name}: {Fore.BLUE}{value}$")
  input(Style.BRIGHT+ Fore.LIGHTBLACK_EX + "Press anything to exit.")
except:
  os.system("cls")
  print(Fore.RED + "Invalid Cookie")
  input("Press anything to exit.")