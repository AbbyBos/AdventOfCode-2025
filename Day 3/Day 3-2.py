Source = 'AdventOfCode-2025\Day 3\Day 3 data.txt'
data = []
awnser = 0
keep_numbers = 12

with open(Source, "r") as f:   
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    for line in lines:
        number_list = []
        for number in line:
            number_list.append(number)
        data.append(number_list)


def highest_number (data):
    removals_left = int(len(data)) - keep_numbers
    while removals_left > 0:    
        deletion_check = []
        for i in range(len(data)):
            permutation = data.copy()
            permutation.pop(i)
            number = ''
            for i in range(len(permutation)):
                number += permutation[i]
            deletion_check.append(number)   
        bigest_number = max(deletion_check)
        removals_left -= 1
        if removals_left != 0:
            data=[]
            for i in range(len(str(bigest_number))):
                data.append(str(bigest_number)[i])
    return(int(bigest_number)) 

for numberset in data:
    awnser += highest_number(numberset)

print(awnser)

    


    
    
    

    