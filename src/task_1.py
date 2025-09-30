from avl_tree import AVLNode, insert_node, delete_node
import random


def get_min_key(node: AVLNode | None) -> int | None:
    if node is None:
        return None
    while node.left is not None:
        node = node.left
    return node.key


def get_max_key(node: AVLNode | None) -> int | None:
    if node is None:
        return None
    while node.right is not None:
        node = node.right
    return node.key


if __name__ == "__main__":
    root: AVLNode | None = None
    keys = [random.randint(1, 100) for _ in range(10)]

    for key in keys:
        root = insert_node(root, key)

    print("Tree:")
    print(root)

    min_key = get_min_key(root)
    max_key = get_max_key(root)

    assert min_key == min(keys)
    assert max_key == max(keys)

    print(f"Minimum key in the tree: {min_key}")
    print(f"Maximum key in the tree: {max_key}")
