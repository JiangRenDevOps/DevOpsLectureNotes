"""
A list is a collection of homogeneous/heterogenous elements (int, float, string, etc.)

Read (with index) / append / add: O(1)
Insert / delete: O(n) - expensive as the items have to be rearranged after insertion or deletion
Value lookup: O(n)
"""
import math


def list_demo():
    list_ = ['hello', 'how', 'are', 'you', 1, 10, 'how', 'well', 'are']  # created a simple list
    # read
    print(list_)
    print(list_[0])  # first element
    print(list_[-1])  # last element
    # slicing
    print(list_[:3])  # What does it do?
    print(list_[-1:])
    print(list_[::-1])  # how about this?
    # replace
    list_[4] = 1232
    # pop
    print(list_.pop(4))
    # insert
    list_.insert(4, 111)
    print(list_)
    # append
    list_.append(3)
    # pop
    print(list_)
    string_ = ""
    # traverse
    for el in list_:
        string_ += str(el) + ", "
    print(string_)
    # do we have another way to traverse a list?


"""
Immutable, homogeneous, and dynamic
Time complexity:
Same as that of lists and arrays - O(1) with index and O(n) for lookup
Reading/slicing:
Same as in lists. Just consider each character in the string as an element of a list.
"""


def string_demo():
    string_ = "Hello, I am Yu and I am a DevOps"
    # slicing
    print(string_[2])
    # replace
    # cannot replace a character, because string is immutable
    # string_[1] = 'r' # try this
    # However, you can replace the word this way
    string_.replace("Jack", "John")

    # Another useful function
    string_list = string_.split(" ")
    print(string_list)
    print(",".join(string_list))

    # traverse: could you try to traverse each element in a string?

    # exercise: are you able to check if a string is palindromic?

    # Input : malayalam
    # Output : Yes

    # Input : geeks
    # Output : No


"""
Immutable and static
Tuples are used when we want to in the list
Time complexity:
Same as that of lists and arrays - O(1) with index and O(n) for lookup
"""


def tuple_demo():
    # Tuples are used for grouping data
    julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
    print(julia[2])

    my_name = 18
    my_age = "Yu"
    (my_name, my_age) = (my_age, my_name)
    # temp = my_name
    # my_name = my_age
    # my_age = temp
    print(my_name, my_age)

    def f(r):
        """ Return (circumference, area) of a circle of radius r """
        c = 2 * math.pi * r
        a = math.pi * r * r
        return c, a

    print(f(5))


"""
A set is an unordered collection with . Set is another data type that we often use in data wrangling. It is used to eliminate duplicate values from a list or an array.

Immutable and dynamic
"""


def set_demo():
    set = {111, 1232, 'are', 'hello', 'how', 'well', 'you'}
    set.add(111)
    set.add(112)
    set.update({5})
    print(set)
    pass


_end = '*'


# takes in a list of words
def make_trie(*words):
    # creates our root dict()
    trie = dict()

    for word in words:
        # create a temporary dict based off our root
        # dict object
        temp_dict = trie

        for letter in word:
            # update our temporary dict and add our current
            # letter and a sub-dictionary
            temp_dict = temp_dict.setdefault(letter, {})

        # If our word is finished, add {'*': '*'}
        # this tells us our word is finished
        temp_dict[_end] = _end
    return trie


"""
A dictionary consists of key-value pairs in no specific order. The key-value pairs are stored in an associative array. Each key maps to a value or a list or another dictionary.

The keys are usually hash codes that are generated using a hash function. The idea is to have a unique hash code for every value to be stored. Hence the read operation is much faster than any other data types - O(1) (even for search operations - the best case). Please note that here we .

Time complexity:
Most dict operations O(1) (even for lookup operation)
"""


def dict_demo():
    # Lets store age of people as dictionary
    dict_ = {"Julie": 32, "Rahul": 23, "Jasmine": 12, "Jack": 15, "Jennifer": 18}
    print(dict_["Julie"])
    # traverse
    for k, v in dict_.items():
        print(k, v)
    # An interesting data structure: trie
    trie = make_trie('hi', 'hello', 'howdy', "heaven", "hippo", "hat", "hub")
    print(trie)


if __name__ == '__main__':
    list_demo()
    string_demo()
    tuple_demo()
    set_demo()
    dict_demo()
    # Can you choose the right data structure to write a simple queue and stack using above data structures?
    # Hint: what is a queue's characteristic? FIFO
    # Hint: what is a stack's characteristic? LIFO
