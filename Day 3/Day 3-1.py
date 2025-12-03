Source = 'AdventOfCode-2025\Day 3\Day 3 data.txt'
data = []
anwser = 0

with open(Source, "r") as f:   
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    for line in lines:
        number_list = []
        for number in line:
            number_list.append(number)
        data.append(number_list)


def highest_number (data):
    solution = []
    for i in range(len(data)):
        for j in range(len(data)):
            if i > j:
                value = data[j] + data[i]
                solution.append(value)              
            if i == j:
                continue
            if i < j:
                value = data[i] + data[j] 
                solution.append(value)
    return(int(max(solution)))

for numberset in data:
    anwser += highest_number(numberset)

print(anwser)

    


    
    
    

    