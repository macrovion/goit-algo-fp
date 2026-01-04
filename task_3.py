import heapq

def dijkstra(graph, start_node):
    # ініціалізація відстаней, встановлюємо відстань до всіх вершин як нескінченність
    distances = {node: float('infinity') for node in graph}
    distances[start_node] = 0
    
    # словник для відновлення шляху 
    predecessors = {node: None for node in graph}
    
    # створення бінарної купи 
    priority_queue = [(0, start_node)]
    
    while priority_queue:
        # витягуємо вершину з найменшою відомою відстанню
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # якщо ми витягли застарілий запис, пропускаємо
        if current_distance > distances[current_node]:
            continue
        
        # перевірка сусідів
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # якщо знайдено коротший шлях до сусіда
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                # додаємо оновлений шлях у купу
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances, predecessors

# допоміжна функція для відновлення шляху
def get_shortest_path(predecessors, target_node):
    path = []
    current = target_node
    while current is not None:
        path.append(current)
        current = predecessors.get(current)
    return path[::-1] # розвертаємо список

# тести

# граф: {Вершина: {Сусід: Вага, ...}}
my_graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 5, 'D': 10},
    'C': {'E': 3},
    'D': {'F': 11},
    'E': {'D': 4},
    'F': {}
}

start_vertex = 'A'
dists, preds = dijkstra(my_graph, start_vertex)

print(f"Найкоротші відстані від '{start_vertex}':")
for vertex, distance in dists.items():
    print(f"До {vertex}: {distance}")

print("\nПриклад відновлення шляху до вершини 'D':")
path_to_D = get_shortest_path(preds, 'D')
print(f"Шлях: {' -> '.join(path_to_D)}")
