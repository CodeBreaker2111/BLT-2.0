import subprocess
import os

def main(Ipath, Opath, code):
    print("Compiling {} into {}...".format(Ipath, Opath))

    read(Ipath, Opath, code)

def read(Ipath, Opath, code):
    Icode = ""
    IcodeLines = []

    Ocode = "import time\n\ndef main():"

    try:
        with open(Ipath, "r") as f:
            Icode = f.read()
    except FileNotFoundError as E:
        print("\nFile does not exist.\n{}".format(E))
    
    IcodeLines = [line.lstrip(';').strip() for line in Icode.split('\n') if line.startswith(';')]

    if code == "python":
        compile_python(IcodeLines, Opath)
    
    if code == "c++":
        compile_cpp(IcodeLines, Opath, False)
    
    if code == "machine code":
        compile_cpp(IcodeLines, Opath, True)

def compile_python(IcodeLines, Opath):
    Ocode = "import time\n\ndef main():"

    variables = []

    for line in IcodeLines:

        ItokenCode = line.split()

        if ItokenCode[0] == "print":
            if ItokenCode[1] == "0":
                if len(ItokenCode) > 3:

                    Print = ""
                    iteration = 0

                    for i in ItokenCode:
                        iteration += 1

                        if iteration >= 3:
                            Print = Print + " " + i
                    
                    Ocode = Ocode + "\n    print(\"{}\")".format(Print)
                else:
                    if ItokenCode[2] == "\n":
                        Ocode = Ocode + "\n    print(\"\n\")"
            
            if ItokenCode[1] == "1":
                Ocode = Ocode + "\n    print({})".format("v" + ItokenCode[2])
        
        if ItokenCode[0] == "wait":
            if ItokenCode[1] == "0":
                Ocode = Ocode + "\n    time.sleep({})".format(ItokenCode[2])
            
            if ItokenCode[1] == "1":
                Ocode = Ocode + "\n    time.sleep({})".format("v" + ItokenCode[2])
        
        if ItokenCode[0] == "var":
            if ItokenCode[2] == "0":
                if ItokenCode[1] == "0":
                    variables.append(int(ItokenCode[4]))

                    Ocode = Ocode + "\n    v{} = {}".format(len(variables) - 1, ItokenCode[4])
                elif ItokenCode[1] == "1":
                    try:
                        variables[int(ItokenCode[3])] = int(ItokenCode[4])

                        Ocode = Ocode + "\n    v{} = {}".format(ItokenCode[3], ItokenCode[4])
                    except IndexError as E:
                        print("\nVariable does not exist. If you meant to create a new variable, set the first attribute to 0.\n")

                        print(E)
                        return E
                
            if ItokenCode[2] == "1":
                if len(ItokenCode) > 5:

                    var = ""
                    iteration = 0

                    for i in ItokenCode:
                        iteration += 1

                        if iteration >= 5:
                            var = var + " " + i
                        
                    if ItokenCode[1] == "0":
                        variables.append(var)

                        Ocode = Ocode + "\n    v{} = \"{}\"".format(len(variables) - 1, var)
                    else:
                        try:
                            variables[int(ItokenCode[3])] = var

                            Ocode = Ocode + "\n    v{} = \"{}\"".format(ItokenCode[3], var)
                        except IndexError as E:
                            print("\nVariable does not exist. If you meant to create a new variable, set the first attribute to 0.\n")

                            print(E)
                            return E
            
            if ItokenCode[2] == "2":
                if ItokenCode[1] == "0":
                    Ocode = Ocode + "\n    v{} = input()".format(len(variables) - 1, len(variables) - 1)
                elif ItokenCode[1] == "1":
                    try:
                        variables[int(ItokenCode[3])] = input()
                    except IndexError as E:
                        print("\nVariable does not exist. If you meant to create a new variable, set the first attribute to 0.\n")

                        print(E)
                        return E
        
        if ItokenCode[0] == "break":
            Ocode = Ocode + "\n    return \"break\""
    
    Ocode = Ocode + "\n\nmain()"
    print("\nResult Code:\n\n" + Ocode)

    write_file(Opath, Ocode)

def compile_cpp(IcodeLines, Opath, machine_code):
    Ocode = "#include <iostream>\n#include <thread>\n#include <chrono>\n#include <string>\n\nusing namespace std;\n\nint main() {"

    variables = []

    for line in IcodeLines:

        ItokenCode = line.split()

        if ItokenCode[0] == "print":
            if ItokenCode[1] == "0":
                if len(ItokenCode) > 3:

                    Print = ""
                    iteration = 0

                    for i in ItokenCode:
                        iteration += 1

                        if iteration >= 3:
                            Print = Print + " " + i
                    
                    Ocode = Ocode + "\n    cout << \"{}\" << endl;".format(Print)
                else:
                    if ItokenCode[2] == "\n":
                        Ocode = Ocode + "\n    cout << endl;"
            
            if ItokenCode[1] == "1":
                Ocode = Ocode + "\n    cout << {} << endl;".format("v" + ItokenCode[2])
        
        if ItokenCode[0] == "wait":
            if ItokenCode[1] == "0":
                Ocode = Ocode + "\n    this_thread::sleep_for(chrono::seconds({}));".format(ItokenCode[2])
            
            if ItokenCode[1] == "1":
                Ocode = Ocode + "\n    this_thread::sleep_for(chrono::seconds({}));".format("v" + ItokenCode[2])
        
        if ItokenCode[0] == "var":
            if ItokenCode[2] == "0":
                if ItokenCode[1] == "0":
                    variables.append(int(ItokenCode[4]))

                    Ocode = Ocode + "\n    int v{} = {};".format(len(variables) - 1, ItokenCode[4])
                elif ItokenCode[1] == "1":
                    try:
                        variables[int(ItokenCode[3])] = int(ItokenCode[4])

                        Ocode = Ocode + "\n    v{} = {};".format(ItokenCode[3], ItokenCode[4])
                    except IndexError as E:
                        print("\nVariable does not exist. If you meant to create a new variable, set the first attribute to 0.\n")

                        print(E)
                        return E
                
            if ItokenCode[2] == "1":
                if len(ItokenCode) > 5:

                    var = ""
                    iteration = 0

                    for i in ItokenCode:
                        iteration += 1

                        if iteration >= 5:
                            var = var + " " + i
                        
                    if ItokenCode[1] == "0":
                        variables.append(var)

                        Ocode = Ocode + "\n    string v{} = \"{}\";".format(len(variables) - 1, var)
                    else:
                        try:
                            variables[int(ItokenCode[3])] = var

                            Ocode = Ocode + "\n    v{} = \"{}\";".format(ItokenCode[3], var)
                        except IndexError as E:
                            print("\nVariable does not exist. If you meant to create a new variable, set the first attribute to 0.\n")

                            print(E)
                            return E
            
            if ItokenCode[2] == "2":
                if ItokenCode[1] == "0":
                    Ocode = Ocode + "\n    string v{} = \"\";\n    cin << v{};".format(len(variables) - 1, len(variables) - 1)
                elif ItokenCode[1] == "1":
                    try:
                        variables[int(ItokenCode[3])] = input()
                    except IndexError as E:
                        print("\nVariable does not exist. If you meant to create a new variable, set the first attribute to 0.\n")

                        print(E)
                        return E
        
        if ItokenCode[0] == "break":
            Ocode = Ocode + "\n    return 0;"
    
    Ocode = Ocode + "\n}"

    if machine_code == False:
        print("\nResult Code:\n\n" + Ocode)
        write_file(Opath, Ocode)
    
    elif machine_code == True:
        print("\nResult c++ Code:\n\n" + Ocode)
        write_file(".f.cpp", Ocode)
        cpp_machine_code(Opath)
        os.remove(".f.cpp")

def cpp_machine_code(outputPath):
    subprocess.call(["g++", "-o", outputPath, ".f.cpp"])

def write_file(Opath, Ocode):
    with open(Opath, "w") as f:
        f.write(Ocode)
    
    print("\n\nCode sucseffuly compiled.")