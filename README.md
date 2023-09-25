# BLT-2.0

### Sorry about the README not being very readable. I also probably have a lot of typoes. I'm not good at spelling.

## Tutorial

### Coding

#### Basic stuff

The BLT has 8 main commands:

1. print: prints text to screen can be variable too
2. var: stores data including user input
3. wait: waits an amount of seconds can be a variable
4. break: ends the program with a return value of "break"
5. add: adds two numbers and writes the result to a variable
6. subtract: subtracts two numbers and writes the result to a variable
7. multiply: multiplies two numbers and writes the result to a variable
8. divide: divides two numbers and writes the result to a variable

This next program here (example.blt) explains some stuff in the comments:

```Lines without a semicolon at the beggining are comments. Place a semicolon at the beggining to make a line of code.

var says it's a variable, first attribute: 0 means to create a new variable, second attribute: 0 means integer, third attribute: null is placeholder text since variable is new, last attribute: 2 is value.
;var 0 0 null 2
;var 0 0 null 1

second attribute: 1 means the value is a string.
;var 0 1 null Hello World!

print says to print to the screen, first attribute: 0 says the value is not a variable, and last attribute: Hello vute Chelsie! is the value.
;print 0 0 Hello cute Chelsie!

wait says to wait time, first attribute: 1 says the value is a variable, and last attribute: 0 is the variable: 2
;wait 1 0
;print 0 0 Hello cute Rizo!

;print 0 0 \n
;wait 1 1

first attribute: 1 says it is a variable, the second attribute: 0 is aying that the variable is a string, and last attribute: 2 is the variable: Hello World!
;print 1 0 2

first attribute: 1 says this variable is not a new variable, and the third attribute: 2 is the variable to change: Hello World!
;var 1 1 2 Hello Big City!
;print 1 0 2

;print 0 Please type something

The second attribute: 2, is saying that the variable is taking user input.
;var 0 2
;print 1 0 3

;var 0 0 null 0

add says to use addition the first and third attributes: 0 say that both of the numbers are not variables, the second and fourth attributes: 50 are the values of the numbers, and the last attribute: 4 is the variable to write the answer to.
;add 0 50 0 50 4
;print 1 1 4

;var 0 1 4 0

subtract says to use subtraction
;subtract 0 678 0 159 4
;print 1 1 4

;var 0 1 4 0

multiply says to use multiplication
;multiply 0 50 0 50 4
;print 1 1 4

;var 0 1 4 0

divide says to use division
;divide 0 50 0 50 4
;print 1 1 4

This doesn't do much because it is at the end of the program, but break ends the program.
;break
```

#### Some quirks about the BLT

1. Lines beggining with a ';' are commands, lines with no ';' are comments.
2. Each command has a lot of attributes and most stuff is not automatick.
3. The BLT is VERY hard to read and I will fix that soon.

#### UI

This one is pretty selfexplanitory.

## How the BLT works

### UI

The UI is simple. 'ui.py' mages most of the UI. It first asks you what action you want to do, the some other stuff about the action if necisary and returns the action and attributes to main.py.

### Interpretting

The program 'run.py' handles this. It first splits up the program into a list of each line and discards all the comments. Then, it goes through a loop that keeps track of what line it is on. Each iteration of the loop, the code splits up each line into it's tokens. A token is each word which does mean with strings, they go through an overly complicated function to join the words into one string. For variables, a list keeps track of all of them. In the loop are a lot of if statements which eventually runs code.

### Compiling

Compiling code is pretty similar to interpretting code. The 'compileFile.py' handles this. I am planning on compiling code to bash, but right now these are the languages it compiles to:

1. Python
2. C++
3. Machine code

A lot of the code was just coppied from 'run.py' because I'm pretty much just rather than running the code on the spot, I write it to a file. I do not know any assembly at all, so I just used G++ since my code already compiles to C++.

## What is next for the BLT?

The next main feature I am going to add is readability. Due to commands using numbers to define attributes and variables not having names, it is very hard to read. Those two things I mentioned I will change in the next update.
