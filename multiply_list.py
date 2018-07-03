# list_of_nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]
# multiplier = int(raw_input("Enter a number: "))

# new_list = []

# for num in list_of_nums:
#     new_list.append(num * multiplier)

# print new_list


# Turn above into function

def multiplied_list(input_list, multiplier):
    new_list = []
    for num in input_list:
        new_list.append(num * multiplier)
    return new_list


list_of_nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]
number = int(raw_input("Enter a number: "))
result = multiplied_list(list_of_nums, number)

print result


