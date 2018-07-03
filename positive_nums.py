# list_of_nums = [1, -1, 2, -2, 3, -3, 4, -4, -5, 5, 6, -6]

# for i in range(len(list_of_nums)):
#     if list_of_nums[i] > 0:
#         print list_of_nums[i]


# Turn above into function

def create_positive_number_list(input_list):
    list_of_positives = []
    for num in input_list:
        if num > 0:
            list_of_positives.append(num)
    return list_of_positives


list_of_nums = [1, -1, 2, -2, 3, -3, 4, -4, -5, 5, 6, -6]

result = create_positive_number_list(list_of_nums)

for item in result:
    print item