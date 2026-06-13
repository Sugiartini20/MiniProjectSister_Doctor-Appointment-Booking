from datetime import datetime

nodes = [1, 2, 3]

leader = max(nodes)

history = []


def elect_leader():

    global leader

    leader = max(nodes)

    time = datetime.now().strftime("%H:%M:%S")

    history.append(
        f"[{time}] Leader Node {leader}"
    )

    print("\n======================")
    print("Leader elected:", leader)
    print("======================")


def remove_node(node):

    global nodes

    if node in nodes:

        nodes.remove(node)

        print(f"\nNode {node} failed!")

        elect_leader()


elect_leader()

print("\nCurrent nodes:", nodes)

remove_node(3)

print("Current nodes:", nodes)


remove_node(2)

print("Current nodes:", nodes)

print("\n===== Election History =====")

for h in history:

    print(h)