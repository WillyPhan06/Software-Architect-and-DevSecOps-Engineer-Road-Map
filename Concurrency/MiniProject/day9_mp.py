#This is saved as count_primary_library.py to allow import to count prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def count_prime_num(start_and_end):
    start, end = start_and_end
    return sum(1 for i in range(start,end) if is_prime(i))