def file_reader(file_name):
    f = open(file_name)
    matrix = []
    lines = f.readlines()
    n = int(lines[0])
    for i in range(1, len(lines)):
        line = lines[i]
        ls = line.split(None)
        for i in range(len(ls)):
            ls[i] = int(ls[i])
        matrix.append(ls)
    f.close()
    return n, matrix


def total_distances(d):
    sums = []
    for row in d:
        sums.append(sum(row))
    return sums


def nj_matrix(d):
    n = len(d)
    total = total_distances(d)
    d_prime = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(0.00)
        d_prime.append(row)

    for i in range(n):
        for j in range(n):
            if i != j:
                d_prime[i][j] = float((n-2) * d[i][j] - total[i] - total[j])

    return d_prime


def get_min_ij(d_prime):
    min_i = None
    min_j = None
    min_val = float('inf')
    for i in range(len(d_prime)):
        for j in range(len(d_prime)):
            if i != j and d_prime[i][j] < min_val:
                min_val = d_prime[i][j]
                min_i = i
                min_j = j
    return min_i, min_j


def remove_row_col(d, k):
    for i in range(len(d)):
        del d[i][k]
    del d[k]


def add_row_col(d):
    for i in range(len(d)):
        d[i].append(0.00)
    row = []
    for i in range(len(d)+1):
        row.append(0.00)
    d.append(row)


def neighbor_joining(d, n, new_node, names):
    if n == 2:
        # tree = [(names[0], names[1], round(d[0][1], 3))]
        tree = [(names[0], names[1], d[0][1]), (names[1], names[0], d[0][1])]
        return tree

    total = total_distances(d)
    d_prime = nj_matrix(d)
    i, j = get_min_ij(d_prime)
    delta = (total[i] - total[j]) / (n - 2)
    limb_length_i = (d[i][j] + delta) / 2
    limb_length_j = (d[i][j] - delta) / 2

    m = n
    add_row_col(d)
    for k in range(n):
        d[k][m] = (d[k][i] + d[k][j] - d[i][j]) / 2
        d[m][k] = (d[k][i] + d[k][j] - d[i][j]) / 2
    remove_row_col(d, max(i, j))
    remove_row_col(d, min(i, j))
    name_i = names[i]
    name_j = names[j]
    del names[max(i, j)]
    del names[min(i, j)]
    names.append(new_node)

    tree = neighbor_joining(d, n-1, new_node+1, names)
    # tree.extend([(new_node, name_i, round(limb_length_i, 3)),
    #              (name_i, new_node, round(limb_length_i, 3)),
    #              (new_node, name_j, round(limb_length_j, 3)),
    #              (name_j, new_node, round(limb_length_j, 3))])
    tree.extend([(new_node, name_i, limb_length_i),
                 (name_i, new_node, limb_length_i),
                 (new_node, name_j, limb_length_j),
                 (name_j, new_node, limb_length_j)])
    return tree


def output(tree):
    tree.sort(key = lambda x: x[0])
    out = []
    # for i in tree:
    #     s = str(i[0]) + '->' + str(i[1]) + ':' + str(i[2])
    #     out.append(s)
    for i in tree:
        print("%d->%d:%f" % (i[0], i[1], i[2]))


if __name__ == '__main__':
    d = [[0, 23, 27, 20],
         [23, 0, 30, 28],
         [27, 30, 0, 30],
         [20, 28, 30, 0]]

    name = []
    for i in range(32):
        name.append(i)

    n, matrix = file_reader('input.txt')
    output(neighbor_joining(matrix, n, n, name))
