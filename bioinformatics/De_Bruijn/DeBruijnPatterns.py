def path_graph(patterns):
    adj_list = {}

    for kmer in patterns:
        pre = prefix(kmer)
        suf = suffix(kmer)
        if pre in adj_list:
            adj_list[pre].append(suf)
        else:
            adj_list.update({pre: [suf]})
    return adj_list


def prefix(s):
    return s[:len(s)-1]


def suffix(s):
    return s[1:]

def file_reader(txt):
    ls = []
    with open(txt, "r") as file:
        for i in file:
            ls.append(i[:-1])
    return ls


if __name__ == '__main__':
    ls = ['TTACCTTAAG', 'GTTCCATAAC', 'TAACCTTGAC', 'TTACCTCAAC', 'TTAGATCAAC']
    print(path_graph(ls))

    ls2 = ['ACACAGGCAC', 'TGAACCGGAC', 'GATCCGGCGC', 'CACGGATCTC', 'ACACCGGTAC']
    print(path_graph(ls2))

    # graph = path_graph(file_reader('pat.txt'))
    # f = open('output.txt', 'w')
    #
    # for key in sorted(graph):
    #     values = graph[key]
    #     f.write(key + ' -> ')
    #     f.write(",".join(sorted(values)) + '\n')
