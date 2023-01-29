"""
Author: Rohan Singh
1/29/2023
In this python file we will learn how to create a quantum circuit, use logical gates and measuring the states of the qubits
"""

#  Imports
from qiskit import QuantumCircuit

#  Creating a circuit with 2 qubits
qc = QuantumCircuit(2) 

#  Measuring the states
qc.measure_all()
print("Intial State of the circuit")
print(qc.draw())

#  Applying the Hadamard gate on the first qubit
qc.h(0)  

#  Measuring the states
qc.measure_all()
print("Applying Hadamard gate to qubit 0")
print(qc.draw())

#  Using the CNOT gate on q1 controlled by q0
qc.cx(0,1) 

#  Measuring the states
qc.measure_all()
print("Final State of the circuit")
print(qc.draw())
