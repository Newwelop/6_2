import colorama

from colorama import Fore, Style, Back

print(Fore.RED + "Цей текст буде червоним.")
print(Back.BLUE + "Текст на синьому фоні.")
print(Style.BRIGHT + "Яскравий текст.")
print(Fore.RED + "Цей текст червоний." + Fore.RESET + " А цей - звичайний.")



