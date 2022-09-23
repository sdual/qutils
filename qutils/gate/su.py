from dataclasses import dataclass

from qulacs import ParametricQuantumCircuit


@dataclass
class GateParam:
    qubit_index: int
    angle: float


@dataclass
class SU2Param:
    param1: GateParam
    param2: GateParam
    param3: GateParam


@dataclass
class ParamA:
    param1: GateParam
    param2: GateParam
    param3: GateParam


@dataclass
class SU4Param:
    su2Param1: SU2Param
    su2Param2: SU2Param
    aParam: ParamA
    su2Param3: SU2Param
    su2Param4: SU2Param


class SU4:

    @staticmethod
    def add_interaction(circuit: ParametricQuantumCircuit,
                        param: SU4Param
                        ) -> ParametricQuantumCircuit:
        circuit = SU4._add_local_interaction(circuit, param.su2Param1)
        circuit = SU4._add_local_interaction(circuit, param.su2Param2)
        circuit = SU4._add_non_local_interaction(circuit, param.aParam)
        circuit = SU4._add_local_interaction(circuit, param.su2Param3)
        circuit = SU4._add_local_interaction(circuit, param.su2Param4)
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
            param.param1.qubit_index, XX_pauli_ids, param.param1.angle
        )
        circuit.add_parametric_multi_Pauli_rotation_gate(
            param.param2.qubit_index, YY_pauli_ids, param.param2.angle
        )
        circuit.add_parametric_multi_Pauli_rotation_gate(
            param.param3.qubit_index, ZZ_pauli_ids, param.param3.angle
        )
        return circuit
