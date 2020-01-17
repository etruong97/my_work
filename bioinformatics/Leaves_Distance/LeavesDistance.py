def file_reader(file_name):
    graph = {}
    f = open(file_name)
    for line in f:
        split_1 = line.split('->')
        split_2 = split_1[1].split(':')
        key = int(split_1[0])
        val_node = int(split_2[0])
        val_dist = int(split_2[1].strip())
        if key in graph:
            graph[key].append((val_node, val_dist))
        else:
            graph.update({key: [(val_node, val_dist)]})
    return graph


def dfs_dist(graph, p, q, d, row, distances, state):
    state[q] = 1
    if p == -1:
        distances[q] = 0
    else:
        distances[q] = distances[p] + d
    children = graph[q]
    if len(children) == 1:
        row[q] = distances[q]
    for neighbor in children:
        if state[neighbor[0]] == 0:
            dfs_dist(graph, q, neighbor[0], neighbor[1], row, distances, state)

    return row


def build_matrix(g, n):
    matrix = []
    for leaf in range(n):
        n_leaves = []
        n_vertices = []
        for i in range(n):
            n_leaves.append(0)
        for i in range(len(g)):
            n_vertices.append(0)
        row = dfs_dist(g, -1, leaf, -1, n_leaves, n_vertices, n_vertices)
        row[leaf] = 0
        matrix.append(row)
    return matrix


def to_string(m):
    s = ""
    for row in m:
        for i in range(len(row)):
            if i == len(row)-1:
                s = s + str(row[i]) + '\n'
            else:
                s = s + str(row[i]) + ' '
    return s


if __name__ == '__main__':
    row = [0, 0, 0, 0]
    state = [0, 0, 0, 0, 0, 0]

    g = file_reader('input.txt')
    m = build_matrix(g, 32)
    print(to_string(m))
