import os
import json
from scipy.stats import kendalltau
import numpy as np


def read_betweenness_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


def calculate_kendall_tau(exact_betweenness, approx_betweenness):

    exact_keys = sorted(exact_betweenness.keys())
    approx_keys = sorted(approx_betweenness.keys())

    exact_values = [exact_betweenness[key] for key in exact_keys]
    approx_values = [approx_betweenness[key] for key in exact_keys]

    tau, _ = kendalltau(exact_values, approx_values)
    return tau


def main():
    exact_file_path = 'NetworkX_Results/09-12-2023_networkx_exact.json'
    exact_betweenness = read_betweenness_from_json(exact_file_path)

    file1 = open('networkit_output.log', 'r')
    Lines = file1.readlines()

    for line in Lines:
        line = line.strip()
        printLine = line + ','
        if 'Approximation' in line:
            path = line.split(',')[3]
            approx_betweenness = read_betweenness_from_json(path)
            tau = calculate_kendall_tau(exact_betweenness, approx_betweenness)
            printLine += str(tau)
        print(printLine)


if __name__ == "__main__":
    main()
