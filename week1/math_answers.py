import math
def get_one_answer(answer_length):
    one_answers = []
    cur_answer = 1
    for x in range(answer_length):
        one_answers.append(cur_answer)
        if (cur_answer == 5):
            cur_answer = 1
        else:
            cur_answer += 1
    return one_answers

def get_two_answer(answer_length):
    two_answers = []
    odd_answer = 1
    for x in range(answer_length):
        if ((x % 2) == 0):
            two_answers.append(2)
        if ((x % 2) == 1):
            two_answers.append(odd_answer)
            if (odd_answer == 5):
                odd_answer = 1
            else:
                if (odd_answer == 1):
                    odd_answer += 1
                odd_answer += 1
    return two_answers

def get_three_answer(answer_length):
    answer_order = [3,1,2,4,5]
    three_answers = []
    idx = 0
    cur_answer = 3
    for x in range(answer_length):
        
        if (x % 2 == 0):
            cur_idx = math.floor(x / 2) if x !=0 else 0
            cur_idx = cur_idx % 5
            cur_answer = answer_order[cur_idx]
            three_answers.append(cur_answer)
        if (x % 2 == 1):
            three_answers.append(cur_answer)
    return three_answers

def solution(answers):
    answer = []
    one_answers = get_one_answer(len(answers))
    print(one_answers)
    two_answers = get_two_answer(len(answers))
    print(two_answers)
    three_answers = get_three_answer(len(answers))
    print(three_answers)
    
    one_correct_count = 0
    two_correct_count = 0
    three_correct_count = 0
    for x in range(len(answers)):
        if answers[x] == one_answers[x]:
            one_correct_count += 1
        if answers[x] == two_answers[x]:
            two_correct_count += 1
        if answers[x] == three_answers[x]:
            three_correct_count += 1
    
    max_corrects = max([one_correct_count, two_correct_count, three_correct_count])
    if (one_correct_count == max_corrects):
        answer.append(1)
    if (two_correct_count == max_corrects):
        answer.append(2)
    if (three_correct_count == max_corrects):
        answer.append(3)
    return answer
