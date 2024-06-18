import os
import sys 
import subprocess

# The subprocess module is a module used for executing programs and processes in the system

command = ["vagrant", "init", "ubuntu/focal64"]
command2 = ["vagrant", "up"]

dirPath = "/Users/malchiel.urias/Documents/KodeCamp/HandsOn/Python for DevOps"

sp = subprocess.Popen(command,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
sp2 = subprocess.Popen(command2,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)

# Define get_version function
def get_version():
    print("\nExecuting get_version() Function....\n")

    version = sys.version

    versionID = version[0:6]
    return versionID

# Define create function function
def create_folder():
    # prints statement on a newline
    print("\nExecuting create_folder() Function....\n")

    # create variable to hold getversion return value 
    vid = get_version()

    # check if 3 is in the return of get_version
    if "3" in vid:
        os.mkdir("kc_osFolder-%s"%vid) 

def chDir():
    os.chdir("resources")

def resource():
    dir = os.getcwd()

    # Is current directory /Users/malchiel.urias/Documents/KodeCamp/HandsOn/Python for DevOps?
    if dir == dirPath: 
        os.mkdir("resources")
        chDir()
    else:
        os.chdir(dirPath)
        os.mkdir("resources")
        chDir() 

def createResource():
    resource()
    sp 
    sp2

    


def main():
    print("Executing Main Function....")

    # Execute Get Version Function
    print(get_version())

    create_folder()

    # Execute createResource function
    createResource()


main()


