from datetime import datetime
import networkx as nx
import time
import json
import math

# Directed and unweighted:
if __name__ == "__main__":

    filename = '../../Data/email-Eu-core.txt'
    current_datetime = datetime.now()
    current_date_string = current_datetime.strftime("%d-%m-%Y")

    G = nx.read_edgelist(filename,
                         nodetype=int,
                         create_using=nx.DiGraph,
                         data=(("weight", float), ))

    start_time_exact = time.time()
    betweenness = nx.betweenness_centrality(G)
    end_time_exact = time.time()

    # Write exact betweenness to file:
    sorted_betweenness = {k: betweenness[k] for k in sorted(betweenness)}
    path = f"NetworkX_Results/{current_date_string}_networkx_exact.json"
    with open(path, 'w') as json_file:
        json.dump(sorted_betweenness, json_file, indent=2, sort_keys=True)

    # Output statistics
    printLine = 'Exact_Brandes_NetworkX,' + filename + ',' +\
        str(end_time_exact - start_time_exact) + ',' + path + '\n'
    with open('networkx_output.log', 'a') as file:
        file.write(printLine)

    # Approximations of betweenness using sampling/pivotting
    # Sample sizes ranging from 20-80%, 10 runs for each sample size
    samples = [20, 40, 60, 80]
    for sample in samples:
        sampleSize = math.floor(len(G.nodes) * (sample/100))
        for i in range(0, 10):
            # Approximation of betweenness
            start_time_approx = time.time()
            betweenness_approx = nx.betweenness_centrality(G, k=sampleSize)
            end_time_approx = time.time()

            # Write approximated betweenness to file
            sorted_betweenness_approx = {k: betweenness_approx[k]
                                         for k in sorted(betweenness_approx)}
            path = f"NetworkX_Results/{current_date_string}_networkx_approximation_{str(sample)}_{str(i)}.json"
            with open(path, 'w') as json_file:
                json.dump(sorted_betweenness_approx, json_file,
                          indent=2, sort_keys=True)

            printLine = f'Approximation_Brandes_NetworkX_{str(sample)}_{str(i)},' + filename + ',' +\
                str(end_time_approx - start_time_approx) + ',' + path + '\n'
            with open('networkx_output.log', 'a') as file:
                file.write(printLine)
