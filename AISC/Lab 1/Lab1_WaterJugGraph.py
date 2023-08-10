from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

def bfs_water_jug(jug1_capacity, jug2_capacity, target_amount):

    queue = deque([(0, 0, [])])
    visited = set()
    visited.add((0, 0))
    tree = {}

    while queue:
        jug1_amount, jug2_amount, actions = queue.popleft()
        current_state = (jug1_amount, jug2_amount)

        if jug1_amount == target_amount or jug2_amount == target_amount:
            return tree, actions

        next_states = [
            (jug1_capacity, jug2_amount, actions + ['fill_jug1']),
            (jug1_amount, jug2_capacity, actions + ['fill_jug2']),
            (0, jug2_amount, actions + ['empty_jug1']),
            (jug1_amount, 0, actions + ['empty_jug2']),
            (jug1_amount - min(jug1_amount, jug2_capacity - jug2_amount),
            jug2_amount + min(jug1_amount, jug2_capacity - jug2_amount),
            actions + ['pour_jug1_to_jug2']),
            (jug1_amount + min(jug2_amount, jug1_capacity - jug1_amount),
             jug2_amount - min(jug2_amount, jug1_capacity - jug1_amount),
             actions + ['pour_jug2_to_jug1'])
        ]

        tree[current_state] = {}
        for next_jug1_amount, next_jug2_amount, next_actions in next_states:
            if (next_jug1_amount, next_jug2_amount) not in visited:
                queue.append((next_jug1_amount, next_jug2_amount, next_actions))
                visited.add((next_jug1_amount, next_jug2_amount))
                next_state = (next_jug1_amount, next_jug2_amount)
                tree[current_state][next_state] = next_actions[-1]

    return tree, []

def print_solution_tree(tree, node, level=0):
    if node in tree:
        print("    " * level + f"{node}")
        for child_node, action in tree[node].items():
            print("    " * (level + 1) + f"{action} -> {child_node}")
            print_solution_tree(tree, child_node, level + 2)

def draw_states(tree, path_taken):
    # Draw the graph manually and save as an image
    plt.figure(figsize=(12, 8))
    pos = {}

    for parent, children in tree.items():
        if parent not in pos:
            pos[parent] = (parent[0], parent[1])
        for child in children:
            if child not in pos:
                pos[child] = (child[0], child[1])
            if (parent, child) in path_taken or (child, parent) in path_taken:
                plt.plot([parent[0], child[0]], [parent[1], child[1]], 'r--', lw=2, label='Path Taken')
            else:
                plt.plot([parent[0], child[0]], [parent[1], child[1]], 'b-', lw=1)

    plt.scatter([pos[coord][0] for coord in pos], [pos[coord][1] for coord in pos], s=1000, c='lightblue', edgecolors='black', linewidths=1)
    plt.xlabel('Jug 1 (liters)')
    plt.ylabel('Jug 2 (liters)')
    plt.title("Water Jug Problem Solution Tree")
    plt.legend()
    plt.grid(True)
    plt.axis('equal')

    # Save the graph as an image file
    plt.savefig('water_jug_solution.png')
    plt.show()

def get_user_input():
    try:
        jug1_capacity = int(input("Enter the capacity of Jug 1 (in liters): "))
        jug2_capacity = int(input("Enter the capacity of Jug 2 (in liters): "))
        target_amount = int(input("Enter the target amount (in liters): "))
        return jug1_capacity, jug2_capacity, target_amount
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return get_user_input()


# Example Usage:
print("Water Jug Problem Solver")
jug1_capacity, jug2_capacity, target_amount = get_user_input()

solution_tree, actions = bfs_water_jug(jug1_capacity, jug2_capacity, target_amount)

print("\nSolution Path:")
for i, action in enumerate(actions):
    print(f"{i + 1}. {action}")

print("\nSolution Tree:")
print_solution_tree(solution_tree, (0, 0))