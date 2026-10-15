# TP-projet-Mario Kart 

from matplotlib import pyplot as plt
import networkx as nx


def display_nx_graph(G):
    """Display a NetworkX graph using matplotlib.

    Parameters:
    -----------
    G : networkx.Graph
        The graph to display.
    """
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(3, 3))
    nx.draw(G, pos, with_labels=True, node_size=700,
            node_color='lightblue', font_size=10)
    plt.show()


def build_graph_from_dict(d):
    """Build a NetworkX graph from a dictionary representation.
    The dictionary should have the format {node: [neighbors]}.

    Parameters:
    -----------
    d : dict
        The dictionary representing the graph.

    Returns:
    --------
    G : networkx.Graph
        The constructed NetworkX graph.
    """
    G = nx.DiGraph()
    for node, neighbors in d.items():
        G.add_node(node)
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    return G


def display_graph_from_dict(d):
    """Display a graph from a dictionary representation.
    The dictionary should have the format {node: [neighbors]}.

    Parameters:
    -----------
    d : dict
        The dictionary representing the graph.
    """
    G = build_graph_from_dict(d)
    display_nx_graph(G)


def tree_width(G, root, parents):
    """Calculate the width of a tree rooted at a given node.

    Parameters:
    -----------
    G : networkx.Graph
        The graph representing the tree.
    root : node
        The root node of the tree.
    parents : list
        List of parent nodes to avoid cycles.

    Returns:
    --------
    int
        The width of the tree.
    """
    # Fonction rÃ©cursive pour calculer la largeur d'un arbre
    neighbors = list(G.neighbors(root))
    children = [c for c in neighbors if c not in parents]
    width = 0
    for c in children:
        width += tree_width(G, c, parents+[root])
    return max(1, width)


def tree_layout(G, root):
    """Generate positions for nodes in a tree layout.

    Parameters:
    -----------
    G : networkx.Graph
        The graph representing the tree.
    root : node
        The root node of the tree.

    Returns:
    --------
    pos : dict
        A dictionary mapping each node to its (x, y) position.
    """
    pos = {}
    queue = [(root, 0, 0)]

    while queue:
        node, depth, offset = queue.pop(0)
        width = tree_width(G, node, list(pos.keys()))
        pos[node] = (offset + width/2, -depth)

        neighbors = list(G.neighbors(node))
        children = [c for c in neighbors if c not in pos.keys()]
        new_offset = 0
        if children:
            for i, child in enumerate(children):
                if child not in pos.keys():
                    queue.append(
                        (child, depth + 1, offset + new_offset))
                    child_width = tree_width(G, child, list(pos.keys()))
                    new_offset += child_width

    return pos


def build_expression_tree_from_dict(d):
    """Build a NetworkX graph from a dictionary representation.
    The dictionary should have the format {node: (operation, [neighbors])}.

    Parameters:
    -----------
    d : dict
        The dictionary representing the graph.

    Returns:
    --------
    G : networkx.Graph
        The constructed NetworkX graph.
    """
    G = nx.DiGraph()
    for node, (operation, neighbors) in d.items():
        G.add_node(node, label=operation)
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    return G


def display_expression_tree_from_dict(d):
    """Display an expression tree from a dictionary representation.
    The dictionary should have the format {node: [children]}.

    Parameters:
    -----------
    d : dict
        The dictionary representing the expression tree.
    """

    # Convert dictionary to NetworkX graph
    G = build_expression_tree_from_dict(d)

    # Node positions
    pos = tree_layout(G, 0)

    # Node labels
    labels = {n: G.nodes[i]['label'] for i, n in enumerate(G.nodes)}

    # Display
    nx.draw(G, pos, with_labels=False, node_size=500,
            node_color='skyblue')  # Draw nodes
    nx.draw_networkx_labels(
        G, pos, labels=labels, font_size=12, font_color='black')

    plt.show()

