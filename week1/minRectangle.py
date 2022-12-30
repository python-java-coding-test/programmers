def solution(sizes):
    for inner in sizes:
        if inner[1]>inner[0]:
            inner[0],inner[1]=inner[1],inner[0]
    
    w=[i[0] for i in sizes]
    h=[i[1] for i in sizes]

    answer = max(w)*max(h)
    return answer