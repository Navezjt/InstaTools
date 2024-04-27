# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
Leetcode: @new92
PyPI: @new92
Contributors: [@Itsfizziks, @ProgramR4732]

Kratos is a powerful tool designed to hunt down accounts owned by gay people on Instagram.

For short code example >>> ./Photos/short_code_example.png

For output example >>> ./Photos/output.jpg

{*********IMPORTANT*********}
User's login credentials (such as: username, session file) won't be stored ! 
Will be used only for the purpose of Kratos.
"""
try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[✘] Error ! Kratos requires Python 3 ! ")
        sleep(1.3)
        print("""[+] Instructions to download Python 3: 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[+] Please install Python3 and then use Kratos ✅")
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
    mods = ('sys', 'time', 'platform', 'os', 'colorama', 'rich', 'logging', 'requests', 'instaloader', 'ctypes', 'csv', 'argparse')
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
    from os import system
    from colorama import init, Fore
    from prettytable import PrettyTable
except (ImportError, ModuleNotFoundError):
    print("[!] WARNING: Not all packages used in Kratos have been installed !")
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
                                                  :
 G:                                               t#,              .
 E#,    : j.                                     ;##W.            ;W
 E#t  .GE EW,                    .. GEEEEEEEL   :#L:WE           f#E
 E#t j#K; E##j                  ;W, ,;;L#K;;.  .KG  ,#D        .E#f 
 E#GK#f   E###D.               j##,    t#E     EE    ;#f      iWW;  
 E##D.    E#jG#W;             G###,    t#E    f#.     t#i    L##Lffi
 E##Wi    E#t t##f          :E####,    t#E    :#G     GK    tLLG##L 
 E#jL#D:  E#t  :K#E:       ;W#DG##,    t#E     ;#L   LW.      ,W#i  
 E#t ,K#j E#KDDDD###i     j###DW##,    t#E      t#f f#:      j#E.   
 E#t   jD E#f,t#Wi,,,    G##i,,G##,    t#E       f#D#;     .D#j     
 j#t      E#t  ;#W:    :K#K:   L##,    t#E        G#t     ,WK,      
  ,;      DWi   ,KK:  ;##D.    L##,     fE         t      EG.       
                      ,,,      .,,       :                ,     
[/]""")

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

output = (os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Kratos.csv')).replace('\\', '/')
terms = ['🏳️‍🌈', '🏳️‍⚧️', '🌈', 'gay', 'bi', 'trans', "in a man's body", "in a woman's body", '👩‍❤️‍💋‍👩', '💏', '👨‍❤️‍💋‍👨', '👨‍❤️‍👨', '💑', '👩‍❤️‍👩', '👭', '👬', 'non binary']

def analyze(username: str, session: str) -> list:
    loader = instaloader.Instaloader()
    sleep(0.5)
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
    print(f"{GREEN}[*] Analyzing...")
    sleep(0.6)
    with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shortcodes.txt')).replace('\\', '/'), 'r', encoding='utf-8') as codes:
        L = [code.replace('\n') for code in codes]
    cluster = []
    for i in range(len(L)):
        post = instaloader.Post.from_shortcode(loader.context, L[i])
        capture, container = [liker.username for liker in post.get_likes() if not liker.is_private] + [comment.owner.username for comment in post.get_comments() if not comment.owner.is_private], []
        if capture:
            for pred in capture:
                profile = instaloader.Profile.from_username(loader.context, pred)
                for term in terms:
                    if term in str(profile.full_name) or term in str(profile.biography) or term in str(profile.username):
                        container.append(pred)
                for follower in profile.get_followers():
                    for term in terms:
                        if term in str(follower.full_name) or term in str(follower.biography) or term in str(follower.username):
                            container.append(follower.username)
                for followee in profile.get_followees():
                    for term in terms:
                        if term in str(followee.full_name) or term in str(followee.biography) or term in str(followee.username):
                            container.append(followee.username)
                if container:
                    print(f"{CYAN}[*] Extracted {len(container)} gays so far...")
        else:
            print(f"{RED}[✘] Error: No likers/commenters with public profile found on {L[i]} post.")
            if i == len(L) - 1:
                if not container:
                    print(f"{RED}[✘] Error: Kratos was unable to find gay accounts in the posts with the given shortcodes.")
                    sleep(1.3)
                    print(f"{RED}[+] Exiting...")
                    sys.exit()
            else:
                print(f"{YELLOW}[*] Next post to check on >>> {L[i+1]}...")
        cluster.append(container)
    users, vers, fols, folls, posts = [], [], [], [], []
    if cluster:
        for container in cluster:
            for username in container:
                users.append(username)
    if users:
        for user in users:
            profile = instaloader.Profile.from_username(loader.context, user)
            if profile.is_verified:
                vers.append(profile.username)
            fols.append(profile.followers)
            folls.append(profile.followees)
            posts.append(profile.mediacount)
        vers.extend([''] * (len(container) - len(vers)))
    return users, vers, fols, folls, posts

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

def main(username: str, session: str, count: int):
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
    console.print("[bold yellow][+] Kratos is a powerful tool designed to hunt down gay accounts on Instagram.[/]")
    print("\n")
    console.print("[bold yellow][1] Uncover gay accounts[/]")
    console.print("[bold yellow][2] Show Kratos's info[/]")
    console.print("[bold yellow][3] Add keywords to the keywords list[/]")
    console.print("[bold yellow][4] Uninstall InstaTools[/]")
    console.print("[bold yellow][5] Exit[/]")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones) >>> "))
    while num not in range(1,6):
        print(f"{RED}[✘] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers >>> [1-5]")
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
                print(f"{YELLOW}[2] Uninstall Kratos and exit")
                num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
                valErr = num in (1, 2)
                while not valErr:
                    try:
                        print(f"{YELLOW}[1] Exit")
                        print(f"{YELLOW}[2] Uninstall Kratos and exit")
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
                    print(f"{YELLOW}[+] Thank you for using Kratos 🫡")
                    sleep(0.8)
                    print(f"{YELLOW}[+] Until we meet again 👋")
                    sleep(0.8)
                    sys.exit()
        captured, vers, fols, folls, posts = analyze(username, session)
        if captured:
            table = PrettyTable()
            table.field_names = ['Gays', 'Verified', 'Followers', 'Followings', 'Posts']
            for i in range(len(captured)):
                table.add_row(row=[captured[i], vers[i], fols[i], folls[i], posts[i]])
            sleep(0.5)
            print(f"{GREEN}[✔] Success.")
            sleep(0.5)
            print(f"{YELLOW}[+] Total gays extracted >>> {len(captured)}")
            sleep(0.4)
            print(f"{YELLOW}[+] Verified accounts >>> {len(vers)}")
            sleep(1.5)
            clear()
            print(f"{YELLOW}{table}")
            L = [
                ['Total gays', 'Total verified'],
                [len(captured), len(vers)],
                ['Gays', 'Verified', 'Followers', 'Followings', 'Posts']
            ]
            for i in range(len(captured)):
                L.append([captured[i], vers[i], fols[i], folls[i], posts[i]])
            with open(output, 'w') as file:
                writer = csv.writer(file)
                writer.writerows(L)
            sleep(1)
            print("\n\n")
            print(f"{GREEN}[✔] Successfully saved data at >>> {output}")
        else:
            print(f"{RED}[✘] Error: Kratos was unable to find gays through the specific post(s). Please check the shortcodes and try again.")
            sleep(1.7)
            print(f"{RED}[+] Exiting...")
            sys.exit()

    elif num == 2:
        clear()
        ScriptInfo()
        sleep(5)
    
    elif num == 3:
        clear()
        print(f"{CYAN}[*] Current search terms list >>> {terms}")
        sleep(5)
        num=int(input(f"{YELLOW}[::] Number of keywords to insert >>> "))
        while num < 1:
            print(f"{RED}[✘] Invalid number !")
            sleep(0.5)
            num=int(input(f"{YELLOW}[::] Number of keywords to insert >>> "))
        counter = 0
        for i in range(num):
            term = input(f"{YELLOW}[::] Enter keyword No{i+1} >>> ").strip().lower()
            if not term in terms:
                terms.append(term)
                counter += 1
            else:
                print(f"{RED}[✘] Keyword already in search terms !")
        sleep(0.5)
        print(f"{GREEN}[✔] Successfully inserted {counter} keywords inside the search terms list.")
        sleep(0.8)

    elif num == 4:
        clear()
        print(Uninstall())
        sleep(2)
        print(f"{GREEN}[+] Thank you for using Kratos 😁")
        sleep(0.8)
        print(f"{GREEN}[+] Until next time 👋")
        sleep(0.8)
        sys.exit()

    else:
        clear()
        print(f"{GREEN}[+] Thank you for using Kratos 😁")
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
        main(username, session, count)
    else:
        clear()
        print(f"{RED}[+] Exiting...")
        sleep(0.8)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(0.8)
        sys.exit()
try:
    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='Kratos is a powerful tool designed to hunt down accounts owned by gay people on Instagram.')
        parser.add_argument('-u', '--username', help='The username of your Instagram account.')
        parser.add_argument('-c', '--count', help='Number of gays the reveal.')
        parser.add_argument('-s', '--session', help='The path to the session file. To generate it >>> python3 cookies.py')
        args = parser.parse_args()
        if len(sys.argv) < 4:
            print(f"{RED}[✘] Error: Missing arguments.")
            sleep(0.7)
            print(f"{GREEN}[+] Usage >>> python3 kratos.py -u <your_username> -c <integer> -s <path_to_session_file>")
            sleep(1.5)
            args.username=input(f"{YELLOW}[::] Please enter your username >>> ") if not args.username else args.username
            args.session=input(f"{YELLOW}[::] Please enter the path to the session file >>> ") if not args.session else args.session
            args.count=input(f"{YELLOW}[::] Please enter the number of gays to reveal >>> ") if not args.count else args.count
        main(args.username.strip().lower(), args.session.strip().replace('\\', '/'), int(args.count))
except (KeyboardInterrupt, EOFError):
    print(f"\n\n{RED}[*] <Ctrl + C> detected. Exiting safely...")
    sys.exit()