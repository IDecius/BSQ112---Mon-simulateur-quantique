from gates import build_ry_gate, control, compose_gates, reorder_qubits_gate, convert_to_more_qubits
from gates import Z_GATE, H_GATE, X_GATE
from states import prepare_init_state
from measure import sample_state
import numpy as np

print("Matrice de la porte Ry(angle) :")
print(build_ry_gate(np.pi/2))

x0_gate = np.array([[0,1],[1,0]])
c0x1_gate = control(x0_gate)
c0c1x2_gate = control(c0x1_gate)
print("\nMatrice de la porte C_0C_1X_2 :")
print(c0c1x2_gate)

XHZ_gate = compose_gates((Z_GATE, H_GATE, X_GATE))
print("\nMatrice de la porte XHZ :")
print(XHZ_gate)

c0x1c2_gate = reorder_qubits_gate(c0c1x2_gate, [0, 2, 1])
print("\nMatrice de la nouvelle porte C_0X_1C_2 :")
print(c0x1c2_gate)

c0x2_gate = convert_to_more_qubits(c0x1_gate, 3, [0, 2])
print("\nMatrice de la porte étendue C_0X_2 :")
np.set_printoptions(threshold=np.inf)
print(c0x2_gate)

init_state = prepare_init_state(2)
print("\nVecteur de l'état initial à 3 qubits :")
print(init_state)


i_gate = np.array([[1,0],[0,1]])
h_gate = np.sqrt(0.5) * np.array([[1,1],[1,-1]])
cx_gate = np.array([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]])
ih_gate = np.kron(i_gate, h_gate)
u_circuit = cx_gate @ ih_gate

bell_state = u_circuit @ init_state
print("\nÉtat de Bell :")
print(bell_state)
counts = sample_state(bell_state, 100)
print("\nÉchantillonage de l'état de Bell :")
print(counts)