class Grammar:
    def __init__(self, input_filename):
        self.__filename = input_filename
        self.__read_grammar()
        self.__set_of_non_terminals = self.__grammar['non_terminals']
        self.__set_of_terminals = self.__grammar['terminals']
        self.__starting_symbol = self.__grammar['starting_symbol']
        self.__productions = self.__grammar['starting_symbol']

    def __read_grammar(self) -> dict:
        self.__grammar = dict()
        with open(self.__filename) as file:
            # non terminals
            line = file.readline()
            self.__grammar['non_terminals'] = line.strip().split()
            # terminals
            line = file.readline()
            self.__grammar['terminals'] = line.strip().split()
            # starting symbol
            line = file.readline()
            self.__grammar['starting_symbol'] = line.strip()
            # productions
            self.__grammar['productions'] = dict()
            line = file.readline()
            while line:
                line = line.strip().split('->')
                left_hand_side = line[0].strip()
                right_hand_side = line[1].strip().split('|')
                self.__grammar['productions'][left_hand_side] = list()
                for production in right_hand_side:
                    self.__grammar['productions'][left_hand_side].append(production.strip())
                line = file.readline()

    def get_grammar(self):
        return self.__grammar

    