import math
import random

class MCTSNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.reward = 0

    def is_fully_expanded(self):
        return len(self.children) > 0

    def best_child(self, c_param=1.4):
        choices_weights = [
            (child.reward / child.visits) + c_param * math.sqrt((2 * math.log(self.visits) / child.visits))
            for child in self.children
        ]
        return self.children[choices_weights.index(max(choices_weights))]

def mcts(root, iterations=100):
    for _ in range(iterations):
        node = tree_policy(root)
        reward = default_policy(node.state)
        backup(node, reward)
    return root.best_child(c_param=0)

def tree_policy(node):
    while not terminal(node.state):
        if not node.is_fully_expanded():
            return expand(node)
        else:
            node = node.best_child()
    return node

def expand(node):
    new_state = node.state  # placeholder
    child_node = MCTSNode(new_state, node)
    node.children.append(child_node)
    return child_node

def default_policy(state):
    return random.random()

def backup(node, reward):
    while node:
        node.visits += 1
        node.reward += reward
        node = node.parent

def terminal(state):
    return False

if __name__ == '__main__':
    root = MCTSNode(state="initial_state")
    best_node = mcts(root, iterations=100)
    print("Best move/state:", best_node.state)
