Source = 'Python\AdventOfCode-2025\Day 2\Day 2 test.txt'
cleandata = []
invalid_ids = 0

with open(Source, "r") as f:   
    lines = f.readlines()
    lines = lines[0].split(',')
    for line in lines:
        cleanline = line.split('-')
        cleandata.append([int(cleanline[0]), int(cleanline[1])])

def is_mirrored_sequence(num):
    s = str(num)
    n = len(s)
    for l in range(1, n // 2 + 1):
        if n % l == 0:
            pattern = s[:n // 2]
            if pattern * 2 == s:
                return True
    return False

for data in cleandata:
    for current_id in range(data[0], data[1] + 1):
        if is_mirrored_sequence(current_id):
            print('Invalid ID', current_id)
            invalid_ids += current_id

print(invalid_ids)