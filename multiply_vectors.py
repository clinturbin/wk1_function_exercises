# list1 = [2, 4, 5]
# list2 = [3, 4, 8]

# new_list = []

# for i in range(len(list1)):
#     product = list1[i] * list2[i]
#     new_list.append(product)

# print new_list


# Turn above into function

def multiply_vectors(list1, list2):
    new_list = []
    for i in range(len(list1)):
        product = list1[i] * list2[i]
        new_list.append(product)
    return new_list

list1 = [2, 4, 5]
list2 = [2, 3, 6]

result = multiply_vectors(list1, list2)

print result
