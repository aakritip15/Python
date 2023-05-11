from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        
        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))
        writefile.seek(0,0)
        print(writefile.read())

    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))
        writefile.seek(0,0)
        print(writefile.read())

genFiles(memReg,exReg)

def cleanFiles(currentMem, exMem):
    # TODO: Open the currentMem file as in r+ mode
    with open(currentMem, 'r+') as current:
        with open(exMem, 'a+') as ex:
            data= current.readlines()

            header = data[0]
            data.pop(0)
            innactive = [ line for line in data if('no' in line)]
            current.seek(0,0)
            current.write(header)
            for line in data:
                if(line in innactive):
                    ex.write(line)
                else:
                    current.write(line)
            current.truncate() 

memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
                