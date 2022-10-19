class HashTableConstant:

    def __init__(self, size=5):
        self.size = size
        self.hash_table = self.create_entries()
        self.index_count = -1

    def create_entries(self):
        return [None for _ in range(self.size)]

    def hash_function(self, constant):
        return constant % self.size

    def add_constant(self, constant):

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

    def get_hashtable_constants(self):
        return self.hash_table


l = [(-1, [12]) for _ in range(12)]

h = HashTableConstant()
h.add_constant(12)
h.add_constant(168)
h.add_constant(15)
h.add_constant(16)
h.add_constant(19)
h.add_constant(18)
h.add_constant(17)

for i in range(len(h.hash_table)):
    print(i, "->", h.hash_table[i])
