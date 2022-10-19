from flcd.FLCD.HashTableIdentifiers import HashTable


class SymbolTable:

    def __init__(self, hashtable_constants, hashtable_identifiers, filename):
        self.filtered_list = []
        self.hashtable_constants = hashtable_constants
        self.hashtable_identifiers = hashtable_identifiers
        self.filename = filename

        self.number_of_tokens = self.count_tokens()
        self.token_list = self.populate_token_list()
        self.identify_line_components()

        self.print_hash_tables()

    def populate_token_list(self):
        fp = open("token.txt")
        index = -1
        tokens = []
        for line in enumerate(fp):
            index += 1
            if index < self.number_of_tokens - 1:
                tokens.append(line[1][:-1])
            else:
                tokens.append(
                    line[1])  # we need to have a special case for the last line, because this one won't contain '\n'
        fp.close()
        return tokens

    @staticmethod
    def count_tokens():
        fp = open("token.txt")
        return len(fp.readlines())

    @staticmethod
    def check_if_const_integer(elem):
        try:
            int(elem)
            ok = True
        except ValueError:
            ok = False
        return ok

    def identify_line_components(self):
        fp = open(self.filename)

        lines = fp.readlines()
        for line in lines:
            components_of_line = line.split(' ')
            self.create_hashtable_identifiers(components_of_line)
        fp.close()

    def append_without_new_line(self, elem):
        if elem.endswith("\n"):
            self.filtered_list.append(elem[:-2])
        else:
            self.filtered_list.append(elem)

    def create_hashtable_identifiers(self, components_of_line):

        const_string = ""
        quote_flag = 0
        for elem in components_of_line:
            if len(elem) != 0:
                if elem == '"' and quote_flag == 0:  # we need to treat the cases when the current string is an identifier or from a constant string
                    quote_flag = 1
                    const_string += elem
                elif elem != '"' and quote_flag == 1:  # elem from the const string
                    const_string += elem
                    const_string += " "
                elif elem == '"' and quote_flag == 1:  # end of the const string
                    quote_flag = 2
                    const_string += elem
                elif quote_flag == 2:
                    self.filtered_list.append(const_string)
                    quote_flag = 0
                    const_string = ""
                    self.append_without_new_line(elem)

                elif elem != '"' and quote_flag == 0:
                    self.append_without_new_line(elem)
                else:
                    self.append_without_new_line(elem)

        # print(self.filtered_list)

        for elem in self.filtered_list:
            if self.check_if_const_integer(elem):
                self.hashtable_constants.add_key(int(elem))

            if elem.__contains__('"'):
                self.hashtable_constants.add_key(elem)

            if elem not in self.token_list and not self.check_if_const_integer(elem) and not elem.__contains__('"'):
                self.hashtable_identifiers.add_key(elem)

    def print_hash_tables(self):

        print(self.filename)
        print("\nIdentifiers: \n")
        identifiers = self.hashtable_identifiers.get_hashtable()
        for i in range(len(identifiers)):
            print(i, "->", identifiers[i])

        print("\nConstants: \n")
        constants = self.hashtable_constants.get_hashtable()
        for i in range(len(constants)):
            print(i, "->", constants[i])



hashtable_constants_p1 = HashTable()
hashtable_identifiers_p1 = HashTable()
symbol_table_p1 = SymbolTable(hashtable_constants_p1, hashtable_identifiers_p1, "p1.txt")

print("----------------------------------------------------------------------------------------------------")

hashtable_constants_p2 = HashTable()
hashtable_identifiers_p2 = HashTable()
symbol_table_p2 = SymbolTable(hashtable_constants_p2, hashtable_identifiers_p2, "p2.txt")

print("----------------------------------------------------------------------------------------------------")

hashtable_constants_p3 = HashTable()
hashtable_identifiers_p3 = HashTable()
symbol_table_p3 = SymbolTable(hashtable_constants_p3, hashtable_identifiers_p3, "p3.txt")
