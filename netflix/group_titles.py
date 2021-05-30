# Group similar titles
# input = ['duel', 'dule', 'speed', 'spede', 'deul', 'cars']
# output = [('duel', 'dule', 'deul'), ('speed', 'spede'), ('cars')]

def ch_relative_index(ch):
    return ord(ch) - ord('a')


def get_frequency_vector(word):
    vector = [0]*26
    for ch in word:
        index_of_ch = ch_relative_index(ch)
        vector[index_of_ch] += 1
    return vector


def group_similar_titles(word_list):
    output_dict = dict()
    for word in word_list:
        f_vector = get_frequency_vector(word)
        key = tuple(f_vector)
        current = output_dict.get(key, [])
        current.append(word)
        output_dict[key] = current
    return output_dict.values()


input_list = ['duel', 'dule', 'speed', 'spede', 'deul', 'cars']
result = group_similar_titles(input_list)
print(result)
