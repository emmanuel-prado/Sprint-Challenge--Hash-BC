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
    # check to see the size of the weights list
    # if length is 0, or 1, return None
    if len(weights) == 0 or len(weights) == 1:
        return None
    # insert key-pair (key: weight, value: list-index) into hash table using hash_table_insert
    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)

    # now search to see if the hashtable has the matching value using retrieve
    # remember to subtract the weight from the limit first
    for i in range(len(weights)):
        match = limit - weights[i]
        index = hash_table_retrieve(ht, match)
        if index != None:
            # we found the other weight that when summed with our current weight, equals the limit
            # compare the index sizes
            if i > index:
                Answer = (i, index)
                return Answer
            else:
                Answer = (index, i)
                return Answer

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
