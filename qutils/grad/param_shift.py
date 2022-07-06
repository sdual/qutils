import numpy as np
from qulacs import Observable, ParametricQuantumCircuit, QuantumState


class ParamShiftGrad:

    @staticmethod
    def calculate_grad(circuit: ParametricQuantumCircuit,
                       param_index: int, obs: Observable) -> float:
        param = circuit.get_parameter(param_index)
        circuit.set_parameter(param_index, param + np.pi / 4.0)
        plus_exp = ParamShiftGrad._expectation_value(circuit, obs)

        circuit.set_parameter(param_index, param - np.pi / 4.0)
        minus_exp = ParamShiftGrad._expectation_value(circuit, obs)

        circuit.set_parameter(param_index, param)
        return plus_exp - minus_exp

    @staticmethod
    def _expectation_value(circuit: ParametricQuantumCircuit,
                           obs: Observable) -> float:
        state = QuantumState(circuit.get_qubit_count)
        state.set_zero_state()
        circuit.update_quantum_state(state)
        return obs.get_expectation_value(state)
