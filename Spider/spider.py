# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
Leetcode: @new92
PyPI: @new92
Contributors: [@Itsfizziks, @ProgramR4732]

Spider is a powerful tool used for gathering URLs from Instagram.
The source of the URLs are the captions of posts, URLs in users bios etc.

For output example >>> ./Photos/output.png

{*********IMPORTANT*********}
User's login credentials (such as: username, session file) won't be stored ! 
Will be used only for the purpose of Spider.
"""
try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[✘] Error ! Spider requires Python 3 ! ")
        sleep(1.3)
        print("""[+] Instructions to download Python 3: 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[+] Please install Python3 and then use Spider ✅")
        sleep(1)
        print("[+] Exiting...")
        sleep(0.8)
        sys.exit()
    import platform
    from rich.align import Align
    from rich.table import Table
    from rich.live import Live
    from rich.console import Console
    console = Console()
    mods = ('sys', 'time', 'platform', 'os', 'colorama', 'rich', 'logging', 'requests', 'instaloader', 'ctypes', 'csv', 'argparse', 're', 'prettytable')
    with console.status('[bold dark_orange]Loading module...[/]') as status:
        for mod in mods:
            sleep(0.85)
            console.log(f'[[bold red]{mod}[/]] => [bold green]okay ✔[/]')
    import instaloader
    import csv
    import argparse
    import ctypes
    import logging
    import requests
    import os
    import re
    from os import system
    from colorama import init, Fore
    from prettytable import PrettyTable
except (ImportError, ModuleNotFoundError):
    print("[!] WARNING: Not all packages used in Spider have been installed !")
    sleep(1.5)
    print("[+] Ignoring warning...")
    sleep(0.6)
    if sys.platform.startswith('linux') or sys.platform == 'darwin':
        if os.geteuid():
            print("[✘] Root user not detected !")
            sleep(1)
            print("[+] Attempting to enable root user...")
            sleep(1)
            os.execvp("sudo", ["sudo", sys.executable] + sys.argv)
            print("[✔] Done.")
            sleep(0.6)
            print("[+] Loading required modules...")
            sleep(0.4)
        system("sudo pip install -r ./../requirements.txt" if sys.platform.startswith('linux') else "python -m pip install ./../requirements.txt")
    elif platform.system() == 'Windows':
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("[✘] Root user not detected !")
            sleep(1)
            print("[+] Attempting to enable root user...")
            sleep(1)
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            if not ctypes.windll.shell32.IsUserAnAdmin():
                print("[+] Root user permission denied.")
                sleep(1)
                print("[+] Exiting...")
                sys.exit()
            print("[✔] Done.")
            sleep(0.6)
            print("[+] Loading required modules...")
            sleep(0.4)
        system("pip install -r ./../requirements.txt")

init(autoreset=True)
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.LIGHTYELLOW_EX
CYAN = Fore.LIGHTBLUE_EX

def clear():
    system('cls' if platform.system() == 'Windows' else 'clear')

sleep(0.8)
clear()
console.print("[bold green][✔] Successfully loaded modules.[/]")
sleep(0.8)
clear()

ANS = ('yes', 'no')
EMPTY = ('', ' ')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
js = ''
resp = requests.get('https://api.github.com/repos/new92/InstaTools', headers=headers)
if resp.status_code == 200:
    js = resp.json()

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))

def ScriptInfo():
    rest = requests.get('https://api.github.com/repos/new92/InstaTools/contributors', headers=headers)
    contribs = []
    if rest.status_code == 200:
        jsn = rest.json()
        contribs = [jsn[i]['login'] for i in range(len(jsn))]
    lang = requests.get('https://api.github.com/repos/new92/InstaTools/languages', headers=headers)
    languages = list(lang.json().keys()) if lang.status_code == 200 else []
    print(f"{YELLOW}[+] Author | {js['owner']['login']}")
    print(f"{YELLOW}[+] Github | @{js['owner']['login']}")
    print(f"{YELLOW}[+] Leetcode | @{js['owner']['login']}")
    print(f"{YELLOW}[+] PyPI | @{js['owner']['login']}")
    print(f"{YELLOW}[+] Contributors | {contribs}")
    print(f"{YELLOW}[+] License | {js['license']['spdx_id']}")
    print(f"{YELLOW}[+] Programming language(s) used | {languages}")
    print(f"{YELLOW}[+] Script's name | {js['name']}")
    print(f"{YELLOW}[+] Latest update | {js['updated_at']}")
    print(f"{YELLOW}[+] File size | {os.stat(__file__).st_size} bytes")
    print(f"{YELLOW}[+] File path | {os.path.abspath(__file__)}")
    print(f"{YELLOW}[+] Directory path | {os.path.dirname(os.path.abspath(__file__))}")
    print(f"{YELLOW}|======|GITHUB REPO INFO|======|")
    print(f"{YELLOW}[+] Repo name | {js['name']}")
    print(f"{YELLOW}[+] Description | {js['description']}")
    print(f"{YELLOW}[+] Repo URL | {js['html_url']}")
    print(f"{YELLOW}[+] Stars | {js['stargazers_count']}")
    print(f"{YELLOW}[+] Forks | {js['forks']}")
    print(f"{YELLOW}[+] Watchers | {js['subscribers_count']}")
    print(f"{YELLOW}[+] Open issues | {js['open_issues_count']}")

def banner() -> str:
    console.print("""[bold green]
   ▄████████    ▄███████▄  ▄█  ████████▄     ▄████████    ▄████████
  ███    ███   ███    ███ ███  ███   ▀███   ███    ███   ███    ███
  ███    █▀    ███    ███ ███▌ ███    ███   ███    █▀    ███    ███
  ███          ███    ███ ███▌ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀
▀███████████ ▀█████████▀  ███▌ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀  
         ███   ███        ███  ███    ███   ███    █▄  ▀███████████
   ▄█    ███   ███        ███  ███   ▄███   ███    ███   ███    ███
 ▄████████▀   ▄████▀      █▀   ████████▀    ██████████   ███    ███
                                                         ███    ███
[/]""", justify='center')
    
TABLE = (
    (
        "[b white]Author[/]: [i light_green]new92[/]",
        "[green]https://new92.github.io/[/]"
    ),
    (
        "[b white]Github[/]: [i light_green]@new92[/]",
        "[green]https://github.com/new92[/]"
    ),
    (
        "[b white]Leetcode[/]: [i light_green]@new92[/]",
        "[green]https://leetcode.com/new92[/]"
    ),
    (
        "[b white]PyPI[/]: [i light_green]@new92[/]",
        "[green]https://pypi.org/user/new92[/]"
    )
)

output = (os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Spider.csv')).replace('\\', '/')

def Uninstall() -> str:
    def rmdir(dire):
        for root, dirs, files in os.walk(dire):
            for file in files:
                os.remove(os.path.join(root,file))
            DIRS = (os.path.join(root, dir) for dir in dirs)
        for i in DIRS:
            os.rmdir(i)
        os.rmdir(dire)
    rmdir(fpath('InstaTools'))
    return f"{GREEN}[✔] Files and dependencies removed successfully !"

loader = instaloader.Instaloader()

global filter_urls, filter_referers
filter_urls, filter_referers = [], []

def crawl(target: str, counter: int):
    while True:
        if len(filter_urls) == counter:
            return
        profile = instaloader.Profile.from_username(loader.context, target) if target else 'cristiano'
        target = ''
        if re.search(r'https?://\S+', profile.biography):
            filter_urls.append(re.findall(r'https?://\S+', profile.biography))
            filter_referers.append(profile.username)
        for post in profile.get_posts():
            for liker in post.get_likes():
                if not liker.is_private:
                    target = liker.username
                    if re.search(r'https?://\S+', liker.biography):
                        filter_urls.append(re.findall(r'https?://\S+', liker.biography))
                        filter_referers.append(target)
            for comment in post.get_comments():
                if not comment.owner.is_private:
                    if not target:
                        target = comment.owner.username
                    if re.search(r'https?://\S+', comment.owner.biography):
                        filter_urls.append(re.findall(r'https?://\S+', comment.owner.biography))
                        filter_referers.append(comment.owner.username)

def main(username: str, session: str, target: str, counter: int):
    console = Console()
    table = Table(show_footer=False)
    centered = Align.center(table)
    clear()
    banner()
    print("\n")
    with Live(centered, console=console, screen=False):
        table.add_column('Socials', no_wrap=False)
        table.add_column('Url', no_wrap=False)
        for row in TABLE:
            table.add_row(*row)
    print("\n")
    console.print("[bold yellow][+] Spider is a powerful tool used for gathering URLs from Instagram.[/]")
    print("\n")
    console.print("[bold yellow][1] Extract URLs[/]")
    console.print("[bold yellow][2] Show Spider's info[/]")
    console.print("[bold yellow][3] Uninstall InstaTools[/]")
    console.print("[bold yellow][4] Exit[/]")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones) >>> "))
    while num not in range(1,5):
        print(f"{RED}[✘] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers >>> [1-4]")
        sleep(0.8)
        num=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones) >>> "))
    if num == 1:
        clear()
        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'consent.txt')):
            print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            con=input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? ").strip().lower()
            while con not in ANS or con in EMPTY:
                print(f"{RED}[✘] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
                sleep(1)
                con=input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? ").strip().lower()
            if con == ANS[0]:
                logging.basicConfig(
                    filename='consent.txt',
                    level=logging.INFO,
                    format='%(asctime)s [%(levelname)s]: %(message)s',
                    datefmt='%d-%m-%Y | %H:%M:%S'
                )
                logging.info('Yes I consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given Instagram account.')
            else:
                print(f"{YELLOW}[OK]")
                sleep(1)
                print(f"{YELLOW}[1] Exit")
                print(f"{YELLOW}[2] Uninstall Spider and exit")
                num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
                valErr = num in (1, 2)
                while not valErr:
                    try:
                        print(f"{YELLOW}[1] Exit")
                        print(f"{YELLOW}[2] Uninstall Spider and exit")
                        sleep(1)
                        num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
                        valErr = num in (1,2)
                    except ValueError:
                        print(f"{RED}[✘] Invalid number.")
                        sleep(1)
                        print(f"{GREEN}[+] Acceptable numbers >>> [1,2]")
                        sleep(1)
                if num == 1:
                    clear()
                    print(f"{RED}[+] Exiting...")
                    sleep(1)
                    sys.exit()
                else:
                    clear()
                    print(Uninstall())
                    sleep(2)
                    print(f"{RED}[+] Exiting...")
                    sleep(1)
                    print(f"{YELLOW}[+] Thank you for using Spider 🫡")
                    sleep(0.8)
                    print(f"{YELLOW}[+] Until we meet again 👋")
                    sleep(0.8)
                    sys.exit()
        sleep(1.4)
        clear()
        sleep(0.5)
        print(f"{GREEN}[*] Using session file >>> {session}...")
        sleep(1.3)
        try:
            with open(session, 'rb') as sessionfile:
                loader.context.load_session_from_file(username, sessionfile)
        except instaloader.exceptions.ConnectionException as ex:
            print(f"{RED}[✘] Error loading session file !")
            sleep(1)
            print(f"{YELLOW}[+] Error message >>> {ex}")
            sleep(0.8)
            print(f"{RED}[+] Exiting...")
            sys.exit()
        print(f"{GREEN}[✔] Session loaded successfully !")
        sleep(1.4)
        print(f"{GREEN}[✔] Login successfull !")
        sleep(0.85)
        clear()
        sleep(0.4)
        print(f"{CYAN}[*] Starting gathering process...")
        sleep(0.5)
        crawl(target, counter)
        sleep(0.5)
        print(f"{GREEN}[✔] Success.")
        sleep(0.4)
        print(f"{CYAN}[*] Spider found {len(filter_urls)} urls.")
        sleep(0.7)
        clear()
        sleep(0.5)
        print(f"{CYAN}[*] Filtering results...")
        sleep(0.4)
        counters = [filter_urls.count(url) for url in filter_urls]
        vers, fols, folls, posts = [], [], [], []
        for i in range(len(filter_referers)):
            profile = instaloader.Profile.from_username(loader.context, filter_referers[i])
            vers.append(profile.is_verified)
            fols.append(profile.followers)
            folls.append(profile.followees)
            posts.append(profile.mediacount)
        table = PrettyTable()
        table.field_names = ['URL', 'Appearances', 'Referer', 'Verified', 'Followers', 'Followings', 'Posts']
        for i in range(len(filter_referers)):
            table.add_row(row=[filter_urls[i], counters[i], filter_referers[i], vers[i], fols[i], folls[i], posts[i]])
        sleep(0.5)
        print(f"{GREEN}[✔] Success.")
        sleep(0.5)
        clear()
        print(f"{YELLOW}{table}")
        sleep(4)
        print(f"\n\n{GREEN}[*] Writing results to csv file...")
        sleep(0.4)
        L = [
            ['URL', 'Appearances', 'Referer', 'Verified', 'Followers', 'Followings', 'Posts']
        ]
        for i in range(len(filter_referers)):
            L.append([filter_urls[i], counters[i], filter_referers[i], vers[i], fols[i], folls[i], posts[i]])
        with open(output, 'w', newline='') as csvf:
            writer = csv.writer(csvf)
            writer.writerows(L)
        print(f"{GREEN}[✔] Done. Saved data at >>> {output}")
        sleep(0.5)
    
    elif num == 2:
        clear()
        ScriptInfo()
        sleep(5)
    
    elif num == 3:
        clear()
        print(Uninstall())
        sleep(1)
        print(f"{GREEN}[+] Thank you for using Spider 😁")
        sleep(0.8)
        print(f"{GREEN}[+] Until next time 👋")
        sleep(0.8)
        sys.exit()
    
    else:
        clear()
        print(f"{GREEN}[+] Thank you for using Spider 😁")
        sleep(0.8)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(0.8)
        sys.exit()
    
    print(f"\n\n{YELLOW}[1] Return to menu\n{YELLOW}[2] Exit")
    number=int(input(f"{YELLOW}[::] Please enter a number (from the above ones) >>> "))
    while number not in range(1,3):
        print(f"{RED}[✘] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers >>> [1,2]")
        sleep(1)
        number=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones) >>> "))
    if number == 1:
        clear()
        main(username, session, target, counter)
    else:
        clear()
        print(f"{RED}[+] Exiting...")
        sleep(1)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(1)
        sys.exit()

try:
    if __name__ == '__main__':
        sleep(2)
        clear()
        parser = argparse.ArgumentParser(description='Spider is a powerful tool used for gathering URLs from Instagram.')
        parser.add_argument('-u', '--username', help='Your instagram username.')
        parser.add_argument('-s', '--session', help='The session file to use. To generate it >> python3 cookies.py')
        parser.add_argument('-c', '--counter', help='The number of URLs to obtain.')
        parser.add_argument('-t', '--target', help='The starter username.')
        args = parser.parse_args()
        if len(sys.argv) < 5:
            print(f"{RED}[✘] Error: Missing arguments.")
            sleep(0.7)
            print(f"{GREEN}[+] Usage >>> python3 spider.py -u <your_username> -s <path_to_session_file> -c <number_of_urls> -t <target_username>")
            sleep(1.5)
            args.username=input(f"{YELLOW}[::] Please enter your username >>> ") if not args.username else args.username
            args.session=input(f"{YELLOW}[::] Please enter the session file >>> ") if not args.session else args.session
            args.counter=input(f"{YELLOW}[::] Please enter the number of URLs to extract >>> ") if not args.counter else args.counter
            args.target=input(f"{YELLOW}[::] Please enter the target username >>> ") if not args.target else args.target
        main(args.username.strip().lower(), args.session.strip().replace('\\', '/'), args.target.strip().lower(), int(args.counter))
except (KeyboardInterrupt, EOFError):
    print(f"\n\n{RED}[*] <Ctrl + C> detected. Exiting safely...")
    sys.exit()