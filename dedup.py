# first_list = [1, 2, 1, "truck", "car", 3, "truck"]
# dedup_list = []

# for item in first_list:
#     if item not in dedup_list:
#         dedup_list.append(item)

# print dedup_list



def remove_duplicates(input_list):
    result = []
    for item in input_list:
        if item not in result:
            result.append(item)
    return result


list1 = [1, 2, 1, "truck", "car", 3, "truck", 3]

result = remove_duplicates(list1)

print result