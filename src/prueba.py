class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.current_state = start_state
        self.accept_states = accept_states

    def reset(self):
        self.current_state = start_state

    def process(self, input_string):
        for char in input_string:
            if char in self.alphabet:
                self.current_state = self.transition_function[self.current_state][char]
            else:
                return False
        return self.current_state in self.accept_states

states = {'q0', 'q1', 'q2'}
alphabet = {'0', '1'}
transition_function = {
    'q0': {'0': 'q0', '1': 'q1'},
    'q1': {'0': 'q2', '1': 'q1'},
    'q2': {'0': 'q0', '1': 'q1'}
}
start_state = 'q0'
accept_states = {'q2'}

dfa = DFA(states, alphabet, transition_function, start_state, accept_states)

input_string = "1101"
if dfa.process(input_string):
    print("Cadena aceptada")
else:
    print("Cadena no aceptada")
