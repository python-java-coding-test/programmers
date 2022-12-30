from itertools import permutations

def solution(k, dungeons):
    dunNum =len(dungeons)
    dunIndex = [i for i in range(dunNum)]
    tripCase= list(permutations(dunIndex,dunNum))

    stat=k
    temp=0
    count=0
    
    for route in tripCase:
        for gRound in range(dunNum):
            index=route[gRound]
            if stat - dungeons[index][0]>=0:
                stat=stat-dungeons[index][1]
                temp +=1
        
        if temp > count:
            count = temp
            stat=k
        temp=0

    return count