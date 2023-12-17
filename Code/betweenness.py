from rich.progress import Progress
from rich.table import Table
import networkx as nx
import networkit as nk
import time
import math
import json


def perform_experiments(console, graph, input_file, directed, writeResult, resultsPath):
    table = Table(title="Experimental Results - Betweenness Centrality")
    table.add_column("Type", justify="left", style="cyan")
    table.add_column("Execution Time(s)", justify="left", style="green")
    with Progress() as progress:
        task = progress.add_task("[cyan]Working...", total=6)

        # !Exact calculation of betweenness centrality using Brandes in NetworkX
        start_time_exact = time.time()
        betweenness = nx.betweenness_centrality(graph)
        end_time_exact = time.time()
        if writeResult == True:
            path = resultsPath + '/BrandesExact.json'
            with open(path, 'w') as json_file:
                json.dump(betweenness, json_file,
                          indent=2, sort_keys=True)
        table.add_row("Exact - Brandes NetworkX",
                      str(end_time_exact - start_time_exact))
        progress.update(task, advance=1)

        # !Approximation of betweenness using sampling/pivotting in NetworkX:
        table.add_row("Approximation using sampling - Brandes/NetworkX")
        samples = [60, 80]
        for sample in samples:
            sampleSize = math.floor(len(graph.nodes) * (sample/100))
            average_time_brandes = 0
            for i in range(0, 1):
                # !Approximation of betweenness
                start_time_approx_brandes = time.time()
                betweenness_approx = nx.betweenness_centrality(
                    graph, k=sampleSize)
                end_time_approx_brandes = time.time()
                average_time_brandes += (end_time_approx_brandes -
                                         start_time_approx_brandes)
                if writeResult == True:
                    path = resultsPath + \
                        f'/BrandesEstimation{sample}_{str(i)}.json'
                    with open(path, 'w') as json_file:
                        json.dump(betweenness_approx, json_file,
                                  indent=2, sort_keys=True)
            average_time_brandes /= 10
            table.add_row(f"\t {sample}% sampled, average of 10 runs",
                          str(average_time_brandes))
        progress.update(task, advance=1)

        # !Approximation of betweenness using networkit:
        try:
            if directed == True:
                G = nk.readGraph(
                    input_file, nk.Format.EdgeListTabZero, directed=True)
            else:
                G = nk.readGraph(
                    input_file, nk.Format.EdgeListTabZero, directed=False)
        except:
            try:
                if directed == True:
                    G = nk.readGraph(
                        input_file, nk.Format.EdgeListSpaceZero, directed=True)
                else:
                    G = nk.readGraph(
                        input_file, nk.Format.EdgeListSpaceZero, directed=False)
            except:
                console.print(
                    f"[bold red]Error: Input file - '{input_file}' not readable by NetworKit.[/bold red]\n")
                exit(1)

        # !"Geisberger" approach:
        table.add_row("Approximation - Geisberger/NetworKit")
        average_time_geisberger = 0
        for i in range(0, 1):
            start_time_approx_geisberger = time.time()
            geisberger_betweenness = nk.centrality.EstimateBetweenness(
                G, 10000, True, False)
            geisberger_betweenness.run()
            end_time_approx_geisberger = time.time()
            average_time_geisberger += (end_time_approx_geisberger -
                                        start_time_approx_geisberger)
            if writeResult == True:
                path = resultsPath + f"/geisberger{str(i)}.json"
                with open(path, 'w') as json_file:
                    json.dump(dict(geisberger_betweenness.ranking()), json_file,
                              indent=2, sort_keys=True)
        average_time_geisberger /= 10
        table.add_row(f"\t Average of 10 runs",
                      str(average_time_geisberger))
        progress.update(task, advance=1)

        # !"Riondato" approach:
        table.add_row("Approximation - Riondato/NetworKit")
        average_time_riondato = 0
        for i in range(0, 1):
            start_time_approx_riondato = time.time()
            riondato_betweenness = nk.centrality.ApproxBetweenness(G,
                                                                   epsilon=0.01,
                                                                   delta=0.1,
                                                                   universalConstant=0.5)
            riondato_betweenness.run()
            end_time_approx_riondato = time.time()
            average_time_riondato += (end_time_approx_riondato -
                                      start_time_approx_riondato)
            if writeResult == True:
                path = resultsPath + f"/riondato{str(i)}.json"
                with open(path, 'w') as json_file:
                    json.dump(dict(riondato_betweenness.ranking()), json_file,
                              indent=2, sort_keys=True)
        average_time_riondato /= 10
        table.add_row(f"\t Average of 10 runs",
                      str(average_time_riondato))
        progress.update(task, advance=1)

        # !"Kadabra" approach:
        table.add_row("Approximation - Kadabra/NetworKit")
        average_time_kadabra = 0
        for i in range(0, 1):
            start_time_kadabra = time.time()
            betweenness_kadabra = nk.centrality.KadabraBetweenness(
                G, 0.1, 0.8)  # these are the default settings
            betweenness_kadabra.run()
            end_time_kadabra = time.time()
            average_time_kadabra += (end_time_kadabra -
                                     start_time_kadabra)
            if writeResult == True:
                path = resultsPath + f"/kadabra{str(i)}.json"
                with open(path, 'w') as json_file:
                    json.dump(dict(betweenness_kadabra.ranking()), json_file,
                              indent=2, sort_keys=True)
        average_time_kadabra /= 10
        table.add_row(f"\t Average of 10 runs",
                      str(average_time_kadabra))
        progress.update(task, advance=1)

        # # !"Bergamini" approach:
        table.add_row("Approximation - Bergamini/NetworKit")
        average_time_bergamini = 0
        for i in range(0, 1):
            start_time_approx_bergamini = time.time()
            bergamini_betweenness = nk.centrality.DynApproxBetweenness(
                G, epsilon=0.075, delta=0.1, storePredecessors=False, universalConstant=0.5)
            bergamini_betweenness.run()
            end_time_approx_bergamini = time.time()
            average_time_bergamini += (end_time_approx_bergamini -
                                       start_time_approx_bergamini)
            if writeResult == True:
                path = resultsPath + f"/bergamini{str(i)}.json"
                with open(path, 'w') as json_file:
                    json.dump(dict(bergamini_betweenness.ranking()), json_file,
                              indent=2, sort_keys=True)
        average_time_bergamini /= 10
        table.add_row(f"\t Average of 10 runs",
                      str(average_time_bergamini))
        progress.update(task, advance=1)

    console.print("\n")
    console.print(table)
    console.print("\n")
