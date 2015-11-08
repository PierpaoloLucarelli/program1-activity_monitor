# file: lab09_example1/FSM.py
# Base class (superclass) for inheritance hierarchy
# of state machine implementations
class FSM:
    def start(self):
        self.state = self.startState
    # now prompt the FSM to step to its next state
    # return output prompted by this transition
    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        # print (s)
        return o
    # method used for testing the FSM implementation
    # method must be invoked with a list of inputs
    # returns a list of total state descriptors
    # where total state is a tuple comprising:
    # input
    # output
    # next state
    def transduce(self, inputs):
        # initialise the FSM
        self.start()
        # now run FSM through a serious of state changes
        # prompted by inputs to the FSM
        return [(str(inp), self.step(inp), self.state) \
                for inp in inputs]
    '''
    # Another version of method transduce implemented as a Python generator 
    def transduce(self, inputs):
        for inp in inputs:
            outp = self.step(inp)
            # problem printing None as string is solved (2 ways) below
            #yield (inp if inp else 'None', outp, self.state)
            yield (str(inp), outp, self.state)
    '''
    
