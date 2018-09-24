import os
import re
import fnmatch
#startdigits = re.compile(r"^\d+")

def isSpace():
    for filename in os.listdir("."):
        if filename.endswith(".m4a"):
            newFileName = filename
            while filename[0].isspace():
                newFileName = newFileName[1:]
            if newFileName != filename:
                print("Renaming %s to %s" % (filename, newFileName))
def isNumber():
    for filename in os.listdir("."):
        if filename.endswith("m4a"):
            newFileName = filename
            while filename[0].isdigit():
                newFileName = newFileName[1:]
            if newFileName != filename:
                print("Renaming %s to %s" % (filename, newFileName))
                os.rename(filename, newFileName)

