# Task 1.

def merge_dicts(dict1, dict2):

    merged_dict = {}

    for key, value in dict1.items():
        merged_dict[key] = value

    for key, value in dict2.items():
        merged_dict[key] = value

    return merged_dict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 4, 'd': 5, 'e': 6}

print(merge_dicts(dict1, dict2))


# Task 2.

def dict_intersection(dict1, dict2):

    intersection_dict = {}
    
    for key in dict1:
        if key in dict2:
            intersection_dict[key] = (dict1[key], dict2[key])
    
    return intersection_dict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 4, 'd': 5, 'e': 6, 'b': 7}

print(dict_intersection(dict1, dict2))


# Task 3.

def count_word_frequencies(word_list):

    word_freq = {}
    
    for word in word_list:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    return word_freq

word_list = ['apple', 'banana', 'cherry', 'apple', 'banana', 'apple', 'cherry', 'pineapple']

print(count_word_frequencies(word_list))
