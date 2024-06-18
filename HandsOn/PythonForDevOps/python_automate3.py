import os

def resource():
    dir = os.getcwd()

    name = "fake_dir"

    os.mkdir(name)

def main():
    resource()

main()