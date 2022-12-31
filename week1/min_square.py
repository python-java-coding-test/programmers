def turn(sizes):
    new_sizes = [size.sort() for size in sizes]
    return new_sizes

def max_width_or_height(sizes, idx):
    val = 0
    for size in sizes:
        if (size[idx] > val):
            val = size[idx]
    return val
        
def solution(sizes):
    answer = 0
    new_sizes = turn(sizes)
    max_width = max_width_or_height(sizes, 0)
    max_height = max_width_or_height(sizes, 1)
    answer = max_width * max_height
    return answer