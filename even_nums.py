# list_of_nums = [5, 15, 14, 13, 22, 43, 28, 16, 95]

# for i in range(len(list_of_nums)):
#     if list_of_nums[i] % 2 == 0:
#         print list_of_nums[i]


# Turn above into function

def get_even_numbers(input_list):
    evens = []
    for num in input_list:
        if num % 2 == 0:
            evens.append(num)
    return evens
    
list_of_nums = [5, 15, 14, 13, 22, 43, 28, 16, 95, 3, 4]

result = get_even_numbers(list_of_nums)
print result