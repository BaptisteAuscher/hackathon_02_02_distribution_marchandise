import osmnx


import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

depot = (0, {"nom": "SOGARIS", "pos": (2.36815, 48.74991)})
Destinataires = [
    (1, {"nom": "Mines Paris", "pos": (2.33969, 48.84563)}),
    (2, {"nom": "Observatoire de Paris", "pos": (2.33650, 48.83730)}),
    (3, {"nom": "Marie du 14e", "pos": (2.32698, 48.83320)}),
    (4, {"nom": "Gare Montparnasse TGV", "pos": (2.32159, 48.84117)}),
    (5, {"nom": "Mairie du 15e", "pos": (2.29991, 48.84126)}),
]

tps_plus_rapide = [0, 5, 3, 2, 4, 1, 0]

#centre des livraisons
liste_coord = [el[1]["pos"] for el in Destinataires]
def centre_points(liste):
    centre = [0,0]
    for el in liste:
        centre = [centre[0] + el[0], centre[1] + el[1]]
    centre[0] = centre[0] /len(liste)
    centre[1] = centre[1] /len(liste)
    return centre

centre_masse_dest = centre_points(liste_coord)

centre_graphe = centre_points([centre_masse_dest, depot[1]["pos"]])

def inverser_coord(coord):
    return coord[1], coord[0]

print(centre_graphe)


G1_depot = osmnx.graph_from_point(inverser_coord(centre_graphe), dist=8000, network_type="drive")



def trajet(depart, arrivee):
    depart_node = osmnx.distance.nearest_nodes(G1_depot, X=depart[0], Y=depart[1])
    arrivee_node = osmnx.distance.nearest_nodes(G1_depot, X=arrivee[0], Y=arrivee[1])
    route = osmnx.shortest_path(G1_depot, depart_node, arrivee_node)
    fig, ax = osmnx.plot_graph_route(G1_depot, route, node_size=0) 
    print(osmnx.utils_graph.route_to_gdf(G1_depot, route))

trajet(depot[1]["pos"], Destinataires[4][1]["pos"])

"""
G2 = osmnx.graph_from_address(
address="60 boulevard Saint-Michel, Paris, France", dist=2000,
dist_type="network",
network_type="drive",
)
fig, ax = osmnx.plot_graph(osmnx.project_graph(G2))
origine = osmnx.distance.nearest_nodes(G2, X=2.34017, Y=48.84635)
destination = osmnx.distance.nearest_nodes(G2, X=2.35036, Y=48.8413)
route = osmnx.shortest_path(G2, origine, destination)
print(route)
fig, ax = osmnx.plot_graph_route(G2, route, node_size=0) 
print(osmnx.utils_graph.route_to_gdf(G2, route))
"""
""" G = nx.Graph()


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
print(chemin, distance_tot) """