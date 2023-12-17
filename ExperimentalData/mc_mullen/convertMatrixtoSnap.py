import numpy as np

adjacency_matrix_file = '../../Data/mc_mullen.txt'
adjacency_matrix = np.loadtxt(adjacency_matrix_file)

edges = np.column_stack(np.where(adjacency_matrix == 1))

edge_list_file = 'mc_mullen_snap.txt'
np.savetxt(edge_list_file, edges, fmt='%d', delimiter='\t', comments='')
