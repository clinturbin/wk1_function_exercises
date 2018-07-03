# list_of_nums = [20, 5, 12, 24, 15, 35]

# largest_num = list_of_nums[0]

# for i in range(1, len(list_of_nums)):
#     if list_of_nums[i] > largest_num:
#         largest_num = list_of_nums[i]

# print "The largest number in the list is %i." % largest_num


# Turn above into a function

def get_largest_number(input_list):
    largest = input_list[0]
    for i in range(1, len(input_list)):
        if input_list[i] > largest:
            largest = input_list[i]
    return largest



list_of_nums = [40, 55, 12, 24, 15, 35]

largest = get_largest_number(list_of_nums)
print "The largest number is : %i." % largest

