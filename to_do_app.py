
choose = input("Please specify a command [list, add, mark, archive]: ")

if choose == "add":
    with open("to_do_list.txt", "a") as f:
        new = input("Add your task here: ")
        f.write(new)
        f.write("\n")

elif choose == "list":
    with open("to_do_list.txt", "r") as f:
        print(f.read())

elif choose == "mark":
    with open("to_do_list.txt", "r+") as f:
        lines = f.readlines()

    for line in lines:
        print(line)

    mark = int(input("Which one you want to mark as completed: "))
    with open("to_do_list.txt", "w") as f:
        for i, v in enumerate(lines):
            print(i , v)
            if i+1 == mark:
                f.write(v + "[X] ")
            else:
                f.write(v)

elif choose == "archive":
    with open("to_do_list.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        print(line)
    with open("to_do_list.txt", "w") as f:
        for i ,v in enumerate(lines):
            if v [:3] != "[X]":
                f.write(v)
