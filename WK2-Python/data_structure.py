"""
A list is a collection of homogeneous/heterogenous elements (int, float, string, etc.)

Read (with index) / append / add: O(1)
Insert / delete: O(n) - expensive as the items have to be rearranged after insertion or deletion
Value lookup: O(n)
"""


def list_demo():
    list_ = ['hello', 'how', 'are', 'you', 1, 10, 'how', 'well', 'are'] # created a simple list
    # read
    print(list_)
    print(list_[0]) # first element
    print(list_[-1]) # last element
    # slicing
    print(list_[:3]) # What does it do?
    print(list_[-1:])
    print(list_[::-1]) # how about this?
    # replace
    list_[4] = 1232
    # insert
    list_.insert(4, 111)
    # traverse


"""
Immutable, homogeneous, and dynamic
Time complexity:
Same as that of lists and arrays - O(1) with index and O(n) for lookup
Reading/slicing:
Same as in lists. Just consider each character in the string as an element of a list.
"""


def string_demo():
    string_ = "Hello, I am Yu and I am a DevOps"


"""
Immutable and static
Tuples are used when we want to in the list
Time complexity:
Same as that of lists and arrays - O(1) with index and O(n) for lookup
"""


def tuple_demo():
    pass


"""
A set is an unordered collection with . Set is another data type that we often use in data wrangling. It is used to eliminate duplicate values from a list or an array.

Immutable and dynamic
"""


def set_demo():
    pass


"""
A dictionary consists of key-value pairs in no specific order. The key-value pairs are stored in an associative array. Each key maps to a value or a list or another dictionary.

The keys are usually hash codes that are generated using a hash function. The idea is to have a unique hash code for every value to be stored. Hence the read operation is much faster than any other data types - O(1) (even for search operations - the best case). Please note that here we .

Time complexity:
Most dict operations O(1) (even for lookup operation)
"""


def dict_demo():
    pass


if __name__ == '__main__':
    list_demo()
    # Can you write a simple queue and stack using above data structures?


