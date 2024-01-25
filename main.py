import ctypes
import string
import os
import time
import requests
from discord_webhook import DiscordWebhook
import numpy

class NitroGen:
    def __init__(self):
        self.fileName = "Nitro.txt"
        self.USE_WEBHOOK = True

    def setup(self):
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

        self.check_module("discord_webhook", "To install, run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'")
        self.check_module("requests", "To install, run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'")
        self.check_module("numpy", "To install, run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'")

        self.check_internet_connection()

    def check_module(self, module_name, install_command):
        try:
            __import__(module_name)
        except ImportError:
            input(f"Error: Module {module_name} not installed. {install_command}\nPress enter to continue.")
            if module_name == "discord_webhook":
                self.USE_WEBHOOK = False

    def check_internet_connection(self):
        url = "https://3mpire.mysellix.io"
        try:
            response = requests.get(url)
            print("Internet check")
            time.sleep(.4)
        except requests.exceptions.ConnectionError:
            input("Error: You are not connected to the internet. Check your connection and try again.\nPress enter to exit")
            exit()

    def main(self):
        self.setup()

        os.system('cls' if os.name == 'nt' else 'clear')

        if os.name == "nt":
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator & Checker")
        else:
            print(f'\33]0;Nitro Generator & Checker\a', end='', flush=True)

        self.print_title_card()

        time.sleep(2)
        self.slow_type("go.3mpire.shop/redirect", .02)
        time.sleep(1)
        self.slow_type("\nInput How Many Codes to Generate and Check: ", .02, new_line=False)

        try:
            num = int(input(''))
        except ValueError:
            input("Error: Specified input wasn't a number.\nPress enter to exit")
            exit()

        if self.USE_WEBHOOK:
            self.setup_webhook()

        valid, invalid = self.generate_and_check_codes(num)

        self.print_results(valid, invalid)

        input("\nThe end! Press Enter 5 times to close the program.")
        [input(i) for i in range(4, 0, -1)]

    def setup_webhook(self):
        self.slow_type("If you want to use a Discord webhook, type it here or press enter to ignore: ", .02, new_line=False)
        url = input('')
        webhook = url if url != "" else None

        if webhook is not None:
            DiscordWebhook(
                url=url,
                content=f"```Started checking urls\nI will send any valid codes here```"
            ).execute()

    def generate_and_check_codes(self, num):
        valid = []
        invalid = 0
        chars = []
        chars[:0] = string.ascii_letters + string.digits

        c = numpy.random.choice(chars, size=[num, 16])
        for s in c:
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"

                result = self.quick_checker(url)

                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except KeyboardInterrupt:
                print("\nInterrupted by user")
                break

            except Exception as e:
                print(f" Error | {url}")

            self.update_title(len(valid), invalid)

        return valid, invalid

    def print_title_card(self):
        print(r"""
   _______  ___      ___    _______   __      _______    _______  
  /" __   )|"  \    /"  |  |   __ "\ |" \    /"      \  /"     "| 
 (__/ _) ./ \   \  //   |  (. |__) :)||  |  |:        |(: ______) 
     /  //  /\\  \/.    |  |:  ____/ |:  |  |_____/   ) \/    |   
 __  \_ \\ |: \.        |  (|  /     |.  |   //      /  // ___)_  
(: \__) :\|.  \    /:  | /|__/ \    /\  |\ |:  __   \ (:      "| 
 \_______)|___|\__/|___|(_______)  (__\_|_)|__|  \___) \_______) 
                                                                 """)

    def slow_type(self, text: str, speed: float, new_line=True):
        for i in text:
            print(i, end="", flush=True)
            time.sleep(speed)
        if new_line:
            print()

    def quick_checker(self, nitro):
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            print(f" Valid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            with open("NitroValid.txt", "a") as file:
                file.write(nitro + '\n')

            self.notify_webhook(url, nitro)

            return True

        else:
            print(f" Invalid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            with open("NitroFailed.txt", "a") as file:
                file.write(nitro + '\n')

            return False


    def notify_webhook(self, url, nitro):
        if self.USE_WEBHOOK:
            DiscordWebhook(
                url=url,
                content=f"Valid Nitro Code detected! @everyone \n{nitro}"
            ).execute()

    def update_title(self, valid_count, invalid_count):
        if os.name == "nt":
            ctypes.windll.kernel32.SetConsoleTitleW(
                f"Nitro Generator & Checker - {valid_count} Valid | {invalid_count} Invalid")
            print("")
        else:
            print(
                f'\33]0;Nitro Generator & Checker - {valid_count} Valid | {invalid_count} Invalid\a', end='', flush=True)

if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()
