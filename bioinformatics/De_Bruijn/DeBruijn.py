def path_graph(text, k):
    adj_list = {}

    for i in range(len(text) - k + 1):
        kmer = text[i: i + k]
        pre = prefix(kmer)
        suf = suffix(kmer)
        if pre in adj_list:
            adj_list[pre].append(suf)
        else:
            adj_list.update({pre: [suf]})


    return adj_list


def file_reader(txt):
    with open(txt, "r") as file:
        data = file.read().replace("\n", "")
        return data


def prefix(s):
    return s[:len(s)-1]


def suffix(s):
    return s[1:]


if __name__ == '__main__':
    # print(path_graph('AAGATTCTCTAC', 4))

    genome = file_reader('dna2.txt')
    graph = path_graph(genome, 12)

    f = open('output.txt', 'w')

    for key in sorted(graph):
        values = graph[key]
        f.write(key + ' -> ')
        f.write(",".join(sorted(values)) + '\n')


    # for i in graph:
    #     print(i[:11] + " " + i[11:])
    #     f.write(i[:11] + " " + i[11:] + '\n')
    # f.close()









