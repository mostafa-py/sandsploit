#!/usr/bin/python3
import requests , json , sys , readline , re
sys.path.append("/opt/sandsploit/lib/")
from complator import *
host = None
name = "SDomins"
author = "@Aμιρ-0x0 (AMJ)"
info = "a Great Tool For Find websites on a Server ....\n"
def help():
    print ("author              to show author name")
    print ("help                to show this massage")
    print ("info                To show description of the tool ")
    print ("set                 to set options such as : [set host http://google.com/]")
    print ("show_options        to show options of Tools")
    print ("exit                to quit from Tool")
def options():
    print ("options               value")
    print ("==========            ============")
    print ("host                ",host)
    print(" \033[95mYou Must Enter URL \033[91mwithout \033[95mProtocol (Example : www.site.com or 127.0.0.1)")
    print(" \033[95mYou Must Write / at The End of URL EX: www.site.com")
def run():
    url = "https://domains.yougetsignal.com/domains.php"
    parameter = {"remoteAddress":host}
    req = requests.post(url , data=parameter , headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"})
    a = req.json()

    print (a['domainCount'],"site on server !\n")
    for i in a.get("domainArray",[]):
        print (i[0])

while True:
    try:
        
        
        option = input ("\033[96m┌─[SSF][\033[91m"+name+"\033[96m]\n└─▪ ")
        op2 = option.split(" ")
        if option == "help":
            help()
        elif option == "author":
            print (author)
        elif option == "info":
            print (info)

        elif option == "show_options":
            options()
        elif op2[0] == "set":
            if op2[1] == "host":
                host = op2[2]
                print ("host => ",host)
            else:
                print ("%s Not Found",op2[2])
        elif option == "run":
            run()
        elif option == "exit":
            break
        else:
            print ("Wrong Command ! ")
    except:
        print ('Unkonwn Error !')