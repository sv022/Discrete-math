#Задача 1. Рассмотрим модель случайных графов на n вершинах, в котором каждое из возможных ребер проводится независимо от всех остальных с с одной и той же вероятностью. Используя библиотеку NetworkX, сгегенрируйте граф на 1000 вершинах при р=0,003. Оцените разницу между количеством ребер и их ожидаемым количеством. Постройте график распределения вершин в log-log координатах. Оцените степенную зависимость закона распределения вершин. 

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Создание случайного графа
G = nx.gnp_random_graph(1000, 0.003)

# Рассчет количества ребер и ожидаемого количества ребер
m = G.number_of_edges()
n = G.number_of_nodes()
expected_m = n * (n-1) / 2 * 0.003

# Вывод результатов
print("Количество ребер: ", m)
print("Ожидаемое количество ребер: ", expected_m)
print("Разница: ", m - expected_m)

# Построение гистограммы распределения степеней вершин
degrees = [G.degree(n) for n in G.nodes()]
plt.hist(degrees, bins=np.logspace(np.log10(1), np.log10(max(degrees)), 50), density=True, log=True)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Степень вершины')
plt.ylabel('Вероятность')
plt.show()
