"""
Author: Rohan Singh
3/1/2023
Python Module to demonstrate the single qubit gates in quantum computing
"""

#  Imports

from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from math import sqrt, pi

svsim = Aer.get_backend('statevector_simulator')

def initial():
    #Defining circuit objects
    qc = QuantumCircuit(1)
    qc.draw(output='mpl')
    qobj = assemble(qc)
    state = svsim.run(qobj).result().get_statevector()
    plot_bloch_multivector(state)

#  X-flip gate
def x_flip():
    print("Demonstration for the X-flip gate")

    #Defining circuit objects
    qc = QuantumCircuit(1)
    qc.x(0)
    qc.draw(output='mpl')

    #Plotting the bloch sphere
    qobj = assemble(qc)
    state = svsim.run(qobj).result().get_statevector()
    plot_bloch_multivector(state)

#  Z-flip gate
def z_flip():
    print("Demonstration for the Z-flip gate")

    #Defining circuit objects
    qc = QuantumCircuit(1) 
    initial_state = [1/sqrt(2),1/sqrt(2)]   
    qc.initialize(initial_state, 0)

    #Plotting the bloch sphere
    qobj = assemble(qc)
    state = svsim.run(qobj).result().get_statevector()
    plot_bloch_multivector(state)

#  Y-flip gate
def y_flip():
    print("Demonstration for the Z-flip gate")

    #Defining circuit objects
    qc = QuantumCircuit(1)
    qc.z(0)

    #Plotting the bloch sphere
    qobj = assemble(qc)
    state = svsim.run(qobj).result().get_statevector()
    plot_bloch_multivector(state)

#  Hadamard gate
def hadamard():
    print("Demonstration for the Hadamard gate")

    qc = QuantumCircuit(1)

    #Defining circuit objects
    qc.h(0)

    #Plotting the bloch sphere
    qobj = assemble(qc)
    state = svsim.run(qobj).result().get_statevector()
    plot_bloch_multivector(state)

#  Phase gate
def phi(phase_angle):
    print("Demonstration for the phase gate")

    #Defining circuit objects
    qc = QuantumCircuit(1) 
    initial_state = [1/sqrt(2),1/sqrt(2)]   
    qc.initialize(initial_state, 0)
    qc.rz(phase_angle,0)

    #Plotting the bloch sphere
    qobj = assemble(qc)
    state = svsim.run(qobj).result().get_statevector()
    plot_bloch_multivector(state)



#  Main function
def main():
    
    #Uncomment the gate you would like to see
    initial()
    x_flip()
    y_flip()
    z_flip()
    hadamard()
    phi(pi/4)


if __name__ == "__main__":
    main()