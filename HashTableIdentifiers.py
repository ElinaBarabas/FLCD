class HashTableIdentifier:

    def __init__(self, size=10):
        self.size = size
        self.hash_table = self.create_entries()
        self.index_count = -1

    def create_entries(self):
        return [[-1, ""] for _ in range(self.size)]

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
        self.hash_table[result][0] = identifier
        self.index_count += 1
        self.hash_table[result][1] = self.index_count

    def search_identifier(self, identifier):

        result = self.hash_function(identifier)
        if self.hash_table[result][0] == -1:
            return False
        return True


l = [(-1, [12]) for _ in range(12)]

h = HashTableIdentifier()
h.add("a")
h.add("ab")
h.add("bbf")
h.add("f_f")
h.add("q~f")

print(h.hash_table)
