import networkx as nx
import matplotlib.pyplot as plt

# Crear grafo dirigido
G = nx.DiGraph()

# -----------------------------
# NODOS ----"nuevamente ---"
# -----------------------------

usuarios = ["Ana", "Luis", "Carlos"]
peliculas = ["Matrix", "Inception", "Interstellar"]
generos = ["SciFi", "Accion", "Drama"]
actores = ["Keanu Reeves", "Leonardo DiCaprio", "Matthew McConaughey"]
directores = ["Wachowski", "Christopher Nolan"]
directores = ["ffffffffff", "gggggggggg ronald"]

# Agregar nodos con tipo
for u in usuarios:
    G.add_node(u, tipo="usuario")

for p in peliculas:
    G.add_node(p, tipo="pelicula")

for g in generos:
    G.add_node(g, tipo="genero")

for a in actores:
    G.add_node(a, tipo="actor")

for d in directores:
    G.add_node(d, tipo="director")

# -----------------------------
# RELACIONES (ARISTAS)
# -----------------------------

# Usuarios ven películas
G.add_edge("Ana", "Matrix", relacion="ve")
G.add_edge("Luis", "Inception", relacion="ve")
G.add_edge("Carlos", "Interstellar", relacion="ve")

# Preferencias
G.add_edge("Ana", "SciFi", relacion="prefiere")
G.add_edge("Luis", "Accion", relacion="prefiere")
G.add_edge("Carlos", "Drama", relacion="prefiere")

# Película pertenece a género
G.add_edge("Matrix", "SciFi", relacion="es_genero")
G.add_edge("Inception", "Accion", relacion="es_genero")
G.add_edge("Interstellar", "Drama", relacion="es_genero")

# Actores participan
G.add_edge("Keanu Reeves", "Matrix", relacion="actua_en")
G.add_edge("Leonardo DiCaprio", "Inception", relacion="actua_en")
G.add_edge("Matthew McConaughey", "Interstellar", relacion="actua_en")

# Directores dirigen
G.add_edge("Wachowski", "Matrix", relacion="dirige")
G.add_edge("Christopher Nolan", "Inception", relacion="dirige")
G.add_edge("Christopher Nolan", "Interstellar", relacion="dirige")

# Recomendaciones inferidas
G.add_edge("Ana", "Interstellar", relacion="recomendado")
G.add_edge("Luis", "Matrix", relacion="recomendado")

# -----------------------------
# COLORES POR TIPO DE NODO
# -----------------------------

color_map = []

for node in G.nodes(data=True):
    tipo = node[1]["tipo"]

    if tipo == "usuario":
        color_map.append("lightblue")
    elif tipo == "pelicula":
        color_map.append("orange")
    elif tipo == "genero":
        color_map.append("lightgreen")
    elif tipo == "actor":
        color_map.append("pink")
    else:
        color_map.append("yellow")

# -----------------------------
# POSICIÓN DEL GRAFO
# -----------------------------

pos = nx.spring_layout(G, k=0.8, seed=42)

# Dibujar nodos
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=color_map,
    node_size=2000,
    font_size=9,
    font_weight="bold",
    arrows=True
)

# Etiquetas de relaciones
edge_labels = nx.get_edge_attributes(G, "relacion")

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_size=8
)

plt.title("Grafo de Conocimiento - Plataforma Streaming", fontsize=14)
plt.show()

print("Nombre: irving Díaz ")
