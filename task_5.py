import uuid
import networkx as nx
import matplotlib.pyplot as plt
import collections
import matplotlib.colors as mcolors

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title="Tree Traversal"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} 

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# функція генерує градієнт з n_steps кольорів від start_hex до end_hex
def generate_color_gradient(n_steps, start_hex, end_hex):
    c1 = mcolors.hex2color(start_hex)
    c2 = mcolors.hex2color(end_hex)
    
    gradient = []
    for i in range(n_steps):
        # лінійна інтерполяція
        t = i / (n_steps - 1) if n_steps > 1 else 0
        r = c1[0] + (c2[0] - c1[0]) * t
        g = c1[1] + (c2[1] - c1[1]) * t
        b = c1[2] + (c2[2] - c1[2]) * t
        gradient.append(mcolors.to_hex((r, g, b)))
    return gradient

# допоміжна функція для підрахунку кількості вузлів
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

# алгоритми обходу в ширину з візуалізацією
def bfs_visualize(root):
    if not root:
        return

    total_nodes = count_nodes(root)
    # генеруємо кольори від темно-синього до світло-блакитного
    colors = generate_color_gradient(total_nodes, "#123456", "#1296F0") 
    
    queue = collections.deque([root])
    visited = set()
    visited.add(root.id)
    
    step = 0
    while queue:
        node = queue.popleft()
        
        # призначаємо колір поточному вузлу
        node.color = colors[step]
        step += 1
        
        if node.left and node.left.id not in visited:
            visited.add(node.left.id)
            queue.append(node.left)
        if node.right and node.right.id not in visited:
            visited.add(node.right.id)
            queue.append(node.right)
            
    draw_tree(root, "BFS: Обхід в ширину (Queue)")

# функція обходу в глибину з візуалізацією
def dfs_visualize(root):
    if not root:
        return

    total_nodes = count_nodes(root)
    # генеруємо кольори від темно-помаранчевого до світло-помаранчевого
    colors = generate_color_gradient(total_nodes, "#8B4500", "#FFD700")
    
    stack = [root]
    visited = set()
    step = 0
    
    while stack:
        node = stack.pop()
        
        if node.id not in visited:
            visited.add(node.id)
            # призначаємо колір
            node.color = colors[step]
            step += 1
            
            # додаємо правий, потім лівий, щоб лівий був оброблений першим 
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
    draw_tree(root, "DFS: Обхід в глибину (Stack)")

# виконання 

# створення дерева для BFS
root_bfs = Node(0)
root_bfs.left = Node(4)
root_bfs.left.left = Node(5)
root_bfs.left.right = Node(10)
root_bfs.right = Node(1)
root_bfs.right.left = Node(3)

# створення дерева для DFS
root_dfs = Node(0)
root_dfs.left = Node(4)
root_dfs.left.left = Node(5)
root_dfs.left.right = Node(10)
root_dfs.right = Node(1)
root_dfs.right.left = Node(3)

# запуск візуалізацій
print("Запуск BFS...")
bfs_visualize(root_bfs)

print("Запуск DFS...")
dfs_visualize(root_dfs)
