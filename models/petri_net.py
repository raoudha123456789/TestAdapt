import networkx as nx

def detect_deadlock(hold_matrix, wait_matrix):
    """
    Construct wait-for graph and check cycle.
    """
    G = nx.DiGraph()
    n, m = hold_matrix.shape

    for t in range(n):
        for r in range(m):
            if hold_matrix[t][r] == 1:
                # Task t holds resource r
                for w in range(n):
                    if wait_matrix[w][r] == 1:
                        G.add_edge(w, t)

    try:
        cycle = nx.find_cycle(G, orientation="original")
        return True, cycle
    except nx.NetworkXNoCycle:
        return False, []

