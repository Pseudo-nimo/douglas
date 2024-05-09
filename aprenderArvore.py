class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order_traversal(node):
    if node is not None:
        print(node.data)  # Visita o nó
        pre_order_traversal(node.right)
        pre_order_traversal(node.left)  # Percorre a subárvore esquerda
          # Percorre a subárvore direita

# Exemplo de uso
# Criando a árvore
root = Node([1,1])
root.left = Node([1,3])
root.right = Node([3,1])
root.right.right = Node([4,2])
root.right.left = Node([4,1])
root.left.left = Node([1,4])
root.left.right = Node([2,4])

# Realizando o percurso em pré-ordem
print("Percurso em pré-ordem:")
pre_order_traversal(root)
