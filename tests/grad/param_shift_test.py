from qulacs import Observable, ParametricQuantumCircuit
from qutils.grad import ParamShiftGrad


def test_calculate_grad():
    num_qubit = 2
    circuit = ParametricQuantumCircuit(num_qubit)

    circuit.add_parametric_RY_gate(0, 0.2)
    circuit.add_parametric_RY_gate(1, 0.6)
    circuit.add_CNOT_gate(0, 1)
    obs = Observable(num_qubit)
    obs.add_operator(1.0, 'Z 1')

    param_index = 0
    actual = ParamShiftGrad.calculate_grad(circuit, param_index, obs)

    assert actual == -0.2318870058356548
