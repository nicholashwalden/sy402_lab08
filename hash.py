#!/usr/bin/python

import os
import sys
import subprocess
import hashlib
from datetime import datetime

def main(): 
    rootDirectory = "/usr"
    offLimits = ["/dev", "/proc", "/run", "/sys", "/tmp", "/var/lib", "/var/run"]
    fileList = []
    missingFiles= 0
    alteredFiles = 0
    newFiles = 0
    fileDictionary = {}

    f1 = open("hashes.txt", "r")
    for line in f1:
        list = line.split(";")
        #print(list)
        try:
            fileDictionary[list[0]] = list[1]
        except:
            continue

    for root, directories, files in os.walk(rootDirectory, topdown=False):
        for name in files:
            fileName = os.path.join(root, name)
            #print(fileName[0:4])
            #print(fileName[0:8])
            if fileName[0:4] not in offLimits and fileName[0:8] not in offLimits:
                fileList.append(fileName)
                #print(fileName)

    f = open("hashes.txt", "w")
    print("Missing or Altered Files:")
    for file in fileList:
        hash = hashFile(file)
        if hash == "failed":
            print("missing file: " + file)
            missingFiles = missingFiles + 1
            continue
        if file not in fileDictionary.keys():
            print("new file:" + file)
            newFiles = newFiles + 1
        try:
            if fileDictionary[file] != hash:
                print("altered file: " + file)
                alteredFiles = alteredFiles + 1
                continue
        except:
            f.write(file + ";" + str(hash) + ";" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n")

        f.write(file + ";" + str(hash) + ";" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n")
    
    print("Hashing Complete")    
    print(str(missingFiles) + " missing files")
    print(str(alteredFiles) + " altered files")
    print(str(newFiles) + " new files")

def hashFile(fileName):
    try:
        f = open(fileName, "rb")
        h = hashlib.sha256()
        h.update(f.read())
        #print(h.hexdigest())
        return(h.hexdigest())
    except:
        return("failed")
    

    #testing code
    #print("Filename: " + fileName)
    #print("SHA256: " + str(sha256Hashed))

if __name__=="__main__":
    main()
