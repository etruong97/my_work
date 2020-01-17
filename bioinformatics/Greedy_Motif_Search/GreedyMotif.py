def greedy_motif_search(dna, k, t):
    best_motifs = []
    for i in range(t):
        best_motifs.append(dna[i][:k])

    best_score = score(best_motifs)

    for i in range(len(dna[0]) - k + 1):
        kmer = dna[0][i: i + k]
        motifs = [kmer]
        for j in range(1, t):
            prof = profile(motifs)
            motifs.append(profile_most_prob(prof, dna[j], k))

        current_score = score(motifs)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs

    return best_motifs


def hamming(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count


def consensus(motifs):
    cons = ""

    for i in range(len(motifs[0])):
        cache = ""
        for motif in motifs:
            cache = cache + motif[i]
        s = most_frequent(cache)
        cons = cons + s

    return cons


def most_frequent(str):
    dictionary = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    for s in str:
        for d in dictionary:
            if s == d:
                dictionary[d] += 1

    max_val = -1
    for d in dictionary:
        if dictionary[d] > max_val:
            max_val = dictionary[d]

    for d in dictionary:
        if dictionary[d] == max_val:
            return d


def distance(motif, motifs):
    total = 0

    for m in motifs:
        x = hamming(m, motif)
        total = total + x

    return total


def score(motifs):
    return distance(consensus(motifs), motifs)


def profile(motifs):
    prof = [[], [], [], []]

    for i in range(len(motifs[0])):
        col = ""
        for motif in motifs:
            col = col + motif[i]

        for x in range(4):
            if x == 0:
                prof[x].append(proportion('A', col))
            if x == 1:
                prof[x].append(proportion('C', col))
            if x == 2:
                prof[x].append(proportion('G', col))
            if x == 3:
                prof[x].append(proportion('T', col))

    return prof


def proportion(letter, string):
    count = 0
    for i in string:
        if i == letter:
            count += 1

    return count/len(string)


def profile_most_prob(profile, text, k):
    dict = {}
    max_prob = 0

    for i in range(len(text) - k + 1):
        kmer = text[i: i + k]
        prob = probability(profile, kmer)
        if prob > max_prob:
            max_prob = prob
        dict.update({kmer: prob})

    for kmer, prob in dict.items():
        if prob == max_prob:
            return kmer


# returns int
def probability(profile, kmer):
    ls = []
    for i in range(len(kmer)):
        if kmer[i] == 'A':
            ls.append(profile[0][i])
        if kmer[i] == 'C':
            ls.append(profile[1][i])
        if kmer[i] == 'G':
            ls.append(profile[2][i])
        if kmer[i] == 'T':
            ls.append(profile[3][i])

    product = 1
    for i in ls:
        product = product * i

    return product


def reader(file_name):
    f = open(file_name)
    motif = []
    for line in f:
        motif.append(line.strip())
    return motif


if __name__ == '__main__':
    for i in greedy_motif_search(reader('dna.txt'), 12, 25):
        print(i)








