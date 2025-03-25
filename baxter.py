# author : djunekz
# -*- coding: utf-8 -*-
#
import os
import sys
import fileinput

N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'

ask = G + '[' + W + 'Name File' + G + '] '
sukses = G + '[' + W + '√' + G + '] '
eror = R + '[' + W + '!' + R + ']'

os.system("clear")
print("""

\33[1;31m     ____             _____ _____ ____   
\33[1;31m    | __ )  __ _\33[1;33m__  _\33[1;31m|_   _| ____|  _ \  
\33[1;31m    |  _ \ / _` \ \33[1;33m\/ /\33[1;31m | | |  _| | |_) | \33[0m
\33[1;37m    | |_) | (_| |\33[1;33m>  < \33[1;37m | | | |___|  _ <  
\33[1;37m    |____/ \__,_/\33[1;33m_/\_\ \33[1;37m|_| |_____|_| \_\ \33[0m

   \33[1;34m Author\33[1;36m :\33[1;33m D J U N E K Z
   \33[1;34m GitHub\33[1;36m :\33[1;33m https://github.com/djunekz/baxter

 \33[1;31m [\33[1;36m Simple Tools for Encrypt and Decrypt files\33[1;31m ]
""").format(D,W,D,W,D,W,Y,W,D,W,D,W,D,W,D,W,D,Y,D,W,D,Y,D,G,W,G,D,G,W,G,Y,D,Y,D,Y,D,Y,D,Y)

banner2 = """
   {}[{}1{}]{} Encrypt     {}[{}2{}]{} Decrypt
""".format(G,W,G,W,G,W,G,W)

print banner2

def dekrip():
   try:
       sc = raw_input(ask + W + "Script " + G + "> " + W)
       f = open(sc,'r')
       filedata = f.read()
       f.close()

       newdata = filedata.replace("eval","echo")

       out = raw_input(ask + W + "Output" + G + " > " + W)
       f = open(out,'w')
       f.write(newdata)
       f.close()

       os.system("touch tes.sh")
       os.system("bash " + out + " > tes.sh")
       os.remove(out)
       os.system("mv -f tes.sh " + out)
       print (sukses + "Decrypt Successful...")

   except KeyboardInterrupt:
       print (eror + " Stopped!")
   except IOError:
       print (eror + " File Not Found!")

def enkrip():
   try:
       script = raw_input(ask + W + "Script " + G + "> " + W)
       f = open(script, 'r')
       filedata = f.read()
       f.close()
       output = raw_input(ask + W + "Output " + G + "> " + W)
       f = open(output, 'w')
       f.write(output)
       f.close()
       os.system("bash-obfuscate " + script + " -o " + output )
       print (sukses + " Encrypt Successful...")
   except KeyboardInterrupt:
       print (eror + " Stopped!")
   except IOError:
       print (eror + " File Not Found!")

takok = raw_input(W + "Choose" + G + " > ")

if takok == "1" or takok == "01":
   enkrip()
elif takok == "2" or takok == "02":
   dekrip()
else:
   print (eror + " Wrong input")
