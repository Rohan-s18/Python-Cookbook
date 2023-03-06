import numpy as np
import qiskit
from qiskit_experiments.library import T2Ramsey
from qiskit.providers.fake_provider import FakeVigo
from qiskit.providers.aer import AerSimulator
from qiskit.providers.aer.noise import NoiseModel

"""
1. Hadamard gate
2. delay
3. RZ gate that rotates the qubit in the x-y plane
4. Hadamard gate
5. measurement
"""

qubit = 0
# set the desired delays
delays = list(np.arange(1e-6, 50e-6, 2e-6))

# Create a T2Ramsey experiment. Print the first circuit as an example
exp1 = T2Ramsey(qubit, delays, osc_freq=1e5)

print(exp1.circuits()[0])


# Create a pure relaxation noise model for AerSimulator
noise_model = NoiseModel.from_backend(
    FakeVigo(), thermal_relaxation=True, gate_error=False, readout_error=False
)

# Create a fake backend simulator
backend = AerSimulator.from_backend(FakeVigo(), noise_model=noise_model)

# Set scheduling method so circuit is scheduled for delay noise simulation
exp1.set_transpile_options(scheduling_method='asap')

# Run experiment
expdata1 = exp1.run(backend=backend, shots=2000, seed_simulator=101)
expdata1.block_for_results()  # Wait for job/analysis to finish.

# Display the figure
display(expdata1.figure(0))


# Print results
for result in expdata1.analysis_results():
    print(result)
    
    
user_p0={
    "A": 0.5,
    "T2star": 20e-6,
    "f": 110000,
    "phi": 0,
    "B": 0.5
        }
exp_with_p0 = T2Ramsey(qubit, delays, osc_freq=1e5)
exp_with_p0.analysis.set_options(p0=user_p0)
exp_with_p0.set_transpile_options(scheduling_method='asap')
expdata_with_p0 = exp_with_p0.run(backend=backend, shots=2000, seed_simulator=101)
expdata_with_p0.block_for_results()

# Display fit figure
display(expdata_with_p0.figure(0))

# Print results
for result in expdata_with_p0.analysis_results():
    print(result)
