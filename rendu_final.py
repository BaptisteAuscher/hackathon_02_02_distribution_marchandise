#Calcul de l'ordre le plus court

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import requests
import json

import osmnx

#Récupérer l'ordre le plus court

G = nx.Graph()


Lieux = [
    (0, {"nom": "SOGARIS", "pos": (2.36815, 48.74991)}),
    (1, {"nom": "Mines Paris", "pos": (2.33969, 48.84563)}),
    (2, {"nom": "Observatoire de Paris", "pos": (2.33650, 48.83730)}),
    (3, {"nom": "Marie du 14e", "pos": (2.32698, 48.83320)}),
    (4, {"nom": "Gare Montparnasse TGV", "pos": (2.32159, 48.84117)}),
    (5, {"nom": "Mairie du 15e", "pos": (2.29991, 48.84126)}),
]
G.add_nodes_from(Lieux)

F = [elmt[1]["pos"] for elmt in Lieux]
L = []
T = {}
for l in range(len(G)):
    for k in range(l, len(G)):
        if l != k:
            try:
                r = requests.get(
                    f"https://wxs.ign.fr/essentiels/geoportail/itineraire/rest/1.0.0/route?resource=bdtopo-osrm&start={F[l][0]},{F[l][1]}&end={F[k][0]},{F[k][1]}"
                ).json()
                # print(f"Distance : {r['distance']} mètres, Durée :{r['duration']} minutes")
            except Exception:
                print(f"erreur requete !")
                print(k, l)
            L.append((l, k, r["distance"]))
            T[(l, k)] = r["duration"]


# print(G.)

G.add_weighted_edges_from(L)
for i in range(len(G.nodes) - 1):
    for j in range(i + 1, len(G.nodes)):
        G[i][j]["durée"] = T[(i, j)]



tsp = nx.approximation.traveling_salesman_problem

chemin_tps_min = tsp(G, weight="durée", nodes=None, cycle=True, method=None)
tps_tot = 0
for i in range(len(chemin_tps_min) - 1):
    edge_data = G.get_edge_data(chemin_tps_min[i], chemin_tps_min[i + 1])
    tps_tot += edge_data["durée"]

print(chemin_tps_min)
chemin_geo_tps_min = [Lieux[element][1]["nom"] for element in chemin_tps_min]

#calcul des trajets 

depot = (0, {"nom": "SOGARIS", "pos": (2.36815, 48.74991)})
Destinataires = [
    (1, {"nom": "Mines Paris", "pos": (2.33969, 48.84563)}),
    (2, {"nom": "Observatoire de Paris", "pos": (2.33650, 48.83730)}),
    (3, {"nom": "Marie du 14e", "pos": (2.32698, 48.83320)}),
    (4, {"nom": "Gare Montparnasse TGV", "pos": (2.32159, 48.84117)}),
    (5, {"nom": "Mairie du 15e", "pos": (2.29991, 48.84126)}),
]


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




