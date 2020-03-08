import os
import subprocess
import sys

def config(s):
    wget = ["wget","-O","payload.zip",s]
    unzip = ["unzip", "payload"]
    cmd = [wget, unzip]
    for c in cmd:
        subprocess.run(c)
    

def main():
    ps = sys.argv[1]
    if(ps == "config"):
        config(sys.argv[2])

main()
