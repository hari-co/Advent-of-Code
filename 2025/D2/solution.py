def part1(input):
    with open(input, 'r') as f:
        text = f.read()
        ranges = text.split(',')
    
    sum = 0
    for ids in ranges:
        start = int(ids.split('-')[0])
        end = int(ids.split('-')[1])
        for i in range(start, end + 1):
            stringi = str(i)
            if stringi[:len(stringi)//2] == stringi[len(stringi)//2:]:
                sum += i

    print(sum)

def part2(input):
    with open(input, 'r') as f:
        text = f.read()
        ranges = text.split(',')
    
    sum = 0
    for ids in ranges:
        start = int(ids.split('-')[0])
        end = int(ids.split('-')[1])
        for i in range(start, end + 1):
            if findrepeat(i):
                sum += i

    print(sum)

def findrepeat(num):
    stringnum = str(num)
    pattern = ''
    for x in stringnum:
        pattern = pattern + x

        if len(pattern) == len(stringnum):
            return False
    
        if len(stringnum) % len(pattern) != 0:
            continue

        if stringnum == pattern * (len(stringnum) // len(pattern)):
            return True

part1('input.txt')
part2('input.txt')