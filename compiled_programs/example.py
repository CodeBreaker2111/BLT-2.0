import time

def main():
    v0 = 2
    v1 = 1
    v2 = " Hello World!"
    print(" Hello cute Chelsea!")
    time.sleep(v0)
    print(" Hello cute Rizo!")
    time.sleep(v1)
    print(v2)
    v2 = " Hello Big City!"
    print(v2)
    print(" Please type something:")
    v3 = input()
    print(v3)
    v4 = 0
    v4 = 50 + 50
    print(v4)
    v4 = 678 - 159
    print(v4)
    v4 = 50 * 50
    print(v4)
    v4 = 50 / 50
    print(v4)
    print(" Please type something:")
    v5 = input()
    print(" Please type something:")
    v6 = input()
    if v5 == v6 :
        print(" You typed the same thing twice!")
        time.sleep(1)
        print(" I hope ;)")
    if v5 != v6 :
        print(" You did not typed the same thing twice!")
        time.sleep(1)
        print(" I hope ;)")
    return "break"

main()