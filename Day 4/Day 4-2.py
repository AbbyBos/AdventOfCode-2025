Source = 'AdventOfCode-2025\Day 4\Day 4 data.txt'
data_matrix = []
anwser = int
anwser_full = 0

with open(Source, "r") as f:   
    data_matrix = [list(line.strip()) for line in f]

def is_accesable(x,y):
    nearby_rolls_of_paper = 0
    options = [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
    for option in options: 
        x_t = option[0]
        y_t = option[1]
        if x_t < len(data_matrix) and x_t >= 0:
            if y_t < len(data_matrix[x]) and y_t >= 0:
                if data_matrix[x_t][y_t] in ['@','X']:
                    nearby_rolls_of_paper += 1
    if nearby_rolls_of_paper <= 3:
        data_matrix[x][y] = 'X'
        return(True)

def clean_up():
    for i in range(len(data_matrix)):
        for j in range(len(data_matrix[i])):
            if data_matrix[i][j] == 'X':
                data_matrix[i][j] = '.'
                
def check_matrix():
    anwser = 0    
    for i in range(len(data_matrix)):
        for j in range(len(data_matrix[i])):
            if data_matrix[i][j] == '@':
                if is_accesable(i,j) == True:
                    anwser += 1
    return(anwser)
                
while anwser != 0:
    clean_up()
    anwser = check_matrix()
    anwser_full += anwser

print(anwser_full)