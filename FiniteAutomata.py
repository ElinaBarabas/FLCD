class FiniteAutomata:

    def __init__(self, filename):

        self.filename = filename

        self.finalStates = None
        self.transitions = None
        self.nonTerminalSet = None
        self.setOfStates = None
        self.initialState = None

        self.processFile()

    def checkDeterministicFinalAutomata(self):

        sourceNonTerminalPair = set(self.transitions.keys())
        for sourceNonTerminal in sourceNonTerminalPair:
            if len(self.transitions[sourceNonTerminal]) > 1:
                return False
        return True

    def checkSequence(self, inputCharacterSequence):
        if not self.checkDeterministicFinalAutomata():
            return False

        else:

            currentState = self.initialState
            for character in inputCharacterSequence:
                if (currentState, character) in self.transitions.keys():
                    currentState = self.transitions[(currentState, character)][0]
                else:
                    return False

            if currentState in self.finalStates:
                return True

    def processFile(self):
        with open(self.filename) as file:
            q = file.readline().strip().split(' ')[2:]
            nonTerminalSet = file.readline().strip().split(' ')[2:]
            q0 = file.readline().strip().split(' ')[2:][0]
            finalStates = file.readline().strip().split(' ')[2:]

            transitions = {}
            file.readline()

            for line in file:
                source = line.strip().split(':')[0].strip().replace('(', '').replace(')', '').split(',')[0]
                nonTerminal = line.strip().split(':')[0].strip().replace('(', '').replace(')', '').split(',')[1]
                destination = line.strip().split(':')[1].strip()

                if not (source, nonTerminal) in transitions.keys():
                    transitions[(source, nonTerminal)] = [destination]
                else:
                    transitions[(source, nonTerminal)].append(destination)

        self.setOfStates = q
        self.nonTerminalSet = nonTerminalSet
        self.initialState = q0
        self.transitions = transitions
        self.finalStates = finalStates
