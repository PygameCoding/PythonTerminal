from random import randint

running = 1




def do(argument1):
    runner = open("Runner.py", "a+")
    runner.close()
    runner = open("Runner.py", "a+")
    runner.write("\n" + argument1)
    runner.close()
    with open("Runner.py") as f:
        output = exec(f.read())
    return(output)




while running == 1:
    userinput = input(": ")
    lis = list(userinput)
    if lis[len(lis) - 1] == "#":
        runner = open("Runner.py", "w")
        runner.truncate()
        runner.close()
        y = 0
        userinput = ""
        while y < len(lis) - 1:
            userinput += lis[y]
            y += 1
    


    if userinput == "stop(True)":
        running = 0
    elif userinput == "help()":
        print("help() shows commands")
        print("stop(True) stops program")
        print("clear() clears data")
        print("nl() newline")
    elif userinput == "clear()":
        runner = open("Runner.py", "w")
        runner.truncate()

    elif userinput == "nl()":
        userinput = ""
    
    out = do(userinput)
        
    print(out)
    

