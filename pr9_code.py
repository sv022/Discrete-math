import numpy as np
import networkx as nx
import random
from networkx.algorithms import tournament

# функция для генерации неопределенного графа
def undirected_graph(lsNumber):
    # Неориентированный граф
    G1 = nx.Graph()
    G1.add_edges_from(lsNumber)
    vertices = list(G1.nodes())
    edges = list(G1.edges())

    # Получение степеней вершин
    degrees = np.zeros(len(vertices))
    for i, v in enumerate(vertices):
        degrees[i] = G1.degree(v)

    # Получение матрицы смежности
    adj_matrix = nx.adjacency_matrix(G1).todense()

    # Получение матрицы инцидентности
    inc_matrix = nx.incidence_matrix(G1, oriented=True).todense()

    print("Неориентированный граф")
    print("Список вершин:", vertices)
    print("Список ребер:", edges)
    print("Степени вершин:", degrees)
    print("Матрица смежности:\n")
    for x in adj_matrix: print(*x)
    print("Матрица инцидентности:")
    for x in inc_matrix: print(*x)

    print("")

# Функция для генерации определенного графа
def defind_graph(lsNumber):
    # Ориентированный граф
    G2 = nx.DiGraph()
    G2.add_edges_from(lsNumber)
    vertices = list(G2.nodes())
    edges = list(G2.edges())

    # Получение степеней вершин
    in_degrees = np.zeros(len(vertices))
    out_degrees = np.zeros(len(vertices))
    for i, v in enumerate(vertices):
        in_degrees[i] = G2.in_degree(v)
        out_degrees[i] = G2.out_degree(v)

    # Получение списка ребер
    edges = [(e[0], e[1]) for e in edges]

    # Получение матрицы смежности
    adj_matrix = nx.adjacency_matrix(G2).todense()

    # Получение матрицы инцидентности
    inc_matrix = nx.incidence_matrix(G2, oriented=True).todense()

    print("Список вершин:", *vertices)
    print("Список ребер:", *edges)
    print("Ориентированный граф")
    print("Степени захода вершин:", *in_degrees)
    print("Степени исхода вершин:", *out_degrees)
    print("Матрица смежности:")
    for x in adj_matrix: print(*x)
    print("Матрица инцидентности:")
    for x in inc_matrix: print(*x)
    print("")
    if nx.is_eulerian(G2):
        print("Есть эйлеров цикл")
    else:
        print("Нету Эйлерова цикла")

    if nx.has_eulerian_path(G2):
        print("Есть Эйлеров путь")
    else:
        print("Нету Эйлерова пути")
    print(f"Гамильнов путь: {tournament.hamiltonian_path(G2)}\n")

def genList():
    n = random.randint(1, 10)
    ls = []
    for i in range(n):
        tup = ()
        ls.append(tup + (random.randint(0, 10),) + (random.randint(0, 10),))
    return list(set(ls))


f = open("input.txt", "r").readline().replace("\n", "").split(" ") # здесь указывать файл с матрицей
# можно ввести руками
f = [int(x) for x in f]
ls = []
for i in range(len(f) - 1):
    ls.append((f[i],) + (f[i + 1],))

defind_graph(genList())
undirected_graph(genList())

undirected_graph(ls)

G2 = nx.DiGraph()
G2.add_edges_from(genList())

print(f"Количество циклов в графе {nx.number_of_selfloops(G2)}")