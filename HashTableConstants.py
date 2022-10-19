class HashTableConstants:

    def __init__(self, size=3):
        self.size = size
        self.hash_table = self.create_entries()
        self.index_count = -1

    def create_entries(self):
        return [None for _ in range(self.size)]

    def hash_function(self, constant):
        return constant % self.size

    def add(self, constant):

        if self.search_identifier(constant):
            return
        result = self.hash_function(constant)
        self.index_count += 1
        key_value_pair = (constant, self.index_count)
        if self.hash_table[result] is None:
            self.hash_table[result] = []
            self.hash_table[result].append(key_value_pair)
        else:
            self.hash_table[result].append(key_value_pair)

    def search_identifier(self, constant):

        result = self.hash_function(constant)
        if self.hash_table[result] is None:
            return False
        for key_value_pairs in self.hash_table[result]:
            if key_value_pairs[0] == constant:
                return True
        return False

# l = [(-1, [12]) for _ in range(12)]
#
# h = HashTableConstants()
# h.add(12)
# h.add(168)
# h.add(15)
# h.add(16)
# h.add(19)
# h.add(18)
# h.add(17)
# print(h.hash_table)
