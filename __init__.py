print("Initializing...")

import os

directory_path = "programs"
directory_path2 = "compiled_programs"

if not os.path.exists(directory_path):
    os.makedirs(directory_path)

if not os.path.exists(directory_path2):
    os.makedirs(directory_path2)

with open("{}/example.blt".format(directory_path), "w") as f:
    f.write("Lines without a semicolon at the beggining are comments. Place a semicolon at the beggining to make a line of code.\n\nvar says it's a variable, first attribute: 0 means to create a new variable, second attribute: 0 means integer, third attribute: null is placeholder text since variable is new, last attribute: 2 is value.\n;var 0 0 null 2\n;var 0 0 null 1\n\nsecond attribute: 1 means the value is a string.\n;var 0 1 null Hello World!\n\nprint says to print to the screen, first attribute: 0 says the value is not a variable, and last attribute: Hello vute Chelsie! is the value.\n;print 0 Hello cute Chelsie!\n\nwait says to wait time, first attribute: 1 says the value is a variable, and last attribute: 0 is the variable: 2\n;wait 1 0\n\n;print 0 Hello cute Rizo!\n\n;print 0 \\n\n;wait 1 1\n\nfirst attribute: 1 says it is a variable, and last attribute: 2 is the variable: Hello World!\n;print 1 2\n\nfirst attribute: 1 says this variable is not a new variable, and the third attribute: 2 is the variable to change: Hello World!\n;var 1 1 2 Hello Big City!\n;print 1 2\n")

print("Initialization complete.")