import os
import subprocess
import sys

mserver = ""
fserver = ""

def config(s):
    wget = ["wget","-O","payload.zip",s]
    unzip = ["unzip", "payload"]
    move = ["mv", "mods/", "bin/"]
    cmd = [wget, unzip, move]
    for c in cmd:
        subprocess.run(c)
    for root, dirs, files in os.walk('bin/'):
        for f in files:
            if("forge" in f):
                fserver = f
            elif("minecraft_server" in f):
                mserver = f
    os.chdir('bin/')
    eula_gen = ['java', '-Xmx1g', '-Xms1g', '-jar', mserver]
    subprocess.run(eula_gen)
    
def runserver():
    os.chdir('bin/')
    run_gen = ['java', '-Xmx7g', '-Xms1g', '-jar', jserver]
    subprocess.run(run_gen)
    

def main():
    ps = sys.argv[1]
    if(ps == "config"):
        config(sys.argv[2])
    elif(ps == "runserver" or  ps == "preet"):
        runserver()
main()
