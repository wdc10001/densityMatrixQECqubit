import cirq
import numpy as np

class X2m(cirq.Gate):
    def __init__(self):
        super(X2m, self)

    def _num_qubits_(self):
        return 1

    def _qid_shape_(self):
        return (3,)

    def _unitary_(self):
        return np.array([[1, 1j, 0],
                         [1j, 1, 0],
                         [0, 0, 1]]/ np.sqrt(2))

    def _circuit_diagram_info_(self, args):
        return 'X2m'

# def func():
#     circ = cirq.Circuit([X2m().on(cirq.LineQid(0,dimension=3))])
#     print(circ)
# func()

def func(gate:cirq.Gate):
    circ = cirq.Circuit([gate.on(cirq.LineQid(0,dimension=3))])
    print(circ)
func(X2m())