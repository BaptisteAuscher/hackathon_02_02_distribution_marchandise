import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.Graph()


Dépôt = [(0, {"nom": "SOGARIS", "pos": (2.36815, 48.74991)})]
Destinataires = [
    (1, {"nom": "Mines Paris", "pos": (2.33969, 48.84563)}),
    (2, {"nom": "Observatoire de Paris", "pos": (2.33650, 48.83730)}),
    (3, {"nom": "Marie du 14e", "pos": (2.32698, 48.83320)}),
    (4, {"nom": "Gare Montparnasse TGV", "pos": (2.32159, 48.84117)}),
    (5, {"nom": "Mairie du 15e", "pos": (2.29991, 48.84126)}),
]
G.add_nodes_from(Dépôt)
print(G)
G.add_nodes_from(Destinataires)
print(G)


def distance_cartesienne(x1, x2, y1, y2):
    return np.sqrt(np.square(x1 - x2) + np.square(y1 - y2))


# print(G.)
xsource, ysource = G.nodes[0]["pos"]

for i in range(len(G.nodes) - 1):
    xi, yi = G.nodes[i]["pos"]
    for j in range(i + 1, len(G.nodes)):
        x, y = G.nodes[j]["pos"]
        G.add_edge(i, j, weight=distance_cartesienne(xi, x, yi, x))


G.add_nodes_from(Dépôt)
print(G)
G.add_nodes_from(Destinataires)
print(G)

pos = nx.spring_layout(G, weight="weight")

subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight="bold")
subax2 = plt.subplot(122)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight="bold")
plt.show()

tsp = nx.approximation.traveling_salesman_problem
chemin = tsp(G, weight="weight", nodes=None, cycle=True, method=None)
distance_tot = 0
for i in range(len(chemin) - 1):
    edge_data = G.get_edge_data(chemin[i], chemin[i + 1])
    print(edge_data)
    distance_tot += edge_data["weight"]
print(chemin, distance_tot)
