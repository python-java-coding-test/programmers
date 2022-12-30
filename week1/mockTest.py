def solution(answers):
    stu1 =[1,2,3,4,5]*2000
    stu2 = [2,1,2,3,2,4,2,5]*1250
    stu3=[3,3,1,1,2,2,4,4,5,5]*1000
    stu = [stu1,stu2,stu3]
    
    count=[0,0,0]
    for i in range(len(answers)):
        for j in range(3):
            if answers[i] == stu[j][i]:
                count[j]+=1
						
    answer = []
    score = max(count)
    for i in range(3):
        if count[i]==score:
            answer.append(i+1)
        
    return answer