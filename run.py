import data as data
import subprocess
import time

rawCode = ""
ocode = []

def split_code(code):
    lines = code.split('\n')
    result_list = [line.lstrip(';').strip() for line in lines if line.startswith(';')]

    print("\n")
    return result_list

def main(code):
    rawCode = code
    ocode = split_code(rawCode)

    interpret(ocode)

def interpret(code):
    subprocess.call(["clear"])

    lineNum = 0
    while True:
        tokenCode = code[lineNum].split()

        if tokenCode[0] == "print":
            if tokenCode[1] == "0":
                if len(tokenCode) > 3:

                    Print = ""
                    iteration = 0

                    for i in tokenCode:
                        iteration += 1

                        if iteration >= 3:
                            Print = Print + " " + i
                    
                    print(Print)
                else:
                    if tokenCode[2] == "\n":
                        print("\n")
            
            if tokenCode[1] == "1":
                print(data.variables[int(tokenCode[2])])
        
        if tokenCode[0] == "wait":
            if tokenCode[1] == "0":
                time.sleep(int(tokenCode[2]))
            
            if tokenCode[1] == "1":
                time.sleep(data.variables[int(tokenCode[2])])
        
        if tokenCode[0] == "var":
            if tokenCode[2] == "0":
                if tokenCode[1] == "0":
                    data.variables.append(int(tokenCode[4]))
                elif tokenCode[1] == "1":
                    try:
                        data.variables[int(tokenCode[3])] = int(tokenCode[4])
                    except IndexError as E:
                        print("\nVariable does not exist. If you meant to create a new variable, set the first attribute to 0.\n")

                        print(E)
                        return E
                
            if tokenCode[2] == "1":
                if len(tokenCode) > 5:

                    var = ""
                    iteration = 0

                    for i in tokenCode:
                        iteration += 1

                        if iteration >= 5:
                            var = var + " " + i
                        
                    if tokenCode[1] == "0":
                        data.variables.append(var)
                    else:
                        try:
                            data.variables[int(tokenCode[3])] = var
                        except IndexError as E:
                            print("\nVariable does not exist. If you meant to create a new variable, set the first attribute to 0.\n")

                            print(E)
                            return E
            
            if tokenCode[2] == "2":
                if tokenCode[1] == "0":
                    data.variables.append(input())
                elif tokenCode[1] == "1":
                    try:
                        data.variables[int(tokenCode[3])] = input()
                    except IndexError as E:
                        print("\nVariable does not exist. If you meant to create a new variable, set the first attribute to 0.\n")

                        print(E)
                        return E
        
        if tokenCode[0] == "break":
            break
        
        lineNum += 1

        if lineNum >= len(code):
            break
