#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    Find two items whose sum of weights equal the weight limit.
    Retrun an Answer tuple that has the following form:
    <zero, one)
    Each element represents the item weights of the two packages.
    The higher valued index should be placed in the 0 index, smaller in the 1st.
    If a pair doesn't exist for the given inputs, return None.
    """

    Answer = ()

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
