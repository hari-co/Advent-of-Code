def part1(input):
    with open(input, 'r') as f:
        lines = f.read().splitlines()
    
    rollcount = 0

    for linenum, line in enumerate(lines):
        for i, x in enumerate(line):
            neighbours = []
            if linenum == 0:
                neighbours.append(lines[linenum + 1][i])
                if i == 0:
                    neighbours.append(line[i + 1])
                    neighbours.append(lines[linenum + 1][i + 1])
                elif i == len(line) - 1:
                    neighbours.append(line[i - 1])
                    neighbours.append(lines[linenum + 1][i - 1])
                else:
                    neighbours.append(line[i + 1])
                    neighbours.append(lines[linenum + 1][i + 1])
                    neighbours.append(line[i - 1])
                    neighbours.append(lines[linenum + 1][i - 1])
            elif linenum == len(lines) - 1:
                neighbours.append(lines[linenum - 1][i])
                if i == 0:
                    neighbours.append(line[i + 1])
                    neighbours.append(lines[linenum - 1][i + 1])
                elif i == len(line) - 1:
                    neighbours.append(line[i - 1])
                    neighbours.append(lines[linenum - 1][i - 1])
                else:
                    neighbours.append(line[i + 1])
                    neighbours.append(lines[linenum - 1][i + 1])
                    neighbours.append(line[i - 1])
                    neighbours.append(lines[linenum - 1][i - 1])
            else:
                neighbours.append(lines[linenum + 1][i])
                neighbours.append(lines[linenum - 1][i])
                if i == 0:
                    neighbours.append(line[i + 1])
                    neighbours.append(lines[linenum + 1][i + 1])
                    neighbours.append(lines[linenum - 1][i + 1])
                elif i == len(line) - 1:
                    neighbours.append(line[i - 1])
                    neighbours.append(lines[linenum + 1][i - 1])
                    neighbours.append(lines[linenum - 1][i - 1])
                else:
                    neighbours.append(line[i + 1])
                    neighbours.append(lines[linenum + 1][i + 1])
                    neighbours.append(lines[linenum - 1][i + 1])
                    neighbours.append(line[i - 1])
                    neighbours.append(lines[linenum + 1][i - 1])
                    neighbours.append(lines[linenum - 1][i - 1])

            if x == '@' and neighbours.count('@') <= 3:
                rollcount += 1
                
    print(rollcount)

def part2(input):
    with open(input, 'r') as f:
        lines = f.read().splitlines()
    print(removerolls(lines, 0))

def removerolls(lines, rollcount):
    accessible = set()
    oldcount = rollcount

    for linenum, line in enumerate(lines):
        lines[linenum] = list(line)
        for i, x in enumerate(line):
            neighbours = []
            if linenum == 0:
                neighbours.append(lines[linenum + 1][i])
                if i == 0:
                    neighbours.append(line[i + 1])
                    neighbours.append(lines[linenum + 1][i + 1])
                elif i == len(line) - 1:
                    neighbours.append(line[i - 1])
                    neighbours.append(lines[linenum + 1][i - 1])
                else:
                    neighbours.append(line[i + 1])
                    neighbours.append(lines[linenum + 1][i + 1])
                    neighbours.append(line[i - 1])
                    neighbours.append(lines[linenum + 1][i - 1])
            elif linenum == len(lines) - 1:
                neighbours.append(lines[linenum - 1][i])
                if i == 0:
                    neighbours.append(line[i + 1])
                    neighbours.append(lines[linenum - 1][i + 1])
                elif i == len(line) - 1:
                    neighbours.append(line[i - 1])
                    neighbours.append(lines[linenum - 1][i - 1])
                else:
                    neighbours.append(line[i + 1])
                    neighbours.append(lines[linenum - 1][i + 1])
                    neighbours.append(line[i - 1])
                    neighbours.append(lines[linenum - 1][i - 1])
            else:
                neighbours.append(lines[linenum + 1][i])
                neighbours.append(lines[linenum - 1][i])
                if i == 0:
                    neighbours.append(line[i + 1])
                    neighbours.append(lines[linenum + 1][i + 1])
                    neighbours.append(lines[linenum - 1][i + 1])
                elif i == len(line) - 1:
                    neighbours.append(line[i - 1])
                    neighbours.append(lines[linenum + 1][i - 1])
                    neighbours.append(lines[linenum - 1][i - 1])
                else:
                    neighbours.append(line[i + 1])
                    neighbours.append(lines[linenum + 1][i + 1])
                    neighbours.append(lines[linenum - 1][i + 1])
                    neighbours.append(line[i - 1])
                    neighbours.append(lines[linenum + 1][i - 1])
                    neighbours.append(lines[linenum - 1][i - 1])

            if x == '@' and neighbours.count('@') <= 3:
                rollcount += 1
                accessible.add((linenum, i))
    if rollcount == oldcount:
        return rollcount
    
    for x in accessible:
        linenum = x[0]
        i = x[1]
        lines[linenum][i] = '.'

    return removerolls(lines, rollcount)

part1('input.txt')
part2('input.txt')