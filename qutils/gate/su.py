from dataclasses import dataclass
from typing import Tuple

from qulacs import ParametricQuantumCircuit


@dataclass
class OneQubitGateParam:
    qubit_index: int
    angle: float


@dataclass
class TwoQubitGateParam:
    qubit_indices: Tuple[int, int]
    angle: float


@dataclass
class SU2Param:
    param1: OneQubitGateParam
    param2: OneQubitGateParam
    param3: OneQubitGateParam


@dataclass
class ParamA:
    param1: TwoQubitGateParam
    param2: TwoQubitGateParam
    param3: TwoQubitGateParam


@dataclass
class SU4Param:
    su2_param1: SU2Param
    su2_param2: SU2Param
    a_param: ParamA
    su2_param3: SU2Param
    su2_param4: SU2Param


class SU4:

    @staticmethod
    def add_interaction(circuit: ParametricQuantumCircuit,
                        param: SU4Param
                        ) -> ParametricQuantumCircuit:
        circuit = SU4._add_local_interaction(circuit, param.su2_param1)
        circuit = SU4._add_local_interaction(circuit, param.su2_param2)
        circuit = SU4._add_non_local_interaction(circuit, param.a_param)
        circuit = SU4._add_local_interaction(circuit, param.su2_param3)
        circuit = SU4._add_local_interaction(circuit, param.su2_param4)
        return circuit

    @staticmethod
    def _add_local_interaction(circuit: ParametricQuantumCircuit,
                               param: SU2Param
                               ) -> ParametricQuantumCircuit:
        circuit.add_parametric_RZ_gate(param.param1.qubit_index, param.param1.angle)
        circuit.add_parametric_RY_gate(param.param2.qubit_index, param.param2.angle)
        circuit.add_parametric_RZ_gate(param.param3.qubit_index, param.param3.angle)
        return circuit

    @staticmethod
    def _add_non_local_interaction(circuit: ParametricQuantumCircuit,
                                   param: ParamA) -> ParametricQuantumCircuit:
        XX_pauli_ids = [1, 1]
        YY_pauli_ids = [2, 2]
        ZZ_pauli_ids = [3, 3]

        circuit.add_parametric_multi_Pauli_rotation_gate(
            param.param1.qubit_indices,
            XX_pauli_ids,
            param.param1.angle
        )
        circuit.add_parametric_multi_Pauli_rotation_gate(
            param.param2.qubit_indices,
            YY_pauli_ids,
            param.param2.angle
        )
        circuit.add_parametric_multi_Pauli_rotation_gate(
            param.param3.qubit_indices,
            ZZ_pauli_ids,
            param.param3.angle
        )
        return circuit
