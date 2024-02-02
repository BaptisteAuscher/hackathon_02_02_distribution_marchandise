import networkx as nx
import matplotlib.pyplot as plt
import random

# Création d'un graphe vide
G = nx.Graph()

# Ajout de 10 nœuds
nodes = range(1, 11)
G.add_nodes_from(nodes)

# Ajout d'arêtes pour créer une toile d'araignée
for node in nodes:
    num_edges = random.randint(2, 5)  # Nombre aléatoire d'arêtes par nœud
    for _ in range(num_edges):
        target_node = random.choice(nodes)
        # Assurez-vous que l'arête n'existe pas déjà
        while G.has_edge(node, target_node) or node == target_node:
            target_node = random.choice(nodes)
        G.add_edge(node, target_node)

# Dessin du graphe
pos = nx.spring_layout(G)
nx.draw(
    G,
    pos,
    with_labels=True,
    font_weight="bold",
    node_size=700,
    node_color="skyblue",
    font_color="black",
    font_size=8,
    edge_color="gray",
)

# Affichage du graphe
plt.show()
