from collections import namedtuple
data_list = [
    {'key1': 1, 'key2': 2},
    {'key1': 3, 'key2': 4},
    {'key1': 5, 'key2': 6, 'key3': 7},
    {'key2': 100}
]
def tuplify(dict_list):
    keys = {keys for dict in dict_list for keys in dict.keys()}
    struct = namedtuple("struct", sorted(keys), rename=True)
    struct.__new__.__defaults__=(None,)*len(keys)
    return [struct(**dict)for dict in dict_list]


if __name__ == "__main__":
    print(tuplify(data_list))