import os;

if __name__ == "__main__":
    fileName = "C:\\abc\\test.pom"
    if os.path.isfile(fileName):
        print(fileName + " exists!")
    else:
        print(fileName + " does NOT exists!")