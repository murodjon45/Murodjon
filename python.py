list = ([1, 2, 3, 8, 9])
def get_pairs(list):
    if len(list) == 1:
        return None
    pairs_list = []
    for i in range(len(list)-1):
        pairs_list.append((list[i], list[i+1]))
    return pairs_list
print(get_pairs(list))