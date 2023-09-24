def main():
    print("exc = execute code, ccc = compile code to code")
    print("What action would you like to do? : ", end = "")

    action = input()

    if action == "exc":
        print("\nPlease enter the relative path to the file: ", end = "")
        path = input()

        return [1, path]
    elif action == "ccc":
        print("\nPlease enter relative path to the file you want to compile: ", end = "")
        Ipath = input()

        print("\nPlease enter relative path to the output: ", end = "")
        Opath = input()

        print("\nWhat language do you want to compile to?\npython, c++, machine code")
        code = input()

        return [2, Ipath, Opath, code]
    else:
        print("\nNo action selected\n")

        return [0]