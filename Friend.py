#!/usr/bin/env python
# Created By ybenel

#Libraries#
try:
    from os import system as sy, path; import requests,socket,optparse
    sy("")
except ImportError:
    print(unknown2 +"Error Please Install [Requests] Module !!!")
    print(unknown6 +"Use This Command > pip install requests")
    exit(1)
# Check Internet Connection #
def cnet():
    try:
        ip = socket.gethostbyname("www.google.com")
        con = socket.create_connection((ip, 80), 2)
        return True
    except socket.error:
        pass
    return False
#Check-Email-Function#
#

def Friend(email):
    try:
        data = {"email": email}
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24'}
        response = requests.post("https://verifyemailaddress.com/result", headers=headers, data=data).text
        if "is valid" in response:
            print(unknown9+"["+unknown9+"+"+unknown9+"] Email["+unknown8+email+unknown8+"] STATUS["+unknown5+" Found "+unknown5+"]")
        else:
            print(Red+"["+Red+"-"+Red+"] Email["+Grey+email+Grey+"] STATUS["+cyan+" Not Found "+cyan+"]"+cyan)
    except(KeyboardInterrupt,EOFError):
        print(cyan+" ")
        exit(1)
##############################3
Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
yellow="\033[1;36m"
Red="\033[1;31m"
purple="\033[35m"
Light="\033[95m"
cyan="\033[96m"
stong="\033[39m"
unknown="\033[38;5;82m"
unknown2="\033[38;5;198m"
unknown3="\033[38;5;208m"
unknown4="\033[38;5;167m"
unknown5="\033[38;5;91m"
unknown6="\033[38;5;210m"
unknown7="\033[38;5;165m"
unknown8="\033[38;5;49m"
unknown9="\033[38;5;160m"
unknown10="\033[38;5;51m"
unknown11="\033[38;5;13m"
unknown12="\033[38;5;162m"
unknown13="\033[38;5;203m"
unknown14="\033[38;5;113m"
unknown15="\033[38;5;14m"
      ###############################3

print("        "+unknown+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+unknown2+"MMMMMMMMMMNKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+unknown3+"MMMMMMMMMNc.dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+unknown4+"MMMMMMMMWd. .kWMMMMMMMMMMMMMMMMMMMMMMW0KMMMMMMMMMM")
print("        "+unknown15+"MMMMMMMMk:;. 'OMMMMMMMMMMMMMMMMMMMMMWx.,0MMMMMMMMM")
print("        "+unknown14+"MMMMMMMK:ok.  ,0MMMMMMMMMMMMMMMMMMMWO. .cXMMMMMMMM")
print("        "+unknown13+"MMMMMMNl:KO.   ;KWNXK00O0000KXNWMMWO' .c;dWMMMMMMM")
print("        "+unknown12+"MMMMMMx,xNk.    .;'...    ....';:l:.  ,0l,0MMMMMMM")
print("        "+unknown11+"MMMMMK;,l;. .,:cc:;.                  .dx,lWMMMMMM")
print("        "+unknown10+"MMMMWo    ,dKWMMMMWXk:.      .cdkOOxo,. ...OMMMMMM")
print("        "+unknown5+"MMMM0'   cXMMWKxood0WWk.   .lkONMMNOOXO,   lWMMMMM")
print("        "+unknown2+"MMMWl   ;XMMNo.    .lXWd. .dWk;;dd;;kWM0'  '0MMMMM")
print("        "+unknown9+"kxko.   lWMMO.      .kMO. .OMMK;  .kMMMNc   oWMMMM")
print("        "+unknown8+"X0k:.   ;KMMXc      :XWo  .dW0c,lo;;xNMK,   'xkkk0")
print("        "+unknown10+"kko'     :KMMNkl::lkNNd.   .dkdKWMNOkXO,    .lOKNW")
print("        "+unknown15+"0Kk:.     .lOXWMMWN0d,       'lxO0Oko;.     .ckkOO")
print("        "+unknown4+"kkkdodo;.    .,;;;'.  .:ooc.     .        ...ck0XN")
print("        "+unknown8+"0XWMMMMWKxc'.          ;dxc.          .,cxKK0OkkOO")
print("        "+unknown+"MMMMMMMMMMMN0d:'.  .'        .l'  .;lxKWMMMMMMMMMN")
print("        "+unknown2+"MMMMMMMMMMMMMMMN0xo0O:,;;;;;;xN0xOXWMMMMMMMMMMMMMM")
print("        "+unknown14+"MMMMMMMMMMMMMMMMMMMMMMWWWWWMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+unknown6+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+unknown7+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+unknown8+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+unknown9+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+Blue+"                   "+unknown2+"["+unknown14+"Friend"+unknown5+"]"+unknown+"         ")
print("     "+purple+"             "+unknown13+"["+unknown8+"  Created By ybenel"+unknown2+"]"+unknown10+"    "+Reset+"\n")
parse = optparse.OptionParser(unknown +"""
Usage : python friend.py [Option]
Options:
|-------------------------------------------------------------------------|
|       -s --single [Email]                        :> Check Single Email  |
|-------------------------------------------------------------------------|
|       -m --many [Email,Email2,etc]               :> Check Many Emails   |
|-------------------------------------------------------------------------|
|       -f --file [File Contain Emails]       :> Check All Email From File|
|-------------------------------------------------------------------------|
|----------------------------[Examples]-----------------------------------|
|-------------------------------------------------------------------------|
| --------python friend.py -s ybenel@pm.me -------------------- |
|-------------------------------------------------------------------------|
|-------python friend.py -m ybenel@molero.xyz,ybenel@molero.xyz-----|
|-------------------------------------------------------------------------|
|--------python friend.py -f emails.txt-----------------------------------|
|-------------------------------------------------------------------------|
""",version="1.0")
def Main():
    parse.add_option('-s','-S','--single','--SINGLE', dest="Smail",type="string")
    parse.add_option('-m','-m','--many','--MANY', dest="Mmail",type="string")
    parse.add_option('-f','-F','--file','--FILE', dest="Fmail",type="string")
    (opt,args) = parse.parse_args()
    if opt.Smail !=None:
        if cnet() !=True:
            print(Red +"[!]"+unknown5+"Error Check Your Connection")
            exit(1)
        email = opt.Smail
        if not email.strip() or "@" not in email:
            print(Red+"\n["+Red+"!"+yellow+"] Invalid Email["+Red+email+yellow+"] STATUS["+Red+" SKIPPED "+yellow+"]"+cyan)
            exit(1)
        email = email.strip()
        print(unknown6+"["+unknown4+"~"+unknown3+"]"+unknown2+" Checking....\n"+cyan)
        Friend(email)

    elif opt.Mmail !=None:
        if cnet() !=True:
            print(Red+"\n["+unknown8+"!"+unknown9+"]"+unknown10+" Error: Please Check Your Internet Connection "+unknown12+"!!!"+cyan)
            exit(1)
        many_email = opt.Mmail
        print(Red+"["+yellow+"~"+Green+"]"+Red+" Checking....\n"+cyan)
        if ',' in many_email:
            emails = many_email.split(",")
        else:
            print(Red+"\n["+unknown15+"!"+unknown+"] Error: Please Use[ "+cyan+","+cyan+" ] To Split The Emails"+Red+" !!!"+cyan)
            exit(1)
        try:
            for email in emails:
                if not email.strip() or "@" not in email: continue
                email = email.strip()
                Friend(email)
        except (KeyboardInterrupt,EOFError):
            print(cyan+" ")
            exit(1)

    elif opt.Fmail !=None:
        emails_file = opt.Fmail
        print(unknown+"["+unknown2+"~"+unknown3+"]"+unknown4+" Checking....\n"+cyan)
        if not path.isfile(emails_file):
            print(yellow+"\n["+Red+"!"+Green+"]"+Grey+" Error:"+purple+" No Such File: [ "+Light+emails_file+Light+" ]"+Red+" !!!"+cyan)
            print(cyan+"["+Red+"!"+cyan+"]"+yellow+" Please:"+cyan+" Check Your Emails File Path."+Grey+"!"+cyan)
            exit(1)
        try:
            with open(emails_file) as fop:
                for email in fop:
                    if not email.strip() or "@" not in email: continue
                    email = email.strip()
                    Friend(email)
            fop.close()
        except (KeyboardInterrupt,EOFError):
            print(wi+" ")
            exit(1)
    else:
        print(parse.usage)
        exit(1)

if __name__=="__main__":
    Main()
# Done!
