import re

def solve1():
    fd = open("input.txt")
    txt = fd.read()

    tot = 0

    muls = re.findall(r"mul\(([0-9]+),([0-9]+)\)",txt)

    for i in muls:
        tot += int(i[0]) * int(i[1])

    print(tot)

def solve2():
    fd = open("input.txt")
    txt = fd.read()

    tot = 0

    enables = txt.split("do()")
    for i in enables:
        enable = i.split("don't()")[0]
        muls = re.findall(r"mul\(([0-9]+),([0-9]+)\)",enable)

        for j in muls:
            tot += int(j[0]) * int(j[1])

    print(tot)

solve1()
solve2()