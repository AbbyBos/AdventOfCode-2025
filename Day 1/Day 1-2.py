source = 'Python\AdventOfCode-2025\Day 1\Day 1 data.txt'
dial_place = 50
anwser = 0

with open(source, "r") as f:   
    lines = f.readlines()
    action_list = [line.strip() for line in lines]

for command in action_list:
    Direction = command[0]
    Amount = int(command[1:])
    for i in range(Amount):
        if Direction == 'R':
            dial_place += 1
        elif Direction == 'L':
            dial_place -= 1
        dial_place = dial_place%100
        if dial_place == 0:
            anwser += 1

print(anwser)
    
