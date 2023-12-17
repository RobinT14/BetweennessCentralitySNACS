# This script contains the code as presented in course paper: 'A novel
# comparison of betweennesscentrality calculation and approximation approaches'.
#
# This script will perform the follwing:
# - Exact calculation of betweenness centrality using the Brandes approach.
# - Approximation of betweenness centrality using NetworkX and NetworKit.
#
# Created by R Wensveen & R The

import argparse
import os
from Code.format import print_header
from Code.graph import read_file, print_graph_stats
from Code.betweenness import perform_experiments
from rich.console import Console


def main():
    parser = argparse.ArgumentParser(
        description='This script will perform exact calculation and approximation of betweenness centrality, and will present the statistics of this.')

    parser.add_argument(
        'input_file', help='Path to the input file, of a give graph')

    parser.add_argument(
        '-d', '--directed', help='Set input graph type to directed graph. True OR False, Default=True')

    parser.add_argument(
        '-w', '--weighted', help='Set input graph type to weighted graph. Float OR Int, Default=Float')

    args = parser.parse_args()

    # Arguments:
    input_file = args.input_file
    directed = True
    if args.directed is not None:
        if args.directed == "True":
            directed = True
        elif args.directed == "False":
            directed = False
        else:
            console.print(
                f"[bold red]Error: Command Line Argument '-d', '--directed' shoud be True or False.[/bold red]\n")
            exit(1)

    if os.path.isfile(input_file):
        console.print(
            f"[bold green]Reading graph from input file: '{input_file}'[/bold green]\n")
    else:
        console.print(
            f"[bold red]Error: Input file - '{input_file}' does not exist.[/bold red]\n")
        exit(1)

    graph = read_file(input_file, console, directed)
    print_graph_stats(console, input_file, graph)

    perform_experiments(console, graph, input_file)


if __name__ == "__main__":
    console = Console()
    print_header(console)
    main()
