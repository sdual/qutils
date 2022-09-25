from qulacs import ParametricQuantumCircuit


class CircuitConstructor:

    def __init__(self, num_qubit: int, num_layers: int):
        self._num_qubit = num_qubit
        self._num_layers = num_layers

    def construct(self) -> ParametricQuantumCircuit:
        pass


class SU4CircuitConstructor:

    def __init__(self):
        pass
