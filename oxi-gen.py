#imports
from os import system
import time
import string
import random
import colorama
from datetime import datetime
from colorama import Fore, Back, init
colorama.init(convert=True)

string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

string.digits
'01234567'

def logo():
    print(f' ╔══════════════════════╗')
    print(f' ║{Fore.LIGHTCYAN_EX}  ██████╗ ██╗  ██╗██╗ {Fore.RESET}║')
    print(f' ║{Fore.LIGHTCYAN_EX} ██╔═══██╗╚██╗██╔╝██║ {Fore.RESET}║')
    print(f' ║{Fore.LIGHTCYAN_EX} ██║   ██║ ╚███╔╝ ██║ {Fore.RESET}║')
    print(f' ║{Fore.LIGHTCYAN_EX} ██║   ██║ ██╔██╗ ██║ {Fore.RESET}║')
    print(f' ║{Fore.LIGHTCYAN_EX} ╚██████╔╝██╔╝ ██╗██║ {Fore.RESET}║')
    print(f' ║{Fore.LIGHTCYAN_EX}  ╚═════╝ ╚═╝  ╚═╝╚═╝ {Fore.RESET}║')
    print(f' ╠══════════════════════╣')
    print(f' ║ {Fore.LIGHTYELLOW_EX}1 {Fore.RESET}>{Fore.LIGHTYELLOW_EX} 1,000 card       {Fore.RESET}║')
    print(f' ║ {Fore.LIGHTYELLOW_EX}2 {Fore.RESET}>{Fore.LIGHTYELLOW_EX} 2,000 card       {Fore.RESET}║')
    print(f' ║ {Fore.LIGHTYELLOW_EX}3 {Fore.RESET}>{Fore.LIGHTYELLOW_EX} 5,000 card       {Fore.RESET}║')
    print(f' ║ {Fore.LIGHTYELLOW_EX}4 {Fore.RESET}>{Fore.LIGHTYELLOW_EX} 10,000 card      {Fore.RESET}║')
    print(f' ╠══════════════════════╝')

def gen():
    a_list = [string.ascii_uppercase, string.digits]
    distribution = [.75, .25]

    slug = random.choices(a_list, distribution)

    s = ''
    chanceint = s.join(map(str, slug))


logo()
print(f' ╚╡ option > ', end='')
optn = int(input())

if optn == 1:
    while True:
        system('CLS')
        logo()
        gen()
        g1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        g2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        g3 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

        print(f' ╚╡{Fore.LIGHTCYAN_EX}1K {Back.LIGHTGREEN_EX}{Fore.LIGHTWHITE_EX}[{g1}-{g2}-{g3}]{Back.RESET}')
        time.sleep(random.uniform(.3, .7))
        print()
elif optn == 2:
    while True:
        system('CLS')
        logo()
        gen()
        g1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        g2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        g3 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

        print(f' ╚╡{Fore.LIGHTCYAN_EX}2K {Back.LIGHTGREEN_EX}{Fore.LIGHTWHITE_EX}[{g1}-{g2}-{g3}]{Back.RESET}')
        time.sleep(random.uniform(.3, .7))
        print()
elif optn == 3:
    while True:
        system('CLS')
        logo()
        gen()
        g1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        g2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        g3 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

        print(f' ╚╡{Fore.LIGHTCYAN_EX}5K {Back.LIGHTGREEN_EX}{Fore.LIGHTWHITE_EX}[{g1}-{g2}-{g3}]{Back.RESET}')
        time.sleep(random.uniform(.3, .7))
        print()
else:
    while True:
        system('CLS')
        logo()
        gen()
        g1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        g2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        g3 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

        print(f' ╚╡{Fore.LIGHTCYAN_EX}10K {Back.LIGHTGREEN_EX}{Fore.LIGHTWHITE_EX}[{g1}-{g2}-{g3}]{Back.RESET}')
        time.sleep(random.uniform(.3, .7))
        print()