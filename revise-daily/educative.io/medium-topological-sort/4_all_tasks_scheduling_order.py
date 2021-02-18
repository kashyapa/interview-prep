# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to print all possible ordering of tasks meeting all prerequisites.
#
# Example 1:
#
# Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
# Output: [0, 1, 2]
# Explanation: There is only possible ordering of the tasks.

from collections import deque


def print_orders(tasks, prerequisites):
    graph = {i: [] for i in range(tasks)}
    in_degree = {i: 0 for i in range(tasks)}

    for parent, child in prerequisites:
        graph[parent].append(child)
        in_degree[child] += 1

    sources = []

    for k, v in in_degree.items():
        if v == 0:
            sources.append(k)

    print_all_sources(graph, sources, [], in_degree)


def print_all_sources(graph, source_list, sorted_order, in_degree):
    if source_list:
        for vertex in source_list:
            sources_for_next_call = deque(source_list)
            sorted_order.append(vertex)
            sources_for_next_call.remove(vertex)

            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources_for_next_call.append(child)

            print_all_sources(graph, sources_for_next_call, sorted_order, in_degree)

            sorted_order.remove(vertex)
            for child in graph[vertex]:
                in_degree[child] += 1

    if len(sorted_order) == len(graph):
        print(sorted_order)


def main():
    print("Task Orders: ")
    print_orders(3, [[0, 1], [1, 2]])

    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


if __name__ == "__main__":
    main()
