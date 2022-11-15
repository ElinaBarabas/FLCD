from flcd.FLCD.FiniteAutomata import FiniteAutomata


class HashTable:

    def __init__(self, size=5):
        self.size = size
        self.hash_table = self.create_entries()
        self.index_count = -1

    def create_entries(self):
        return [None for _ in range(self.size)]

    def hash_function(self, key):
        if type(key) == int:
            key = str(key)

        list_of_chars = [x for x in key]
        sum_chars = 0
        for character in list_of_chars:
            sum_chars += ord(character)
        return sum_chars % self.size

    def add_key(self, key):

        if self.search_key(key) or key == " " or len(str(key)) == 0:
            return

        result = self.hash_function(key)
        self.index_count += 1
        key_value_pair = (key, self.index_count)
        if self.hash_table[result] is None:
            self.hash_table[result] = []
            self.hash_table[result].append(key_value_pair)
        else:
            self.hash_table[result].append(key_value_pair)

    def search_key(self, key):

        result = self.hash_function(key)
        if self.hash_table[result] is None:
            return False
        for key_value_pairs in self.hash_table[result]:
            try:
                converted_key = int(key)
            except ValueError:
                converted_key = str(key)
            if key_value_pairs[0] == converted_key:
                return True
        return False

    def retrieve_value(self, key):

        if not self.search_key(key):
            return None
        else:
            result = self.hash_function(key)
            try:
                converted_key = int(key)
            except ValueError:
                converted_key = str(key)
            for key_value_pairs in self.hash_table[result]:
                if key_value_pairs[0] == converted_key:
                    return key_value_pairs[1]


    def get_hashtable(self):
        return self.hash_table




# hashtable_identifiers = HashTable()
#
# hashtable_identifiers.add_key("a")
# hashtable_identifiers.add_key("ba")
# hashtable_identifiers.add_key("ab")
# hashtable_identifiers.add_key("ab")
# hashtable_identifiers.add_key("bbf")
# hashtable_identifiers.add_key("f_f")
# hashtable_identifiers.add_key("q~f")
# hashtable_identifiers.add_key("ab")
#
# for i in range(len(hashtable_identifiers.hash_table)):
#     print(i, "->", hashtable_identifiers.hash_table[i])


# hashtable_constants = HashTable()
#
# hashtable_constants.add_key(1)
# hashtable_constants.add_key(2)
# hashtable_constants.add_key("Enter a value")
# hashtable_constants.add_key(11)
# hashtable_constants.add_key("12")
# hashtable_constants.add_key("15")
# hashtable_constants.add_key(15)
# hashtable_constants.add_key("1.0")
#
# for i in range(len(hashtable_constants.hash_table)):
#     print(i, "->", hashtable_constants.hash_table[i])