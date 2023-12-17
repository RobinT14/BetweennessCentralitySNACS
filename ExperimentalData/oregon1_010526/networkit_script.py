from datetime import datetime
import networkit as nk
import time
import json


if __name__ == "__main__":
    filename = '../../Data/oregon1_010526.txt'
    current_datetime = datetime.now()
    current_date_string = current_datetime.strftime("%d-%m-%Y")

    try:
        G = nk.readGraph(filename, nk.Format.EdgeListTabZero, directed=False)
    except:
        try:
            G = nk.readGraph(
                filename, nk.Format.EdgeListSpaceZero, directed=False)
        except:
            print("Wrong format")
            exit(1)

    # "Geisberger" approach:
    for i in range(0, 10):
        start_time_geisberger = time.time()
        betweenness = nk.centrality.EstimateBetweenness(G, 50, True, False)
        betweenness.run()
        end_time_geisberger = time.time()

        # Write exact betweenness to file:
        path = f"NetworKit_Results/{current_date_string}_networkit_geisberger_{str(i)}.json"
        with open(path, 'w') as json_file:
            json.dump(dict(betweenness.ranking()), json_file,
                      indent=2, sort_keys=True)

         # Output statistics
        printLine = f'Approximation_Geisberger_NetworKit_{i},' + filename + ',' +\
            str(end_time_geisberger - start_time_geisberger) + ',' + path + '\n'
        with open('networkit_output.log', 'a') as file:
            file.write(printLine)

    # "Riondato" approach:
    for i in range(0, 10):
        start_time_riondato = time.time()
        betweenness_riondato = nk.centrality.ApproxBetweenness(G,
                                                               epsilon=0.1,
                                                               delta=0.1,
                                                               universalConstant=0.5)
        betweenness_riondato.run()
        end_time_riondato = time.time()

        # Write exact betweenness to file:
        path = f"NetworKit_Results/{current_date_string}_networkit_riondato_{str(i)}.json"
        with open(path, 'w') as json_file:
            json.dump(dict(betweenness_riondato.ranking()), json_file,
                      indent=2, sort_keys=True)

         # Output statistics
        printLine = f'Approximation_Riondato_NetworKit_{i},' + filename + ',' +\
            str(end_time_riondato - start_time_riondato) + ',' + path + '\n'
        with open('networkit_output.log', 'a') as file:
            file.write(printLine)

    # Van der Grinten A., Angriman E., and Meyerhenke H. (2019) approach of Kadabra algorithm
    for i in range(0, 10):
        start_time_kadabra = time.time()
        betweenness_kadabra = nk.centrality.KadabraBetweenness(
            G, 0.05, 0.8)  # these are the default settings
        betweenness_kadabra.run()
        end_time_kadabra = time.time()

        # Write exact betweenness to file:
        path = f"NetworKit_Results/{current_date_string}_networkit_kadabra_{str(i)}.json"
        with open(path, 'w') as json_file:
            json.dump(dict(betweenness_kadabra.ranking()), json_file,
                      indent=2, sort_keys=True)

         # Output statistics
        printLine = f'Approximation_Kadabra_NetworKit_{i},' + filename + ',' +\
            str(end_time_kadabra - start_time_kadabra) + ',' + path + '\n'
        with open('networkit_output.log', 'a') as file:
            file.write(printLine)

    # "Bergamini and Meyerhenke" approach:
    for i in range(0, 10):
        start_time_bergamini = time.time()
        betweenness_bergamini = nk.centrality.DynApproxBetweenness(
            G, epsilon=0.1, delta=0.1, storePredecessors=True, universalConstant=0.5)
        betweenness_bergamini.run()
        end_time_bergamini = time.time()

        # Write exact betweenness to file:
        path = f"NetworKit_Results/{current_date_string}_networkit_bergamini_{str(i)}.json"
        with open(path, 'w') as json_file:
            json.dump(dict(betweenness_bergamini.ranking()), json_file,
                      indent=2, sort_keys=True)

         # Output statistics
        printLine = f'Approximation_Bergamini_NetworKit_{i},' + filename + ',' +\
            str(end_time_bergamini - start_time_bergamini) + ',' + path + '\n'
        with open('networkit_output.log', 'a') as file:
            file.write(printLine)
