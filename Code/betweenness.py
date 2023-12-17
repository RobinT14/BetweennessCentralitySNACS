from rich.progress import Progress
from rich.table import Table
import networkx as nx
import networkit as nk
import time
import math


def perform_experiments(console, graph, input_file):
    table = Table(title="Experimental Results - Betweenness Centrality")
    table.add_column("Type", justify="left", style="cyan")
    table.add_column("Execution Time(s)", justify="left", style="green")
    with Progress() as progress:
        task = progress.add_task("[cyan]Working...", total=5)

        # !Exact calculation of betweenness centrality using Brandes in NetworkX
        start_time_exact = time.time()
        betweenness = nx.betweenness_centrality(graph)
        end_time_exact = time.time()
        # TODO Write Exact To File
        table.add_row("Exact - Brandes NetworkX",
                      str(end_time_exact - start_time_exact))
        progress.update(task, advance=1)

        # !Approximation of betweenness using sampling/pivotting in NetworkX:
        table.add_row("Approximation using sampling - Brandes/NetworkX")
        samples = [60, 80]  # TODO Add more sample percentages if wanted?
        for sample in samples:
            sampleSize = math.floor(len(graph.nodes) * (sample/100))
            average_time_brandes = 0
            for i in range(0, 10):
                # !Approximation of betweenness
                start_time_approx_brandes = time.time()
                betweenness_approx = nx.betweenness_centrality(
                    graph, k=sampleSize)
                end_time_approx_brandes = time.time()
                average_time_brandes += (end_time_approx_brandes -
                                         start_time_approx_brandes)
            average_time_brandes /= 10
            table.add_row(f"\t {sample}% sampled, average of 10 runs",
                          str(average_time_brandes))
        progress.update(task, advance=1)

        # !Approximation of betweenness using networkit:
        try:
            G = nk.readGraph(
                input_file, nk.Format.EdgeListTabZero, directed=False)
            # G = nk.readGraph(
            #     input_file, nk.Format.EdgeListTabOne)
        except:
            try:
                G = nk.readGraph(
                    input_file, nk.Format.EdgeListSpaceZero, directed=False)
                # G = nk.readGraph(
                #     input_file, nk.Format.EdgeListSpaceOne)
            except:
                console.print(
                    f"[bold red]Error: Input file - '{input_file}' not readable by NetworKit.[/bold red]\n")
                exit(1)

        # !"Geisberger" approach:
        table.add_row("Approximation - Geisberger/NetworKit")
        average_time_geisberger = 0
        for i in range(0, 10):
            start_time_approx_geisberger = time.time()
            geisberger_betweenness = nk.centrality.EstimateBetweenness(
                G, 50, True, False)
            geisberger_betweenness.run()
            end_time_approx_geisberger = time.time()
            average_time_geisberger += (end_time_approx_geisberger -
                                        start_time_approx_geisberger)
        average_time_geisberger /= 10
        table.add_row(f"\t Average of 10 runs",
                      str(average_time_geisberger))
        progress.update(task, advance=1)

        # !"Riondato" approach:
        table.add_row("Approximation - Riondato/NetworKit")
        average_time_riondato = 0
        for i in range(0, 10):
            start_time_approx_riondato = time.time()
            riondato_betweenness = nk.centrality.ApproxBetweenness(G,
                                                                   epsilon=0.1,
                                                                   delta=0.1,
                                                                   universalConstant=0.5)
            riondato_betweenness.run()
            end_time_approx_riondato = time.time()
            average_time_riondato += (end_time_approx_riondato -
                                      start_time_approx_riondato)
        average_time_riondato /= 10
        table.add_row(f"\t Average of 10 runs",
                      str(average_time_riondato))
        progress.update(task, advance=1)

        # # !"Bergamini" approach:
        table.add_row("Approximation - Bergamini/NetworKit")
        average_time_bergamini = 0
        for i in range(0, 10):
            start_time_approx_bergamini = time.time()
            bergamini_betweenness = nk.centrality.DynApproxBetweenness(
                G, epsilon=0.01, delta=0.1, storePredecessors=True, universalConstant=0.5)
            bergamini_betweenness.run()
            end_time_approx_bergamini = time.time()
            average_time_bergamini += (end_time_approx_bergamini -
                                       start_time_approx_bergamini)
        average_time_bergamini /= 10
        table.add_row(f"\t Average of 10 runs",
                      str(average_time_bergamini))
        progress.update(task, advance=1)

    console.print("\n")
    console.print(table)
    console.print("\n")
