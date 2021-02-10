# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed
# before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, find out if it is possible
# to schedule all the tasks.

# Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
# Output: true
# Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish
# before '2' can be scheduled. A possible sceduling of tasks is: [0, 1, 2]

from collections import deque

def is_scheduling_possible(tasks, prerequisites):

    graph = {i: [] for i in range(tasks)}
    in_degree = {i: 0 for i in range(tasks)}
    sources = deque()

    for parent, child in prerequisites:
        graph[parent].append(child)
        in_degree[child] += 1

    for vertex, deps in in_degree.items():
        if deps == 0:
            sources.append(vertex)

    sorted_vertices = []

    while sources:
        vertex = sources.popleft()
        sorted_vertices.append(vertex)

        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    return len(sorted_vertices) == len(graph)


def main():
    print("Is scheduling possible: " +
          str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

if __name__ == "__main__":
    main()
