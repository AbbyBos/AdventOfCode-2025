def parse_input(filename):
    with open(filename, "r") as f:
        data = [line.strip() for line in f]
    try:
        separator_index = data.index('')
        range_lines = data[:separator_index]
    except ValueError:
        range_lines = data

    fresh_ranges = []
    for range_str in range_lines:
        start, end = range_str.split('-')
        fresh_ranges.append([int(start), int(end)])
        
    return fresh_ranges


def merge_overlapping_ranges(ranges):
    if not ranges:
        return []
    ranges.sort(key=lambda interval: interval[0])
    merged = [ranges[0]]
    for current_start, current_end in ranges[1:]:
        last_merged_start, last_merged_end = merged[-1]
        if current_start <= last_merged_end:
            merged[-1][1] = max(last_merged_end, current_end)
        else:
            merged.append([current_start, current_end])
            
    return merged
    
if __name__ == "__main__":
    SOURCE_FILE = 'AdventOfCode-2025\Day 5\Day 5 data.txt'
    initial_ranges = parse_input(SOURCE_FILE)
    merged_ranges = merge_overlapping_ranges(initial_ranges)
    total_length = sum(end - start + 1 for start, end in merged_ranges)

    print("Total fresh food count:", total_length)


  

    