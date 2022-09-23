from qulacs import ParametricQuantumCircuit
from qutils.gate import (SU4, OneQubitGateParam, ParamA, SU2Param, SU4Param,
                         TwoQubitGateParam)


def test_su4_add_interaction():
    num_qubit = 2
    circuit = ParametricQuantumCircuit(num_qubit)

    su2_param11 = SU2Param(
        OneQubitGateParam(0, 0.2),
        OneQubitGateParam(0, 0.4),
        OneQubitGateParam(0, 0.3)
    )
    su2_param12 = SU2Param(
        OneQubitGateParam(1, 0.1),
        OneQubitGateParam(1, 0.6),
        OneQubitGateParam(1, 0.2)
    )

    a_param = ParamA(
        TwoQubitGateParam((0, 1), 0.5),
        TwoQubitGateParam((0, 1), 0.4),
        TwoQubitGateParam((0, 1), 0.2)
    )

    su2_param21 = SU2Param(
        OneQubitGateParam(0, 0.3),
        OneQubitGateParam(0, 0.2),
        OneQubitGateParam(0, 0.3)
    )

    su2_param22 = SU2Param(
        OneQubitGateParam(1, 0.1),
        OneQubitGateParam(1, 0.5),
        OneQubitGateParam(1, 0.3)
    )

    su4_param = SU4Param(
        su2_param11,
        su2_param12,
        a_param,
        su2_param21,
        su2_param22
    )

    actual = SU4.add_interaction(circuit, su4_param)
    assert actual.get_gate_count() == 15
    assert actual.get_parameter_count() == 15
