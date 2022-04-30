import os
import time
import requests
from bs4 import BeautifulSoup
import re
from pathlib import Path
from discord_webhook import DiscordWebhook, DiscordEmbed

os.system("clear")

print(f'''
███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ 
███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝                                                                                                                                                     
[1] SQLI scanner 
[2] JSON/XML/JS/TXT finder 
[3] XSS scanner 
[4] Param spider 
[5] Open redirect scanner 
[6] Directory scan with many options 
[7] Nuclei vulnerability scanner 
[8] Google hacking 
''')

def sqliauto():

    embed = DiscordEmbed(title=f'SQLI SCAN STARTED AGAINST: __{domain}__', color='0000FF')
    embed.set_image(url='https://www.seekpng.com/png/full/369-3696460_sql-injection-sql-injection-png.png')

    sqli.add_embed(embed)
    sqli.execute(remove_embeds=True, remove_files=True)

    os.system(f"subfinder -d {domain} | waybackurls | grep '=' | httpx -mc 200 > ./LOGGER/{domain}/paramsXSS.txt")

    os.system(f"sort ./LOGGER/{domain}/paramsXSS.txt | uniq > ./LOGGER/{domain}/uniqSQLI.txt")

    time.sleep(3)

    os.system(f"grep -r --no-filename -e 'php?' ./LOGGER/{domain}/uniqSQLI.txt > ./LOGGER/{domain}/finalSQLI.txt")

    time.sleep(1)

    file = open(f'./LOGGER/{domain}/finalSQLI.txt')

    while True:

        for line in file:
            line = line.strip()

            time.sleep(5)

            print(f"testing: {line}")

            os.system(f"sqlmap -u {line} --risk 1 --level 1 --random-agent --random-agent --batch --threads=10 --dbs > ./LOGGER/{domain}/logSQLI.txt")

            w = "might be vulnerable"

            if w in open(f'./LOGGER/{domain}/logSQLI.txt').read():

                with open(f'./LOGGER/{domain}/logSQLI.txt') as f:

                    vuln = DiscordEmbed(title=f'TARGET MIGHT BE VULNERABLE TO SQLI', description=f'[ - ] URL: {line}', color='00FF00')
                    sqli.add_file(file=f.read(), filename='log.txt')
                    sqli.add_embed(vuln)
                    sqli.execute(vuln)

                    time.sleep(20)

            else:
                    notvuln = DiscordEmbed(title=f'TARGET MIGHT NOT BE VULNERABLE BUT HERE IS THE LOG', description=f'[ - ] URL: {line}', color='FF0000')
                    sqli.add_file(file=f.read(), filename='log.txt')
                    sqli.add_embed(notvuln)
                    sqli.execute(notvuln)

                    time.sleep(20)

def ifinder():

    embed = DiscordEmbed(title=f'SENSI INFO FINDER STARTED AGAINST: __{domain}__', color='0000FF')
    embed.set_image(url='https://sysnetgs.com/wp-content/uploads/2016/12/iStock_000038899232_1350.jpg')

    sensinfo.add_embed(embed)
    sensinfo.execute(remove_embeds=True, remove_files=True)

    os.system(f"subfinder -d {domain} | waybackurls | httpx -mc 200 > ./LOGGER/{domain}/activesFIND.txt")

    os.system(f"sort ./LOGGER/{domain}/activesFIND.txt | uniq > ./LOGGER/{domain}/uniqFIND.txt")

    time.sleep(3)

    os.system(f"grep -r --no-filename '.json\|.xml\|.js\|.txt\|.git\|sql\|mdb\|dbf\|log\|bak\|bkp\|bkf\|old\|backup' ./LOGGER/{domain}/uniqFIND.txt > ./LOGGER/{domain}/finalFIND.txt")

    time.sleep(1)

    file = open(f'./LOGGER/{domain}/finalFIND.txt')

    while True:

        for line in file:
            line = line.strip()

            interesting = ['password:', 'secret key', 'access-key', 'access token', 'access_token', 'aws-access', 'secret:', 'secret key', 'secret :', 'secret is:', 'secret=', 'secret =', 'password =', 'password=', 'privatekey', 'api-key', 'api-token', 'client=secret', 'ftp', 'login', 'apikey', 'api', 'secret', 'vpn', 'server', 'email', 'root', 'admin', 'backup', 'ssh', 'db_username', 'token', 'client_secret', 'aws', 'datacenter', 'secretkey', 'keys', 'serverHMACSecretKey', 'auth', 'db_database', 'access_key', 'secret_access', 'amazonaws', 'sql', 'mdb', 'dbf']

            r = requests.get(f"{line}")

            if r.status_code == 200:

                for word in interesting:
                    if word in r.text:

                        j2 = DiscordEmbed(title=f'FOUND SOMETHING INTERESTING:', description=f'[ - ] URL: {line} \n[ - ] WORD: {word}', color='FF0000')

                        time.sleep(5)
 
                        sensinfo.add_embed(j2)
                        sensinfo.execute(j2) 

                        time.sleep(30)

                    else:

                        print(f"found: {line}")

                        time.sleep(30)


def xss():

    embed = DiscordEmbed(title=f'XSS SCAN STARTED', color='0000FF')
    embed.set_image(url='https://www.wpexplorer.com/wp-content/uploads/wordpress-cross-site-scripting-guide-prevention.png')

    xssw.add_embed(embed)
    xssw.execute(remove_embeds=True, remove_files=True)

    os.system(f"subfinder -d {domain} | waybackurls | grep '=' | httpx -mc 200 > ./LOGGER/{domain}/pxss.txt")

    time.sleep(3)

    file = open(f'./LOGGER/{domain}/pxss.txt')

    while True:

        for line in file:
            line = line.strip()

            os.system(f"dalfox url {line} -b https://hahwul.xss.ht/ > ./LOGGER/{domain}/logXSS.txt")

            w = "POC"

            if w in open(f'./LOGGER/{domain}/logXSS.txt').read():

                with open(f'./LOGGER/{domain}/logXSS.txt') as f:

                    vuln = DiscordEmbed(title=f'TARGET MIGHT BE VULNERABLE TO XSS', description=f'[ - ] URL: {line}', color='00FF00')
                    xssw.add_file(file=f.read(), filename='logXSS.txt')
                    xssw.add_embed(vuln)
                    xssw.execute(vuln)

                    time.sleep(20)
            else:

                    notvuln = DiscordEmbed(title=f'TARGET MIGHT NOT BE VULNERABLE BUT HERE IS THE LOG', description=f'[ - ] URL: {line}', color='FF0000')
                    xssw.add_file(file=f.read(), filename='logXSS.txt')
                    xssw.add_embed(notvuln)
                    xssw.execute(notvuln)

                    time.sleep(20)

def paramspider():

    embed = DiscordEmbed(title=f'PARAM SCAN STARTED AGAINST: __{domain}__', color='0000FF')
    embed.set_image(url='https://cdn-icons-png.flaticon.com/512/47/47282.png')

    param.add_embed(embed)
    param.execute(remove_embeds=True, remove_files=True)

    os.system(f"python ParamSpider/paramspider.py -d {domain} | httpx > ./LOGGER/{domain}/paramspider.txt")

    embed = DiscordEmbed(title=f'FOUND PARAMS FOR: __{domain}__', color='00FF00')

    param.add_embed(embed)

    with open(f"./LOGGER/{domain}/paramspider.txt", "rb") as f:
        param.add_file(file=f.read(), filename='paramspider.txt')

    param.execute()

def openr():

    embed = DiscordEmbed(title=f'OPEN REDIRECT SCAN STARTED AGAINST: __{domain}__', color='0000FF')
    embed.set_image(url='https://cdn-icons-png.flaticon.com/512/3165/3165554.png')

    redirect.add_embed(embed)
    redirect.execute(remove_embeds=True, remove_files=True)

    os.system(f"subfinder -d {domain} | waybackurls > ./LOGGER/{domain}/waybackOR.txt")

    os.system(f"sort ./LOGGER/{domain}/waybackOR.txt | uniq > ./LOGGER/{domain}/uniqOR.txt")

    time.sleep(3)

    os.system(f"grep -r --no-filename 'forward=https\|url=\|redirect=\|dest=\|redirectto=\|redirecturi=\|uri=\|path=\|continue=\|forward=\|window=\|to=\|out=\|view=\|dir=\|show=\|navigation=\|Open=\|file=\|validate=\domain=\|callback=\|return=\|page=\|feed=\|host=\|port=\|next=\|data=\|reference=\|site=\|html=\|=https\|goto=|navigateto=' ./LOGGER/{domain}/uniqOR.txt > ./LOGGER/{domain}/finalOR.txt")

    time.sleep(1)

    file = open(f'./LOGGER/{domain}/finalOR.txt')

    while True:

        for line in file:
            line = line.strip()

            r = requests.get(f'{line}', stream=True)

            if r.status_code == 301:

                print(f"found: {line}")

                o = DiscordEmbed(title=f'POSSIBLE OPEN REDIRECT FOUND:', description=f'[ - ] URL: {line} \n[ - ] CODE: {r.status_code}', color='00FF00')
                redirect.add_embed(o)
                redirect.execute(o) 

                time.sleep(30)

            else:

                if r.status_code == 200:

                    print(f"found: {line}")

                    o = DiscordEmbed(title=f'PROBABLY NOT A OPEN REDIRECT BUT YOU BETTER TAKE A LOOK AT IT:', description=f'[ - ] URL: {line} \n[ - ] CODE: {r.status_code}', color='FF0000')
                    redirect.add_embed(o)
                    redirect.execute(o) 

                    time.sleep(30)

def directoryscan():

    wordlistinput = input("wordlist => ")

    if wordlistinput == "1":
        w = "./wordlist/directory-list-2.3-medium.txt"
        os.system(f"gobuster dir -u https://{domain}/ -w {w} > mediumdir.txt")

        with open("mediumdir.txt", "rb") as f:

            d = DiscordEmbed(title=f'FINISHED SCANNING DIRECTORY', description=f'[ - ] URL: https://{domain} \n[ - ] WORDLIST: directory-list-2.3-medium.txt', color='00FF00')
            directory.add_file(file=f.read(), filename='mediumdir.txt')
            directory.add_embed(d)
            directory.execute(d)

        os.system("rm mediumdir.txt")

    if wordlistinput == "2":
        w = "./wordlist/admin.txt"
        os.system(f"gobuster dir -u https://{domain}/ -w {w} > admindir.txt")

        with open("mediumdir.txt", "rb") as f:

            d = DiscordEmbed(title=f'FINISHED SCANNING DIRECTORY', description=f'[ - ] URL: https://{domain} \n[ - ] WORDLIST: admin.txt', color='00FF00')
            directory.add_file(file=f.read(), filename='admindir.txt')
            directory.add_embed(d)
            directory.execute(d)        

        os.system("rm admindir.txt")

    if wordlistinput == "3":    
        w = "./wordlist/apache.txt"
        os.system(f"gobuster dir -u https://{domain}/ -w {w} > apachedir.txt")

        with open("apachedir.txt", "rb") as f:

            d = DiscordEmbed(title=f'FINISHED SCANNING DIRECTORY', description=f'[ - ] URL: https://{domain} \n[ - ] WORDLIST: apache.txt', color='00FF00')
            directory.add_file(file=f.read(), filename='admindir.txt')
            directory.add_embed(d)
            directory.execute(d)        

        os.system("rm apachedir.txt")

    if wordlistinput == "4":    
        w = "./wordlist/asp.txt"
        os.system(f"gobuster dir -u https://{domain}/ -w {w} > aspdir.txt")

        with open("aspdir.txt", "rb") as f:

            d = DiscordEmbed(title=f'FINISHED SCANNING DIRECTORY', description=f'[ - ] URL: https://{domain} \n[ - ] WORDLIST: asp.txt', color='00FF00')
            directory.add_file(file=f.read(), filename='aspdir.txt')
            directory.add_embed(d)
            directory.execute(d)        

        os.system("rm aspdir.txt")

    if wordlistinput == "5":    
        w = "./wordlist/backup.txt"
        os.system(f"gobuster dir -u https://{domain}/ -w {w} > backupdir.txt")

        with open("backupdir.txt", "rb") as f:

            d = DiscordEmbed(title=f'FINISHED SCANNING DIRECTORY', description=f'[ - ] URL: https://{domain} \n[ - ] WORDLIST: backup.txt', color='00FF00')
            directory.add_file(file=f.read(), filename='backupdir.txt')
            directory.add_embed(d)
            directory.execute(d)        

        os.system("rm backupdir.txt")

    if wordlistinput == "6":    
        w = "./wordlist/dll.txt"
        os.system(f"gobuster dir -u https://{domain}/ -w {w} > dlldir.txt")

        with open("dlldir.txt", "rb") as f:

            d = DiscordEmbed(title=f'FINISHED SCANNING DIRECTORY', description=f'[ - ] URL: https://{domain} \n[ - ] WORDLIST: dll.txt', color='00FF00')
            directory.add_file(file=f.read(), filename='dlldir.txt')
            directory.add_embed(d)
            directory.execute(d)        

        os.system("rm dlldir.txt")

    if wordlistinput == "7":    
        w = "./wordlist/jsp.txt"
        os.system(f"gobuster dir -u https://{domain}/ -w {w} > jspdir.txt")

        with open("jspdir.txt", "rb") as f:

            d = DiscordEmbed(title=f'FINISHED SCANNING DIRECTORY', description=f'[ - ] URL: https://{domain} \n[ - ] WORDLIST: jsp.txt', color='00FF00')
            directory.add_file(file=f.read(), filename='jspdir.txt')
            directory.add_embed(d)
            directory.execute(d)        

        os.system("rm jspdir.txt")

    if wordlistinput == "8":    
        w = "./wordlist/logs.txt"
        os.system(f"gobuster dir -u https://{domain}/ -w {w} > logsdir.txt")

        with open("logsdir.txt", "rb") as f:

            d = DiscordEmbed(title=f'FINISHED SCANNING DIRECTORY', description=f'[ - ] URL: https://{domain} \n[ - ] WORDLIST: logs.txt', color='00FF00')
            directory.add_file(file=f.read(), filename='logsdir.txt')
            directory.add_embed(d)
            directory.execute(d)        

        os.system("rm logsdir.txt")

    if wordlistinput == "9":    
        w = "./wordlist/php.txt"
        os.system(f"gobuster dir -u https://{domain}/ -w {w} > phpdir.txt")

        with open("phpdir.txt", "rb") as f:

            d = DiscordEmbed(title=f'FINISHED SCANNING DIRECTORY', description=f'[ - ] URL: https://{domain} \n[ - ] WORDLIST: php.txt', color='00FF00')
            directory.add_file(file=f.read(), filename='phpdir.txt')
            directory.add_embed(d)
            directory.execute(d)        

        os.system("rm phpdir.txt")

    if wordlistinput == "10":    
        w = "./wordlist/top_robotstxt_disallow.txt"
        os.system(f"gobuster dir -u https://{domain}/ -w {w} > top_robotsdisallowdir.txt")

        with open("top_robotsdisallowdir.txt", "rb") as f:

            d = DiscordEmbed(title=f'FINISHED SCANNING DIRECTORY', description=f'[ - ] URL: https://{domain} \n[ - ] WORDLIST: top_robotstxt_disallow.txt', color='00FF00')
            directory.add_file(file=f.read(), filename='robotsdir.txt')
            directory.add_embed(d)
            directory.execute(d)        

        os.system("rm top_robotsdisallowdir.txt")

    if wordlistinput == "11":    
        w = "./wordlist/kibana.txt"
        os.system(f"gobuster dir -u https://{domain}/ -w {w} > kibana.txt")

        with open("kibana.txt", "rb") as f:

            d = DiscordEmbed(title=f'FINISHED SCANNING DIRECTORY', description=f'[ - ] URL: https://{domain} \n[ - ] WORDLIST: top_robotstxt_disallow.txt', color='00FF00')
            directory.add_file(file=f.read(), filename='phpdir.txt')
            directory.add_embed(d)
            directory.execute(d)        

        os.system("rm kibana.txt")

    if wordlistinput == "12":    
        w = "./wordlist/pl.txt"
        os.system(f"gobuster dir -u https://{domain}/ -w {w} > pl.txt")

        with open("pl.txt", "rb") as f:

            d = DiscordEmbed(title=f'FINISHED SCANNING DIRECTORY', description=f'[ - ] URL: https://{domain} \n[ - ] WORDLIST: top_robotstxt_disallow.txt', color='00FF00')
            directory.add_file(file=f.read(), filename='pldir.txt')
            directory.add_embed(d)
            directory.execute(d)        

        os.system("rm pl.txt")

    if wordlistinput == "13":    
        w = "./wordlist/xml.txt"
        os.system(f"gobuster dir -u https://{domain}/ -w {w} > xml.txt")

        with open("pl.txt", "rb") as f:

            d = DiscordEmbed(title=f'FINISHED SCANNING DIRECTORY', description=f'[ - ] URL: https://{domain} \n[ - ] WORDLIST: top_robotstxt_disallow.txt', color='00FF00')
            directory.add_file(file=f.read(), filename='xmldir.txt')
            directory.add_embed(d)
            directory.execute(d)        

        os.system("rm xml.txt")

    if wordlistinput == "14":    
        w = "./wordlist/cgi-bin.txt"
        os.system(f"gobuster dir -u https://{domain}/ -w {w} > cgi-bin.txt")

        with open("cgi-bin.txt", "rb") as f:

            d = DiscordEmbed(title=f'FINISHED SCANNING DIRECTORY', description=f'[ - ] URL: https://{domain} \n[ - ] WORDLIST: top_robotstxt_disallow.txt', color='00FF00')
            directory.add_file(file=f.read(), filename='cgi-bindir.txt')
            directory.add_embed(d)
            directory.execute(d)        

        os.system("rm cgi-bin.txt")

    if wordlistinput == "15":    
        w = "./wordlist/mix.txt"
        os.system(f"gobuster dir -u https://{domain}/ -w {w} > mix.txt")

        with open("mix.txt", "rb") as f:

            d = DiscordEmbed(title=f'FINISHED SCANNING DIRECTORY', description=f'[ - ] URL: https://{domain} \n[ - ] WORDLIST: top_robotstxt_disallow.txt', color='00FF00')
            directory.add_file(file=f.read(), filename='mixdir.txt')
            directory.add_embed(d)
            directory.execute(d)        

        os.system("rm mix.txt")

    if wordlistinput == "16":    
        w = "./wordlist/php2.txt"
        os.system(f"gobuster dir -u https://{domain}/ -w {w} > php2.txt")

        with open("php2.txt", "rb") as f:

            d = DiscordEmbed(title=f'FINISHED SCANNING DIRECTORY', description=f'[ - ] URL: https://{domain} \n[ - ] WORDLIST: top_robotstxt_disallow.txt', color='00FF00')
            directory.add_file(file=f.read(), filename='php2dir.txt')
            directory.add_embed(d)
            directory.execute(d)        

        os.system("rm php2.txt")

    if wordlistinput == "17":    
        w = "./wordlist/jsf.txt"
        os.system(f"gobuster dir -u https://{domain}/ -w {w} > jsf.txt")

        with open("jsf.txt", "rb") as f:

            d = DiscordEmbed(title=f'FINISHED SCANNING DIRECTORY', description=f'[ - ] URL: https://{domain} \n[ - ] WORDLIST: top_robotstxt_disallow.txt', color='00FF00')
            directory.add_file(file=f.read(), filename='jsfdir.txt')
            directory.add_embed(d)
            directory.execute(d)        

        os.system("rm jsf.txt")

def nucleiscan():

    embed = DiscordEmbed(title=f'NUCLEI SCAN STARTED AGAINST: __{domain}__', color='0000FF')
    embed.set_image(url='https://cdn-icons-png.flaticon.com/512/3003/3003592.png')

    nuclei.add_embed(embed)
    nuclei.execute(remove_embeds=True, remove_files=True)

    os.system(f"subfinder -d {domain} | waybackurls | httpx | nuclei > ./LOGGER/{domain}/log.txt")

    with open(f'./LOGGER/{domain}/log.txt') as f:
        contents = f.read()
        w = "medium"
        if w in contents:
            vuln = DiscordEmbed(title=f'NUCLEI FOUND A VULNERABILITY', description=f'[ - ] URL: {domain}', color='00FF00')
            nuclei.add_file(file=f.read(), filename='log.txt')
            nuclei.add_embed(vuln)
            nuclei.execute(vuln)
        else:
            print("[!] not vulnerable! skipping...")
            notvuln = DiscordEmbed(title=f'NUCLEI DID NOT FOUND A VULNERABILITY BUT HERE IS THE LOG FOR INFORMATIONS', description=f'[ - ] URL: {domain}', color='FF0000')
            nuclei.add_file(file=f.read(), filename='log.txt')
            nuclei.add_embed(notvuln)
            nuclei.execute(notvuln)

            os.system(f"rm ./LOGGER/{domain}/log.txt")

def googlehacking():

    def r():
        soup = BeautifulSoup(page.content, "html5lib")
        links = soup.findAll("a")

        for link in links:
            link_href = link.get('href')
            if "url?q=" in link_href and not "webcache" in link_href:
                title = link.find_all('h3')
                if len(title) > 0:
                    print(title[0].getText())
                    print(link.get('href').split("?q=")[1].split("&sa=U")[0], file=open("webh.txt", "a"))
                    print("---")

    def l():

        checker = 'webh.txt'
        path = Path(checker)

        if path.is_file():

            with open("webh.txt", "rb") as f:

                g = DiscordEmbed(title=f'GOOGLE HACKING', description=f'[ - ] URL: https://{domain} \n[ - ] DORK: {dork}', color='00FF00')
                googleh.add_file(file=f.read(), filename='webh.txt')
                googleh.add_embed(g)
                googleh.execute(g)

                os.system("rm webh.txt")

        else:
            pass

    print("""
[1] Publicly exposed documents
[2] Directory listing vulnerabilities 
[3] Configuration files exposed
[4] Database files exposed
[5] Log files exposed
[6] Backup and old files
[7] Login pages
[8] SQL errors
[9] PHP errors / warning
[10] phpinfo()
[11] Search pastebin.com / pasting sites
[12] Search github.com and gitlab.com 
[13] Search stackoverflow.com
[14] Signup pages

[all] sends all the options at the same time but delayed.
    """)

    dork = input("dork option => ")

    results = 20

    if dork == "1":
        dork = "ext:doc | ext:docx | ext:odt | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv"
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

    if dork == "2":
        dork = "intitle:index.of"
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

    if dork == "3":
        dork = "ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini | ext:env"
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

    if dork == "4":
        dork = "ext:sql | ext:dbf | ext:mdb"
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

    if dork == "5":
        dork = "ext:log"
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

    if dork == "6":
        dork = "ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup"
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

    if dork == "7":
        dork = 'inurl:login | inurl:signin | intitle:Login | intitle:"sign in" | inurl:auth'
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

    if dork == "8":
        dork = 'intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()'
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

    if dork == "9":
        dork = '"PHP Parse error" | "PHP Warning" | "PHP Error"'
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

    if dork == "10":
        dork = 'ext:php intitle:phpinfo "published by the PHP Group"'
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

    if dork == "11":
        dork = "pastebin.com | site:paste2.org | site:pastehtml.com | site:slexy.org | site:snipplr.com | site:snipt.net | site:textsnip.com | site:bitpaste.app | site:justpaste.it | site:heypasteit.com | site:hastebin.com | site:dpaste.org | site:dpaste.com | site:codepad.org | site:jsitor.com | site:codepen.io | site:jsfiddle.net | site:dotnetfiddle.net | site:phpfiddle.org | site:ide.geeksforgeeks.org | site:repl.it | site:ideone.com | site:paste.debian.net | site:paste.org | site:paste.org.ru | site:codebeautify.org  | site:codeshare.io | site:trello.com"
        page = requests.get(f"https://www.google.com/search?q=site:{dork} {domain}")
        r()
        l()

    if dork == "12":
        dork = "github.com | site:gitlab.com"
        page = requests.get(f"https://www.google.com/search?q=site:{dork} {domain}")
        r()
        l()

    if dork == "13":
        dork = "stackoverflow.com"
        page = requests.get(f"https://www.google.com/search?q=site:{dork} {domain}")
        r()
        l()

    if dork == "14":
        dork = "inurl:signup | inurl:register | intitle:Signup"
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

    if dork == "all":

        embed = DiscordEmbed(title=f'FULL GOOGLEHACKING SCAN STARTED!', description=f'[ - ] TARGET: {domain} \n[ - ] DORKS: 14\n[ - ] ESTIMATED TIME TO BE DONE: 7 MINUTES', color='0000FF')
        embed.set_image(url='https://thehackernews.com/images/-t0syJYrfZA4/Xd5M5DAou8I/AAAAAAAA13A/GM5c_TEqqmkDAiqdmvNCcInVJ_-q1TEwgCLcBGAsYHQ/s728-e100/google-hacking.png')

        googleh.add_embed(embed)
        googleh.execute(remove_embeds=True, remove_files=True)

        time.sleep(10)

        #1
        dork = "ext:doc | ext:docx | ext:odt | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv"
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

        time.sleep(30)
        #2
        dork = "intitle:index.of"
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

        time.sleep(30)
        #3
        dork = "ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini | ext:env"
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

        time.sleep(30)
        #4
        dork = "ext:sql | ext:dbf | ext:mdb"
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

        time.sleep(30)
        #5
        dork = "ext:log"
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

        time.sleep(30)
        #6
        dork = "ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup"
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

        time.sleep(30)
        #7
        dork = 'inurl:login | inurl:signin | intitle:Login | intitle:"sign in" | inurl:auth'
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

        time.sleep(30)
        #8
        dork = 'intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()'
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

        time.sleep(30)
        #9
        dork = '"PHP Parse error" | "PHP Warning" | "PHP Error"'
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

        time.sleep(30)
        #10
        dork = 'ext:php intitle:phpinfo "published by the PHP Group"'
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

        time.sleep(30)

        #11
        dork = "pastebin.com | site:paste2.org | site:pastehtml.com | site:slexy.org | site:snipplr.com | site:snipt.net | site:textsnip.com | site:bitpaste.app | site:justpaste.it | site:heypasteit.com | site:hastebin.com | site:dpaste.org | site:dpaste.com | site:codepad.org | site:jsitor.com | site:codepen.io | site:jsfiddle.net | site:dotnetfiddle.net | site:phpfiddle.org | site:ide.geeksforgeeks.org | site:repl.it | site:ideone.com | site:paste.debian.net | site:paste.org | site:paste.org.ru | site:codebeautify.org  | site:codeshare.io | site:trello.com"
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

        time.sleep(30)

        #12
        dork = "github.com | site:gitlab.com"
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

        time.sleep(30)

        #13
        dork = "stackoverflow.com"
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

        time.sleep(30)

        #14
        dork = "inurl:signup | inurl:register | intitle:Signup"
        page = requests.get(f"https://www.google.com/search?q=site:{domain} {dork}")
        r()
        l()

        time.sleep(30)

option = input("option => ")

if option == "1":
    os.system("clear")
    domain = input("domain => ")
    os.system(f"mkdir ./LOGGER/{domain}")
    url = input("webhook => ")
    sqli = DiscordWebhook(url=f'{url}', username="sqli")
    sqliauto()

if option == "2":
    os.system("clear")
    domain = input("domain => ")
    os.system(f"mkdir ./LOGGER/{domain}")
    url = input("webhook => ")
    sensinfo = DiscordWebhook(url=f'{url}', username="sensinfo")
    ifinder()

if option == "3":
    os.system("clear")
    domain = input("domain => ")
    os.system(f"mkdir ./LOGGER/{domain}")
    url = input("webhook => ")
    xssw = DiscordWebhook(url=f'{url}', username="xss")
    xss()

if option == "4":
    os.system("clear")
    domain = input("domain => ")
    url = input("webhook => ")
    param = DiscordWebhook(url=f'{url}', username="paramspider")
    paramspider()

if option == "5":
    os.system("clear")
    domain = input("domain => ")
    os.system(f"mkdir ./LOGGER/{domain}")
    url = input("webhook => ")
    redirect = DiscordWebhook(url=f'{url}', username="openredirect")
    openr()

if option == "6":
    os.system("clear")
    domain = input("domain => ")
    url = input("webhook => ")
    print("""
[1] Normal
[2] Admin
[3] Apache
[4] ASP NET
[5] Backup 
[6] dll
[7] JSP
[8] Logs
[9] PHP
[10] Top robots.txt disallow
[11] Kibana
[12] PL
[13] XML
[14] CGI-BIN
[15] Mix
[16] PHP 2
[17] JSF
    """)    
    directory = DiscordWebhook(url=f'{url}', username="directory")
    directoryscan()

if option == "7":
    os.system("clear")
    domain = input("domain => ")
    os.system(f"mkdir ./LOGGER/{domain}")
    url = input("webhook => ")
    nuclei = DiscordWebhook(url=f'{url}', username="nuclei")
    nucleiscan()

if option == "8":
    os.system("clear")
    domain = input("domain => ")
    url = input("webhook => ")
    googleh = DiscordWebhook(url=f'{url}', username="googlehacking")
    googlehacking()
