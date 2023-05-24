from random import randint

running = 1

runner = open("Runner.py", "w")
runner.truncate()

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
    if userinput == "stop(True)":
        running = 0
    elif userinput == "help()":
        print("help() shows commands")
        print("stop(True) stops program")
        print("clear() clears data")
    elif userinput == "clear()":
        runner = open("Runner.py", "w")
        runner.truncate()
    else:
        out = do(userinput)
        runner = open("Runner.py", "a+")
        runner.truncate()
        runner.close()
    print(out)
    

