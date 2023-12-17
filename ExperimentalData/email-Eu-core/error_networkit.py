import os
import json
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error


def read_betweenness_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


def calculate_errors(exact_betweenness, approx_betweenness):
    exact_keys = sorted(exact_betweenness.keys())
    approx_keys = sorted(approx_betweenness.keys())

    exact_values = np.array([exact_betweenness[key] for key in exact_keys])
    approx_values = np.array([approx_betweenness[key] for key in exact_keys])

    # Calculate Mean Absolute Error (MAE)
    mae = mean_absolute_error(exact_values, approx_values)

    # Calculate Root Mean Squared Error (RMSE)
    rmse = np.sqrt(mean_squared_error(exact_values, approx_values))

    return mae, rmse


def main():
    exact_file_path = 'NetworkX_Results/08-12-2023_networkx_exact.json'
    exact_betweenness = read_betweenness_from_json(exact_file_path)

    file1 = open('networkit_output.log', 'r')
    Lines = file1.readlines()

    for line in Lines:
        line = line.strip()
        printLine = line + ','
        if 'Approximation' in line:
            path = line.split(',')[3]
            approx_betweenness = read_betweenness_from_json(path)
            mae, rmse = calculate_errors(exact_betweenness, approx_betweenness)
            printLine += f'{mae},{rmse}'
        print(printLine)


if __name__ == "__main__":
    main()
