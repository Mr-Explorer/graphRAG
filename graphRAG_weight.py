# !pip install pyvis

import networkx as nx
from pyvis.network import Network

G = nx.DiGraph()
edges = [
    ("Python", "Agentic AI", 10),
    ("Python", "FastAPI", 7),
    ("Agentic AI", "GraphRAG", 9),
    ("GraphRAG", "VectorDB", 5),
    ("Agentic AI", "Ollama", 8),
    ("Ollama", "Small Models", 10),
    # Let's add YOUR custom goal
    ("Python", "Unique Developer", 10),
    ("Unique Developer", "Cloud Deployment", 8)
]

for src,dst,w in edges:
    G.add_edge(src, dst, weight=w, title=f"{w}", lable=f"{w}")

def find_learning_path(start_node, end_node):
    try:
        path = nx.shortest_path(G, source=start_node, target=end_node, weight='weight')
        return "->".join(path)
    except:
        return "No Connection Found"

net = Network(notebook=True, cdn_resources='remote', bgcolor="#1a1a1a", font_color="white")
net.from_nx(G)

for node in net.nodes:
    if node['id'] == "Unique Developer":
        node['color'] = '#FFD700'
        node['size'] = 40

print(f"Recommended Path: {find_learning_path('Python', 'GraphRAG')}")
net.show("unique_dev_map.html")