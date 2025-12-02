filepath = "day1input.txt"

with open(filepath, "r", encoding="utf-8") as input:
    lines = input.readlines()

curr = 50
zeros = 0
for line in lines:
    direction = line[0]
    turns = int(line[1:])
    if direction == "R":
        next = curr + turns
    else:
        next = curr - turns

    curr = next % 100
    
    if curr == 0:
        zeros += 1

print(zeros)