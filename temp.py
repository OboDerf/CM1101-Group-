
temp = "hello"

def menu2():
    print(temp)

def menu3(temp):
    print(temp)

def main():
    global temp
    print(temp)
    temp = "hi"
    menu2()
    menu3(temp)

if __name__ == "__main__":
    main()
