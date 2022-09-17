import os
import subprocess
import sys
import signal
import psutil
from tinydb import TinyDB, Query

fserver = "mohist.jar"
processes = TinyDB('db.json')

def config(s):
    wget = ["wget","-O","payload.zip",s]
    unzip = ["unzip", "payload"]
    cmd = [wget, unzip]
    for c in cmd:
        subprocess.run(c)

def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        try:
            proc.kill()
        except:
            print("Failed to kill ", proc)
    process.kill()

def runserver():
    #SET UP/CLEAR
    server_cmd = 'java -Xmx512m -Xms1g -jar ' + fserver
    try:
        os.remove('server_log.txt')
        os.remove('server_err.txt')
    except:
        pass
    server_log = open('server_log.txt', 'a')
    server_err = open('server_err.txt', 'a')
    
    #RUN PROCESS
    sproc = subprocess.Popen(server_cmd, stdout=server_log, stderr=server_err, shell=True)
    print("server pid = ", sproc.pid)
    #SAVE STATE
    processes.insert({'process':'server', 'pid':sproc.pid})

def backup(secret):
    #SET UP/CLEAR
    script = "python3 backup.py "  + secret
    try:
        os.remove('backup.out')
    except:
        pass
    backup_log = open('backup.out', 'a')
    
    #RUN PROCESS
    sproc = subprocess.Popen(script, stdout=backup_log, shell=True)
    print("backup pid = ", sproc.pid)
    #SAVE STATE
    processes.insert({'process':'backup', 'pid':sproc.pid})

def nuke():
    running = processes.all()
    if(running):
        for p in running:
            pid = p['pid']
            print("Killing ", pid) 
            kill(pid)
            q = Query()
            processes.remove(q.pid == pid)
    else:
        print("No processes found/spawned")

def main():
    ps = sys.argv[1]
    if(ps == "config"):
        config(sys.argv[2])
    elif(ps == "runserver" or  ps == "preet"):
        runserver()
    elif(ps == "databackup"):
        backup(sys.argv[2])
    elif(ps == "nuke"):
        nuke()
main()
