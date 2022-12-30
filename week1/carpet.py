import math
def solution(brown, yellow):
    limit = math.trunc(math.sqrt(yellow))
    
    for i in range(1,limit+1):
        if yellow%i==0 and 2*(i+yellow//i+2)==brown:
            return [yellow//i+2,i+2]