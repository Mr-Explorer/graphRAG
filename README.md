GraphRAG Learning Path Demo (With & Without Weights)

This project demonstrates a real-time, simplified implementation of GraphRAG concepts using graph-based relationships between technologies.

It visualizes how different concepts are connected and helps identify the optimal learning path using:
1. Weighted Graph (priority-based learning)
2. Unweighted Graph (basic connections)
3. Interactive visualization using PyVis

📌 Problem Statement
In today's fast-paced tech world, developers often struggle with:
1. What to learn next?
2. Which topics are more important?
3. How concepts are connected?
This project solves that using a Graph-based approach (GraphRAG concept).

🧠 Concept Used
1. Graph Theory
2. Shortest Path Algorithm
3. Knowledge Graph Representation
4. GraphRAG (Graph-based Retrieval Augmented Generation idea)

🛠️ Tech Stack
1. Python
2. NetworkX
3. PyVis
4. HTML (for visualization)

📂 Project Structure
graphRAG/
│
├── graphRAG.py                # Basic graph (without weights)
├── graphRAG_weight.py        # Weighted graph implementation
├── unique_dev_map.html       # Output visualization
├── my_node_link.html         # Graph visualization
└── .gitignore
🔗 Sample Graph Relationships
edges = [
    ("Python", "Agentic AI", 10),
    ("Python", "FastAPI", 7),
    ("Agentic AI", "GraphRAG", 9),
    ("GraphRAG", "VectorDB", 5),
    ("Agentic AI", "Ollama", 8),
    ("Ollama", "Small Models", 10),
    ("Python", "Unique Developer", 10),
    ("Unique Developer", "Cloud Deployment", 8)
]

🔍 Key Feature: Smart Learning Path
The system calculates the best path using weighted shortest path:

nx.shortest_path(G, source=start_node, target=end_node, weight='weight')

🧾 Example Output:
Recommended Path: Python -> Agentic AI -> GraphRAG

🎯 Highlight
1. "Unique Developer" node is specially highlighted
2. Interactive dark-themed graph visualization
3. Weight-based decision making

📸 Visualization
Run the script and open:
unique_dev_map.html
to see the interactive graph.

▶️ How to Run
pip install networkx pyvis
python graphRAG_weight.py

💡 Use Cases
1. Learning path recommendation
2. Skill roadmap generation
3. Knowledge graph exploration
4. AI-based career guidance systems

🔥 Future Improvements
1. Integrate LLM for dynamic path generation
2. Add real-time data sources
3. Convert into web app (FastAPI + React)

🤝 Contribution
Feel free to fork, improve, and contribute!

⭐ If you like this project
Give it a ⭐ on GitHub and connect with me on LinkedIn!
