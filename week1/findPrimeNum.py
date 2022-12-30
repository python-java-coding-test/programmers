from itertools import permutations
import math

def is_prime_num(n):
    if n < 2:
        return False
    for i in range(2, math.trunc(math.sqrt(n))+1):
        if n % i == 0:
            return False 
    return True


def solution(numbers):
    num_list = list(numbers)
    numberList=[]
    for i in range(len(num_list)):
        numberList+=map(int, map("".join, permutations(num_list,i+1)))
        numberList=list(set(numberList))
    
    answerList=[]
    for num in numberList:
        if is_prime_num(num):
            answerList.append(num)

    return len(answerList)