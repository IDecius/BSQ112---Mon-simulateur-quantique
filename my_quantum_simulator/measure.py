import numpy as np
from numpy.typing import NDArray


def sample_state(state_vector: NDArray, shots: int) -> dict:
    """
    Simulate the sampling for a given statevector

    Args:
        state_vector (NDArray): A statevector
        shots (int): The total number of samples to take.

    Returns:
        dict: Results of the sampling given as a dictionary. Keys are bit strings (ex : "0110") and values integers.
    """

    ### À compléter
    number_of_qubits = int(np.log2(len(state_vector)))
 
    # Règle de Born : probabilité = module au carré de l'amplitude
    probabilities = np.abs(state_vector) ** 2
    probabilities = probabilities / probabilities.sum()  # corrige les erreurs d'arrondi
 
    # Chaque échantillon est l'entier j qui représente un état de base
    samples = np.random.choice(len(state_vector), size=shots, p=probabilities)
 
    # Seuls les états réellement obtenus apparaissent dans le dictionnaire
    basis_states, counts = np.unique(samples, return_counts=True)
    bit_strings = [f"{state:0{number_of_qubits}b}" for state in basis_states]
    ###

    return dict(zip(bit_strings, [int(count) for count in counts]))
