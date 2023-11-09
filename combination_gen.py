def gen_comb_list(input_lists):
    if not input_lists:
        return [[]]

    result = [[]]
    for inner_list in input_lists:
        new_result = []
        for item in inner_list:
            for prev_list in result:
                new_result.append(prev_list + [item])
        result = new_result

    return result

# Examples
print(gen_comb_list([[1, 2, 3]]))
print(gen_comb_list([[1, 2, 3], [4, 5]]))
print(gen_comb_list([[1, 2, 3], [4, 5], [6, 7, 8]]))

