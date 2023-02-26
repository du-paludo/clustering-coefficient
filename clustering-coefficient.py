import networkx as nx
import math
import random

def maxdegree(G):
    k = 0
    for i in G:
        if G.degree[i] > k:
            k = G.degree[i]
    return k

def LocalClusteringEstimation(G, e, delta, p):
    T = [0] * G.number_of_nodes()
    l = [0] * G.number_of_nodes()
    m = G.number_of_edges()
    c = 1
    r = math.ceil((c/(e*e*p)) * ((math.floor(math.log(maxdegree(G)-1, 2)) + 1) * math.log(1/p) + math.log(1/delta)))
    for i in range(r):
        (a, b) = random.choice(list(G.edges))
        for v in G.neighbors(a):
            if v in G.neighbors(b):
                T[v] += m/r
    for v in G.nodes:
        l[v] = 2*T[v] / (G.degree(v)*(G.degree(v)-1))
    return l

G = nx.complete_graph(5)
l = LocalClusteringEstimation(G, 1, 0.1, 0.5)
print(l)