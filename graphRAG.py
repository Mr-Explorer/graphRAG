import networkx as nx
from pyvis.network import Network

G = nx.DiGraph()
edges = [
    ("Python", "Agentic AI", "Powers"),
    ("Agentic AI", "GraphRAG", "Uses"),
    ("GraphRAG", "Knowledge", "Organizes"),
    ("Small Models", "Agentic AI", "Efficient Brain"),
    ("Docker", "AI App", "Packages")
]

for src, dst, label in edges:
    G.add_edge(src, dst, title=label, label=label)

net = Network(notebook=True, cdn_resources='remote', directed=True, bgcolor="#222222", font_color="white")
net.from_nx(G)

net.show("my_node_link.html")