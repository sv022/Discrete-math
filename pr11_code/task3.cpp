#Задача 3. Найдите число компонено связности в графе из предыдущей задачи. Есть ли в нем гигантская уомпонента? Сколько в ней вершин, каков ее диаметр? Удажите из графа 50 самых больших по степени вершин. Остентся ли в графе гигантская компонента? Сделайте исследование при какой доле вершин гигантская компонента разрушается.  

import networkx as nx
import numpy as np

# Создание графа
G = nx.gnp_random_graph(1000, 0.003)

# Определение количества компонент связности
num_components = nx.number_connected_components(G)
print("Число компонент связности: ", num_components)

# Определение гигантской компоненты и ее характеристик
largest_component = max(nx.connected_components(G), key=len)
print("Число вершин в гигантской компоненте: ", len(largest_component))
print("Диаметр гигантской компоненты: ", nx.diameter(G.subgraph(largest_component)))

# Вывод 50 вершин с наибольшей степенью
degrees = dict(G.degree())
sorted_degrees = sorted(degrees.items(), key=lambda x: x[1], reverse=True)
top_50_nodes = [x[0] for x in sorted_degrees[:50]]
print("50 вершин с наибольшей степенью: ", top_50_nodes)

# Исследование гигантской компоненты при удалении доли вершин
percentages = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for p in percentages:
    nodes_to_remove = int(p * G.number_of_nodes())
    G_copy = G.copy()
    G_copy.remove_nodes_from(np.random.choice(G.nodes(), nodes_to_remove, replace=False))
    largest_component = max(nx.connected_components(G_copy), key=len)
    if len(largest_component) < 0.1 * G.number_of_nodes():
        print("При удалении ", p*100, "% вершин, гигантская компонента разрушилась")
        break
