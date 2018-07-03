# list_of_nums = [1, 2, 5, 10, 18]
# sum = 0
# for num in list_of_nums:
#     sum += num

# print "The sum of list is: %i" % sum


# Turn into function


def sum_of_numbers(input_list):
    sum = 0
    for num in input_list:
        sum += num
    return sum

list_of_nums = [1, 2, 5, 10, 18]

result = sum_of_numbers(list_of_nums)
print result