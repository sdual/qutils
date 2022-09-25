from nptyping import NDArray
from qulacs import ParametricQuantumCircuit
from qutils.model.circuit_constructor import CircuitConstructor


class TrainMixin:

    def _train(self,
               circuit: ParametricQuantumCircuit,
               X: NDArray,
               y: NDArray) -> None:
        pass


class SU4CircuitLearning:

    def __init__(self, num_qubit: int, num_layers: int):
        self._num_qubit = num_qubit
        self._num_layers = num_layers
        self._circuit_contructor = None

    def fit(self, X: NDArray, y: NDArray) -> None:
        pass

    def predict(self, X: NDArray) -> NDArray:
        pass
