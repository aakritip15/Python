import urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)


import asyncio

from pyodide.http import pyfetch

import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt"


example1 = "example1.txt"
file1 = open(example1, "r")
print(file1.name)

FileContent = file1.read()
print(FileContent)

with open(example1, "r") as file1:
    print(file1.readline(20)) # does not read past the end of line
    print(file1.read(200)) # Returns the next 20 chars

with open("Example2.txt", "w") as writefile:
    writefile.write("This in line A\n")

with open("Example2.txt", "w") as writefile:
    writefile.write("This in line B\n")

with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n") 

with open('Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())


with open('Example2.txt', 'w+') as testwritefile:
    testwritefile.seek(0,0) #write at beginning of file
   
    testwritefile.write("Line 11" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("finished\n")
    testwritefile.seek(0,0)
    print(testwritefile.read())


with open('Example2.txt', 'r+') as testwritefile:
    testwritefile.seek(0,0) #write at beginning of file
   
    testwritefile.write("Line 11" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("finished\n")
    testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())

with open('Example1.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)