"""
Пошук у ширину (Breadth-First Search, BFS)

Алгоритм обходу графа, який досліджує вершини "шар за шаром":
спочатку всі сусіди початкової вершини, потім сусіди сусідів і так далі.
Використовує черга (queue) за принципом FIFO.
"""

from collections import deque


def bfs(graph, start):
    """
    Обхід графа в ширину.

    graph - словник {вершина: [список сусідів]}
    start - вершина, з якої починаємо обхід

    Повертає список вершин у порядку їх відвідування.
    """
    visited = {start}          # множина відвіданих вершин
    queue = deque([start])     # черга вершин для обробки
    order = []                 # порядок відвідування

    while queue:
        vertex = queue.popleft()
        order.append(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def bfs_shortest_path(graph, start, goal):
    """
    Знаходження найкоротшого шляху між start і goal за допомогою BFS.
    Працює коректно тільки для неважених графів (всі ребра "однакові").

    Повертає список вершин шляху або None, якщо шлях не існує.
    """
    if start == goal:
        return [start]

    visited = {start}
    queue = deque([[start]])   # у черзі зберігаємо вже сформовані шляхи

    while queue:
        path = queue.popleft()
        vertex = path[-1]

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                if neighbor == goal:
                    return path + [neighbor]

                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None


def bfs_levels(graph, start):
    """
    Обхід графа в ширину з підрахунком рівнів (відстані від start).

    Повертає словник {вершина: відстань_у_кроках}.
    Корисно, коли треба знати, на якому "рівні" знаходиться кожна вершина.
    """
    distances = {start: 0}
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        for neighbor in graph.get(vertex, []):
            if neighbor not in distances:
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)

    return distances


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    print("Граф:")
    for vertex, neighbors in graph.items():
        print(f"  {vertex}: {neighbors}")

    print("\n1) Звичайний обхід BFS, починаючи з 'A':")
    print("  Порядок відвідування:", bfs(graph, "A"))

    print("\n2) Найкоротший шлях від 'A' до 'F':")
    path = bfs_shortest_path(graph, "A", "F")
    print("  Шлях:", " -> ".join(path))

