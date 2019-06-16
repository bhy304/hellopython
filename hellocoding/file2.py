with open("tuple.py", mode="r", encoding="UTF8") as file:
    i = 0
    for line in file:
        print(i, line, end="")
        i += 1