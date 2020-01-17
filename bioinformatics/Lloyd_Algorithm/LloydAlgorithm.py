import math


def center_of_gravity(data):
    cog_point = []
    for i in range(len(data[0])):
        dimension_i = []
        for j in range(len(data)):
            dimension_i.append(data[j][i])
            x = round(sum(dimension_i)/len(data), 3)
        cog_point.append(x)
    return tuple(cog_point)


def distance(p1, p2):
    ls = []
    for i in range(len(p1)):
        diff = math.pow(p1[i] - p2[i], 2)
        ls.append(diff)
    return math.sqrt(sum(ls))


def min_center(datapoint, centers):
    min_dist = float('inf')
    closest_center = None
    for center in centers:
        if distance(datapoint, center) < min_dist:
            min_dist = distance(datapoint, center)
            closest_center = center
    return closest_center


def centers_to_clusters(centers, data):
    clusters = []
    for i in range(len(centers)):
        clusters.append([])
    for datapoint in data:
        min_center_point = min_center(datapoint, centers)
        i = centers.index(min_center_point)
        clusters[i].append(datapoint)
    return clusters


def clusters_to_centers(clusters):
    centers = []
    for cluster in clusters:
        cog = center_of_gravity(cluster)
        centers.append(cog)
    return centers


def k_means(data, k):
    previous_centers = []
    current_centers = data[:k]
    while previous_centers != current_centers:
        previous_centers = current_centers
        clusters = centers_to_clusters(current_centers, data)
        current_centers = clusters_to_centers(clusters)
    return current_centers


def file_reader(txt):
    with open(txt, "r") as file:
        ls = []
        for line in file:
            line = line.rstrip()
            point = line.split(' ')
            point = [float(i) for i in point]
            ls.append(point)
    return ls


def output(data):
    s = ''
    for i in data:
        for j in range(len(i)):
            if j == len(i)-1:
                s = s + str(i[j]) + '\n'
            else:
                s = s + str(i[j]) + ' '
    return s


if __name__ == '__main__':
    data = [[1.3, 1.1], [1.3, 0.2], [0.6, 2.8], [3.0, 3.2], [1.2, 0.7], [1.4, 1.6], [1.2, 1.0], [1.2, 1.1],
            [0.6, 1.5], [1.8, 2.6], [1.2, 1.3], [1.2, 1.0], [0.0, 1.9]]

    data =file_reader('input3.txt')
    print(output(k_means(data, 6)))