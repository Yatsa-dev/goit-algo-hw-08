from avl_tree import AVLNode, insert_node, delete_node
import random


def get_sum(node: AVLNode | None) -> int:
    if node is None:
        return 0
    return node.key + get_sum(node.left) + get_sum(node.right)


if __name__ == "__main__":
    root: AVLNode | None = None
    # keys = [random.randint(1, 100) for _ in range(10)]
    keys = random.sample(range(1, 101), 10)

    for key in keys:
        root = insert_node(root, key)

    print("Tree:")
    print(root)

    control_sum = sum(set(keys))
    total_sum = get_sum(root)
    assert total_sum == control_sum 

    print(f"Total sum of keys in the tree: {total_sum}")

