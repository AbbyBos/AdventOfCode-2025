Source = 'AdventOfCode-2025\Day 5\Day 5 data.txt'
fresh_ranges = []
fresh_food_index = []
available_food = []
import_state = ''
anwser = 0


with open(Source, "r") as f:
    data = []
    for line in f:
        data.append(line.strip())
    fresh_ranges = data[:data.index('')]
    available_food = data[data.index('')+1:]      

def check_freshness(available_food, anwser):
    for food in available_food:
        food = int(food)
        for fresh_range in fresh_ranges:
            range_end = int(fresh_range[fresh_range.find('-')+1:])
            range_start = int(fresh_range[:fresh_range.find('-')])
            if food >= range_start and food <= range_end:
                anwser += 1
                break
    return(anwser)    
        
fresh_food_index = set(fresh_food_index)
anwser = check_freshness(available_food, anwser)
print(anwser)


  

    