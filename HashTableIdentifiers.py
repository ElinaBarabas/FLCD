class HashTableIdentifier:

    def __init__(self, size=3):
        self.size = size
        self.hash_table = self.create_entries()
        self.index_count = -1

    def create_entries(self):
        return [None for _ in range(self.size)]

    def hash_function(self, identifier):
        list_of_chars = [x for x in identifier]
        sum_chars = 0
        for character in list_of_chars:
            sum_chars += ord(character)
        return sum_chars % self.size

    def add(self, identifier):

        if self.search_identifier(identifier):
            return
        result = self.hash_function(identifier)
        self.index_count += 1
        key_value_pair = (identifier, self.index_count)
        if self.hash_table[result] is None:
            self.hash_table[result] = []
            self.hash_table[result].append(key_value_pair)
        else:
            self.hash_table[result].append(key_value_pair)

    def search_identifier(self, identifier):

        result = self.hash_function(identifier)
        if self.hash_table[result] is None:
            return False
        for key_value_pairs in self.hash_table[result]:
            if key_value_pairs[0] == identifier:
                return True
        return False


l = [(-1, [12]) for _ in range(12)]

h = HashTableIdentifier()
h.add("a")
h.add("ba")
h.add("ab")
h.add("ab")
h.add("bbf")
h.add("f_f")
h.add("q~f")
h.add("ab")

print(h.hash_table)
