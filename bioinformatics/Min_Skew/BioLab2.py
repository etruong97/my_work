def min_skew(genome):
    count = 0
    ls = [0]

    for nuc in genome:
        if nuc == 'G':
            count += 1
        if nuc == 'C':
            count -= 1
        ls.append(count)

    min_value = find_min(ls)
    indices = []

    for x in range(len(ls)):
        if ls[x] == min_value:
            indices.append(x)

    return indices


def find_min(ls):
    curr_min = -1
    for x in ls:
        if x < curr_min:
            curr_min = x

    return curr_min


def file_reader(txt):
    with open(txt, "r") as file:
        data = file.read().replace("\n", "")
        return data


if __name__ ==  '__main__':
    gen = file_reader('input.txt')
    print(min_skew(gen))