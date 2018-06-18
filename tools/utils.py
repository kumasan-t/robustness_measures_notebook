import networkx as nx


def important_nodes(graph):
    """
    Returns the most important nodes
    according to betweenness centrality result
    :param graph: a networkx graph
    :return: a subgraph of the most important nodes and the betweenness centrality values
    """
    betweenness_centrality = nx.betweenness_centrality(graph)
    betweenness_sorted = sorted(betweenness_centrality.items(), key=lambda x: x[1])
    betweenness_values = [x[1] for x in betweenness_sorted]
    betweenness_mean = sum(betweenness_values) / len(betweenness_values)
    subgraph = graph.copy()
    threshold = 3 * betweenness_mean
    for v, k in betweenness_sorted:
        if k < threshold:
            subgraph.remove_node(v)
    return subgraph, betweenness_values


def clean_isolated_nodes(graph):
    """
    Removes nodes without edges from the graph
    :param graph: a networkx graph
    :return:
    """
    graph.remove_nodes_from(list(nx.isolates(graph)))


def fix_connectivity(graph):
    """
    Select the largest connected subgraph among the set of connected subgraph.
    :param graph: a networkx graph
    :return: the largest subgraph
    """
    connected = nx.is_connected(graph)
    if not connected:
        # Cut out the largest set of connected components and return it as a subgraph
        return max(nx.connected_component_subgraphs(graph), key=len)


def parse_graph_from_json(json_graph):
    """
    Converts the Lightning Network JSON representation to a networkx representation.
    :param json_graph: a JSON file
    :return: a networkx undirected graph
    """
    graph = nx.Graph()

    # Add each node in the graph
    for node in json_graph['nodes']:
        graph.add_node(node['pub_key'], last_update=node['last_update'])

    # Add each edge in the graph
    # Some edges are missing the node1 and node2 policy fields,
    # so a check is needed before processing it
    for edge in json_graph['edges']:
        if edge['node1_policy'] is not None and \
                edge['node2_policy'] is not None:
            graph.add_edge(edge['node1_pub'],
                           edge['node2_pub'],
                           capacity=int(edge['capacity']),
                           weight=int(edge['capacity']),
                           last_update=int(edge['last_update']),
                           channel_id=edge['channel_id'],
                           chan_point=edge['chan_point'],
                           node1_timelock_delta=int(edge['node1_policy']['time_lock_delta']),
                           node1_min_htlc=int(edge['node1_policy']['min_htlc']),
                           node1_fee_base_msat=int(edge['node1_policy']['fee_base_msat']),
                           node1_fee_rate_milli_msat=int(edge['node1_policy']['fee_rate_milli_msat']),
                           node2_timelock_delta=int(edge['node2_policy']['time_lock_delta']),
                           node2_min_htlc=int(edge['node2_policy']['min_htlc']),
                           node2_fee_base_msat=int(edge['node2_policy']['fee_base_msat']),
                           node2_fee_rate_milli_msat=int(edge['node2_policy']['fee_rate_milli_msat'])
                           )
    return graph
