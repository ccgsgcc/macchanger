import subprocess


while True:
    keyboard = input("Введите ваш интерфейс: ")

    if keyboard == "eth0":
        subprocess.call("sudo macchanger -r eth0", shell=True)
    else:
        print("Введите правильный интерфейс")
        continue
            
