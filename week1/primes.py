from itertools import permutations

def generate_numbers(card_list):
    number_list = card_list
    perms = permutations(card_list, len(card_list))
    for x in perms:
        num = ''.join(x)
        number_list.append(num)    
    number_list.extend(list(number_list))
    number_list = list(set(number_list))
    print(number_list)
    return number_list

def is_prime(str_num):
    num = int(str_num)
    i = 2
    is_prime = True
    while (i < num):
        if (num % i == 0):
            isPrime = False
            break
        i += 1
    return is_prime
        
def solution(numbers):
    prime_count = 0
    number_list = generate_numbers(list(numbers))
    
    for x in number_list:
        if (is_prime(x)):
            prime_count += 1
    
    answer = prime_count
    
    return answer

solution("17")