# please dont read part 1 solution
def part1(input):
    with open(input, 'r') as f:
        lines = f.read().splitlines()
    
    joltages = []
    for line in lines:
        i = 0
        j = len(line) - 1
        bigi = 0
        bigj = 0
        while i != j:
            if int(line[i]) > int(line[bigi]):
                bigi = i
            i += 1
        
        for idx, _ in enumerate(line[bigi + 1:]):
            if int(line[bigi + 1:][idx]) > int(line[bigi + 1:][bigj]):
                bigj = idx
            
        bigj = bigj + bigi + 1

        joltages.append(int(line[bigi] + line[bigj]))
    
    print(sum(joltages))

def part2(input):
    with open(input, 'r') as f:
        lines = f.read().splitlines()

    joltages = []
    for line in lines:
        joltages.append(int(find_joltage(line, 0, 12)))

    print(sum(joltages))

def find_joltage(lst, start, length):
    if length == 0:
        return ''

    searchlist = lst[start:len(lst) - (length - 1)]
    big = 0

    for i, x in enumerate(searchlist):
        if int(x) > big:
            big = int(x)
            bigi = start + i

    return str(big) + find_joltage(lst, bigi + 1, length - 1)

part1('input.txt')
part2('input.txt')