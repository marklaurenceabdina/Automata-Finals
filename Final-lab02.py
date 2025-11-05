class FiniteStateMachine:
    def __init__(self, states, initial_state):
        self.states = states
        self.initial_state = initial_state
        self.state = initial_state

    def reset(self):
        self.state = self.initial_state


class MooreMachine(FiniteStateMachine):
    MOORE_TRANSITIONS = {
        'A/A': {'0': 'A/A', '1': 'B/B'},
        'B/B': {'0': 'C/A', '1': 'D/B'},
        'D/C': {'0': 'B/B', '1': 'C/C'},
        'C/A': {'0': 'D/C', '1': 'B/B'},
        'C/C': {'0': 'D/C', '1': 'B/B'},
        'D/B': {'0': 'B/B', '1': 'C/C'},
        'E/C': {'0': 'D/C', '1': 'E/C'}
    }

    def __init__(self):
        super().__init__(states=list(self.MOORE_TRANSITIONS.keys()), initial_state='A/A')

    def get_output(self, state):
        return state.split('/')[1]

    def process(self, inp):
        self.reset()
        output = self.get_output(self.state)

        for ch in inp:
            self.state = self.MOORE_TRANSITIONS[self.state][ch]
            output += self.get_output(self.state)

        print(f"Input:  {inp}")
        print(f"Output: {output}")
        print("----------------")


if __name__ == "__main__":
    moore = MooreMachine()
    test_inputs = ["00110", "11001", "1010110", "101111"]

    for test in test_inputs:
        moore.process(test)
