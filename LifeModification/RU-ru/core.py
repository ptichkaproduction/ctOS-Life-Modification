#! configs/system.cfg python
# -*- coding: utf-8 -*-
#OPERATING SYSTEM ctOS
import os
import time
from datetime import datetime
import platform
class TextColor:
    # ANSI escape codes for text colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'  # Reset color

com = str("")
start = "false"
user = "User"
clean = ""
syst = ""
buffer = ""
buffer2 = ""
count = 1
security = ""
passwd = "c650"
accessDenied = TextColor.RED + "У вас нет разрешения на выполнение этой операции!" + TextColor.RESET
rootAttention = TextColor.RED + "<<===========================================>>\n|| ATTENTION! We are not responsible for all ||\n|| Your actions in this user! Be careful!    ||\n<<===========================================>>"+TextColor.RESET

ver = TextColor.RED + "╔╗  ╔══╗╔══╗╔═══╗   ╔╗  ╔╗╔══╗╔══╗ ╔══╗╔══╗╔══╗╔══╗╔══╗╔════╗╔══╗╔══╗╔╗ ╔╗\n║║  ╚╗╔╝║╔═╝║╔══╝   ║║  ║║║╔╗║║╔╗╚╗╚╗╔╝║╔═╝╚╗╔╝║╔═╝║╔╗║╚═╗╔═╝╚╗╔╝║╔╗║║╚═╝║\n" + TextColor.GREEN + "║║   ║║ ║╚═╗║╚══╗   ║╚╗╔╝║║║║║║║╚╗║ ║║ ║╚═╗ ║║ ║║  ║╚╝║  ║║   ║║ ║║║║║╔╗ ║\n║║   ║║ ║╔═╝║╔══╝   ║╔╗╔╗║║║║║║║ ║║ ║║ ║╔═╝ ║║ ║║  ║╔╗║  ║║   ║║ ║║║║║║╚╗║\n" + TextColor.BLUE + "║╚═╗╔╝╚╗║║  ║╚══╗   ║║╚╝║║║╚╝║║╚═╝║╔╝╚╗║║  ╔╝╚╗║╚═╗║║║║  ║║  ╔╝╚╗║╚╝║║║ ║║\n╚══╝╚══╝╚╝  ╚═══╝   ╚╝  ╚╝╚══╝╚═══╝╚══╝╚╝  ╚══╝╚══╝╚╝╚╝  ╚╝  ╚══╝╚══╝╚╝ ╚╝\n\n" + TextColor.CYAN + "<<==========>>        <<==========>>\n||" +TextColor.RESET + " ctOS 0.9 " +TextColor.CYAN + "||" +TextColor.GREEN + " Release candidate! " + TextColor.CYAN + "||\n" +TextColor.CYAN + "||" +TextColor.RESET +" Life modification (ver 0.9)    " + TextColor.CYAN + "||\n" + TextColor.CYAN + "||" +TextColor.RESET +" Modified by PerryTheBalloon    " + TextColor.CYAN + "||\n||" +TextColor.RESET +" AshotCoins Inc.                " + TextColor.CYAN + "||\n" + TextColor.CYAN + "<<==========>>        <<==========>>\n" +TextColor.RESET

#O_o

if platform.system() == "Windows":
    clean = "cls"
    syst = "| base system: WINDOWS |"
elif platform.system() == "Linux" or platform.system() == "Darwin":
    clean = "clear"
    syst = "| base system: LINUX   |"      
os.system(clean)   
print("Starting.")
time.sleep(0.2)
os.system(clean)
print("Starting..")
time.sleep(0.2)
os.system(clean)
print("Starting...")
time.sleep(0.2)                #основа
settings = open("LifeModification/configs/build.cfg", "r")
if (settings == ''):
    settings = 700                                #основа
settings = open("LifeModification/configs/build.cfg", "r")
build = int(settings.read())
build += 1
settings.close()
set = open("LifeModification/configs/build.cfg", "w")
set.write(str(build))
if(syst == "| base system: LINUX   |"):
    os.system("python3 LifeModification/bootanimation.py")
if(syst == "| base system: WINDOWS |"):
    os.system("python LifeModification/bootanimation.py")
print("ok")
cuser = open("LifeModification/configs/user.cfg", "r")
buffer = cuser.readline()
fix = len(buffer)
user = buffer[:fix-1]
buser = user
buffer3 = cuser.readline()
fix = len(buffer3)
years = buffer3[:fix-1]
city = cuser.readline()
cuser.close()
time.sleep(0.1)
start = "true"
os.system(clean)
comlog = open("LifeModification/logs/comlog.txt", "w")
buflog = open("LifeModification/logs/buflog.txt", "w")
print(ver)
while(start == "true"):
    times = datetime.today()
    if(buffer != ""):
        buflog.writelines(str(times) + " buffer: " + str(buffer) + "\n")
    if(buffer2 != ""):
        buflog.writelines(str(times) + " buffer2: " + str(buffer2) + "\n")
    buffer = ""
    buffer2 = ""
    time1 = datetime.now()
    pwd = os.getcwd()
    print(" ╭──[" + TextColor.GREEN +  user + TextColor.BLUE + "@lifeMod" + TextColor.RESET +"]────["+TextColor.YELLOW + str(time1) + TextColor.RESET +"]────["+ TextColor.RED + str(build) + TextColor.RESET +"]")
    print("["+str(count)+"]")
    com = input(" ╰──["+ TextColor.GREEN + pwd + TextColor.RESET +"]──>$ ")
    buffer = ""
    buffer2 = ""
    count += 1
    comlog.writelines(str(times) + ": " + com + "\n")

    #Control Panel (Useless...)

    if (com == 'control'):
        print(TextColor.CYAN + "\n<<=================>>" + TextColor.RESET)
        print(TextColor.CYAN + "||" + TextColor.RESET + "  Control panel  " + TextColor.CYAN + "||" + TextColor.RESET)
        print(TextColor.CYAN + "<<=================>>" + TextColor.RESET)
        print("1. Сменить язык")
        print("2. Настройки пользователей")
        print("3. Install/update modules")
        print("4. Сделать заводской сброс")
        print("5. On/off title screen")
        print("6. О системе")
        print("   Или нажмите Enter для выхода")
        buffer = input(TextColor.YELLOW + "Выбор действия: " + TextColor.RESET)
        if(buffer == "1"):
            print("")
            print(TextColor.YELLOW + "Хотите сменить язык системы? ")
            print(TextColor.CYAN + "<<================================>>" + TextColor.RESET)
            query = input(TextColor.YELLOW + "Do you want to change the system language?" + TextColor.RESET + " ("+ TextColor.GREEN + "Y" + TextColor.RESET + "/" + TextColor.RED + "n" + TextColor.RESET + ") ")
            print("")
            if(query == "Y" or query == "y"):
                lang = open("LifeModification/configs/lang.cfg", "r")
                buffer = lang.read()
                lg = ""
                if(buffer == "eng"):
                    lg = "eng"
                if(buffer == "rus"):
                    lg = "rus"
                    lang.close()
                langed = open("LifeModification/configs/lang.cfg", "w")
                if(lg == "eng"):
                    langed.write("rus")
                if(lg == "rus"):
                    langed.write("eng")
                    print(TextColor.GREEN + "Язык системы изменён, перезапустите систему для применения параметров." + TextColor.RESET)
                    print(TextColor.CYAN + "<<================================>>" + TextColor.RESET)
                    print(TextColor.GREEN + "The system language has been changed, restart the system to apply the settings." + TextColor.RESET)
            if(query == "n" or query == "N"):
                print(TextColor.YELLOW + "Exiting..." + TextColor.RESET)
        if(buffer == "2"):
            print("")
            print(TextColor.CYAN + "<<======== Users ========>>" + TextColor.RESET)
            print(TextColor.GREEN + buser +TextColor.RESET)
            print(TextColor.RED + "ROOT ()" + TextColor.RESET)
            print(TextColor.CYAN + "<<============       ===========>>" + TextColor.RESET)
            print("")
            print("Possible actions:")
            print("1. View user information")
            print("2. Change username")
            print("   Or press any key or enter to exit")
            buffer = input(TextColor.YELLOW + "Select action: " + TextColor.RESET)
            if(buffer == "1"):
                print("")
                buffer = input(TextColor.YELLOW + "Enter the desired username: " + TextColor.RESET)
                if (buffer == buser):
                    print(TextColor.CYAN + "<<================>>" + TextColor.RESET)
                    print("Username: " + user)
                    print(years + " yrs")
                    print("City: " + city)
                    print(TextColor.CYAN + "<<================>>" + TextColor.RESET)
            if(buffer == "2"):
                print(TextColor.YELLOW + "Changing username:" + TextColor.RESET)
                print("")
                user = open("LifeModification/configs/user.cfg", "w")
                buffer = input("Enter your username: ")
                user.write(buffer + "\n")
                user.close()
                cuser = open("LifeModification/configs/user.cfg", "r")
                buffer = cuser.readline()
                fix = len(buffer)
                user = buffer[:fix-1]
                buser = user
                cuser.close()
                time.sleep(0.3)
                print(TextColor.GREEN + "Done" + TextColor.RESET)
        if(buffer == "3"):
            if(syst == "| base system: LINUX   |"):
                os.system("python3 LifeModification/ObPy.py")
            if(syst == "| base system: WINDOWS |"):
                os.system("python LifeModification/ObPy.py")
        if(buffer == "4"):
            fcheck = open("LifeModification/configs/oobe.cfg", "w")
            fcheck.write("true")
            fcheck.close()
            user = open("LifeModification/configs/user.cfg", "w")
            user.write("")
            os.system(clean)
            print("Reset.")
            time.sleep(0.5)
            os.system(clean)
            print("Reset..")
            time.sleep(0.5)
            os.system(clean)
            print("Reset...")
            time.sleep(0.5)
            os.system(clean)
            print("Reset...Done!")
            time.sleep(0.5)
            start = "false"
            os.system(clean)
            time.sleep(0.1)
            start = "false"
            os.system(clean)
            time.sleep(0.5)
            os.system("python ctOS.py")
        if(buffer == "5"):
            title = open("LifeModification/configs/title.cfg", "r")
            buffer = title.read()
            ttl = ""
            if(buffer == "true"):
                ttl = "true"
            if(buffer == "false"):
                ttl = "false"
                title.close()
            titled = open("LifeModification/configs/title.cfg", "w")
            if(ttl == "true"):
                titled.write("false")
                print("Off")
                titled.close()
            if(ttl == "false"):
                titled.write("true")
                print("On")    
                titled.close()
        if(buffer == "6"):
            if(syst == "| base system: LINUX   |"):
                os.system("python3 LifeModification/vers.py")
            if(syst == "| base system: WINDOWS |"):
                os.system("python LifeModification/vers.py")


    if (com == "pip"):
        buffer = input("Enter function for pip: ")
        if(syst == "| base system: LINUX   |"):
            os.system("python3 -m pip " + buffer)
        if(syst == "| base system: WINDOWS |"):
            os.system("python -m pip " + buffer)

    if(com == "pacman"):
        com = input("Enter command: ")
        if (com == "install"):
            file_name = input("Enter file name for install package: ")
            file = open(file_name, "r", encoding="utf8")
            buffer6 = file.readline(100)
            fix = len(buffer6)
            buffer7 = buffer6[:fix-1]
            buffer5 = file.read()
            print(TextColor.CYAN + "<<================>>" + TextColor.RESET)
            print("Package name: " + buffer7)
            print(TextColor.CYAN + "<<================>>" + TextColor.RESET)
            package = open(buffer7, "w", encoding="utf8")
            package.write(buffer5)
            package.close()
            file.close()


        if(com == "new-package"):       
            file_name = input("Enter a file name to convert to an installation package file: ")
            file = open(file_name, "r")
            buffer1 = file.read()
            backup_name = input("Enter the filename of the installation package, but DO NOT USE THE FILE EXTENSION!!!!!! ")
            backup = open(backup_name + ".ct", "w")
            backup.writelines(file_name + "\n")
            backup.write(buffer1)
            file.close()
            backup.close()

    if(com == "dev"):
        if(user == "ROOT"):
            print(TextColor.CYAN + "<<===================>>" + TextColor.RESET)
            print(TextColor.CYAN + "||" + TextColor.RESET + " ctOS              " + TextColor.CYAN + "||" + TextColor.RESET)
            print(syst)
            print(TextColor.CYAN + "||" + TextColor.RESET + " Build: " + str(build)  + TextColor.CYAN + "        ||" + TextColor.RESET)
            print(TextColor.CYAN + "<<===================>>" + TextColor.RESET)
        if(user != "ROOT"):
            print(accessDenied)
    if(com == "cd"):
        buffer = input("Enter the name folder or leave the field blank to go to the root folder: ")
        if (buffer != ""):
            os.chdir(buffer)
        if (buffer == ""):
            os.chdir("../")

            #Working with users

    if(com == "usr edit" or com == "user edit"):
        print(TextColor.YELLOW + "User information edit:" + TextColor.RESET)
        print("")
        user = open("LifeModification/configs/user.cfg", "w")
        buffer = input("Enter your username: ")
        user.write(buffer + "\n")
        buffer = input("Enter your years old: ")
        user.write(buffer + "\n")
        buffer = input("Enter your city: ")
        user.write(buffer)
        user.close()
        cuser = open("LifeModification/configs/user.cfg", "r")
        buffer = cuser.readline()
        fix = len(buffer)
        user = buffer[:fix-1]
        buser = user
        buffer3 = cuser.readline()
        fix = len(buffer3)
        years = buffer3[:fix-1]
        city = cuser.readline()
        cuser.close()
        time.sleep(0.3)
        print("")
        print(TextColor.GREEN + "Done!" + TextColor.RESET)
        print("")

    if(com == "usr info" or com == "user info"):
        print("Выберите пользователя для вывода информации о нем: ")
        print("")
        print(TextColor.CYAN + "<<== Пользователи ==>>" + TextColor.RESET)
        print(TextColor.GREEN + buser + TextColor.RESET)
        print(TextColor.RED + "ROOT" + TextColor.RESET)
        print(TextColor.CYAN + "<<===>>         <<==>>" + TextColor.RESET)
        buffer = input("")
        if (buffer == buser):
            print(TextColor.CYAN + "<<================>>" + TextColor.RESET)
            print("Name: " + buser)
            print(years + " years old")
            print("City: " + city)
            print(TextColor.CYAN + "<<================>>" + TextColor.RESET)

    if (com == "usr switch" or com == "user switch" or com == "usr change" or com == "user change"):
        print("Select username:")
        print(TextColor.CYAN + "<<========== Users ==========>>" + TextColor.RESET)
        print(TextColor.GREEN + buser +TextColor.RESET)
        print(TextColor.RED + "ROOT (All permissions OS)" + TextColor.RESET)
        print(TextColor.CYAN + "<<===========================>>" + TextColor.RESET)
        print("")
        print(TextColor.YELLOW + "Cancel (type 'back')" + TextColor.RESET)
        buffer = input()
        if(buffer == "ROOT" or buffer == "root" or buffer == "Root"):
            buffer2 = input(TextColor.YELLOW + "Enter password: " + TextColor.RESET)
            if (buffer2 == passwd):
                user = "ROOT"
                print(rootAttention)
                time.sleep(0.5)
                print(TextColor.GREEN + "Complete" +TextColor.RESET)
                print("")
            if (buffer2 != passwd):
                print(TextColor.RED + "Password incorrect. Try Again" +TextColor.RESET)
                print("")
        if(buffer == buser):
            user = buser
            time.sleep(0.5)
            print(TextColor.GREEN + "Complete" +TextColor.RESET)

    if(com == "usr list"):
        print("")
        print(TextColor.CYAN + "<<========== Users ==========>>" + TextColor.RESET)
        print(TextColor.GREEN + buser +TextColor.RESET)
        print(TextColor.RED + "ROOT (All permissions OS)" + TextColor.RESET)
        print(TextColor.CYAN + "<<===========================>>" + TextColor.RESET)
        print("")

        #Working with files

    if(com == "ls"):
        if(user != "ROOT"):                                             #Простое разрешение [заметка для разработчика]
            print(accessDenied)
        if(user == "ROOT"):
            print(TextColor.CYAN + "<<========================================>>" + TextColor.RESET)
            buffer = os.listdir(pwd)
            print(buffer)
            print(TextColor.CYAN + "<<========================================>>"+ TextColor.RESET)

    if(com == "openpy"):
        buffer = input("Enter the path to the file or file name: ")
        if(syst == "| base system: LINUX   |"):
            os.system("python3 " + buffer)
        if(syst == "| base system: WINDOWS |"):
            os.system(buffer)

    if(com == "cfile"):
        if(user != "ROOT"):
            print(accessDenied)
        if(user == "ROOT"):
            buffer = input("Enter old path file: ")
            buffer2 = input("Enter new path file: ")
            os.replace(buffer, buffer2)

    if(com == "fi"):
        if(user == "ROOT"):
            buffer = input("Enter file: ")
            open(buffer, "r")
            print(TextColor.CYAN + "<<==================>>" + TextColor.RESET)
            buffer2 = os.stat(buffer)
            print(buffer2)
            print(TextColor.CYAN + "<<====================>>" + TextColor.RESET)
            print("st_size — file size in bytes")
            print("st_atime — last access time in seconds (timestamp)")
            print("st_mtime — last modified time")
            print("st_ctime — on Windows, this is the time the file was created, and on Linux, the time the metadata was last modified")
            print(TextColor.CYAN + "<<====================>>" + TextColor.RESET)
        if(user != "ROOT"):
            print(accessDenied)

    if(com == "df"):
        if(user != "ROOT"):
            print(accessDenied)
        if(user == "ROOT"):
            buffer = input("Enter file: ")
            os.remove(buffer)

    if(com == "renf"):
        if(user != "ROOT"):
            print(accessDenied)
        if(user == "ROOT"):
            buffer = input("Enter file: ")
            buffer2 = input("Enter new file name: ")
            os.rename(buffer, buffer2)

    if(com == "rf"):
        buffer = input("Enter file name: ")
        file = open(buffer, "r")
        print(TextColor.CYAN + "<<====================>>" + TextColor.RESET)
        print(*file)
        print(TextColor.CYAN + "<<====================>>" + TextColor.RESET)
        file.close()

    if(com == "wf"):
        buffer = input("Enter file name: ")
        file = open(buffer, "w")
        print(TextColor.CYAN + "<<=======================>>" + TextColor.RESET)
        text = input()
        print(TextColor.CYAN + "<<=======================>>" + TextColor.RESET)
        file.write(text)
        time.sleep(0.1)
        file.close()
        print(TextColor.GREEN + "Saved!")

    if(com == "run"):
        if(user != "ROOT"):
            print(accessDenied)
        if(user == "ROOT"):
            buffer = input("Enter the path to the file, or file name, or other command: ")
            os.system(buffer)

    if(com == "md"):
        buffer = input("Enter folder name: ")
        if not os.path.isdir(buffer):
            os.mkdir(buffer)
            time.sleep(0.05)
            print("Complete!")

    if(com == "rd"):
        buffer = input("Enter folder name: ")
        os.rmdir(buffer)
        time.sleep(0.05)
        print("Complete!")

    if(com=="help"):
         print("")
         print(TextColor.CYAN + "<<========           Список комманд           ========>>" +TextColor.RESET)
         print("")
         print("Для вывода этого списка, введите 'help'")
         print("")
         print(TextColor.CYAN + "<<======== Работа с файлами ========>>" +TextColor.RESET)
         print("md - Создать директорию (папку)")
         print("rd - Удалить директорию (папку)")
         print("openpy - Выполнить файлы *.py")
         print("rf - Прочитать файл")
         print("cd - Переход между папками и директориями")
         print("apt - install, backup and recover file or package")
         print("wf - Write information to file or create new file")
         print(TextColor.CYAN + "<<======== Офисные ========>>" +TextColor.RESET)
         print("date - Отобразить дату и время")
         print("timer - start 'timer' " + TextColor.YELLOW + " [package]" +TextColor.RESET)
         print("calc - calculator - Start calculator " + TextColor.YELLOW + " [package]" +TextColor.RESET)
         print("filemgr - file manager - Launching file manager " + TextColor.YELLOW + " [package]" +TextColor.RESET)
         print("calen - Start calendar " + TextColor.YELLOW + " [package]" +TextColor.RESET)
         print(TextColor.CYAN + "<<======== Требуют " + TextColor.RED + "ROOT" + TextColor.CYAN + " ========>>" +TextColor.RESET)
         print("ls - Список файлов и директорий " + TextColor.RED + "[ROOT]" +TextColor.RESET)
         print("df - Удалить файл " + TextColor.RED + "[ROOT]" +TextColor.RESET)
         print("renf - Переименовать файл " + TextColor.RED + "[ROOT]" +TextColor.RESET)
         print("fi - Вывести информацию о файле " + TextColor.RED + "[ROOT]" +TextColor.RESET)
         print("cfile - Передача файлов " + TextColor.RED + "[ROOT]" +TextColor.RESET)
         print("run - Выполнение других файлов " + TextColor.RED + "[ROOT]" +TextColor.RESET)
         print(TextColor.CYAN + "<<======== Параметры ========>>" +TextColor.RESET)
         print("control - Открыть панель управления")
         print("lang - Сменить язык")
         print("obpy - Установить/обновить модули")
         print(TextColor.CYAN + "<<======== Работа над пользователями ========>>" +TextColor.RESET)
         print("Кстати: можно вводить как 'usr', так и 'user'")
         print("usr edit - Изменить информацию о пользователе")
         print("usr switch/change - Сменить пользователя")
         print("usr (list) - Вывести список всех пользователей в системе")
         print("usr info - Вывести информацию о конкретном пользователе")
         print(TextColor.CYAN + "<<======== Другие ========>>" +TextColor.RESET)
         print("echo - Вывести ваш текст")
         print("clear - Очистить экран")
         print("ver - Вывести версию ctOS " + TextColor.YELLOW + " [package]" +TextColor.RESET)
         print("pacman - install a new package or create a new one (new-package)")
         print("pip - Ввести команду для pip")
         print("apct - package downloader")
         print(TextColor.CYAN + "<<======== Питание ========>>" +TextColor.RESET)
         print("restart/reboot - Перезапуск ctOS")
         print("logout/shutdown/exit - Выключение ctOS")
         print(TextColor.CYAN + "<<=========                                  ========>>" +TextColor.RESET)

         #Packages

    if (com == "apct"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 LifeModification/apct.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python LifeModification/apct.py")

    if(com=="obpy"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 LifeModification/ObPy.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python LifeModification/ObPy.py")

    if(com == "ver"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 LifeModification/vers.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python LifeModification/vers.py")

    if(com == "timer"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 apps/timer.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python apps/timer.py")

    if(com == "calen"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 apps/Calen.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python apps/Calen.py")

    if(com == "filemgr"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 apps/filemgr.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python apps/filemgr.py")

    if(com=="calc"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 apps/calcs.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python apps/calcs.py")

    if(com == "timer"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 Programs/timer.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python Programs/timer.py")

    if(com == "lang"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 LifeModification/lang.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python LifeModification/lang.py")

    if(com=="restart" or com=="reboot"):
        if(syst == "| base system: LINUX   |"):
            os.system(clean)
            print("Перезапуск.")
            time.sleep(0.2)
            os.system(clean)
            print("Перезапуск..")
            time.sleep(0.2)
            os.system(clean)
            print("Перезапуск...")
            time.sleep(0.2)
            os.system(clean)
            print("Перезапуск...Done!")
            time.sleep(0.2)
            start = "false"
            os.system(clean)
            times1 = datetime.today()
            comlog.writelines("RUS: ")
            comlog.writelines("Restarting in: " + str(times1) + "\n")
            os.system("python3 ctOS.py")
        if(syst == "| base system: WINDOWS |"):
            os.system(clean)
            print("Перезапуск.")
            time.sleep(0.2)
            os.system(clean)
            print("Перезапуск..")
            time.sleep(0.2)
            os.system(clean)
            print("Перезапуск...")
            time.sleep(0.2)
            os.system(clean)
            print("Перезапуск...Done!")
            time.sleep(0.2)
            start = "false"
            os.system(clean)
            times1 = datetime.today()
            comlog.writelines("ENG: ")
            comlog.writelines("Restarting in: " + str(times1) + "\n")
            os.system("python ctOS.py")

    if(com == "echo"):
        buffer = input("Input string: ")
        print(buffer)

    if(com=="date"):
        print(datetime.today())

    if(com=="clear" or com=="clr"):
        os.system(clean)

    if(com=="logout" or com == "exit" or com=="shutdown"):
        os.system(clean)
        print("Выключение.")
        time.sleep(0.2)
        os.system(clean)
        print("Выключение..")
        time.sleep(0.2)
        os.system(clean)
        print("Выключение...")
        time.sleep(0.2)
        os.system(clean)
        print("Выключение...Done!")
        time.sleep(0.2)
        start = "false"
        times1 = datetime.today()
        comlog.writelines("ENG: ")
        comlog.writelines("Shutting Down in: " + str(times1) + "\n")


