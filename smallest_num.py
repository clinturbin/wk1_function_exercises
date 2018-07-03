# list_of_nums = [5, 15, 20, 3, 1, 2]

# smallest_num = list_of_nums[0]

# for i in range(1, len(list_of_nums)):
#     if list_of_nums[i] < smallest_num:
#         smallest_num = list_of_nums[i]

# print "The smallest number in the list is %i." % smallest_num


# Turn above into function

def get_smallest_number(input_list):
    smallest = input_list[0]
    for i in range(1, len(input_list)):
        if input_list[i] < smallest:
            smallest = input_list[i]
    return smallest

list_of_nums = [15, 15, 20, 13, 10, 12]

smallest = get_smallest_number(list_of_nums)

print "The smallest number is %i." % smallest