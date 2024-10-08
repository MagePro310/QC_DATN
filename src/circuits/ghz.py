"""GHZ state circuit generators."""
from functools import lru_cache

from qiskit import QuantumCircuit

"""
The GHZ state is an entangled quantum state that is a superposition of all qubits being in the state |0⟩ and all qubits being in the state |1⟩.
The GHZ state is defined as:
    |GHZ⟩ = 1/sqrt(2) * (|0⟩^⊗n + |1⟩^⊗n)
where n is the number of qubits in the state.
The GHZ state is a maximally entangled state and is used in many quantum information protocols.

The circuit to create a GHZ state is as follows:
    1. Apply a Hadamard gate to the first qubit.
    2. Apply a CNOT gate to the first qubit and the second qubit.
    3. Apply a CNOT gate to the second qubit and the third qubit.
    4. Repeat step 3 for all qubits in the state.
    5. Measure all qubits in the state.
    
The circuit to create a GHZ state without measurement is as follows:
    1. Apply a Hadamard gate to the first qubit.
    2. Apply a CNOT gate to the first qubit and the second qubit.
    3. Apply a CNOT gate to the second qubit and the third qubit.
    4. Repeat step 3 for all qubits in the state.
    
The GHZ state is used in many quantum information protocols, such as quantum teleportation, superdense coding, and quantum error correction.
"""

@lru_cache                                                         # Cache the result of the function
def create_ghz(n_qubits: int) -> QuantumCircuit:
    """Generates a n-qubit GHZ state.

    Includes measurement.
    Args:
        n_qubits (int): Number of qubits.

    Returns:
        QuantumCircuit: The quantum circuit object.
    """
    circuit = QuantumCircuit(n_qubits, n_qubits)                    # n_qubits qubits and n_qubits classical bits
    circuit.h(0)                                                    # Apply Hadamard gate to the first qubit
    for i in range(n_qubits - 1):
        circuit.cx(i, i + 1)                                        # Apply CNOT gate to the qubits
    circuit.measure(list(range(n_qubits)), list(range(n_qubits)))   # Measure all qubits
    return circuit                                                  # Return the circuit object


@lru_cache                                                          # Cache the result of the function
def create_quantum_only_ghz(n_qubits: int) -> QuantumCircuit:
    """Generater a n-qubit GHZ state.

    Without measurement.
    Args:
        n_qubits (int): Number of qubits.

    Returns:
        QuantumCircuit: The quantum circuit object.
    """
    circuit = QuantumCircuit(n_qubits)                              # n_qubits qubits and no classical bits
    circuit.h(0)                                                    # Apply Hadamard gate to the first qubit
    for i in range(n_qubits - 1):                                   
        circuit.cx(i, i + 1)                                        # Apply CNOT gate to the qubits
    return circuit                                                  # Return the circuit object
