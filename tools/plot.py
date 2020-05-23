from tools import utils
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
    plt.xticks(np.arange(len(graph_list), step=step), np.arange(len(graph_list), step=step))
    plt.plot([sum([x[1] for x in graph.degree()]) / float(graph.order()) for graph in graph_list], label='Average degree')
    plt.ylabel('Average degree')
    plt.xlabel('Snapshot')
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
    plt.xticks(np.arange(len(graph_list), step=step))
    plt.plot([item.order() for item in graph_list])
    plt.ylabel('Number of nodes')
    plt.xlabel('Snapshot')
    # plt.plot([item.order() for item in graph_list], 'o', color='orange')
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
    plt.xticks(np.arange(len(graph_list), step=step))
    plt.plot([item.number_of_edges() for item in graph_list], label='Number of edges')
    # plt.plot([item.number_of_edges() for item in graph_list], 'o', color='orange')
    plt.ylabel('Number of edges')
    plt.xlabel('Snapshot')
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
    plt.ylabel('Average eccentricity')
    plt.xlabel('Number of snapshots')
    plt.savefig(filename, bbox_inches='tight')
    plt.show()


def plot_degree_distribution(graph, step=1, filename='degree_distribution'):
    """
    Plots the degree distribution.
    :param graph_list: a networkx graph
    :param step: (optional) set thhe steps for x axis ticks
    :param filename: (optional) set the name of the output image
    :return:
    """
    degree_bucket = [0] * graph.order()
    for node in graph.nodes:
        degree_bucket[nx.degree(graph, node)] += 1
    for i, elem in enumerate(degree_bucket):
        plt.scatter(i, elem, color='red', marker='.')
    plt.show()


def plot_overall_capacity(graph_list, step=1, filename='overall_capacity'):
    """
    Plots the capacity of the graph
    :param graph_list: a list of capacities
    :param step: (optional) set thhe steps for x axis ticks
    :param filename: (optional) set the name of the output image
    :return:
    """
    overall_capacity = list()
    for graph in graph_list:
        overall_capacity.append(utils.overall_balance(graph) / 10 ** 8)
    plt.xticks(np.arange(len(graph_list), step=step))
    plt.plot(overall_capacity)
    plt.ylabel('BTC')
    plt.xlabel('Snapshot')
    plt.savefig(filename, bbox_inches='tight')
    plt.show()


def plot_completeness(graph_list, step=1, filename='completeness'):
    """
    Plots the completeness of the graph list
    :param graph_list: a list of networkx graphs
    :param step: (optional) the distance between x axes ticks
    :param filename: (optional) name of the output image
    :return:
    """
    density = [nx.density(graph) for graph in graph_list]
    plt.xticks(np.arange(len(graph_list), step=step))
    plt.plot(density)
    plt.ylabel('Density')
    plt.xlabel('Snapshot')
    plt.savefig(filename, bbox_inches='tight')
    plt.show()
