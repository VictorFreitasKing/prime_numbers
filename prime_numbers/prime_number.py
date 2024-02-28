def __is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def list_primes(nums):
    num_start=nums[0]
    num_finish=nums[1]
    prime_numbers = []

    for i in range(num_start, num_finish + 1):
        if __is_prime(i):
            prime_numbers.append(i)

    return prime_numbers