# max_num = 1000
# list_of_nums = range(1, max_num)

# multiple1 = 3
# multiple2 = 5

# final_list = []

# for num in list_of_nums:
#     if num % multiple1 == 0 or num % multiple2 == 0:
#         final_list.append(num)

# sum = 0
# for num in final_list:
#     sum += num

# print sum



#=======================================
#              Fibonacci
#=======================================

# max_num = 4000000

# fib_array = [1, 2]
# evens = []
# num_to_add = fib_array[0] + fib_array[1]

# while num_to_add < max_num:
#     fib_array.append(num_to_add)
#     num_to_add = fib_array[-1] + fib_array[-2]
        
        
# for num in fib_array:
#     if num % 2 == 0:
#         evens.append(num)

# sum = 0
# for num in evens:
#     sum += num

# print sum


#========================================
#          Prime Factorization
#=========================================

# def get_prime_factors(number):
#     prime = 2
#     max_iterator = get_max_iterator(number)
#     prime_factors = []
#     while prime <= max_iterator:
#         if number % prime == 0:
#             prime_factors.append(prime)
#             number = number / prime
#             if number == prime:
#                 prime_factors.append(number)
#             max_iterator = get_max_iterator(number)
#         else:
#             if prime == max_iterator:
#                 prime_factors.append(number)
#             prime += 1
#     return prime_factors

# def get_max_iterator(num):
#     if num % 2 == 0:
#         max_iterator = num / 2
#     else:
#         max_iterator = (num - 1) / 2
#     return max_iterator

# def get_largest_prime_factor(prime_factors_list):
#     largest_num = prime_factors_list[0]
#     for num in prime_factors_list:
#         if num > largest_num:
#             largest_num = num
#     return largest_num

# number = 600851475143
# prime_factors = get_prime_factors(number)
# largest_prime_factor = get_largest_prime_factor(prime_factors)

# print largest_prime_factor


#================= Class Solution ==================

number = 600851475143
# good edge cases to test - 2, 18, 45,

remainder = number
factor = 2
while remainder != 1:
    if remainder % factor == 0:
        remainder /= remainder
    else:
        factor += 1

print factor

#... done when remainder = 1

