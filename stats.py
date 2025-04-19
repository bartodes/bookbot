def get_number_words(text):
    counter = 0
    for word in text.split():
        counter += 1
        # if word.isalpha():
            # counter += 1
    return counter

def get_number_char(text):
    char_counter = {}
    for char in text.lower():
        if char not in char_counter:
            char_counter[char] = 1
        else:
            char_counter[char] += 1
    return char_counter

def sort_number_char(char_counter):
    list_char_counter = []
    for i in char_counter:
        if i.isalpha():
            list_char_counter.append({"char": i, "num":char_counter[i]})

    list_char_counter.sort(reverse=True,key=lambda x: x["num"])
    
    return list_char_counter

# def sort_number_char(char_counter):
#     sorted_items = []
#     list_char_counter = []
#     for i in char_counter:
#         sorted_items.append(i)
    
#     sorted_items.sort()
    
#     for char in sorted_items:
#         list_char_counter.append({char: char_counter[char]})
    
#     print(list_char_counter)