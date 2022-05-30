from colorama import Fore
from datetime import datetime
time = datetime.now().strftime("%H:%M")
class functions:
    def errorf(z):
        return print(Fore.RED + f"{time} | Error: {z}")
    def warnf(z):
        return print(Fore.YELLOW + f"{time} | Warning: {z}")