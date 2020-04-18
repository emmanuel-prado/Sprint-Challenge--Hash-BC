#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * (length - 1)

    """
    :tickets: [list] containing Ticket class objects
    :length: <int>
    """

    # insert tickets as source-destination (key-value) into hashtable using hash_table_insert
    for x in tickets:
        hash_table_insert(ht, x.source, x.destination)
    # build list using retrieve, use "NONE" as the initial value
    curr_location = hash_table_retrieve(ht, "NONE")
    # set index to 0 for while loop
    index = 0
    # since the route list doesn't include the initial location as part of it's size, make sure to subract 1 from the length total
    while index < length - 1:
        # since that index to be the current location
        route[index] = curr_location
        # find the next destination
        next_destination = hash_table_retrieve(ht, curr_location)
        # set the current location to the next destination
        curr_location = next_destination
        # increment the index
        index += 1
    return route
