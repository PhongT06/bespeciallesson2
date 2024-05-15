# Task 1.

def squares(n):
    result = []
    for i in range(1, n+1):
        result.append(i**2)
    return result

print(squares(4))

# Task 2.

def reverse_sublist(list, i, j):

    reversed_sublist = []

    for index in range(j, i - 1, -1):
        reversed_sublist.append(list[index])

    sublist_index = i
    for element in reversed_sublist:
        list[sublist_index] = element
        sublist_index += 1

    return list

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 2  
j = 6 

print("Original list:", original_list)
reversed_list = reverse_sublist(original_list, i, j)
print("List with sublist reversed:", reversed_list)

# Task 3.

def merge_sorted_lists(list1, list2):

    merged_list = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8, 10]

merged_list = merge_sorted_lists(list1, list2)
print(merged_list)