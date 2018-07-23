import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def plot_average_degree(graph_list, step=1, filename='average_degree.png'):
    """
    Plots the average degree for each graph in the list.
    :param graph_list: a list of networkx graphs
    :param step: (optional) set the steps for x axis ticks
    :param filename: (optional) set the name of the output image
    :return:
    """
    plt.title('Avg. degree')
    plt.xticks(np.arange(len(graph_list), step=step), np.arange(len(graph_list), step=step))
    plt.plot([sum([x[1] for x in graph.degree()]) / float(graph.order()) for graph in graph_list])
    plt.plot([sum([x[1] for x in graph.degree()]) / float(graph.order()) for graph in graph_list], 'o', color='orange')
    plt.savefig(filename, bbox_inches='tight')
    plt.show()


def plot_number_of_nodes(graph_list, step=1, filename='number_of_nodes.png'):
    """
    Plots the number of nodes for each graph in the list.
    :param graph_list: a list of networkx graphs
    :param step: (optional) set the steps for x axis ticks
    :param filename: (optional) set the name of the output image
    :return:
    """
    plt.title('Nodes variation')
    plt.xticks(np.arange(len(graph_list), step=step), np.arange(len(graph_list), step=step))
    plt.plot([item.order() for item in graph_list])
    plt.plot([item.order() for item in graph_list], 'o', color='orange')
    plt.savefig(filename, bbox_inches='tight')
    plt.show()


def plot_number_of_edges(graph_list, step=1, filename='number_of_edges.png'):
    """
    Plots the number of edges for each graph in the list
    :param graph_list: a list of netwrokx graphs
    :param step: (optional) set the steps for x axis ticks
    :param filename: (optional) set the name of the output image
    :return:
    """
    plt.title('Edges variation')
    plt.xticks(np.arange(len(graph_list), step=step), np.arange(len(graph_list), step=step))
    plt.plot([item.number_of_edges() for item in graph_list])
    plt.plot([item.number_of_edges() for item in graph_list], 'o', color='orange')
    plt.savefig(filename, bbox_inches='tight')
    plt.show()


def plot_average_eccentricity(graph_list, step=1, filename='avg_eccentricity.png'):
    """
    Eccentricity is the maximum distance from v to all other nodes in a given graph.
    Plots the average eccentricity for each graph in the list
    :param graph_list: a list of networkx graphs
    :param step: (optional) set the steps for x axis ticks
    :param filename: (optional) set the name of the output image
    :return:
    """
    avg_eccentricity = list()
    for graph in graph_list:
        eccentricity_values = [x[1] for x in nx.eccentricity(graph).items()]
        avg_eccentricity.append(sum(eccentricity_values) / len(eccentricity_values))
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.xticks(np.arange(len(graph_list), step=step))
    plt.plot(avg_eccentricity)
    plt.plot(avg_eccentricity, 'o', color='orange')
    plt.savefig(filename, bbox_inches='tight')
    plt.show()

