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
    indentation = 0
    indent = "    "

    Ocode = "import time\n\ndef main():"

    variables = []

    for line in IcodeLines:

        ItokenCode = line.split()

        if ItokenCode[0] == "print":
            if ItokenCode[1] == "string":
                if len(ItokenCode) > 4:

                    Print = ""
                    iteration = 0

                    for i in ItokenCode:
                        iteration += 1

                        if iteration >= 4:
                            Print = Print + " " + i
                    
                    Ocode = Ocode + "\n{}    print(\"{}\")".format(indent * indentation, Print)
                else:
                    if ItokenCode[3] == "\n":
                        Ocode = Ocode + "\n{}    print(\"\n\")".format(indent * indentation)
            
            if ItokenCode[1] == "variable":
                Ocode = Ocode + "\n{}    print({})".format(indent * indentation, "v" + ItokenCode[3])
        
        if ItokenCode[0] == "wait":
            if ItokenCode[2] == "seconds":
                Ocode = Ocode + "\n{}    time.sleep({})".format(indent * indentation, ItokenCode[1])
            
            if ItokenCode[1] == "variable":
                Ocode = Ocode + "\n{}    time.sleep({})".format(indent * indentation, "v" + ItokenCode[2])
        
        if ItokenCode[0] == "var":
            if ItokenCode[2] == "int":
                if ItokenCode[1] == "not-exists":
                    variables.append(int(ItokenCode[4]))

                    Ocode = Ocode + "\n{}    v{} = {}".format(indent * indentation, len(variables) - 1, ItokenCode[4])
                elif ItokenCode[1] == "exists":
                    try:
                        variables[int(ItokenCode[3])] = int(ItokenCode[4])

                        Ocode = Ocode + "\n{}    v{} = {}".format(indent * indentation, ItokenCode[3], ItokenCode[4])
                    except IndexError as E:
                        print("\nVariable does not exist. If you meant to create a new variable, set the first attribute to 0.\n")

                        print(E)
                        return E
                
            if ItokenCode[2] == "string":
                if len(ItokenCode) > 5:

                    var = ""
                    iteration = 0

                    for i in ItokenCode:
                        iteration += 1

                        if iteration >= 5:
                            var = var + " " + i
                        
                    if ItokenCode[1] == "not-exists":
                        variables.append(var)

                        Ocode = Ocode + "\n{}    v{} = \"{}\"".format(indent * indentation, len(variables) - 1, var)
                    elif ItokenCode[1] == "exists":
                        try:
                            variables[int(ItokenCode[3])] = var

                            Ocode = Ocode + "\n{}    v{} = \"{}\"".format(indent * indentation, ItokenCode[3], var)
                        except IndexError as E:
                            print("\nVariable does not exist. If you meant to create a new variable, set the first attribute to 0.\n")

                            print(E)
                            return E
            
            if ItokenCode[2] == "user-input":
                if ItokenCode[1] == "not-exists":
                    variables.append("")
                    Ocode = Ocode + "\n{}    v{} = input()".format(indent * indentation, len(variables) - 1, len(variables) - 1)
                elif ItokenCode[1] == "exists":
                    try:
                        variables[int(ItokenCode[3])] = input()
                    except IndexError as E:
                        print("\nVariable does not exist. If you meant to create a new variable, set the first attribute to 0.\n")

                        print(E)
                        return E
        
        if ItokenCode[0] == "break":
            Ocode = Ocode + "\n{}    return \"break\"".format(indent * indentation)
        
        if ItokenCode[0] == "add":
            num1 = 0
            num2 = 0
            answer = 0

            Ocode = Ocode + "\n{}    v{} =".format(indent * indentation, int(ItokenCode[5]))

            if ItokenCode[1] == "int":
                num1 = int(ItokenCode[2])
                Ocode = Ocode + " {}".format(ItokenCode[2])
            if ItokenCode[1] == "variable":
                num1 = data.variables[int(ItokenCode[2])]
                Ocode = Ocode + " v{}".format(ItokenCode[2])
            
            Ocode = Ocode + " +"
            
            if ItokenCode[3] == "int":
                num2 = int(ItokenCode[4])
                Ocode = Ocode + " {}".format(ItokenCode[4])
            if ItokenCode[3] == "variable":
                num2 = data.variables[int(ItokenCode[4])]
                Ocode = Ocode + " v{}".format(ItokenCode[4])
            
            answer = num1 + num2
            variables[int(ItokenCode[5])] = answer
        
        if ItokenCode[0] == "subtract":
            num1 = 0
            num2 = 0
            answer = 0

            Ocode = Ocode + "\n{}    v{} =".format(indent * indentation, int(ItokenCode[5]))

            if ItokenCode[1] == "int":
                num1 = int(ItokenCode[2])
                Ocode = Ocode + " {}".format(ItokenCode[2])
            if ItokenCode[1] == "variable":
                num1 = data.variables[int(ItokenCode[2])]
                Ocode = Ocode + " v{}".format(ItokenCode[2])
            
            Ocode = Ocode + " -"
            
            if ItokenCode[3] == "int":
                num2 = int(ItokenCode[4])
                Ocode = Ocode + " {}".format(ItokenCode[4])
            if ItokenCode[3] == "variable":
                num2 = data.variables[int(ItokenCode[4])]
                Ocode = Ocode + " v{}".format(ItokenCode[4])
            
            answer = num1 - num2
            variables[int(ItokenCode[5])] = answer
        
        if ItokenCode[0] == "multiply":
            num1 = 0
            num2 = 0
            answer = 0

            Ocode = Ocode + "\n{}    v{} =".format(indent * indentation, int(ItokenCode[5]))

            if ItokenCode[1] == "int":
                num1 = int(ItokenCode[2])
                Ocode = Ocode + " {}".format(ItokenCode[2])
            if ItokenCode[1] == "variable":
                num1 = data.variables[int(ItokenCode[2])]
                Ocode = Ocode + " v{}".format(ItokenCode[2])
            
            Ocode = Ocode + " *"
            
            if ItokenCode[3] == "int":
                num2 = int(ItokenCode[4])
                Ocode = Ocode + " {}".format(ItokenCode[4])
            if ItokenCode[3] == "variable":
                num2 = data.variables[int(ItokenCode[4])]
                Ocode = Ocode + " v{}".format(ItokenCode[4])
            
            answer = num1 * num2
            variables[int(ItokenCode[5])] = answer
        
        if ItokenCode[0] == "divide":
            num1 = 0
            num2 = 0
            answer = 0

            Ocode = Ocode + "\n{}    v{} =".format(indent * indentation, int(ItokenCode[5]))

            if ItokenCode[1] == "int":
                num1 = int(ItokenCode[2])
                Ocode = Ocode + " {}".format(ItokenCode[2])
            if ItokenCode[1] == "variable":
                num1 = data.variables[int(ItokenCode[2])]
                Ocode = Ocode + " v{}".format(ItokenCode[2])
            
            Ocode = Ocode + " /"
            
            if ItokenCode[3] == "int":
                num2 = int(ItokenCode[4])
                Ocode = Ocode + " {}".format(ItokenCode[4])
            if ItokenCode[3] == "variable":
                num2 = data.variables[int(ItokenCode[4])]
                Ocode = Ocode + " v{}".format(ItokenCode[4])
            
            answer = num1 / num2
            variables[int(ItokenCode[5])] = answer
        
        if ItokenCode[0] == "if":
            Ocode = Ocode + "\n{}    if ".format(indent * indentation)

            object1 = 0
            object2 = 0
            answer = False

            if ItokenCode[1] == "variable":
                Ocode = Ocode + "v{} ".format(ItokenCode[2])
            
            if ItokenCode[1] == "int":
                Ocode = Ocode + "{} ".format(ItokenCode[2])
            
            if ItokenCode[3] == "=" or ItokenCode[3] == "==": # Equal to
                Ocode = Ocode + "== "
            
            if ItokenCode[3] == ">": # Greater than
                Ocode = Ocode + "> "
            
            if ItokenCode[3] == "<": # Less than
                Ocode = Ocode + "< "
            
            if ItokenCode[3] == ">=": # Greater than or equal to
                Ocode = Ocode + ">= "
            
            if ItokenCode[3] == "<=": # Less than or equal to
                Ocode = Ocode + "<= "
            
            if ItokenCode[3] == "!=": # Not equal to
                Ocode = Ocode + "!= "
            
            if ItokenCode[4] == "variable":
                Ocode = Ocode + "v{}".format(ItokenCode[5])
            
            if ItokenCode[4] == "int":
                Ocode = Ocode + ItokenCode[5]
            
            Ocode = Ocode + " :"

            indentation += 1
        
        if ItokenCode[0] == "}":
            indentation -= 1
    
    Ocode = Ocode + "\n\nmain()"
    print("\nResult Code:\n\n" + Ocode)

    write_file(Opath, Ocode)

def compile_cpp(IcodeLines, Opath, machine_code):
    indentation = 0
    indent = "    "

    Ocode = "#include <iostream>\n#include <thread>\n#include <chrono>\n#include <string>\n\nusing namespace std;\n\nint main() {"

    variables = []

    for line in IcodeLines:

        ItokenCode = line.split()

        if ItokenCode[0] == "print":
            if ItokenCode[1] == "string":
                if len(ItokenCode) > 4:

                    Print = ""
                    iteration = 0

                    for i in ItokenCode:
                        iteration += 1

                        if iteration >= 4:
                            Print = Print + " " + i
                    
                    Ocode = Ocode + "\n    cout << \"{}\" << endl;".format(Print)
                else:
                    if ItokenCode[2] == "\n":
                        Ocode = Ocode + "\n{}    cout << endl;".format(indent * indentation)
            
            if ItokenCode[1] == "variable":
                if ItokenCode[2] == "to-string":
                    Ocode = Ocode + "\n    cout << to_string({}) << endl;".format("v" + ItokenCode[3])
                elif ItokenCode[2] == "null":
                    Ocode = Ocode + "\n    cout << {} << endl;".format("v" + ItokenCode[3])
        
        if ItokenCode[0] == "wait":
            if ItokenCode[2] == "seconds":
                Ocode = Ocode + "\n    this_thread::sleep_for(chrono::seconds({}));".format(ItokenCode[1])
            
            if ItokenCode[1] == "variable":
                Ocode = Ocode + "\n    this_thread::sleep_for(chrono::seconds({}));".format("v" + ItokenCode[2])
        
        if ItokenCode[0] == "var":
            if ItokenCode[2] == "int":
                if ItokenCode[1] == "not-exists":
                    variables.append(int(ItokenCode[4]))

                    Ocode = Ocode + "\n    int v{} = {};".format(len(variables) - 1, ItokenCode[4])
                elif ItokenCode[1] == "exists":
                    try:
                        variables[int(ItokenCode[3])] = int(ItokenCode[4])

                        Ocode = Ocode + "\n    v{} = {};".format(ItokenCode[3], ItokenCode[4])
                    except IndexError as E:
                        print("\nVariable does not exist. If you meant to create a new variable, set the first attribute to 0.\n")

                        print(E)
                        return E
                
            if ItokenCode[2] == "string":
                if len(ItokenCode) > 5:

                    var = ""
                    iteration = 0

                    for i in ItokenCode:
                        iteration += 1

                        if iteration >= 5:
                            var = var + " " + i
                        
                    if ItokenCode[1] == "not-exists":
                        variables.append(var)

                        Ocode = Ocode + "\n    string v{} = \"{}\";".format(len(variables) - 1, var)
                    elif ItokenCode[1] == "exists":
                        try:
                            variables[int(ItokenCode[3])] = var

                            Ocode = Ocode + "\n    v{} = \"{}\";".format(ItokenCode[3], var)
                        except IndexError as E:
                            print("\nVariable does not exist. If you meant to create a new variable, set the first attribute to 0.\n")

                            print(E)
                            return E
            
            if ItokenCode[2] == "user-input":
                if ItokenCode[1] == "not-exists":
                    variables.append("")
                    Ocode = Ocode + "\n    string v{} = \"\";\n    cin >> v{};".format(len(variables) - 1, len(variables) - 1)
                elif ItokenCode[1] == "exists":
                    try:
                        variables[int(ItokenCode[3])] = input()
                    except IndexError as E:
                        print("\nVariable does not exist. If you meant to create a new variable, set the first attribute to 0.\n")

                        print(E)
                        return E
        
        if ItokenCode[0] == "break":
            Ocode = Ocode + "\n    return 0;"
        
        if ItokenCode[0] == "add":
            num1 = 0
            num2 = 0
            answer = 0

            Ocode = Ocode + "\n    v{} =".format(int(ItokenCode[5]))

            if ItokenCode[1] == "int":
                num1 = int(ItokenCode[2])
                Ocode = Ocode + " {}".format(ItokenCode[2])
            if ItokenCode[1] == "variable":
                num1 = data.variables[int(ItokenCode[2])]
                Ocode = Ocode + " v{}".format(ItokenCode[2])
            
            Ocode = Ocode + " +"
            
            if ItokenCode[3] == "int":
                num2 = int(ItokenCode[4])
                Ocode = Ocode + " {}".format(ItokenCode[4])
            if ItokenCode[3] == "variable":
                num2 = data.variables[int(ItokenCode[4])]
                Ocode = Ocode + " v{}".format(ItokenCode[4])
            
            answer = num1 + num2
            variables[int(ItokenCode[5])] = answer

            Ocode = Ocode + ";"
        
        if ItokenCode[0] == "subtract":
            num1 = 0
            num2 = 0
            answer = 0

            Ocode = Ocode + "\n    v{} =".format(int(ItokenCode[5]))

            if ItokenCode[1] == "int":
                num1 = int(ItokenCode[2])
                Ocode = Ocode + " {}".format(ItokenCode[2])
            if ItokenCode[1] == "variable":
                num1 = data.variables[int(ItokenCode[2])]
                Ocode = Ocode + " v{}".format(ItokenCode[2])
            
            Ocode = Ocode + " -"
            
            if ItokenCode[3] == "int":
                num2 = int(ItokenCode[4])
                Ocode = Ocode + " {}".format(ItokenCode[4])
            if ItokenCode[3] == "variable":
                num2 = data.variables[int(ItokenCode[4])]
                Ocode = Ocode + " v{}".format(ItokenCode[4])
            
            answer = num1 - num2
            variables[int(ItokenCode[5])] = answer

            Ocode = Ocode + ";"
        
        if ItokenCode[0] == "multiply":
            num1 = 0
            num2 = 0
            answer = 0

            Ocode = Ocode + "\n    v{} =".format(int(ItokenCode[5]))

            if ItokenCode[1] == "int":
                num1 = int(ItokenCode[2])
                Ocode = Ocode + " {}".format(ItokenCode[2])
            if ItokenCode[1] == "variable":
                num1 = data.variables[int(ItokenCode[2])]
                Ocode = Ocode + " v{}".format(ItokenCode[2])
            
            Ocode = Ocode + " *"
            
            if ItokenCode[3] == "int":
                num2 = int(ItokenCode[4])
                Ocode = Ocode + " {}".format(ItokenCode[4])
            if ItokenCode[3] == "variable":
                num2 = data.variables[int(ItokenCode[4])]
                Ocode = Ocode + " v{}".format(ItokenCode[4])
            
            answer = num1 * num2
            variables[int(ItokenCode[5])] = answer

            Ocode = Ocode + ";"
        
        if ItokenCode[0] == "divide":
            num1 = 0
            num2 = 0
            answer = 0

            Ocode = Ocode + "\n    v{} =".format(int(ItokenCode[5]))

            if ItokenCode[1] == "int":
                num1 = int(ItokenCode[2])
                Ocode = Ocode + " {}".format(ItokenCode[2])
            if ItokenCode[1] == "variable":
                num1 = data.variables[int(ItokenCode[2])]
                Ocode = Ocode + " v{}".format(ItokenCode[2])
            
            Ocode = Ocode + " /"
            
            if ItokenCode[3] == "int":
                num2 = int(ItokenCode[4])
                Ocode = Ocode + " {}".format(ItokenCode[4])
            if ItokenCode[3] == "variablint":
                num2 = data.variables[int(ItokenCode[4])]
                Ocode = Ocode + " v{}".format(ItokenCode[4])
            
            answer = num1 / num2
            variables[int(ItokenCode[5])] = answer

            Ocode = Ocode + ";"
        
        if ItokenCode[0] == "if":
            Ocode = Ocode + "\n    if "

            object1 = 0
            object2 = 0
            answer = False

            if ItokenCode[1] == "variable":
                Ocode = Ocode + "( v{} ".format(ItokenCode[2])
            
            if ItokenCode[1] == "int":
                Ocode = Ocode + "( {} ".format(ItokenCode[2])
            
            if ItokenCode[3] == "=" or ItokenCode[3] == "==": # Equal to
                Ocode = Ocode + "== "
            
            if ItokenCode[3] == ">": # Greater than
                Ocode = Ocode + "> "
            
            if ItokenCode[3] == "<": # Less than
                Ocode = Ocode + "< "
            
            if ItokenCode[3] == ">=": # Greater than or equal to
                Ocode = Ocode + ">= "
            
            if ItokenCode[3] == "<=": # Less than or equal to
                Ocode = Ocode + "<= "
            
            if ItokenCode[3] == "!=": # Not equal to
                Ocode = Ocode + "!= "
            
            if ItokenCode[4] == "variable":
                Ocode = Ocode + "v{}".format(ItokenCode[5])
            
            if ItokenCode[4] == "int":
                Ocode = Ocode + ItokenCode[5]
            
            Ocode = Ocode + " ) {"
        
        if ItokenCode[0] == "}":
            Ocode = Ocode + "\n    }"
    
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