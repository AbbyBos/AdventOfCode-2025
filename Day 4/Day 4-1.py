Source = 'AdventOfCode-2025\Day 4\Day 4 test.txt'
data_matrix = []
anwser = 0

with open(Source, "r") as f:   
    data_matrix = [list(line.strip()) for line in f]

def is_accesable(x,y):
    nearby_rolls_of_paper = 0
    options = [
        (x-1,y-1),(x,y-1),(x+1,y-1),
        (x-1,y),(x+1,y),
        (x-1,y+1),(x,y+1),(x+1,y+1)]
    for option in options: 
        x_t = option[0]
        y_t = option[1]
        if x_t < len(data_matrix) and x_t >= 0:
            if y_t < len(data_matrix[x]) and y_t >= 0:
                if data_matrix[x_t][y_t] in ['@']:
                    nearby_rolls_of_paper += 1
    if nearby_rolls_of_paper <= 3:
        return(True)
    
for i in range(len(data_matrix)):
    for j in range(len(data_matrix[i])):
        if data_matrix[i][j] == '@':
            if is_accesable(i,j) == True:
                anwser += 1              

print(anwser)

    