import numpy as np


def adjacency_matrix_to_weighted_snap(adj_matrix, output_file):
    with open(output_file, 'w') as f:
        num_nodes = adj_matrix.shape[0]

        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                if adj_matrix[i, j] != 0:
                    weight = adj_matrix[i, j]
                    f.write(f"{i} {j} {weight}\n")


file_path = '../../Data/mol_yeast_spliceosome.txt'
adj_matrix = np.loadtxt(file_path, dtype=float)

# Replace 'output_weighted_snap.txt' with the desired output file name
output_file_path = 'mol_yeast_spliceosome_snap.txt'
adjacency_matrix_to_weighted_snap(adj_matrix, output_file_path)
