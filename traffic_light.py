import time
from os import system, name
from colorama import Fore

class Traffic_lights():
    def __init__(self):
        self.lightbox1 = "████████████"
        self.lightbox2 = "████████████"
        self.lightbox3 = "████████████"
        self.colors = [1, 2, 3]

    def bannerArtDisplay(self):
        print(Fore.RED+"""
▄▄▄█████▓ ██▀███   ▄▄▄        █████▒ █████▒██▓ ▄████▄      ██▓     ██▓  ▄████  ██░ ██ ▄▄▄█████▓  ██████ 
▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▓██   ▒▓██   ▒▓██▒▒██▀ ▀█     ▓██▒    ▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒▒██    ▒ 
▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒████ ░▒████ ░▒██▒▒▓█    ▄    ▒██░    ▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░░ ▓██▄   
░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ░▓█▒  ░░▓█▒  ░░██░▒▓▓▄ ▄██▒   ▒██░    ░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░   ▒   ██▒
  ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒░▒█░   ░▒█░   ░██░▒ ▓███▀ ░   ░██████▒░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░ ▒██████▒▒
  ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░    ▒ ░   ░▓  ░ ░▒ ▒  ░   ░ ▒░▓  ░░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░   ▒ ▒▓▒ ▒ ░
    ░      ░▒ ░ ▒░  ▒   ▒▒ ░ ░      ░      ▒ ░  ░  ▒      ░ ░ ▒  ░ ▒ ░  ░   ░  ▒ ░▒░ ░    ░    ░ ░▒  ░ ░
  ░        ░░   ░   ░   ▒    ░ ░    ░ ░    ▒ ░░             ░ ░    ▒ ░░ ░   ░  ░  ░░ ░  ░      ░  ░  ░  
            ░           ░  ░               ░  ░ ░             ░  ░ ░        ░  ░  ░  ░               ░                                                                                                
              """+Fore.RESET)

    def displayTrafficLightBannerArt(self, lightBox1, lightBox2, lightBox3):
        print(f"""
                                         ██████████████████
                                         █                █
                                    ═════█  {lightBox1}  █═════
                                     ════█  {lightBox1}  █════
                                      ═══█  {lightBox1}  █═══
                                       ══█  {lightBox1}  █══
                                        ═█                █═
                                         ██████████████████
                                         █                █
                                    ═════█  {lightBox2}  █═════
                                     ════█  {lightBox2}  █════
                                      ═══█  {lightBox2}  █═══
                                       ══█  {lightBox2}  █══
                                        ═█                █═
                                         ██████████████████
                                         █                █
                                    ═════█  {lightBox3}  █═════
                                     ════█  {lightBox3}  █════
                                      ═══█  {lightBox3}  █═══
                                       ══█  {lightBox3}  █══
                                        ═█                █═
                                         ██████████████████
                                                 ║║
                                                 ║║
                                                 ║║
                                                 ║║
                                                 ║║
                                                 ║║
                                                 ║║ 
                                                 ║║
 """)
    
    def clearance(self):
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")
    


        
def main():
    instance1 = Traffic_lights()
    instance1.clearance()
    while True:
        for i in instance1.colors:
            if i == 1:
                instance1.bannerArtDisplay()
                instance1.displayTrafficLightBannerArt(Fore.BLACK+instance1.lightbox1+Fore.RESET, Fore.BLACK+instance1.lightbox2+Fore.RESET, Fore.GREEN+instance1.lightbox3+Fore.RESET)
                time.sleep(5)
                instance1.clearance()
            elif i==2:
                instance1.bannerArtDisplay()
                instance1.displayTrafficLightBannerArt(Fore.BLACK+instance1.lightbox1+Fore.RESET, Fore.YELLOW+instance1.lightbox2+Fore.RESET, Fore.BLACK+instance1.lightbox3+Fore.RESET)
                time.sleep(5)
                instance1.clearance()
            elif i==3:
                instance1.bannerArtDisplay()
                instance1.displayTrafficLightBannerArt(Fore.RED+instance1.lightbox1+Fore.RESET, Fore.BLACK+instance1.lightbox2+Fore.RESET, Fore.BLACK+instance1.lightbox3+Fore.RESET)
                time.sleep(5)
                instance1.clearance()

main()

# made by that one guy from IT branch.