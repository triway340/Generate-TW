import random, string
import platform
import time
import os
try:
        from colorama import init, Fore
except ModuleNotFoundError:
        if platform.system() == "Windows":
                print("\nEsto instalacion pasa una vez...\n")
                os.system("pip install requests")
                os.system("pip install colorama")
        else:
                print("\nEsta instalacion pasa una vez...\n")
                os.system("apt install python3 -y")
                os.system("python3 -m pip install colorama")
                os.system("python3 -m pip install requests")
RED = Fore.RED
BLUE = Fore.BLUE
CYAN = Fore.CYAN
RESET = Fore.WHITE
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
def clear():
        if platform.system() == "Windows":
                os.system("cls")
        else:
                os.system("clear")
clear()
def magic(numbers):
        f = open("Codes.txt", "w", encoding="utf-8")
        for n in range(int(numbers)):
                y = "".join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
                f.write("https://discod.gift/")
                f.write(y)
                f.write("\n")
        f.close()
def home():
        while True:
                init(autoreset=False)
                print(f"\n\n{RESET}--{YELLOW}Nitro unchecked{RESET}--\n")
                print(f"""
{BLUE}[ {CYAN}1 {BLUE}] {RESET}- {CYAN}Generar Codes Unchecked
{BLUE}[ {CYAN}X {BLUE}] {RESET}- {CYAN}Salir{RESET}
""")
                peticion = input("Ingrese una opcion ---> ")
                print()
                if peticion=="1":
                        try:
                                numbers = int(input("\nIngrese cuantos quieres generar >>> "))
                                print()
                                time.sleep(1)
                                magic(numbers)
                        except:
                                print(f"'\n{GREEN}Ha ocurrido un {RED}error{GREEN}, lo lamentamos...")
                                print(f"\nVuelva a ejecutar el script...{RESET}")
                                exit()
                        print(f"\n{GREEN}Bien se han guardado: {BLUE}{numbers} codes unchecked en: {BLUE}Codes.txt{RESET}\n")
                        print(f"\t--{YELLOW}AVISO{RESET}--\n{GREEN}Si vuelves a {RED}generar codes{GREEN}, se {RED}borraran {GREEN}los que anteriormente has usado.\n{RESET}")
                        time.sleep(15)
                elif peticion=="X" or peticion=="x":
                        print(f"{GREEN}Okey saliendo...")
                        time.sleep(1)
                        print(f"\n¡ADIOS!{RESET}")
                        exit()
                else:
                        print(f"{GREEN}Opcion {RED}incorrecta{GREEN}...")
                        time.sleep(1)
                        print(f"\n{GREEN}Vuelva a intentarlo...")
                        time.sleep(8)
home()
