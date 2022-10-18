class HashTableIdentifier:

    def __init__(self, size=40):
        self.index_count = -1
        self.size = size
        self.hash_table = self.create_entries()

    def create_entries(self):
        return [[-1, ""] for _ in range(self.size)]

    def hash_function(self, constant):
        int_to_str = str(constant)
        list_of_chars = [x for x in int_to_str]
        sum_chars = 0
        for character in list_of_chars:
            sum_chars += ord(character)
        return sum_chars % self.size

    def add(self, constant):
        if self.search_identifier(constant):
            return

        result = self.hash_function(constant)
        self.hash_table[result][0] = constant
        self.index_count += 1
        self.hash_table[result][1] = self.index_count

    def search_identifier(self, constant):

        result = self.hash_function(constant)
        if self.hash_table[result][0] == -1:
            return False
        return True


l = [(-1, [12]) for _ in range(12)]

h = HashTableIdentifier()
h.add(12)
h.add(168)
print(h.hash_table)
