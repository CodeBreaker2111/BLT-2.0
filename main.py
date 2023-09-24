import run as exCode
import ui as userInterface
import compileFile as compileFile

def main():
    uiResults = userInterface.main()

    if uiResults[0] == 1:
        run_file(uiResults[1])
    
    if uiResults[0] == 2:
        compile_file(uiResults[1], uiResults[2], uiResults[3])

def run_file(path):
    print("\nOpening File {}...".format(path))

    try:
        with open(path, "r") as f:
            print("Succsefully opened the file {}.".format(path))
            exCode.main(f.read())
    except FileNotFoundError as E:
        print("\nAn error has occured. The file you entered does not exist")
        print(E)
    #except:
        #print("\nAn error has occured")

def compile_file(Ipath, Opath, code):
    compileFile.main(Ipath, Opath, code)



main()