source = 'Python\AdventOfCode-2025\Day 1\Day 1 test.txt'
dial_place = 50
anwser = 0

with open(source, "r") as f:   
    lines = f.readlines()
    action_list = [line.strip() for line in lines]

for command in action_list:
    Direction = command[0]
    Amount = int(command[1:])
    if Direction == 'R':
        dial_place += Amount
    elif Direction == 'L':
        dial_place -= Amount
    dial_place = dial_place%100
    if dial_place == 0:
        anwser += 1
        
print(anwser)
    
