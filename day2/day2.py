

def solve1(list, gain):
    pos = 0
    for i in list:
        if pos != 0:
            if gain:
                diff = list[pos] - list[pos-1]
            else: diff = list[pos-1] - list[pos]
            if diff < 1 or diff > 3: return False
        pos += 1
    return True

def solve2(list, gain, removed = False):
    pos = 0
    for i in list:
        if pos != 0:
            if gain:
                diff = list[pos] - list[pos-1]
            else: diff = list[pos-1] - list[pos]
            if diff < 1 or diff > 3:
                if removed == False:
                    list2 = list.copy()
                    del list2[0]
                    if solve2(list2, not gain, True): return True
                    if solve2(list2, gain, True): return True

                    list2 = list.copy()
                    del list2[1]
                    if solve2(list2, not gain, True): return True
                    if solve2(list2, gain, True): return True

                    list2 = list.copy()
                    del list2[pos-1]
                    if solve2(list2, gain, True): return True

                    del list[pos]
                    if solve2(list, gain, True): return True

                    return False

                else:
                    return False
        pos += 1
    return True

fd = open('input.txt')
lists = fd.read().split('\n')

tot = 0
tot2 = 0
for i in lists:
    current = i.split(' ')
    for j in range(len(current)):
        current[j] = int(current[j])
    if current[1] > current[0]: gain = True
    else: gain = False
    if solve1(current, gain):
        tot += 1
    if solve2(current, gain):
        tot2 += 1

print(tot)
print(tot2)