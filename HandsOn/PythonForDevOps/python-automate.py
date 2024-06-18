# A module is collection of function to perform a tasks

# importing os module
import os 
import subprocess

# Create a variable. Saves a path in the variable.
dirVariable = "/Users/malchiel.urias/Documents/KodeCamp/HandsOn/Python for DevOps"

# Define command
command = ["vagrant", "up"]

# Getting the working directory. Equivalent to the linux command "$ pwd"
cwd = os.getcwd() 

# Check if dir exist
def check_dir():
    dirs = os.listdir("./")
    for dir in dirs:
        if dirs == "testcodes/":
            exist = "Directory exists"
        else:
            exist = "Directory does not exist"
    return exist
        
# Conditional Statement that creates dir if we are in dirVariable 
def create_dir():
    if cwd == dirVariable:
        dirExist = check_dir()
        if dirExist == "Directory does not exists":
            os.mkdir("testcodes/")
    else:
        os.chdir(dirVariable)
        os.mkdir("testcodes/")

def create_vm():
    # Execute Vagrant up command
    print("creating vm") 
    vagrant_sp = subprocess.Popen(command,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)

    vagrant_sp

def main():
    create_dir()
    create_vm()