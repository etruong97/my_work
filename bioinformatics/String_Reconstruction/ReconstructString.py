def reconstruct(patterns):
    s = patterns[0]
    for i in range(1, len(patterns)):
        s = s + patterns[i][-1]
    return s


def file_reader(txt):
    ls = []
    with open(txt, "r") as file:
        for i in file:
            ls.append(i[:-1])
    return ls


if __name__ == '__main__':
    # ls = ['ACCGA', 'CCGAA', 'CGAAG', 'GAAGC', 'AAGCT']
    # print(reconstruct(ls))

    patterns = file_reader('dna.txt')
    s = reconstruct(patterns)
    f = open('output.txt', 'w')
    f.write(s)




