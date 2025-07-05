# time complexity: O(n)
def check_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

# time complexity: O(n/2)
def check_prime_n_by_2(x):
    if x <= 1:
        return False
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True

# time complexity: O(sqrt(n))
def check_prime_sqrt_n(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

# Example usage:
print(check_prime(7))   # Output: True
print(check_prime(10))  # Output: False
