

import math

# create a function name is_prime
def is_prime(n):
    # handling numbers if its 1 or less than that
    if n <= 1:
        return False
    if n <= 3:
        return True

    # handle even numbers and multiplication by 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # check for factors of 5 to a sqrt(n) and skip even numbers and multiples by 3
    limit = int(math.sqrt(n)) + 1
    for i in range(5, limit, 6):
        if n % i == 0 or n % ( i + 2) == 0:
            return False
    return True

print(is_prime(100000007))