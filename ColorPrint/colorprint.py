import os

def clear():
    os.system("cls")

class cprint:
    def __init__(self, text):
        self.text = text
    
    def black(self):
        print(f"\033[30m{self.text}\033[0m")

    def red(self):
        print(f"\033[31m{self.text}\033[0m")

    def green(self):
        print(f"\033[32m{self.text}\033[0m")

    def yellow(self):
        print(f"\033[33m{self.text}\033[0m")

    def blue(self):
        print(f"\033[34m{self.text}\033[0m")

    def magenta(self):
        print(f"\033[35m{self.text}\033[0m")

    def cyan(self):
        print(f"\033[36m{self.text}\033[0m")

    def white(self):
        print(f"\033[37m{self.text}\033[0m")


    def bright_black(self):
        print(f"\033[90m{self.text}\033[0m")

    def bright_red(self):
        print(f"\033[91m{self.text}\033[0m")

    def bright_green(self):
        print(f"\033[92m{self.text}\033[0m")

    def bright_yellow(self):
        print(f"\033[93m{self.text}\033[0m")

    def bright_blue(self):
        print(f"\033[94m{self.text}\033[0m")

    def bright_magenta(self):
        print(f"\033[95m{self.text}\033[0m")

    def bright_cyan(self):
        print(f"\033[96m{self.text}\033[0m")

    def bright_white(self):
        print(f"\033[97m{self.text}\033[0m")