import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import requests
import json

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
"""
chemin_dist_min = tsp(G, weight="weight", nodes=None, cycle=True, method=None)
distance_tot = 0
for i in range(len(chemin_dist_min) - 1):
    edge_data = G.get_edge_data(chemin_dist_min[i], chemin_dist_min[i + 1])
    distance_tot += edge_data["weight"]

chemin_geo_dist_min = [Lieux[element][1]["nom"] for element in chemin_dist_min]
print(f"Le chemin le plus cpurt est {chemin_geo_dist_min} et fait {distance_tot}mètres")
"""

chemin_tps_min = tsp(G, weight="durée", nodes=None, cycle=True, method=None)
tps_tot = 0
for i in range(len(chemin_tps_min) - 1):
    edge_data = G.get_edge_data(chemin_tps_min[i], chemin_tps_min[i + 1])
    tps_tot += edge_data["durée"]

print(chemin_tps_min)
chemin_geo_tps_min = [Lieux[element][1]["nom"] for element in chemin_tps_min]
print(f"Le chemin le plus rapide est {chemin_geo_tps_min} et fait {tps_tot} minutes")


