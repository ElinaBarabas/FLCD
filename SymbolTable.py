from flcd.FLCD.FiniteAutomata import FiniteAutomata
from flcd.FLCD.HashTable import HashTable


class SymbolTable:

    def __init__(self, hashtable_constants, hashtable_identifiers, filename):
        self.filtered_list = []
        self.token_list = []
        self.pif_form = []
        self.create_string = ""
        self.string_flag = 0
        self.line_number = 0
        self.error_value = 1

        self.tokens_identifiers_constants = {}

        self.hashtable_constants = hashtable_constants
        self.hashtable_identifiers = hashtable_identifiers
        self.filename = filename

        self.finiteAutomataConstants = FiniteAutomata("finite_automata_for_constants.txt")
        self.finiteAutomataIdentifiers = FiniteAutomata("finite_automata_for_identifiers.txt")

        self.number_of_tokens = self.count_tokens()
        self.identify_tokens()
        self.identify_line_components()
        #
        self.write_output_in_files()

        self.print_menu()

    def identify_tokens(self):
        fp = open("token.txt")
        index = -1
        for line in enumerate(fp):
            index += 1
            if index < self.number_of_tokens - 1:
                self.token_list.append(line[1][:-1])
            else:
                self.token_list.append(
                    line[1])  # we need to have a special case for the last line, because this one won't contain '\n'

        self.tokens_identifiers_constants["CONSTANT"] = 0
        self.tokens_identifiers_constants["IDENTIFIER"] = 1

        token_id = 2
        for token in self.token_list:
            self.tokens_identifiers_constants[token] = token_id
            token_id += 1

        # print(self.tokens_identifiers_constants)
        fp.close()

    @staticmethod
    def count_tokens():
        fp = open("token.txt")
        return len(fp.readlines())

    def check_if_valid_const_integer(self, elem):
        return self.finiteAutomataConstants.checkSequence(elem)

    def check_if_valid_identifier(self, elem):
        return self.finiteAutomataIdentifiers.checkSequence(elem)

    def identify_line_components(self):
        fp = open(self.filename)

        lines = fp.readlines()
        for line in lines:
            components_of_line = line.strip()
            components_of_line = components_of_line.split(' ')
            self.create_hashtable_identifiers(components_of_line)
            self.line_number += 1
            self.create_pif_table(components_of_line)

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

        for elem in self.filtered_list:
            if self.check_if_valid_const_integer(elem):
                self.hashtable_constants.add_key(int(elem))

            if elem.__contains__('"'):
                self.hashtable_constants.add_key(elem)

            if elem not in self.token_list and self.check_if_valid_identifier(elem) and not elem.__contains__('"'):
                self.hashtable_identifiers.add_key(elem)

    def write_output_in_files(self):

        filename = self.filename + "_ST.txt"
        f = open(filename, "w")

        if self.error_value == 1:
            print(self.filename + " is lexical correct")
            f.write(self.filename + " is lexical correct\n")

        f.write("The Symbol Table for identifiers: \n")
        f.write("\n")

        identifiers = self.hashtable_identifiers.get_hashtable()

        for i in range(len(identifiers)):
            line = str(i) + " -> " + str(identifiers[i]) + "\n"
            f.write(line)

        f.write("\nThe Symbol Table for constants: \n")
        f.write("\n")

        constants = self.hashtable_constants.get_hashtable()

        for i in range(len(constants)):
            line = str(i) + " -> " + str(constants[i]) + "\n"
            f.write(line)

        f.close()

        filename2 = self.filename + "_PIF.txt"

        f1 = open(filename2, "a")
        f1.write("The Program Internal Form is: \n\n")
        for i in range(len(self.pif_form)):
            line = self.pif_form[i]
            f1.write(str(line) + "\n")
        f1.close()

    def create_pif_table(self, components_of_line):

        for elem in components_of_line:

            if not self.check_elem(elem):
                break

            if elem == '"' and self.string_flag == 0:
                self.string_flag = 1

            elif elem != '"' and self.string_flag == 1:
                self.create_string += elem
                self.create_string += " "

            elif elem == '"' and self.string_flag == 1:
                pif_constant = (
                    self.create_string, self.tokens_identifiers_constants["CONSTANT"],
                    self.hashtable_constants.retrieve_value('"' + self.create_string + '"'))
                self.pif_form.append(pif_constant)
                self.string_flag = 0
                self.create_string = ""

            if self.hashtable_identifiers.search_key(elem):
                pif_identifier = (
                    elem, self.tokens_identifiers_constants["IDENTIFIER"],
                    self.hashtable_identifiers.retrieve_value(elem))
                self.pif_form.append(pif_identifier)

            elif self.hashtable_constants.search_key(elem):
                pif_constant = (
                    elem, self.tokens_identifiers_constants["CONSTANT"], self.hashtable_constants.retrieve_value(elem))
                self.pif_form.append(pif_constant)

            elif elem in self.tokens_identifiers_constants.keys():
                pif_token = (elem, self.tokens_identifiers_constants[elem], -1)
                self.pif_form.append(pif_token)

    def check_elem(self, elem):
        list_of_chars = [x for x in elem]
        for character in list_of_chars:
            character = character.strip()
            if not character.isalnum():
                if character not in self.token_list:
                    self.error_value = 0
                    filename2 = self.filename + "_PIF.txt"
                    f1 = open(filename2, "a")
                    f1.write("Lexical error in " + self.filename + " at line" + str(self.line_number) + "(" + str(
                        elem) + ")\n\n")
                    print("Lexical error in " + self.filename + " at line", self.line_number, "(", elem, ")\n")
                    f1.close()
                    return False
        return True

    def print_menu(self):

        while True:
            print("\n\n\nMENU - choose an option")
            print("1. List the set of states")
            print("2. List the alphabet")
            print("3. List the set of transitions")
            print("4. List the initial state")
            print("5. List the final state(s)")
            print("6. Check sequence")

            option = int(input("Enter the value: "))
            print("\n \n \n")
            if option == 1:
                print("List the set of states")
                print("Identifiers ", self.finiteAutomataIdentifiers.setOfStates)
                print("Constants ", self.finiteAutomataConstants.setOfStates)
            elif option == 2:
                print("List the alphabet")
                print("Identifiers ", self.finiteAutomataIdentifiers.nonTerminalSet)
                print("Constants ", self.finiteAutomataConstants.nonTerminalSet)
            elif option == 3:
                print("List the set of transitions")
                print("Identifiers ", self.finiteAutomataIdentifiers.transitions)
                print("Constants ", self.finiteAutomataConstants.transitions)
            elif option == 4:
                print("List the initial state")
                print("Identifiers ", self.finiteAutomataIdentifiers.initialState)
                print("Constants ", self.finiteAutomataConstants.initialState)
            elif option == 5:
                print("List the final state(s)")
                print("Identifiers ", self.finiteAutomataIdentifiers.finalStates)
                print("Constants ", self.finiteAutomataConstants.finalStates)
            else:
                print("Check if a sequence is FA!")
                valueToBeChecked = input("Enter the value: ")
                print("1. Check if it is a constant integer")
                print("2. Check if it is a identifier")
                value = int(input("What do you want to check?"))
                if value == 1:
                    print("Isconstant integer: ", self.finiteAutomataConstants.checkSequence(valueToBeChecked))
                else:
                    print("Is identifier: ", self.finiteAutomataIdentifiers.checkSequence(valueToBeChecked))

#
# hashtable_constants_p1 = HashTable()
# hashtable_identifiers_p1 = HashTable()
# symbol_table_p1 = SymbolTable(hashtable_constants_p1, hashtable_identifiers_p1, "p1.txt")
#
# print("----------------------------------------------------------------------------------------------------")
#
# hashtable_constants_p2 = HashTable()
# hashtable_identifiers_p2 = HashTable()
# symbol_table_p2 = SymbolTable(hashtable_constants_p2, hashtable_identifiers_p2, "p2.txt")
#
# print("----------------------------------------------------------------------------------------------------")
#
hashtable_constants_p3 = HashTable()
hashtable_identifiers_p3 = HashTable()
symbol_table_p3 = SymbolTable(hashtable_constants_p3, hashtable_identifiers_p3, "p3.txt")


# print("----------------------------------------------------------------------------------------------------")

# hashtable_constants_p4 = HashTable()
# hashtable_identifiers_p4 = HashTable()
# symbol_table_p4 = SymbolTable(hashtable_constants_p4, hashtable_identifiers_p4, "pE.txt")
