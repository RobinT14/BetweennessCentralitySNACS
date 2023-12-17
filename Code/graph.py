from rich.table import Table
import networkx as nx


def read_file(filename, console, diGraph=True, weighted='Float'):
    try:
        if diGraph:
            if weighted == 'Float':
                G = nx.read_edgelist(filename,
                                     nodetype=int,
                                     create_using=nx.DiGraph,
                                     data=(("weight", float), ))
            else weighted == 'Int':
                G = nx.read_edgelist(filename,
                                     nodetype=int,
                                     create_using=nx.DiGraph,
                                     data=(("weight", int), ))
        else:
            if weighted == 'Float':
                G = nx.read_edgelist(filename,
                                     nodetype=int,
                                     create_using=nx.Graph,
                                     data=(("weight", float), ))
            else weighted == 'Int':
                G = nx.read_edgelist(filename,
                                     nodetype=int,
                                     create_using=nx.Graph,
                                     data=(("weight", int), ))
    except:
        console.print(
            f"[bold red]Error: Input file - '{filename}' not readable by NetworkX.[/bold red]\n")
        exit(1)
    return G


def print_graph_stats(console, input_file, graph):
    table = Table(title="Graph Statistics")
    table.add_column("Graph File", justify="left", style="cyan")
    table.add_column(f"{str(input_file)}", justify="left", style="green")
    table.add_row("Directed", str(nx.is_directed(graph)))
    table.add_row("No Nodes", str(nx.number_of_nodes(graph)))
    table.add_row("No Edges", str(nx.number_of_edges(graph)))
    console.print(table)
    console.print("\n")
