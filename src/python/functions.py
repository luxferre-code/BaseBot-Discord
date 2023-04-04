from colorama import Fore, init

init(autoreset=True)

def logger(message, type="INFO"):
    if(type == "INFO"):
        print(Fore.GREEN + "[INFO] " + message + Fore.RESET)
    elif(type == "WARNING"):
        print(Fore.YELLOW + "[WARNING] " + message + Fore.RESET)
    elif(type == "ERROR"):
        print(Fore.RED + "[ERROR] " + message + Fore.RESET)
    else:
        print(Fore.CYAN + "[DEBUG] " + message + Fore.RESET)