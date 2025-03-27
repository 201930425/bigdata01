def is_prime(number):
    """
    Function to determine whether a number is a prime number
    :param number: The number to determine whether it is prime or not
    :return: Returns True if it is a prime number, False if it is not a prime number.
    """
    if number >= 2:
        i = 2
        while i * i <= number:
            if number % i == 0:
                return False
            i = i + 1
    else:
        return False
    return True

n = int(input())

if is_prime(n):
    print(f"{n}는(은) 소수입니다")
else:
    print(f"{n}는(은) 소수가 아닙니다!")
