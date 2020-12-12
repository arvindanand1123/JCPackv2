import os
import subprocess
import sys
import signal
import pickle

fserver = "mohist.jar"
processes = []

def config(s):
    wget = ["wget","-O","payload.zip",s]
    unzip = ["unzip", "payload"]
    cmd = [wget, unzip]
    for c in cmd:
        subprocess.run(c)
    
def save_processes():
    running_processes = open('processes', 'ab')
    pickle.dump(processes, running_processes)
    running_processes.close()


def load_processes():
    running_processes

def runserver():
    #SET UP/CLEAR
    server_cmd = 'java -Xmx8g -Xms4g -jar ' + fserver
    os.remove('server_log.txt')
    os.remove('server_err.txt')
    server_log = open('server_log.txt', 'a')
    server_err = open('server_err.txt', 'a')
    
    #RUN PROCESS
    sproc = subprocess.Popen(server_cmd, stdout=server_log, stderr=server_err, shell=True)
    processes.append(sproc)

    #SAVE STATE
    save_processes()




def nuke():
    print("todo")



def main():
    ps = sys.argv[1]
    if(ps == "config"):
        config(sys.argv[2])
    elif(ps == "runserver" or  ps == "preet"):
        runserver()
    elif(ps == "backup"):
        #todo
        print("todo")
    elif(ps == "nuke"):
        nuke()
main()
