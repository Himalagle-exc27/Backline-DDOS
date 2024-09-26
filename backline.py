import sys,os
from colorama import Fore

print(Fore.MAGENTA+"""
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
__ )    \     ___| |  / |    _ _|  \  | ____|     __ \  __ \   _ \   ___|
 __ \   _ \   |     ' /  |      |    \ | __|       |   | |   | |   |\___ \
 |   | ___ \  |     . \  |      |  |\  | |  _____| |   | |   | |   |      |
____/_/    _\\____|_|\_\_____|___|_| \_|_____|    ____/ ____/ \___/ _____/
                                                                                                                   
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
                                                                 
BY: Himalaglebruhv
""")

def display_menu():
    print(Fore.GREEN + """
    1: Backline Tools (Hacking Tools)      | 2: Backline-Paid-Tools
    3: Info (about-us)
    """)

def execute_command(command):
    if command == '1':
        os.system('cmd /k "python Backline-Tool/backline-tool.py"' if os.name == 'nt' else 'python Backline-Tool/backline-tool.py')
    elif command == '2':
        print(Fore.RED + 'This option is not available yet! Coming soon...')
        #os.system('cmd /k "python Backline-Web-Hacktool/web_bugger.py"')
    elif command == '3':
        os.system('cmd /k "python info.py"' if os.name == 'nt' else 'python info.py')

        display_menu()
    else:
        print('Invalid option! Please choose the correct one.')

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)