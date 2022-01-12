import os, json, threading, time, random
from ColorPrint import colorprint

os.system("mode con:cols=220 lines=30")
os.system("title Token Checker by. 김명우#0001")

def install_module(module):
    os.system(f"pip install {module}")

try:
    import requests
except:
    install_module("requests")
try:
    import asyncio
except:
    install_module("asyncio")

valid = []
invalid = []
not_valid_and_not_invalid = []

try:
    config = json.loads(open("config.json", "r", encoding="utf-8").read())
except:
    config = json.loads(open("config.json", "r", encoding="cp949").read())

colorprint.clear()

cprint = colorprint.cprint

print("""
████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

Developer: 김명우#0001
Discord Server: discord.gg/fastdm

""")

def set_title():
    os.system(f"title Token Checker by. 김명우#0001ㅣVALID: {len(valid)}, INVALID: {len(invalid)}")

def randstr(len_):
    rstr = ""
    for _ in range(len_):
        rstr += random.choice("qwertyuopasdfghjkl;zxcvbnm1029384756")
    return rstr

def headers(token):
    return {
        "authority": "discord.com",
        "method": "POST",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US",
        "Authorization": token,
        "content-length": "0",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
        "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
    }

async def check(token):
    global valid
    global invalid
    try:
        t = token.split(":")[2]
    except:
        t = token
    while True:
        try:
            req = requests.get("https://discord.com/api/v9/users/@me/library", headers=headers(t))
            if req.status_code == 200:
                verify = []
                req = requests.get("https://discord.com/api/v9/users/@me", headers=headers(t))
                req = req.json()
                phone = req["phone"]
                email = req["email"]
                verified = req["verified"]
                username = req["username"]
                discriminator = req["discriminator"]
                id = req["id"]
                if verified == True:
                    verify.append("email")
                elif phone != None:
                    verify.append("phone")
                while True:
                    guilds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers(t)).json()
                    if not "You are being rate limited." in str(guilds):
                        break
                    await asyncio.sleep(1)
                if "email" in verify and "phone" in verify:
                    verify = "Full Verify"
                else:
                    if "email" in verify:
                        verify = "Email Verify"
                    elif "phone" in verify:
                        verify = "Phone Verify"
                    else:
                        verify = "Not Verify"
                cprint(f"{t} - {verify} TokenㅣGuild Count: {len(guilds)}ㅣUsername: {username}#{discriminator}ㅣUserID: {id}ㅣEmail: {email}ㅣPhone: {phone}").green()
                valid.append(token)
                set_title()
            else:
                if req.status_code == 401:
                    cprint(f"{t} - INVALID").red()
                    invalid.append(token)
                elif req.status_code == 403:
                    cprint(f"{t} - LOCKED").red()
                    invalid.append(token)
                else:
                    message = req.json()["message"]
                    cprint(f"{t} - {message}").yellow()
                    not_valid_and_not_invalid.append(token)
            set_title()
            break
        except:
            pass

tokens = open("tokens/tokens.txt", "r").read().split("\n")

for token in tokens:
    threading.Thread(target=asyncio.run, args=(check(token),)).start()
    time.sleep(config["delay"])

while True:
    if len(invalid) + len(valid) == len(tokens):
        set_title()
        if not_valid_and_not_invalid != []:
            print(f"There was an error Please try again in a few moments.")
            os.system("pause")
            break
        if config["save_email_password"] != True:
            vvalid = []
            iinvalid = []
            ssame_tokens = []
            for token in valid:
                try:
                    vvalid.append(token.split(":")[0])
                except:
                    vvalid.append(token)
            for token in invalid:
                try:
                    iinvalid.append(token.split(":")[0])
                except:
                    iinvalid.append(token)
        else:
            vvalid = valid
            iinvalid = invalid
        open("tokens/valid.txt", "w").write("\n".join(valid))
        open("tokens/invalid.txt", "w").write("\n".join(invalid))

        print(f"\nVALID: {len(valid)}ㅣINVALID: {len(invalid)}\n")

        os.system("pause")
        break
